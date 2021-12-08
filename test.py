#import requests 
#import urllib.request
#from urllib.request import Request, urlopen
import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import os
import time
import csv
import re
#from bs4 import BeautifulSoup
#import lxml

option = webdriver.ChromeOptions() #had to add chromedriver to be in PATH on my computer 
option.add_argument("--incognito")
option.add_argument('--ignore-certificate-errors')

browser = webdriver.Chrome()
url = "https://www.webmd.com/drugs/2/index"
browser.get(url)
time.sleep(2)

#Create list of URLs we need to open


#Search for all drugs that start with "A"
def search_a():
    url_a = "https://www.webmd.com/drugs/2/alpha/a"
    browser.get(url_a)
    time.sleep(2)

    #create list of URLs we need to open
    a_drugs = ["/aa","/ab","/ac","/ad","/af","/ag","/ah","/ak","/al","/am","/an","/ap","/aq","/ar","/as","/at","/au","/av","/aw","/ax","/az"]
    url_list = []
    #iterate in order to create URLs
    for drugs in a_drugs:
        url_to_add= "https://www.webmd.com/drugs/2/alpha/a" + str(a_drugs)
        url_list.append(url_to_add)
        print(url_list)
        
        

        #Create blank frame - this is where we add the data we scrap
        a_frame = pd.DataFrame(columns=["anames"])

    #First loop: we iterate over the different webpages we created previously
    for webpage in url_list:

        #We open the page
        browser.get(webpage)

        #On the webpage that is currently open, we create a list of all the listings
        anames = browser.find_elements('/html/body/div[1]/main/div/div[2]')
        
        #Second loop: we iterate over the listings in order to find each listing's details
        for aname in anames:

            #Extract the text from each listing
            a_meds_data = aname.text

            #Create a dictionary
            a_meds_data = {"'A' list": a_meds_data}

            #Add dictionary to a dataframe
            a_frame = pd.DataFrame(a_meds_data, columns=["A drug names"], index=[0])

            #Append frame to main dataframe
            a_frame = a_frame.append(a_frame, ignore_index=True)

            #Wait time
            time.sleep(2)

            #Print frame (Work in progress)
            print(a_frame)

        #Now that the second loop is closed, we go over to the first loop and open the second URL
        #We then launch the second loop over the second URL

    #Print final main frame
    print(a_frame)

    #Our taks is exectued, we quit the browser
    browser.quit()

#excute the function
search_a()
    















#driver = webdriver.Chrome()
#driver.get('https://www.webmd.com/drugs/2/index')


#code to find user agent:
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#object of Options class
#op = webdriver.ChromeOptions()
#set chromedriver.exe path
#driver = webdriver.Chrome()
#maximize browser
#driver.maximize_window()
#launch URL
#driver.get("https://www.seleniumhq.org/download/");
#get user Agent with execute_script
#a= driver.execute_script("return navigator.userAgent")
#print("User agent:")
#print(a)
#close browser session
#driver.quit()


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
##url = "http://www.webmd.com"
#headers={'User-Agent':user_agent,} 
#request=urllib.request.Request(url,None,headers) #The assembled request
#response = urllib.request.urlopen(request)
#data = response.read() # The data u need
# ^^ this code is giving me the http error 403 forbidden when i run it, but without this code chrome driver is still working and opening up a new window of webmd drug index

"""""
def get_links(div_class, url):
    html = urllib.request.urlopen(url)
    bsObj = BeautifulSoup(html,"lxml")
    links = bsObj.find("div", {"class":div_class}).findAll("a")
    return links


root_web = 'http://www.webmd.com'
urlpath = 'http://www.webmd.com/drugs/2/conditions/index'

for link in get_links("drugs-browse-box", urlpath):
    if 'href' in link.attrs:
        link_url = root_web + link.attrs['href']
        if "offmarket" in link_url:
            print ("ignored")
        else:
            print (link_url)
            for link in get_links("drug-list-container", link_url):
                if 'href' in link.attrs:
                    link_url = root_web + link.attrs['href']
                    if "offmarket" in link_url:
                        print ("ignored")
                    else:
                        print (link_url)
                        if "offmarket" in link_url:
                            print ("ignored")
                        else:
                            r=requests.get(link_url)                    
                            soup = BeautifulSoup(r.text,'lxml')
                            table=soup.find("table", {"drugs-treatments-table"})
                            rows=table.findAll("td")
                            y=link_url.split('/',6)
                            for thing in y:
                                cond_name=y[6]
                                print (cond_name)
                                break
                            for td in rows:
                                tags=td.findAll("a")
                                for a in tags: 
                                    name1=a.text
                                    print (name1)                         
                                    with open('index2.csv', 'a') as csv_file:
                                        writer=csv.writer(csv_file)
                                        writer.writerow([cond_name,name1])

for link in get_links("drugs-browse-box", urlpath):
    if 'href' in link.attrs:
        link_url = root_web + link.attrs['href']
        if "offmarket" in link_url:
            print ("ignored")
        else:
            print (link_url)
            for link in get_links("drugs-browse-subbox", link_url):
                if 'href' in link.attrs:
                    link_url = root_web + link.attrs['href']
                    print (link_url)
                    drug = ''
                    for link in get_links("drug-list-container",link_url):
                        if 'href' in link.attrs:
                            link_url = root_web + link.attrs['href']
                            print (link_url)
                            y=link_url.split('/',7)
                            for thing in y:
                                drug_name=y[6]
                                print (drug_name)
                                break
                            try:
                                html=urlopen(link_url)
                                bsobj=BeautifulSoup(html,"lxml")
                                links=bsobj.find("div", {"class":"side-effects"})        
                                name1=links.text
                                print (name1)     
                            except:
                                pass
                            with open('index.csv', 'a') as csv_file:
                                writer=csv.writer(csv_file)
                                writer.writerow([drug_name,name1])













#drug_side_effects = driver.find_elements_by_xpath('//td[@class="//*[@id="ContentPane28"]/div/div[2]"]')
#side_effects_list = []
#for p in range(len(players)):
    #players_list.append(players[p].text)




#import time
#from selenium import webdriver
#driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
#driver.get("http://www.webmd.com/drugs/index");
#time.sleep(5) # Let the user actually see something!
#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
#search_box.submit()
#time.sleep(5) # Let the user actually see something!
#driver.quit()

#from selenium.webdriver import Chrome
#driver = Chrome()
#from webdriver_setup import get_webdriver_for
#driver = get_webdriver_for("Chrome")


#set the path to the chromedriver executable- 
#Chrome(executable_path='/path/to/chromedriver')
"""
