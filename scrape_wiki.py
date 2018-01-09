# -*- coding:utf-8 -*-
__author__ = 'lenovo'
from bs4 import BeautifulSoup
import urllib2 as u
html = u.urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
