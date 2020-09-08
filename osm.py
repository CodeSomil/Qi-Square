from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.openstreetmap.org/search?query=st+vincents").text
source2= requests.get("https://www.openstreetmap.org/geocoder/search_osm_nominatim?query=st+vincents").text

soup = BeautifulSoup(source2,'lxml')

# print(soup.prettify())

res=soup.find('body')
print(res)

summ= soup.find('div',class_="search_results_entry")
# print(summ)

hu=soup.find('ul',class_="results-list list-group list-group-flush")
# print (hu)

# for link in soup.find_all('a',href=True):
#     print(link['href'])

# cla=soup.find_all(class_="list-group-item search_results_entry")
# print(cla)



#<li class="list-group-item search_results_entry">School <a class="set_position" 
#class="results-list list-group list-group-flush"