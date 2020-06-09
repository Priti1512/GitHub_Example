import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import json # library to handle JSON files

#!pip install geopy 
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
#!pip install -U scikit-learn scipy matplotlib
from sklearn.cluster import KMeans

#!conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab
import folium # map rendering library

print('Libraries imported.')

import requests
website_url = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text

#!pip install BeautifulSoup4
from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'html.parser')
print(soup.prettify())


My_table = soup.find('table',{'class':'wikitable sortable'})
My_table


print(My_table.tr.text)

headers="Postcode,Borough,Neighbourhood"

table1=""
for tr in My_table.find_all('tr'):
    row1=""
    for tds in tr.find_all('td'):
        row1=row1+","+tds.text
    table1=table1+row1[1:]
print(table1)



file=open("toronto.csv","wb")
#file.write(bytes(headers,encoding="ascii",errors="ignore"))
file.write(bytes(table1,encoding="ascii",errors="ignore"))

import pandas as pd
df = pd.read_csv('toronto.csv',header=None)
df.columns=["Postalcode","Borough","Neighbourhood"]

df.head(10)

indexNames = df[ df['Borough'] =='Not assigned'].index

df.drop(indexNames , inplace=True)

df.head(10)
df.loc[df['Neighbourhood'] =='Not assigned' , 'Neighbourhood'] = df['Borough']
df.head(10)

result = df.groupby(['Postalcode','Borough'], sort=False).agg( ', '.join)

df_new=result.reset_index()
df_new.head(15)


df_new.shape
