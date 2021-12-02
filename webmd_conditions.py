import requests 
import urllib.request
from urllib.request import Request, urlopen
#import urllib2
import csv
import re
import os
#from urllib import urlopen
from bs4 import BeautifulSoup
import lxml
import pandas as pd


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
url = "http://www.webmd.com"
headers={'User-Agent':user_agent,} 
request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() # The data u need

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