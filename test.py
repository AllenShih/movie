
# -*- coding: utf-8 -*-

import urllib3
from bs4 import BeautifulSoup
import requests
import re
import csv


# 奧斯卡最佳電影爬蟲
# ----------------------------------------------------------------------------------------------------------------------------------
# res = requests.get('https://zh.wikipedia.org/zh-tw/%E5%A5%A5%E6%96%AF%E5%8D%A1%E6%9C%80%E4%BD%B3%E5%BD%B1%E7%89%87%E5%A5%96')
# soup = BeautifulSoup(res.text, "lxml")
#
# areas=soup.find_all('li')
# for eachArea in areas :
#         if eachArea.find('b'):
#                 s=eachArea.find('a')
#                 print(s['title'])
# ----------------------------------------------------------------------------------------------------------------------------------

# data saving
K = open("電影檔案整理.csv","w",newline='')
w = csv.writer(K)
top_row=['movie', 'URL']
w.writerow(top_row)



res = requests.get('http://www.imdb.com/')
soup = BeautifulSoup(res.text, "lxml")
areas = soup.find_all(text=re.compile('In Theaters'))

cnt=0
for eachArea in areas:
    if cnt==0:
        st='http://www.imdb.com'+eachArea.previous_element['href'];

        print(st)
        print('--------------------------')
        res1=requests.get(st)
        soup1 = BeautifulSoup(res1.text, "lxml")

        h4_elements=soup1.find_all('h4')
        for element in h4_elements:
            temp=[]

            temp.append(element.next_element['title'])
            st='http://www.imdb.com'+element.next_element['href'];
            u = urllib3.urlopen(st)
            temp.append(u.geturl())
            w.writerow(temp)
    cnt+=1
