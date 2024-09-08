import requests 
from bs4 import BeautifulSoup
titles=[]
prices=[]
images=[]
for i in range(1,5):
    url="https://www.flipkart.com/cameras/dslr-mirrorless/pr?sid=jek%2Cp31%2Ctrv&page="+str(i)
    print(url)

    response=requests.get(url)

    print(response)

    soup=BeautifulSoup(response.content,'html.parser')
   

    for data in soup.find_all('div',class_='tUxRFH'):
        title=data.find('div',class_='KzDlHZ')
        titles.append(title.string)
        price=data.find('div',class_='Nx9bqj _4b5DiR')
        prices.append(price.string)
        print(titles)
        print(prices)
    

print(titles)
print(prices)

