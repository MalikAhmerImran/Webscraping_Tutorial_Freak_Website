import requests 
from bs4 import BeautifulSoup
import pandas as pd

response=requests.get('https://www.iplt20.com/auction/2022')
print(response)

soup=BeautifulSoup(response.content,'html.parser')

table=soup.find('table',class_="ih-td-tab auction-tbl")

# print(table)

table_headers=table.find_all('th',class_='skip-filter')

# print(table_headers)
header_list=[]

for header in table_headers:

    header_list.append(header.text)


df=pd.DataFrame(columns=header_list)



# print(df)

rows=table.find_all('tr')

for row in rows[1:]:

    table_data=row.find_all('td')
    
    row=[tr.text for tr in table_data]

    df.loc[len(df)]=row

   

print(df)    
    
