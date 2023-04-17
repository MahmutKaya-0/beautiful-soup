import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
import re
import pandas as pd
import numpy as np

url = 'https://yapifuari.com.tr/katılımcı-listesi/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

companies = soup.find_all('a', href=True)

urls = []
for company in companies:
    if '/katılımcı-listesi/' in company['href']:
        company_url = f"{url[:24]}{company['href']}"
        urls.append(company_url)

data = []
for i, url in enumerate(urls[1:len(urls):2], start=1):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        title_tag = soup.find('div', {'class': 'card-body'}).find_all('a')
        title = title_tag[0].get('href')
        title = unidecode(title)
    except:
        title = 'Öğe bulunamadı'
    
    data.append([i, title ])

df = pd.DataFrame(data, columns=['No', 'Şirket Adı'])
df.replace(np.nan, 'Öğe bulunamadı', inplace=True)
df.to_csv('yapifuariwebsite.csv', index=False, sep=';')

print(df)
    