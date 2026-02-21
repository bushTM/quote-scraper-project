#import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

#define the website
url = "https://quotes.toscrape.com"

#send request to website
response = requests.get(url)

#parse the html
soup = BeautifulSoup(response.text, "html.parser")

#create an empty list
qoutesData = []

#find all qoutes on page
qoutes = soup.find_all("div", class_="quote")

for qoute in qoutes:
    text = qoute.find("span", class_="text").text
    author = qoute.find("small", class_="author").text
    tags = [tag.text for tag in qoute.find_all("a", class_="tag")]

    #add data to list
    qoutesData.append(
        {
            "text": text,
            "author": author,
            "tags": ",".join(tags)
        }
    )
#convert to data frame
df = pd.DataFrame(qoutesData)

#clean text
df["text"]=df["text"].str.replace("“", "").str.replace("”", "")

#calculate how long each qoute is, make column
df["text_length"] = df["text"].apply(len)

#save to csv
df.to_csv("qoutes.csv", index=False)

#confirmation 
print("Scraping completed and saved to qoutes.csv")