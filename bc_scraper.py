import requests
from bs4 import BeautifulSoup
from datetime import date
import csv
import os
from pathlib import Path
from urllib.parse import urljoin

# Constants
URL = "https://bleepingcomputer.com/news/"
# headers will allow us to trick the webserver into thinking we are not visiting as a bot
# but need to keep the Chrome version relatively recent to avoid getting caught as suspicious 
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"  
    )
}
log_dir = Path.cwd().parent / 'logs'
log_dir.mkdir(parents=True, exist_ok=True)
output_dir = Path.cwd().parent / 'archives'
output_dir.mkdir(parents=True, exist_ok=True)
filename = output_dir / f"BC-{date.today()}.csv"

# Attempt to fetch page
try:
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status()
    if response.status_code != 200:  # method should raise exception for non 200/300 response, still want to log 300s
        with open(log_dir/'scraper_error_log.txt', 'a', newline='', encoding='utf-8') as log:
            log.write(f'{date.today()} - Non-200 HTTP code \n status code: {response.status_code}\n')
except requests.RequestException as e:
    print(f"Failed to fetch {URL}: \n{e}\n")
    pritn('see scraper_error_log.txt')
    exit(1)  # terminate the program with error to console (should be caught by wrapper and put in log)


# Parse HTML content
soup = BeautifulSoup(response.text, 'lxml')
articles = soup.find_all('div', class_='bc_latest_news_text')

# Extract articles into list of dicts
data_out = []
for article in articles:
    link_tag = article.find('a')
    if link_tag:
        title = link_tag.get_text(strip=True)
        link = urljoin(URL, link_tag['href'])
        data_out.append({"title": title, "link": link})

if not data_out:
    with open(log_dir/'scraper_error_log.txt', 'a', newline='', encoding='utf-8') as log:
        log.write(f'{date.today()} - No articles found - Possible HTML structure change \n')


# Output results to console
print(f"Date: {date.today()}\n")
for i, article in enumerate(data_out, start=1):
    print(f"{i}. {article['title']}")
print('\n -=-=-=-=-=-=-=-=-=-=-=-=-=-=- \n')  # clean break between batches of articles in log

# Write output to CSV
filename = f"BC-{date.today()}.csv"
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "link"])
    writer.writeheader()
    writer.writerows(data_out)
