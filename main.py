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

