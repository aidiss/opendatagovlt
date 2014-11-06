# coding: utf-8

import os

import requests
from bs4 import BeautifulSoup


def download_page(number):
    url = 'http://opendata.gov.lt/index.php?vars=/public/public/search/{}/'.format(number)
    r = requests.get(url)
    r.encoding = 'utf-8'

    if path == None:
        filename = "downloads/{}.html".format(number)
    else:
        filename = "{}".format(destination)
    
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    with open(filename, "wb") as code:
        code.write(r.content)

def download_pages(path=None):
    for number in range(0, 262, 15):
        download_page(number)

def read_downloaded_pages(path=None):
    if path == None:
        f = open('downloads/{}.html'.format(0))
    else:
        f = open(path)

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
