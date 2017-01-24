import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

# Scrape APNewsBriefs with requests
urlAPNewsBriefs = 'http://www.rent.com/tennessee/nashville-houses/74-491'
pageAPNewsBriefs = requests.get(urlAPNewsBriefs)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soupAPNewsBriefs = BeautifulSoup(pageAPNewsBriefs.content, 'lxml')

# Parse APNewsBriefs url
# 'position' marks the beginning of each news brief in the html
# All other data is found in its relationship to 'position'
for brief in soupAPNewsBriefs.find_all('div', class_='prop li-srp'):
    brieff = brief.find('p', class_='prop-address')
    locationRegion = brieff.find('span', itemprop='addressRegion')
    locationRegion.replace_with('')
    locationState = brieff.find('span')
    locationState.replace_with('')
    location = brieff.find('span').string
    #location = brieff.find('span').next_sibling.next_sibling.next_sibling.string
    cost = brief.find('p', class_='prop-rent')
    price = cost.find('span').string
    size = brief.find('span', class_='prop-beds bullet-separator').string
    phone = brief.find('strong', class_='tel').string



    # Make changes to response for APNewsBriefs
    response.append({'location': location, 'price': price, 'size': size, 'phone': phone})

# Write response to JSON file
postingsFile = today + 'RentBriefs.json'

#Write response to JSON file in another location
#postingsFile = '/APBriefs/' + today + '.APNewsBriefs.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
