import mechanize
from bs4 import BeautifulSoup
import os

def scrapDetails(number):
    datas = []
    url = 'https://www.findandtrace.com/trace-mobile-number-location'

    brow = mechanize.Browser()
    brow.set_handle_robots(False)

    brow.open(url)
    brow.select_form(name="trace")
    brow['mobilenumber'] = number
    result = brow.submit()

    soup = BeautifulSoup(result.read(), 'html.parser')
    table = soup.find_all('table', class_='shop_table')
    print(len(table))
    os.system('cls')
    print('Details Collected')
    print('------------------')
    extracted_data = table[0].find('tfoot')
    count = 0
    for row in extracted_data:
        count += 1
        if count in (2,3,5,7,9):
            header = row.find('th')
            data = row.find('td')
            print(header.text, data.text)
            datas.append(header.text+data.text)

    extracted_data = table[1].find('tfoot')
    count2 = 0
    for row in extracted_data:
        count2 += 1
        if count2 in (2,8,10,12,14,16,20,22,24,26):
            header = row.find('th')
            data = row.find('td')
            print(header.text, data.text)
            datas.append(header.text+data.text)        
    return input('Do you want to continue(y/n)? ')