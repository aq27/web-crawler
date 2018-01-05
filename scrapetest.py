# -*- coding: utf-8 -*-
__author__ = 'lenovo'
#使用python2中的urllib2标准库
import urllib2 as u
from bs4 import BeautifulSoup
def getTitle(url): #url="http://pythonscraping.com/pages/page1.html"
    try:
        html = u.urlopen(url)
    except u.HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")   #需指定解析器（本程序使用html.parser）；否则，运行提示警告
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)

