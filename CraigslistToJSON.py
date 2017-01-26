import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

# Scrape APNewsBriefs with requests

urlAPNewsBriefs = 'https://nashville.craigslist.org/search/apa'
pageAPNewsBriefs = requests.get(urlAPNewsBriefs)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soupAPNewsBriefs = BeautifulSoup(pageAPNewsBriefs.content, 'lxml')

# Parse APNewsBriefs url
# 'position' marks the beginning of each news brief in the html
# All other data is found in its relationship to 'position'
for brief in soupAPNewsBriefs.find_all('li', class_='result-row'):
    location = soupAPNewsBriefs.find('span', class_='result-hood').string
    price = soupAPNewsBriefs.find('span', class_='result-price').string
    #size = brief.find('sup').previousSibling.string


    # Make changes to response for APNewsBriefs
    response.append({'location': location, 'price': price,})

# Write response to JSON file
postingsFile = today + 'CraigslistBriefs.json'

#Write response to JSON file in another location
#postingsFile = '/APBriefs/' + today + '.APNewsBriefs.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
