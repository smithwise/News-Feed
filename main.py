import requests
from bs4 import BeautifulSoup
from datetime import date
import csv

# Constants
URL = "https://bleepingcomputer.com/news/"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/135.0.0.0 Safari/537.36"
    )
}

# Attempt to fetch page
response = requests.get(URL, headers=HEADERS)
if response.status_code != 200:
    print(f"Failed to fetch webpage. Status Code: {response.status_code}")
    exit()

# Parse HTML content
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('div', class_='bc_latest_news_text')

# Extract articles into list of dicts
data_out = []
for article in articles:
    link_tag = article.find('a')
    if link_tag:
        title = link_tag.get_text(strip=True)
        link = link_tag['href']
        data_out.append({"title": title, "link": link})

# Output results to console
for i, article in enumerate(data_out, start=1):
    print(f"{i}. {article['title']}")

# Write output to CSV
filename = f"BC-{date.today()}.csv"
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "link"])
    writer.writeheader()
    writer.writerows(data_out)
