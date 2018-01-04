# -*- coding: utf-8 -*-
__author__ = 'lenovo'

import urllib2 as u
from bs4 import BeautifulSoup
html = u.urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.h1)

