import requests
import datetime

today = str(datetime.datetime.now()).split(' ')[0]

sites = {'craigslist': 'https://nashville.craigslist.org/search/apa',
         'Belmont':'http://www.belmont.edu/'}

for name, link in sites.items():
    response = requests.get(link)
    html = response.content

    fileName = today + '.' + name + '.html'
    outfile = open(fileName, "wb")
    outfile.write(html)
    outfile.close()
