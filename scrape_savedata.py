# -*- coding:utf-8 -*-
__author__ = 'lenovo'

from bs4 import BeautifulSoup
import urllib2 as u
import urllib

html = u.urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
urllib.urlretrieve(imageLocation, "logo.jpg") #urlretrieve方法将远程获取的数据下载到本地，默认存放在程序运行的文件夹

