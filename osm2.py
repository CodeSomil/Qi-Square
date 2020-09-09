
import requests
from bs4 import BeautifulSoup
import re

source= requests.get("https://www.openstreetmap.org/geocoder/search_osm_nominatim?query=st+vincents").text

soup=BeautifulSoup(source,'html.parser')

# print(soup.a)

# link=soup.find_all('a')
# print(link.get('href'))
l =[]
for link in soup.find_all('a'):
    link=str(link.get('href'))
    try:
        spl=link.split('/')
        stp1=spl[2]
    except Exception as e:
        stp1=None
    l.append(stp1)
    # print(stp1)

    


print(l[0])
