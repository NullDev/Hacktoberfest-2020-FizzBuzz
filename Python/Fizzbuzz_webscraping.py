# Scrapes answer from http://dontpad.com/fizzbuzzlist
# @lusmoura

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    r = requests.get('http://dontpad.com/fizzbuzzlist')
    soup = BeautifulSoup(r.text, 'lxml')
    text = soup.find('textarea', {'id': 'text'}).text.strip()
    lines = text.split('\n')
    fizzbuzz_list = [(line.split(': ')[0], line.split(': ')[1]) for line in lines]
    print(fizzbuzz_list)
