# Scraping-Assignment

Code for scraping the web using API to fetch financial reports from the SEC (U.S. Securities and Exchange
Commission) and save the report in PDF format.

# How to run the script 

## Linux 
1. Create and activate the virtual environment (python3 -m venv .venv , source .venv/bin/activate)
2. Install requirements (pip3 install -r  requirements.txt)
3. Run the script (python3 apitrial.py)

## Mac
1. Create and activate the virtual environment (python3 -m venv .venv , source .venv/bin/activate)
2. Install requirements (pip3 install -r  requirements.txt)
3. Run the script (python3 apitrial.py)
4. In case of error with weasyprint run the command 'export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib:$DYLD_FALBACK_LIBRARY_PATH' to point to the correct folder with the graphical libraries and then rerun script.

## Windows
1. Create and activate the virtual environment (python3 -m venv .venv , source .venv\Scripts\activate)
2. Install requirements (pip3 install -r  requirements.txt)
3. Run the script (python3 apitrial.py)
4. In case of error with weasyprint install msys2 on the pc, run in msys2 the command pacman -S mingw-w64-x86_64-pango to install the graphical libraries needed and decomment in the script 
the line 'os.add_dll_directory(r"C:\msys64\mingw64\bin")'

The Script then runs for around 4 minutes and saves the htm and the PDF files in the folder where the script is. I also have added the reports already downloaded in the output examples folder.
Of course the code is far from perfect and with more time available it can be improved further.
