# -*- coding:utf-8 -*-
__author__ = 'lenovo'

import csv

csvFile = open("../web crawler/test.csv", 'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2')) #CSV文件通过writerow方法输出
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csvFile.close()
