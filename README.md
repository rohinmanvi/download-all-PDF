This script can be used to download all PDF files from a given url into a folder. Note that this script requires that `BeautifulSoup` be installed within the Python environment you are running this script in.

Example usage:  
python download_all_pdfs_from_url.py -u https://www.example.com -p ~/Downloads

To download all PDF files from https://cms.math.ca/competitions/cmo/ into a folder called “Math Problems", run this:  
python download_all_pdfs_from_url.py -u https://cms.math.ca/competitions/cmo/ -p ./Math\ Problems/
