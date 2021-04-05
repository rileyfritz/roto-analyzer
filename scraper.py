# Dependencies
from bs4 import BeautifulSoup
import requests
# import pymongo
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

# Bringing in browser
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit url 
url = 'https://rotogrinders.com/resultsdb/site/draftkings/date/2021-04-03/sport/mlb/slate/6069d49642e1de0fd1ab7a88/contest/6069d4c142e1de0fd1abe7cc'
browser.visit(url)
 # HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Retrieve the parent divs for all articles
results = soup.find('div', class_= 'ant-table-body')
# data = results.find('tr').text
browser.quit()
# Get the title and teaser from first article
print(f'results are: {results}')