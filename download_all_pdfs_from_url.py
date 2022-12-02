'''
This script downloads all the pdfs from a given url

This script requires that `BeautifulSoup` be installed within the Python
environment you are running this script in.

Example usage:
python download_all_pdfs_from_url.py -u https://www.example.com -p ~/Downloads

This file can also be imported as a module and contains the following
functions:

    * download_all_pdfs - downloads all the pdfs from a given url into the given path
    * main - the main function of the script
'''

import os
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_all_pdfs(base_url, path):
    '''Downloads all the pdfs from a given url into the given path

    Parameters
    ----------
    base_url : str
        The url to download pdfs from
    path : str
        The path to put the pdfs in
    '''

    if not os.path.exists(path):
        os.mkdir(path)
        
    response = requests.get(base_url, headers={'User-Agent': 'Custom'})
    soup = BeautifulSoup(response.text, "html.parser")

    # select all the links with the pdf extension
    selections = soup.select("a[href$='.pdf']")

    files_downloaded = set()

    for selection in selections:
        link = selection['href']
        file_name = link.split('/')[-1]
        file_path = os.path.join(path, file_name)

        # skip previously downloaded files
        if file_name in files_downloaded:
            continue
        files_downloaded.add(file_name)

        with open(file_path, 'wb') as f:
            url = urljoin(base_url, link)
            pdf_content = requests.get(url).content
            f.write(pdf_content)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-u', 
        '--url', 
        required=True, 
        type=str, 
        help='provide a url to download pdfs from'
    )
    parser.add_argument(
        '-p', 
        '--path', 
        required=True, 
        type=str, 
        help='provide a path to put pdfs in'
    )
    args = parser.parse_args()

    base_url = args.url
    path = args.path

    download_all_pdfs(base_url, path)

if __name__ == "__main__":
    main()