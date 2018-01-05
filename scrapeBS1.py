# -*- coding:utf-8 -*-
__author__ = 'lenovo'
#使用BeautifulSoup，基于CSS来爬取内容

import urllib2 as u
from bs4 import BeautifulSoup
html = u.urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")  #获取HTML的全部代码
nameList = bsObj.findAll("span", {"class": "green"}) #nameList为一个列表，获取到包含class：“green”的span标签,包括标签、标签内的文字
for name in nameList:
    print(name.get_text()) #.get_test()清除HTML标签，返回只包含文字的字符串


