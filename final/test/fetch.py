
import re
from selenium import webdriver
import time

class fetch():
    def __init__(self):
        self.driver = webdriver.Chrome("./chromedriver")            
        self.driver.get("https://ebus.gov.taipei/VirtualStop/1156800620")
        self.html = self.driver.page_source
        self.bus = ''
        self.dest = ''
        self.time = ''


    def getbus(self):
        return self.bus
    
    def getdest(self):
        return self.dest
    
    def gettime(self):
        return self.time

    
    def set(self, bus):
        self.bus = bus
        pattern = '<p class="auto-list-routelist-bus">{}</p>(.*?)</a>'
        match = re.search(pattern.format(self.bus), self.html, re.S)
        match2 = re.search('<img.*?>(.*?)</p>',match.group(1), re.S)
        self.dest = match2.group(1).replace("\n","")
        self.dest = self.dest.replace(" ","")
        self.dest = self.dest.replace("　","")
        match2 = re.search('time-in">(.*?)</span>',match.group(1), re.S)
        self.time = match2.group(1)

        
    def __del__(self):
        self.driver.quit()

