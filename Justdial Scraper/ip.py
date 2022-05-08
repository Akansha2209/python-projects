from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import bs4
from fake_useragent import UserAgent
import random

ua=UserAgent()
proxies=[]
headers = {'User-Agent':ua.random}
url='https://www.sslproxies.org/'
r=requests.get(url,headers=headers)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
proxies_table = soup.find(id='proxylisttable')
for row in proxies_table.tbody.find_all('tr'):
    proxies.append({
    'ip':   row.find_all('td')[0].string,
    'port': row.find_all('td')[1].string
  })

proxy_index = random.randint(0, len(proxies) - 1)
proxy = proxies[proxy_index]

print(proxy)

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications": 1 })

option.add_argument("ignore-certificate-errors")
option.add_argument('--proxy-server=http://{}'.format(proxy))
chrome=r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(chrome,options=option)
driver.get("https://web.skype.com/")
