import requests
from bs4 import BeautifulSoup

# Scrape APNewsBriefs with requests
urlAPNewsBriefs = 'https://nashville.craigslist.org/search/apa'
pageAPNewsBriefs = requests.get(urlAPNewsBriefs)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soupAPNewsBriefs = BeautifulSoup(pageAPNewsBriefs.content, 'lxml')

location = soupAPNewsBriefs.find('span', class_='result-hood').string

brief = soupAPNewsBriefs.find('ul', class_='rows')
price = brief.find('span', class_='result-price').string
size = brief.find('sup').previousSibling.string
#price = brief.find('span', class_='altRentDisplay').string
#size = brief.find('span', class_='unitLabel').string
#contact = soupAPNewsBriefs.find('div', class_='phone')
#phone = contact.find('span').string
#postTime = soupAPNewsBriefs.find('span', class_='lastUpdated')
#time = postTime.find('span').string + ' ago'


print(location)
print(price)
print(size)
#print(phone)
#print(time)
