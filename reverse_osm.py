from bs4 import BeautifulSoup
import re
import csv
import pandas as pd
import requests
from geopy.geocoders import Nominatim

ipDF=pd.read_csv('Input2.csv')
osm_list=list(ipDF["Column1.id"])[:20]
outfile=open("reverse_osm.csv","w",newline='')
csv_write=csv.writer(outfile)
csv_write.writerow(["OSM","Building Name","Address","Postal Code", "City", "Latitude", "Longitude"])
# print(osm_list)
#https://www.openstreetmap.org/way/375257537      #Sample for Taj mahal
#https://www.openstreetmap.org/node/1959174767    #
#append osm id to the url here

def zae(dataframe):
    dataframe['Latitude'] = None
    dataframe['Longitude'] = None
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(dataframe.loc[0,'Address'])
    if location != None:
        dataframe.loc[0,'Latitude'] = location.latitude   
        dataframe.loc[0,'Longitude'] = location.longitude
    print(dataframe)
    return [dataframe.loc[0,'Latitude'],dataframe.loc[0,'Longitude']]

count=0
successcount=0
failcount=0
for osm in osm_list:
    #osm=375257537
    searchurl="https://www.openstreetmap.org/way/"+str(osm)
    source=requests.get(searchurl).text
    soup=BeautifulSoup(source,'lxml')
    osmtable=soup.find("table",attrs={"class":"browse-tag-list"})
    # print(osmtable)
    print("OSM number {}".format(count))
    count+=1
    keys=[]
    values=[]
    kv={}
    if osmtable==None:
        print("No entry available")
    else:
        for key,val in zip(osmtable.find_all("tr"),osmtable.find_all("tr")):
            for keyf,valf in zip(key.find_all("th"),val.find_all("td")):
                # print(btf)
                kv[keyf.text.replace('\n','').strip()]=valf.text.replace('\n','').strip()
        print("Dictionary found is : {}\n-----------".format(kv))
        name=""
        city=""
        postcode=""
        final_addr=""
        if "name" in list(kv.keys()):
            name=kv["name"]
        if "addr:housenumber" in list(kv.keys()):
            final_addr+=kv["addr:housenumber"] + " "
        if "addr:street" in list(kv.keys()):
            final_addr+=kv["addr:street"] + " "
        if "addr:city" in list(kv.keys()):
            final_addr+=kv["addr:city"] + " "
            city=kv["addr:city"]    
        if "addr:postcode" in list(kv.keys()):
            final_addr+=kv["addr:postcode"] 
            postcode=kv["addr:postcode"]    
        if final_addr!="" or name!="" or city!="" or postcode!="":
            if final_addr=="":
                final_addr=None
            if name=="":
                name=None
            if postcode=="":
                postcode=None
            if city=="":
                city=None
            if final_addr!= None:
                df=pd.DataFrame({'Address':[final_addr]})
                x=zae(df)
            elif name!=None:
                df=pd.DataFrame({'Address':[name]})
                x=zae(df) 
            csv_write.writerow([osm,name,final_addr,postcode,city,x[0],x[1]])
            successcount+=1
failcount=count-successcount
print("\n----------------------Summary----------------------")
print("Number of OSM ids Scanned : {}".format(count))
print("Number of entries fetched successfully : {}".format(successcount))
print("Number of entries failed to fetch : {}".format(failcount))
print("Done")    






