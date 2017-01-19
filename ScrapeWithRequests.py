import requests
import datetime

today = str(datetime.datetime.now()).split(' ')[0]

sites = {'craigslist': 'https://nashville.craigslist.org/search/apa',
         'apartments.com':'https://www.apartments.com/nashville-tn/',
         'rent.com':'http://www.rent.com/tennessee/nashville-houses/'}

for name, link in sites.items():
    response = requests.get(link)
    html = response.content

    fileName = today + '.' + name + '.html'
    outfile = open(fileName, "wb")
    outfile.write(html)
    outfile.close()
