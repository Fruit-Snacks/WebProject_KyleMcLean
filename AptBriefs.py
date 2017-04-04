import requests
from bs4 import BeautifulSoup

# Scrape APNewsBriefs with requests
urlAPNewsBriefs = 'https://www.apartments.com/nashville-tn/?bb=qrwyv87s3Ig4_x5mY'
pageAPNewsBriefs = requests.get(urlAPNewsBriefs)
# j
# Prepare for parsing APNewsBriefs with BeautifulSoup
soupAPNewsBriefs = BeautifulSoup(pageAPNewsBriefs.content, 'lxml')

position = soupAPNewsBriefs.find('div', class_='location')
location = position.string
brief = soupAPNewsBriefs.find('div', class_='apartmentRentRollupContainer')
price = brief.find('span', class_='altRentDisplay').string
size = brief.find('span', class_='unitLabel').string
contact = soupAPNewsBriefs.find('div', class_='phone')
phone = contact.find('span').string
postTime = soupAPNewsBriefs.find('span', class_='lastUpdated')
time = postTime.find('span').string + ' ago'


print(location)
print(price)
print(size)
print(phone)
print(time)
