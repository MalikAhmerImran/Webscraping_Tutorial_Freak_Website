import requests
from bs4 import BeautifulSoup

web=requests.get('https://www.tutorialsfreak.com/')

print(web.status_code)