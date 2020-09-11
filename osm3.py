import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import csv

ipDF=pd.read_csv('Input.csv')
#print(ipDF.columns)
#li=list(ipDF['Building Name\n'])
count=1
na=0
c=0
b_name_list=list(ipDF['Building Name\n'])[:100]
b_add_list=list(ipDF['Building Address'])[:100]
lines=len(list(b_name_list))
output_file=open("output_osm.csv","w",newline='')
csv_write=csv.writer(output_file)
csv_write.writerow(["Building Name", "Country" , "Zip Code", "OSM id"])

for i,j in zip(b_name_list,b_add_list):
    if type(i)==str and type(j)==str:
        #print(j)
        country_zip=j.split(sep=',')[1]
        country=country_zip.split()[0]
        zipp=country_zip.split()[1]
        c+=1


        search_url="https://www.openstreetmap.org/geocoder/search_osm_nominatim?query="
        search_url=search_url+i+"+"+country+"+"+zipp
        #print(search_url)
        source= requests.get(search_url).text
        soup=BeautifulSoup(source,'html.parser')
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

    
        print("count:{}: OSM for {} {} {} is :".format(count,i,country,zipp),end='')
        if len(l)>0:
            print(l[0])
            csv_write.writerow([i,country,zipp,l[0]])
            
        else:
            na+=1
            csv_write.writerow([i,country,zipp,"Not available"])
            # print("Not available")
        
        
        #print(i,"  {}".format(count))
        count+=1
print("\n\n ----------Summary----------\n\n")
print("Number of records scanned :- {} \n Missing data records :- {} \n Total OSM ids found :- {} \n Unavailable OSM:- {}".format(lines,(lines-c),(c-na),na))

#opDF=ipDF
#opDF['OSM']=li
