# -*- coding:utf-8 -*-
__author__ = 'lenovo'

from bs4 import BeautifulSoup
import urllib2 as u
html = u.urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

# for child in bsObj.find("table", {"id": "giftList"}).children: #查找id为giftList的table标签的下一级标签，即tr标签
#     print(child)
for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings: #查找id为giftList的table标签的兄弟标签，即除自身之外的tr标签
    print(sibling)