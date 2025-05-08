from bs4 import BeautifulSoup #HTML parsing
import requests #HTTP request manipulation
from datetime import date #just in case, plans for date based limiting
import csv #used with date to generate output file, not yet implemented

# "these are surprise variables that will help us later, huh-huh"
article_dict = {}
data_out=[]
today = date.today()
filename = f'BC-{today}.csv'
url = "https://bleepingcomputer.com/news/"

# testing for page fetch success
headers = { #bypass bot protection by adding UAS to http headers
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/135.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    html_content = response.text # stores the HTML for parsing below
else:
    ermsg = f"Failed to fetch webpage Response Status Code:{response.status_code}"
    print(ermsg)

# BS4 to parse the html
soup = BeautifulSoup(html_content, 'html.parser')
articles = soup.find_all('div', class_='bc_latest_news_text')

# iterate through articles and print titles/links, later we will convert to dict
for article in articles:
    link_tag = article.find('a')
    title = link_tag.get_text(strip=True) #strips the <> bit
    link = link_tag['href']
    article_dict.update({title: link})

#listing dictionary entries as tuples
for key,value in article_dict.items():
    data_out.append({key:value})

# adding article count column, and iterating to print each article entry for each skimming, not necessary for end product
entry_no=0
for entry in data_out:
    entry_no +=1
    print(f'{entry_no} {entry}')
