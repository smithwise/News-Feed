#Goal: Scrape BleepingComputer for top headline link. Store in txt.
# using tutorial here: https://realpython.com/python-web-scraping-practical-introduction/
# also getting tutoring services from ChatGPT - be like me, take this with a grain of salt.
# Current issues: not printing titles, listing only one article. See attached file "example.txt" for current page it should match


from bs4 import BeautifulSoup
import requests

url = "https://bleepingcomputer.com/news/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/135.0.0.0 Safari/537.36"
}


response = requests.get(url, headers=headers)

# testing for page fetch success
if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to fetch webpage Response Status Code:{response.status_code}")

soup = BeautifulSoup(html_content, 'html.parser')

# find all articles
articles = soup.find_all('div', class_='bc_latest_news')

# iterate through articles and print titles/links
for article in articles:
    link_tag = article.find('a')
    if link_tag:
        title = link_tag.get_text(strip=True)
        link = link_tag['href']
        print(f'Title: {title}')
        print(f'Link: {link}\n')
