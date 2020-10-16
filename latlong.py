import pandas as pd
from geopy.geocoders import Nominatim

df=pd.DataFrame({'Address':['PUB Service Reservoir Singapore']})         
df['Latitude'] = None
df['Longitude'] = None
locator = Nominatim(user_agent="myGeocoder")

location = locator.geocode(df.loc[0,'Address'])
if location != None:
    df.loc[0,'Latitude'] = location.latitude   
    df.loc[0,'Longitude'] = location.longitude
print([df.loc[0,'Latitude'],df.loc[0,'Longitude']]) 

#61 Nanyang Drive Singapore 637335
#Nanyang Heights
#1.3438358	103.6887197

