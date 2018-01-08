# -*- coding:utf-8 -*-
__author__ = 'lenovo'

from bs4 import BeautifulSoup
import urllib2 as u
html = u.urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)

