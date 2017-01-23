import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

# Scrape APNewsBriefs with requests
urlAPNewsBriefs = 'https://www.apartments.com/nashville-tn/?bb=qrwyv87s3Ig4_x5mY'
pageAPNewsBriefs = requests.get(urlAPNewsBriefs)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soupAPNewsBriefs = BeautifulSoup(pageAPNewsBriefs.content, 'lxml')

# Parse APNewsBriefs url
# 'position' marks the beginning of each news brief in the html
# All other data is found in its relationship to 'position'
for brief in soupAPNewsBriefs.find_all('div', class_='apartmentRentRollupContainer'):
    price = brief.find('span', class_='altRentDisplay').string
    size = brief.find('span', class_='unitLabel').string
    position = soupAPNewsBriefs.find('div', class_='location')
    location = position.string
    contact = soupAPNewsBriefs.find('div', class_='phone')
    phone = contact.find('span').string
    postTime = soupAPNewsBriefs.find('span', class_='lastUpdated')
    time = postTime.find('span').string + ' ago'


    # Make changes to response for APNewsBriefs
    response.append({'location': location, 'price': price, 'size': size, 'phone': phone, 'time': time})

# Write response to JSON file
postingsFile = today + 'AptBriefs.json'

#Write response to JSON file in another location
#postingsFile = '/APBriefs/' + today + '.APNewsBriefs.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
