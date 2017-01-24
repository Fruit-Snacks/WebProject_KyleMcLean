import requests
from bs4 import BeautifulSoup

# Scrape APNewsBriefs with requests
urlAPNewsBriefs = 'http://www.rent.com/tennessee/nashville-houses/74-491'
pageAPNewsBriefs = requests.get(urlAPNewsBriefs)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soupAPNewsBriefs = BeautifulSoup(pageAPNewsBriefs.content, 'lxml')


brief = soupAPNewsBriefs.find('p', class_='prop-address')
locationRegion = brief.find('span', itemprop='addressRegion')
locationRegion.replace_with('')
locationState = brief.find('span')
locationState.replace_with('')
location = brief.find('span').string
cost = soupAPNewsBriefs.find('p', class_='prop-rent')
price = cost.find('span').string
size = soupAPNewsBriefs.find('span', class_='prop-beds bullet-separator').string
phone = soupAPNewsBriefs.find('strong', class_='tel').string

#jjj

print(location)
print(price)
print(size)
print(phone)

