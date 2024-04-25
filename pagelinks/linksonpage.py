# Get all links on a web page and save to a .txt file

import requests
from bs4 import BeautifulSoup
import os

url = "https://"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("a")
for link in links:
    print(link.get("href"))

# Open a file in write mode
with open("pagelinks.txt", "w") as file:
    # Iterate over links and write them to the file
    for link in links:
        file.write(str(link.get("href")) + "\n")
