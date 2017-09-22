from bs4 import BeautifulSoup
import requests
import pdfkit
import os

page = 1
count = 1
max_pages = 5
while page <= max_pages:
    url = 'http://www.geeksforgeeks.org/tag/oracle/page/' + str(page) +'/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for title in soup.findAll('h2', {'class': 'entry-title'}):
        for link in title.findAll('a'):
            link_main = link.get('href')
            html_text = str(link_main)
            options = {'--proxy': 'http://172.16.30.20:8080'}
            config = pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\Bin\wkhtmltopdf.exe")
            name = str(count) + '.pdf'
            pdfkit.from_url(link_main, name, configuration=config, options=options)
            print(link_main)
            os.rename('E:\Python\Web Crawlers\\' + name, 'E:\Geeks For Geeks\Oracle\\' + name)
            count += 1
    page += 1
