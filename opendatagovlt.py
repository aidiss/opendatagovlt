# coding: utf-8

import os
import json
import requests
from bs4 import BeautifulSoup

# Flow nr1
def download_page(number):
    url = 'http://opendata.gov.lt/index.php?vars=/public/public/search/{}/'.format(number)
    r = requests.get(url)
    r.encoding = 'utf-8'
    filename = "downloads/{}.html".format(number)
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    with open(filename, "wb") as code:
        code.write(r.content)

def download_pages(destination=None):
    for number in range(0, 262, 15):
        download_page(number)

def get_table_from_html(path):
    f = open(path)
    soup = BeautifulSoup(f)
    table = soup.findAll('table')[6]
    new_table = []

    count = 0
    for row in table:
        count += 1
        if (count % 2 == 0) or (count == 0):
            new_row = []
            for item in row:
                if item == "\n":
                    continue
                new_row.append(item)
            new_table.append(new_row)
    return new_table

def read_downloaded_pages(path):
    tables = []
    for number in range(0, 262, 15):
        table = get_table_from_html("{}{}.html".format(path, number))
        tables.append(table)
    return tables


# Alternative flow (nr2)
def download_page_alt0(number):
    url = 'http://opendata.gov.lt/index.php?vars=/public/public/print/{}/'.format(number)
    r = requests.get(url)
    r.encoding = 'utf-8'
    filename = "downloads/singular/{}.html".format(number)
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    with open(filename, "wb") as code:
        code.write(r.content)

def download_pages_alt0():
    for number in range(0, 600):
        download_page_alt0(number)

def scrap_singular(path):
    table = []
    soup = BeautifulSoup(open(path).read())
    for tr in soup.find_all('tr'):
        tds = tr.find_all('td')
        try:
            line = (tds[0].text, tds[1].text)
            table.append(line)
        except:
            pass
    return table

def merge_singulars():
    # creates one list out of many
    all_singulars = []
    for number in range(700):
        path = r'd:\coding\opendatagovlt\downloads\singular\{}.html'.format(number)
        try:
            all_singulars.append(scrap_singular(path))
        except:
            pass
    return all_singulars

def filter_entries(entries):
    return [x for x in entries if x[0][1] != '']

def to_list_of_dicts(some_list):
    list_of_dicts = []
    for x in some_list:
        new_dict = {}
        for key, value in x:
            new_dict[key] = value
        list_of_dicts.append(new_dict)
    return list_of_dicts

def dump_json(data):
    with open(r'd:\coding\opendatagovlt\data\raw_entries.json', 'w') as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4) #ensure_ascii=False

def alternative_flow():
    #download_page_alt0()
    temp_list = filter_entries(merge_singulars())
    entries = to_list_of_dicts(temp_list)
    dump_json(entries)


def main():
    #download_pages()
    pages = read_downloaded_pages(path='downloads/')

    columns = ['eil nr', 'Kodas', 'Pavadinimas',
               'Rinkmenos apibūdinimas', 'Kategorija (informacijos sritis)',
               'Tvarkytojas', 'Internetinis adresas','int adresas']

    return(pages)
    #TODO do regex striping inplace
    #TODO retain hyperlinks

result = main()
#print (len(result))
