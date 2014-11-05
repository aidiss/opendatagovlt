# coding: utf-8

import os
import requests
from bs4 import BeautifulSoup


def download_pages():
    r = requests.get('http://opendata.gov.lt/')
    url = ''
    for number in range(0, 262, 15):
        url = 'http://opendata.gov.lt/index.php?vars=/public/public/search/{}/'.format(number)
        r = requests.get(url)
        r.encoding = 'utf-8'
        filename = "downloads/{}.html".format(number)
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        with open(filename, "wb") as code:
            code.write(r.content)


def read_downloaded_pages():
    f = open('downloads/{}.html'.format(0))

    soup = BeautifulSoup(f)
    the_table = soup.findAll('table')[6]

    new_table = []
    count = 0
    for row in the_table:
        count += 1
        if (count % 2 == 0) or (count == 0):
            new_row = []
            for item in row:
                if item == "\n":
                    continue
                new_row.append(item)
            new_table.append(new_row)
    return new_table


def main():
    #download_pages()
    pages = read_downloaded_pages()

    columns = ['eil nr', 'Kodas', 'Pavadinimas',
               'Rinkmenos apibūdinimas', 'Kategorija (informacijos sritis)',
               'Tvarkytojas', 'Internetinis adresas','int adresas']

    #TODO do regex striping inplace
    #TODO retain hyperlinks
