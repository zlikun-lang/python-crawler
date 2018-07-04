# coding:utf-8
# author:zlikun

from urllib import request

# 读取txt文档
url = 'https://en.wikipedia.org/robots.txt'

result = request.urlopen(url).read().decode('utf-8')

print(result)
