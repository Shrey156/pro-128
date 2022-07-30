from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(START_URL)


soup = BeautifulSoup(page.text,'html.parser')

star_t = soup.find_all('table')

temp_list = []
table_r = star_t[7].find_all('tr')

for tr in table_r:
    td = tr.find_all('td')
    row = [i.text.strip()for i in td]
    temp_list.append(row)

Star_names = []
Distance = []
Mass = []
Radius =  []

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][0]) 
    Distance.append(temp_list[i][5]) 
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])
    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)
df2.to_csv("dwarf_stars.csv")