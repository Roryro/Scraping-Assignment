#Importing libraries

import requests
import pandas as pd
from weasyprint import HTML,CSS
import sys
import os


#os.add_dll_directory(r"C:\msys64\mingw64\bin")

#Reading the CIK list file retrieved online
cik_list=pd.read_csv("CIK_list.txt",sep=":00",header=None,engine='python')
cik_list_df=pd.DataFrame(cik_list)

#Retrieving the CIK of the relevant companies companies 

companies=['APPLE INC.','META PLATFORMS','ALPHABET INC.','AMAZON COM INC','NETFLIX INC','GOLDMAN SACHS GROUP INC']

print('fetching info...')

cik_companies=[]
for i in companies:
  for j in range(len(cik_list_df)):
    if i in str(cik_list_df[0][j]):
      cik_companies.append(cik_list_df[1][j].strip(':'))
cik_companies=cik_companies[0:6]

#Creating the url to find the document submitted by each of the relevant companies

url = [f"https://data.sec.gov/submissions/CIK{str(i).zfill(10)}.json" for i in cik_companies]

#Finding and saving in a dataframe the relevant ids for the 10-K reports for each of the relevant companies

header = {
  "User-Agent": "roryro@gmail.com" #needed in order for the request to be allowed.
}

doc_df=pd.DataFrame()
access_numbers=[]
file_names=[]
for i in url:
  company_reports = requests.get(i, headers=header).json()
  company_reports_df = pd.DataFrame(company_reports["filings"]["recent"])

  doc_df=pd.concat([company_reports_df.loc[company_reports_df.form=='10-K'], doc_df])
  if len(company_reports_df.loc[company_reports_df.form=='10-K'])>0:
    access_numbers.append(company_reports_df.loc[company_reports_df.form=='10-K'].accessionNumber.values[0].replace("-", "")) #add only the first value since the data are in chronological descending order
    file_names.append(company_reports_df.loc[company_reports_df.form=='10-K'].primaryDocument.values[0]) #add only the first value since the data are in chronological descending order
  else:
    access_numbers.append('na')
    file_names.append('na')


CIK=[str(i).zfill(10) for i in cik_companies]

access_number = [i for i in access_numbers]

file_name = [i for i in file_names]

#Creating the API request to fetch the 10-K report documents, save the htm files and convert them to PDF format.

url = [f"https://www.sec.gov/Archives/edgar/data/{CIK[i]}/{access_number[i]}/{file_name[i]}" for i in range(len(CIK))]

css = CSS(string="""
    @page {
        size: A4;
        margin: 2cm;
        
        @top-center {
            font-size: 10pt;
        }

        @bottom-right {
            content: "Page " counter(page) " of " counter(pages);
            font-size: 9pt;
        }
    }
""")

for i in range(len(url)):
  req_content = requests.get(url[i], headers=header).content.decode("utf-8")

  with open(file_name[i], "w") as f:
      f.write(req_content)
  print('printing '+str(companies[i])+' report and file.')
  HTML(string=req_content,base_url="").write_pdf(file_name[i] + ".pdf",stylesheets=[css])
 
print('script done, everything saved')
