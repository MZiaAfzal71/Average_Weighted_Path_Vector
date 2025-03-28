import pandas as pd
import requests
from bs4 import BeautifulSoup

def extract_boronic_pages(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    hrefs = [a['href'] for a in soup.find_all('a', href=True)]
    newhrefs = list(filter(lambda x: 'data' in x, hrefs))

    return newhrefs


bor_pages = {'pages' : []}
newlen = 0
for i in range(1, 8):
    search_result = requests.get(f'https://organoborons.com/boronic-acids/page-{i}.html')
    bor_pages['pages'] += extract_boronic_pages(search_result.text)

data = pd.DataFrame(bor_pages)
data.to_excel('Excel Files/Boronic_pages.xlsx')