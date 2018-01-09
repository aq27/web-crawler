# -*- coding:utf-8 -*-
__author__ = 'lenovo'
from bs4 import BeautifulSoup
import urllib2 as u
import re
import random
# html = u.urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon") #爬取维基百科网页，与Kevin_Bacon相关联的链接
# bsObj = BeautifulSoup(html, "html.parser")

#寻找页面的a链接
# for link in bsObj.findAll("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

#过滤链接
# for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
#     if "href" in link.attrs:
#         print(link.attrs["href"])

#定义寻找链接函数
# def getLink(articleUrl):
#     html = u.urlopen("http://en.wikipedia.org/"+articleUrl)
#     bsObj = BeautifulSoup(html, "html.parser")
#     return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
# links = getLink("/wiki/Kevin_Bacon")
# while len(links) > 0:
#     newarticle = links[random.randint(0,(len(links)-1))].attrs["href"]
#     print(newarticle)
#     links = getLink(newarticle)

#过滤重复链接
pages = set()
def getLinks(articleUrl):
    global pages
    html = u.urlopen("http://en.wikipedia.org/"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.find_all("a", href=re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                newPage = link.attrs["href"]
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")