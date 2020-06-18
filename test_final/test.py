import re
from selenium import webdriver
import time
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://ebus.gov.taipei/VirtualStop/1156800620")
#print(driver.title)
html = driver.page_source
match = re.search('<p class="auto-list-routelist-bus">藍39</p>(.*?)</a>',html, re.S)
match2 = re.search('<span class="auto-list-routelist-time-in">(.*?)</span>',match.group(1), re.S)

#print(match.group(1))
print(match2.group(1))
#print(html)
driver.quit()

