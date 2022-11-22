# OSDB-SCRAPER
The Open Spectral Database (OSDB) is an open source database for spectral data from 45 different compounds. The spectral data can be of the types:
- IR
- 13C NMR
- 1H NMR
- MS
- UV-VIS

Additionally, OSDB provides the files in the formats of:
- JCAMP (.jdx)
- XML (.xml)
- JSONLD (.json)

This scraper tool can download whichever type in whichever format required!

## Required
- BeautifulSoup4
- urllib
- requests
- Python >=3.10

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Installation

**NOTE**
This is just a python file and does not have a UI associated. A small amount of coding is necessary, but you knew that.

To use this tool:
1. Download the github repository:
`git clone https://github.com/adiravishankara/OSDB-SCRAPER.git`

2. Install the requirements using a terminal:
`wget https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe'
`pip install -U pip setuptools wheel`
`pip install requests beautifulsoup4`

3. If you want to specify the spectra type, file type or directory, you can do that in the "__main__" section of the code.

It will take a little while to run but will deposit the files in the defined directory.


