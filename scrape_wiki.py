# -*- coding:utf-8 -*-
__author__ = 'lenovo'
from bs4 import BeautifulSoup
import urllib2 as u
import re
html = u.urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon") #爬取维基百科网页，与Kevin_Bacon相关联的链接
bsObj = BeautifulSoup(html, "html.parser")

# for link in bsObj.findAll("a"): #寻找页面的a链接
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if "href" in link.attrs:
        print(link.attrs["href"])
        