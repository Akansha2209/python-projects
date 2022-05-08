from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
import time
import csv
import re
import requests
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications": 1 })
chrome_path=r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(chrome_path,options=option)
file=open('G:\Justdial Scraper\category.csv','r')
read=csv.reader(file)
for row in read:
    s=len(row)
    i=0
    for i in range(s):
         q=row[i]
         print(q)
         i=i+1
         with open("G:\Justdial Scraper\Detail.csv","a+",newline="") as infile:
            writer = csv.writer(infile)
            writer.writerow(["Name","Address","Rating","PhoneNumber","Website","Email"])
            files=open('G:\Justdial Scraper\cities.csv','r')
            reader=csv.reader(files)
            for r in reader:
                     a=len(r)
                     j=0
                     for j in range(a):
                         w=r[j]
                         print(w)
                         j=j+1
                         
                         for k in range(0,61):
                              k=k+1
                              print("Page:"+str(k))
                              try:
                                          driver.get("https://www.justdial.com/Jaipur/Schools/page-{}".format(k))
                                          
                                          lenOfPage=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                                          match=False
                                          while(match==False):
                                             lastCount = lenOfPage
                                             time.sleep(3)
                                             lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                                             if lastCount==lenOfPage:
                                                 match=True

                                          soup=bs4.BeautifulSoup(driver.page_source,'html.parser')
                                          c=soup.find_all("li", {"class": "cntanr"})
                                          if len(c)==0:
                                             break
                                          else:
                                             for contain in c:
                                                         try:
                                                             name_contain=contain.find_all("span",{"class":"jcn"})
                                                             name=name_contain[0].text.strip()
                                                             time.sleep(1)
                                                         except Exception as e:
                                                             name=None
                                                            
                                                         print("Name:"+name)

                                                         try:
                                                             address_contain=contain.find_all("span",{"class":"mrehover"})
                                                             address=address_contain[0].text.strip()
                                                             time.sleep(1)
                                                         except exception as e:
                                                             address=None
                                                         print("Address:"+address)

                                                         try:
                                                                 rating_contain=contain.find_all("span",{"class":"green-box"})
                                                                 rating=rating_contain[0].text.strip()
                                                         except Exception as e:
                                                                 rating=None
                                                         print("Rating:"+str(rating))
                                                            

                                                         
                                                         try:
                                                             d={'<span class="mobilesv icon-ji"></span>':'9',
                                                             '<span class="mobilesv icon-lk"></span>':'8',
                                                             '<span class="mobilesv icon-nm"></span>':'7',
                                                             '<span class="mobilesv icon-po"></span>':'6',
                                                             '<span class="mobilesv icon-rq"></span>':'5',
                                                             '<span class="mobilesv icon-ts"></span>':'4',
                                                             '<span class="mobilesv icon-vu"></span>':'3',
                                                             '<span class="mobilesv icon-wx"></span>':'2',
                                                             '<span class="mobilesv icon-yz"></span>':'1',
                                                             '<span class="mobilesv icon-acb"></span>':'0',
                                                             '<span class="mobilesv icon-dc"></span>':'+',
                                                             '<span class="mobilesv icon-fe"></span>':'(',
                                                             '<span class="mobilesv icon-hg"></span>':')',
                                                             '<span class="mobilesv icon-ba"></span>':'-'
                                                             }
                                                             phoneNumber = ""
                                                             phone_number_contain=contain.find_all('p', {'class':'contact-info'})
                                                             phone_number_a=phone_number_contain[0].find('span')
                                                             phone_number_span=phone_number_a.find_all("span")
                                                                            
                                                             phoneNumber = ""
                                                             
                                                             for item in phone_number_span:                      
                                                                    phoneNumber+=d[str(item)]
                                                             time.sleep(2)
                                                         
                                                         except Exception as e:
                                                             phoneNumber = ""
                                                         print("PhoneNumber:"+phoneNumber)
                                               
                                                         try:
                                                             n=contain.find("span",{"class":"jcn"})
                                                             tags=n.find_all('a', href=True)
                                                             for i in tags:
                                                                     s=(i['href'])
                                                             url=s
                                                             driver.get(url)
                                                             soups=bs4.BeautifulSoup(driver.page_source,'html.parser')
                                                                          
                                                             
                                                             l=[]
                                                             for span in soups.find_all("span",{"class":"mreinfp comp-text"}):
                                                              
                                                                    for link in span.find_all('a'):
                                                                     
                                                                                    l.append(link.get('href'))
                                                             for val in l:
                                                                     if val==None:
                                                                               l.remove(val)
                                                             s=" "
                                                             b=s.join(l)
                                                          
                                                         except Exception as e:
                                                             b=None
                                                         print("Website:"+str(b))
                                                         time.sleep(2)
                                                         v=b
                                                         try:
                                                            url=v
                                                            s=driver.get(url)
                                                            lenOfPage=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                                                            match=False
                                                            while(match==False):
                                                             lastCount = lenOfPage
                                                             time.sleep(3)
                                                             lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                                                             if lastCount==lenOfPage:
                                                                 match=True

                                                            doc=driver.page_source
                                                            emails=re.findall(r"[\w\.-]+@[\w\.-]+",doc)
                                                            for email in emails:
                                                                pass

                                                         except Exception as e:
                                                            email=None
                                                         print("Email:"+str(email))
                                                         
                                                         writer.writerow([name,address,rating,phoneNumber,b,email])
                                                         print('--------------------')
                              except Exception as e:
                                 print(e)
                                 None
