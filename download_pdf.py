"""
Extract PDF from indianculture[dot]gov[dot]in
David Peng
20230621
"""
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import unquote
import os

DEFAULT_TIMEOUT = 10

# script borrowed from https://github.com/lalitaalaalitah/Scrape_IndianCulture.Gov.In_Release
def download(book_page_url):
    try:
        book_page_get = requests.get(book_page_url, timeout=DEFAULT_TIMEOUT)
    except Exception:
        raise Exception("Bad URL!")

    book_page_get = requests.get(book_page_url)
    parsed_book_page = bs(book_page_get.content, 'html.parser')
    class_pdf_in_page = parsed_book_page.find_all('iframe', class_='pdf')

    if len(class_pdf_in_page) >= 1:
        # assume there is just 1 right now
        pdf_item = class_pdf_in_page[0]
        src_each_item = pdf_item['src']
        pdf_address = src_each_item.split('file=')[-1]
        cleaned_pdf_address = unquote(pdf_address)
        pdf_name = cleaned_pdf_address.split('/')[-1]

        cmd_for_curl = 'curl ' + cleaned_pdf_address + " -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.8,sa;q=0.5,hi;q=0.3' --compressed -H 'Referer: https://www.indianculture.gov.in/libraries/pdf.js/web/viewer.html?file=https%3A%2F%2Fwww.indianculture.gov.in%2Fsystem%2Ffiles%2FdigitalFilesICWeb%2Figncarepository%2F963%2Fignca-19280-rb.pdf' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'TE: Trailers'" + " --output " + pdf_name

        print(cmd_for_curl)
        os.system(cmd_for_curl)
        return pdf_name
    else:
        raise Exception("Unexpected number of PDFs (=/= 1)!")
