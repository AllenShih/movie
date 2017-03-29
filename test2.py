# -*- coding: utf-8 -*-
import movie
import csv
import re
import urllib3
from bs4 import BeautifulSoup
import json
import requests
from selenium import webdriver
#from urllib3 import urlencode
res = requests.get('http://www.imdb.com/')
soup = BeautifulSoup(res.text, "lxml")
areas=soup.find_all(text=re.compile('In Theaters'))
st=[]
i=0
for eachArea in areas:
        st.append('http://www.imdb.com'+eachArea.previous_element['href'])
        res1=requests.get(st[i])
        i=i+1
        soup1 = BeautifulSoup(res1.text, "lxml")

for est in st:
        print(est)


movieAll=[]
h4_elements=soup1.find_all('h4')
for element in h4_elements:
        text=element.next_element.text
        genreT=element.find_next('p')
        genre=genreT.find_all('span', itemprop="genre")
        time=element.find_next('time', itemprop="duration").text
        href='http://www.imdb.com'+element.next_element['href']
        temp=movie.Movie(text,genre,time,href)
        movieAll.append(temp)
        
K = open("電影檔案整理.csv","w",newline='')
w = csv.writer(K)
top_row=['Title', 'Time', 'Genre', 'URL']
w.writerow(top_row)

for movieP in movieAll:
        print('\n')
        movieP.print_all()
        movieP.createCSV(w)
K.close()
  
#print(re.split('([w]+)', 'WordsW, words, words.',flags=re.IGNORECASE))
#print( soup1.text)
