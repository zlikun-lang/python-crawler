# coding:utf-8
# author:zlikun

from urllib import request, parse

req = request.Request('https://www.oschina.net')

# 添加请求消息头
req.add_header(
    "User-Agent",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")

# 执行请求，返回 response 实例
resp = request.urlopen(req)

# <class 'http.client.HTTPResponse'>
print(type(resp))

# 读取响应内容，并解码
# print(resp.read().decode('utf-8'))


# 进行POST请求
req = request.Request('http://httpbin.org/post',
                      data=parse.urlencode({'name': 'zlikun', 'gender': 'male'}).encode('utf-8'),
                      headers={"User-Agent":
                                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"})

req.add_header('Host', 'httpbin.org')

resp = request.urlopen(req)

# {"args":{},"data":"","files":{},"form":{"gender":"male","name":"zlikun"},"headers":{"Accept-Encoding":"identity","Connection":"close","Content-Length":"23","Content-Type":"application/x-www-form-urlencoded","Host":"httpbin.org","User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"},"json":null,"origin":"27.27.200.117","url":"http://httpbin.org/post"}
print(resp.read().decode('utf-8'))
