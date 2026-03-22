# Harry Potter - Fandom Wiki Character Scraper

## Wiki Chosen

Wiki: Harry Potter Fandom Wiki  
Page scraped: https://harrypotter.fandom.com/wiki/Category:Gryffindors  
Robots.txt: https://harrypotter.fandom.com/robots.txt  


## Terms of Service & robots.txt

The robots.txt file at https://harrypotter.fandom.com/robots.txt was reviewed before scraping.

- User-agent: GEneral suers are allowed
- Disallowed paths include administrative pages such as:
  - /wiki/Special:
  - /wiki/User:
  - /wiki/Template:
- The script only accesses publicly available wiki pages under `/wiki/`, which are not restricted.

This project complies with the site’s robots.txt rules by avoiding restricted paths and only collecting publicly accessible data.


## Why Harry Potter?

The Harry Potter universe is one of the most widely documented fictional worlds, with a large and diverse set of characters. The fandom wiki organizes these characters into categories such as Hogwarts houses, making it a useful structure for extracting character-level data.

I chose the Gryffindor category because it contains a well-defined group of characters associated with a specific house, allowing for focused and structured data collection.


## What is being scraped?

This script collects character data from the Gryffindor category page.

For each entry, the script extracts:
- character - the name of the character  
- link - the URL to the character’s wiki page  

The script gathers all links that follow the `/wiki/` format and filters out irrelevant entries such as templates or administrative pages.


## Why might this data be useful to researchers?

- **Character relationships**  
  This data can help study how characters are connected within the Harry Potter universe.

- **Fandom organization**  
  It shows how fan communities organize and categorize information.

- **Naming patterns**  
  Researchers can analyze how characters are named and grouped.

- **Digital humanities**  
  The dataset can support research on how online communities build and share knowledge.

## Tools Used

- Python  
- cloudscraper (to retrieve webpage content)  
- BeautifulSoup (to parse HTML)  
- csv (to store structured data)  



## Requirements

- Python 3  
- cloudscraper  
- beautifulsoup4  

Install dependencies:

```bash
pip install cloudscraper beautifulsoup4