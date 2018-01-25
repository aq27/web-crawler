#-*- coding:utf-8 -*-
__author__ = 'lenovo'

import urllib2 as u
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict

def cleanInput(input):
    input = input.upper()
    input = re.sub("\n+", " ", input)  #空格代替换行符或者多个换行符
    input = re.sub("\[[0-9]\]*", "", input) #删除【1】序号类
    input = re.sub(" +", " ", input)  #空格代替多个连续的空格
    input = bytes(input)   #将input装换为字节序列
    input = input.encode("ascii", "ignore")  #将input转换为ascii编码格式
    cleanInput = []
    input = input.split(' ')

    for item in input:
        item = item.strip(string.punctuation) #删除item中的所有标点符号
        if len(item)>1 or (item.lower()=='i' or item.lower()=='a'):
            cleanInput.append(item)
    return cleanInput
def ngram(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        print input[i:i+n]
        output[str(input[i:i+n])] = output.setdefault(str(input[i:i+n]), 0)+1 #截取input每n个词,存放到output中

    return output

html = u.urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngram = ngram(content, 2)
ngram = OrderedDict(sorted(ngram.items(), key=lambda t: t[1], reverse = True))
print ngram
print "2-ngram count is:"+str(len(ngram))