# -*- coding:utf-8 -*-
__author__ = 'lenovo'

from bs4 import BeautifulSoup
import urllib2 as u
import re
html = u.urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

#查找id为giftList的table标签的下一级标签，即tr标签
# for child in bsObj.find("table", {"id": "giftList"}).children:
#     print(child)

#查找id为giftList的table标签的兄弟标签，即除自身之外的tr标签
# for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
#     print(sibling)

#寻找图片商品对应的价格
# print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

#通过正则表达式定位图片路径，来查找商品
images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])

