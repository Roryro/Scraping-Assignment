# Scraping-Assignment

Here can be found the code for scraping the SEC (U.S. Securities and Exchange Commission) website using API calls to fetch financial reports and save them in HTM and PDF formats.
The repository is made of:
1. The script (apitrial.py),
2. The requirement file in txt format,
3. The official CIK list downloaded from the SEC (U.S. Securities and Exchange Commission) website (CIK_list.txt),
4. The Output_Examples folder where there are the 10-K reports for 6 specific companies (Apple, Meta, Alphabet, Amazon, Netflix, Goldman Sachs) in HTM format already downloaded and also converted to PDF format.

# How to run the script

## Linux 
After cloning the repository, use a terminal to go to the folder where you saved the repository on your pc and:
1. Create and activate a python virtual environment ('python3 -m venv .venv' and then 'source .venv/bin/activate')
2. Install the requirements ('pip3 install -r  requirements.txt')
3. Run the script ('python3 apitrial.py')

## Mac
After cloning the repository, use a terminal to go to the folder where you saved the repository on your pc and:
1. Create and activate a python virtual environment ('python3 -m venv .venv' and then 'source .venv/bin/activate')
2. Install the requirements ('pip3 install -r  requirements.txt')
3. Run the script ('python3 apitrial.py')
4. In case of errors with the libgobject libraries run the command 'export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib:$DYLD_FALBACK_LIBRARY_PATH' to point to the correct folder with the graphical libraries and then rerun the script.

## Windows
After cloning the repository, use a terminal to go to the folder where you saved the repository on your pc and:
1. Create and activate a python virtual environment ('python3 -m venv .venv' and then '.venv\Scripts\activate')
2. Install the requirements ('pip3 install -r  requirements.txt')
3. Run the script ('python3 apitrial.py')
4. In case of errors with the libgobject libraries install msys2 on the pc, run in the msys2 GUI the command 'pacman -S mingw-w64-x86_64-pango' to install the graphical libraries needed, decomment in the beginning of the script apitrial.py the line 'os.add_dll_directory(r"C:\msys64\mingw64\bin")' and then rerun the script.

The script runs for about 3 minutes (feedback on the process in progress will appear in the terminal) and saves the HTM and the PDF files in the same folder where the script is. Of course the code is far from perfect and with more time available it could be improved further.
