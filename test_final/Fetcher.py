import re
from selenium import webdriver
import time
driver = webdriver.Chrome("./chromedriver")
#driver.implicitly_wait(1)
driver.get("https://ebus.gov.taipei/VirtualStop/1156800620")
html = driver.page_source
bus='605副'
print(bus)
pattern = '<p class="auto-list-routelist-bus">{}</p>(.*?)</a>'
#print(pattern.format(bus))

match = re.search(pattern.format(bus), html, re.S)
#print(match.group(1))

match2 = re.search('<img.*?>(.*?)</p>',match.group(1), re.S)
dest = match2.group(1).replace("\n","")
dest = dest.replace(" ","")
dest = dest.replace("　","")
print(dest)
match2 = re.search('time-in">(.*?)</span>',match.group(1), re.S)
time = match2.group(1)
print(time)

driver.quit()

