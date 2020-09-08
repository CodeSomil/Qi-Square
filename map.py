import requests
#r = requests.get('http://openstreetmap.org/way/223674050')
#r = requests.get('https://www.openstreetmap.org/search?query=st%20vincents%20high%20school#map=19/17.09138/120.97667')
r = requests.get('https://www.openstreetmap.org/geocoder/search_osm_nominatim?query=st+vincents+high+school')
print(r.status_code)
##print(r.headers)
##print(r.headers['Content-type'])
##print(r.text)
#print("TEXT",r.text)
file=open("test.txt",'w')
li=[r.text]
file.write(str(li))
print("Done")
