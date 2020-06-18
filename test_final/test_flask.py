import re
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    driver.get("https://ebus.gov.taipei/VirtualStop/1156800620")
    regexp = re.compile("^藍23$")
    soup = BeautifulSoup(driver.page_source, "lxml")
    tag_list = soup.find_all(text=regexp)
    print(tag_list)
    return "hello"
if __name__ == "__main__":
    driver = webdriver.Chrome("./chromedriver")
    driver.implicitly_wait(10)
    
    
    app.run(host = "0.0.0.0", port = 8080)
    




