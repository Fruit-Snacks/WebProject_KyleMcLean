import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

# Scrape APNewsBriefs with requests
urlAPNewsBriefs = 'https://www.apartments.com/nashville-tn/'
pageAPNewsBriefs = requests.get(urlAPNewsBriefs)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soupAPNewsBriefs = BeautifulSoup(pageAPNewsBriefs.content, 'lxml')

# Parse APNewsBriefs url
# 'position' marks the beginning of each news brief in the html
# All other data is found in its relationship to 'position'



for brief in soupAPNewsBriefs.find_all('article', class_='diamond placard'):
    price = brief.find('span', class_='altRentDisplay').string
    size = brief.find('span', class_='unitLabel').string
    position = brief.find('div', class_='location')
    location = position.string
    contact = brief.find('div', class_='phone')
    phone = contact.find('span').string
    #postTime = soupAPNewsBriefs.find('span', class_='lastUpdated')
   #time = postTime.find('span').string + ' ago'



    # Make changes to response for APNewsBriefs
    response.append({'location': location, 'size': size, 'price': price, 'phone': phone})

# Write response to JSON file
#postingsFile = today + 'AptBriefs.json'

#Write response to JSON file in another location
postingsFile = '/Users/Owner/PycharmProjects/CSC3130/WebProject_KyleMcLean/' + today + '.AptBriefs.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
