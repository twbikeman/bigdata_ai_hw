import requests
from bs4 import BeautifulSoup
r = requests.get('https://ebus.gov.taipei/EBus/VsSimpleMap?gb=0&routeid=0412000100')
r.encoding = "utf-8"
soup = BeautifulSoup(r.text, "lxml")
print(soup)
