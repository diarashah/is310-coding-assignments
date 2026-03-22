import cloudscraper
from bs4 import BeautifulSoup
import csv

scraper = cloudscraper.create_scraper()

url = "https://harrypotter.fandom.com/wiki/Category:Gryffindors"

response = scraper.get(url)
soup = BeautifulSoup(response.text, "html.parser")

characters = soup.find_all('a')

data = []

for link_tag in characters:
    name = link_tag.get_text().strip()
    link = link_tag.get('href')

    if not link:
        continue
    if not link.startswith("/wiki/"):
        continue
    if ":" in link:
        continue
    if name == "":
        continue

    full_link = "https://harrypotter.fandom.com" + link
    data.append([name, full_link])

with open('hp_characters.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["character", "link"])
    writer.writerows(data)

print("Number of characters:", len(data))