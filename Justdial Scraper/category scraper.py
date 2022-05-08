from selenium import webdriver
import selenium.webdriver.common.keys
import selenium.webdriver.common.by
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import csv
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications": 1 })
chrome_path=r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(chrome_path,options=option)
driver.get("https://www.justdial.com")
html_list =driver.find_element_by_id("sidebarnavleft")
items = html_list.find_elements_by_tag_name("li")
for item in items:
        text = item.text
        print (text)
                
