import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://yapifuari.com.tr/katılımcı-listesi/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = []
for title in soup.find_all('h3', {'class': 'ite-exhibitor-name'}):
    title = title.text.strip().lower()
    titles.append(title)

df = pd.DataFrame({'Şirket Adı': titles})
df.to_csv('yapifuarifirmaisim.csv', index=False, encoding='utf-8')

print(df)

