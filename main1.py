import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'

repsonse=requests.get(url)

print(repsonse)

soup=BeautifulSoup(repsonse.text,'html.parser')

# print(soup)

boxes=soup.find_all('div',class_="col-md-4 col-xl-4 col-lg-4")

print("Total Boxes=",len(boxes))

print(boxes)

#getting the names of all the tablets 

product_names=[]

product_prices=[]

names=soup.find_all('a',class_='title')

# print(names)

for name in names:
    name=name.text
    print(name)

    product_names.append(name)
    
    # names.append(name)
print(product_names)


prices=soup.find_all('h4',class_='price float-end card-title pull-right')   


for price in prices:
    
    price=price.text

    product_prices.append(price)

print(product_prices)    


dic={
    "names":product_names,

    "prices":product_prices
}

df=pd.DataFrame(dic)

print(df)

df.to_csv('C:\\Users\\HP\Desktop\\ahmer\\E-Commerce_Website_Scraping\\data.csv')

print('data saved successfully')