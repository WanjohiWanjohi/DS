from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import requests

def scrape(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content , features="html.parser")
	return soup

url = "https://africafreak.com/100-most-influential-twitter-users-in-africa"
influentials = scrape(url)

names = []
name = influentials.find_all('h2')
for item in name:
	names.append(item)

df = pd.DataFrame({'InfluencerName':names})
df.to_csv('influencers.csv', encoding='utf-8')

