#from selenium import webdriver
import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

#selenium
#browser = webdriver.Chrome()

# Scrape APNewsBriefs with requests
#parse = True
#i =100
# while parse == True:
#     pages = requests.get(url)
#     soup = BeautifulSoup(pages.content, 'lxml')

#if(i<500):
#    url = 'https://nashville.craigslist.org/search/apa' + '?s=' + i
#    i+100


urlAPNewsBriefs ='https://nashville.craigslist.org/search/apa'
#test
#parse = True
#i =100
#while parse ==True:
#    pageAPNewsBriefs = requests.get(urlAPNewsBriefs)
#    soupAPNewsBriefs = BeautifulSoup(pageAPNewsBriefs.content, 'lmxl')
#parse = False
#if(i<500):
#    urlAPNewsBriefs = 'https://nashville.craigslist.org/search/apa' + '?s=' + i
#    i=100
#    parse= True
#selenium
#pageAPNewsBriefs = browser.get(urlAPNewsBriefs)

pageAPNewsBriefs = requests.get(urlAPNewsBriefs)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soupAPNewsBriefs = BeautifulSoup(pageAPNewsBriefs.content, 'lxml')

#soupAPNewsBriefs = BeautifulSoup(browser.page_source, 'lxml')
#browser.quit()

# Parse APNewsBriefs url
# 'position' marks the beginning of each news brief in the html
# All other data is found in its relationship to 'position'
for brief in soupAPNewsBriefs.find_all('p', class_='result-info'):

    if brief.find('span', class_='result-hood') :
        location = brief.find('span', class_='result-hood').string
    else:
        location = 'Not listed'

    if brief.find('span', class_='result-price'):
        price = brief.find('span', class_='result-price').string
    else:
        price = 'Not listed'

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
