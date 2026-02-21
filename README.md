# Quote Scraper Project

## Overview
This project scrapes quotes from [quotes.toscrape.com](https://quotes.toscrape.com) using Python. 
It extracts quote text, author names, and tags, cleans the data, and saves it in a structured CSV format.

## Technologies Used
- Python
- requests
- BeautifulSoup
- pandas

## Features
- Scrapes quotes, authors, and tags from the first page of the website
- Cleans text data by removing smart quotes
- Calculates the length of each quote
- Saves structured data to `quotes.csv`
- Can be extended to scrape multiple pages

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/bushTM/quote-scraper-project.git

Navigate to the project folder:

cd quote-scraper-project

Create a virtual environment and activate it:

python -m venv venv
venv\Scripts\activate   # Windows

Install dependencies:

pip install -r requirements.txt

Run the scraper:

python scraper.py

Output

The scraper creates a CSV file called quotes.csv containing:

text (quote)
author
tags
text_length

License

This project is open source and free to use.