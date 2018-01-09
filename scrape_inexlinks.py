# -*- coding: utf-8 -*-
__author__ = 'lenovo'
from bs4 import BeautifulSoup
import urllib2 as u
import random
import re
import datetime
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

pages = set()
random.seed(datetime.datetime.now())

#获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    #找出所有以“/”开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs["href"] is not None:
            # href = "http://" + re.sub("^(.|/)+", "", link.attrs["href"])
            if link.attrs["href"] not in internalLinks:
                internalLinks.append(link.attrs["href"])
    return internalLinks

# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    #除了参数链接的所有外部链接
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs["href"])
    return externalLinks

#分割链接地址
def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = u.urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        print len(externalLinks)
        internalLinks = getInternalLinks(bsObj, splitAddress(startingPage)[0])
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        print len(externalLinks)
        print externalLinks[random.randint(0, len(externalLinks)-1)]
        return externalLinks[random.randint(0, len(externalLinks)-1)]
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print externalLink
    # print("随机外链是：" + externalLink)
    try:
        followExternalOnly(externalLink)
    except (u.HTTPError,ValueError,u.URLError):
        print None
        followExternalOnly(startingSite)
allExLinks = set()
allInLinks = set()
def getAllExternalLinks(siteUrl):
    html = u.urlopen(siteUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    internalLinks = getInternalLinks(bsObj,splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj,splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExLinks:
            print("即将获取外部链接的URL是："+link)
            allExLinks.add(link)
    for link in internalLinks:
        if link not in allInLinks:
            print("即将获取内部链接的URL是："+link)
            allInLinks.add(link)
getAllExternalLinks("http://oreilly.com")





