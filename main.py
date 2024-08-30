import requests
from bs4 import BeautifulSoup

web=requests.get('https://www.tutorialsfreak.com/')

print(web.status_code)

soup=BeautifulSoup(web.content,'html.parser')

print(soup.prettify())

print(soup.title)

print(soup.title.name)

print(soup.p) #Printing the first paragraph of website

print(soup.a) #Printing the first anchor tag of website

print(soup.h1) #Printing the first header tag of website



# getting the tags from website

tag=soup.html

print(type(tag))

print(tag.p)

print(tag.a)

print(tag.h1)

# getting the navigable string from website

string=tag.p.string # getting the string from paragraph tag

print(string)

string=tag.h1.string #getting the string from  header tag

print(string)


print(soup.find("h1"))

print(soup.find_all("h2"))

print(soup.find_all('p'))

#get the data by class

class_data=soup.find('div',class_='wrapperr h-100')

print(class_data)

print(class_data.find_all('p'))

print(class_data.find_all('a'))

#get the data by id

print('printing data using id')

id_data=soup.find('div',id='__next')

print(id_data)

lines=soup.find_all('p')

print(lines)

for list in lines:
    print(list.text)


class_data=soup.find('p',class_="fs-16 fw-400 lh-24 label-color-1 card-text")

print(class_data.text)


# getting the links from website

links=soup.find_all('a')

print(links)

for link in links:
    print(link.get('href'))

# getting the image from the website   

images=soup.find_all('img')

print(images)

for image in images:
    print(image.get('src'))