from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.openstreetmap.org/search?query=st+vincents+high+school").text

soup = BeautifulSoup(source,'lxml')

# print(soup.prettify())

summ= soup.find('div',class_="search_results_entry")
print(summ)

hu=soup.find('ul',class_="results-list list-group list-group-flush")
# print (hu)

# for link in soup.find_all('a',href=True):
#     print(link['href'])

# cla=soup.find_all(class_="list-group-item search_results_entry")
# print(cla)



#<li class="list-group-item search_results_entry">School <a class="set_position" 
#class="results-list list-group list-group-flush"