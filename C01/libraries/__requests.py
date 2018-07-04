# coding:utf-8
# author:zlikun

import requests

# GET 请求
resp = requests.get('http://httpbin.org/ip')

# 200 {"origin":"27.27.200.117"}
print(resp.status_code, resp.text)

# GET 请求，带参数
resp = requests.get('http://httpbin.org/get', {'name': 'zlikun', 'age': 18, 'hobbies': ['摄影', '旅行']})

# 200
# {
#     'args': {
#         'age': '18',
#         'hobbies': [
#             '摄影',
#             '旅行'
#         ],
#         'name': 'zlikun'
#     },
#     'headers': {
#         'Accept': '*/*',
#         'Accept-Encoding': 'gzip,
#         deflate',
#         'Connection': 'close',
#         'Host': 'httpbin.org',
#         'User-Agent': 'python-requests/2.19.1'
#     },
#     'origin': '27.27.200.117',
#     'url': 'http: //httpbin.org/get?name=zlikun&age=18&hobbies=摄影&hobbies=旅行'
# }
print(resp.status_code, resp.json())

# POST 请求
resp = requests.post(url='http://httpbin.org/post',
                     data={'name': 'zlikun', 'age': 18, 'hobbies': ['摄影', '旅行']},
                     headers={
                         'user-agent': 'python/requests',
                         'host': 'httpbin.org',
                         'referer': 'https://zlikun.com'
                     })

# 200
# {
#     'args': {
#
#     },
#     'data': '',
#     'files': {
#
#     },
#     'form': {
#         'age': '18',
#         'hobbies': [
#             '摄影',
#             '旅行'
#         ],
#         'name': 'zlikun'
#     },
#     'headers': {
#         'Accept': '*/*',
#         'Accept-Encoding': 'gzip,
#         deflate',
#         'Connection': 'close',
#         'Content-Length': '72',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Host': 'httpbin.org',
#         'Referer': 'https: //zlikun.com',
#         'User-Agent': 'python/requests'
#     },
#     'json': None,
#     'origin': '27.27.200.117',
#     'url': 'http: //httpbin.org/post'
# }
print(resp.status_code, resp.json())

# PUT 请求
resp = requests.put('http://httpbin.org/put', {'id': 10000, 'name': 'zlikun'})
# 200
# {
#     'args': {
#
#     },
#     'data': '',
#     'files': {
#
#     },
#     'form': {
#         'id': '10000',
#         'name': 'zlikun'
#     },
#     'headers': {
#         'Accept': '*/*',
#         'Accept-Encoding': 'gzip,
#         deflate',
#         'Connection': 'close',
#         'Content-Length': '20',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Host': 'httpbin.org',
#         'User-Agent': 'python-requests/2.19.1'
#     },
#     'json': None,
#     'origin': '27.27.200.117',
#     'url': 'http: //httpbin.org/put'
# }
print(resp.status_code, resp.json())

# DELETE 请求，怎样携带参数？
resp = requests.delete('http://httpbin.org/delete?id=10000')

# 200
# {
#     'args': {
#         'id': '10000'
#     },
#     'data': '',
#     'files': {
#
#     },
#     'form': {
#
#     },
#     'headers': {
#         'Accept': '*/*',
#         'Accept-Encoding': 'gzip,
#         deflate',
#         'Connection': 'close',
#         'Content-Length': '0',
#         'Host': 'httpbin.org',
#         'User-Agent': 'python-requests/2.19.1'
#     },
#     'json': None,
#     'origin': '27.27.200.117',
#     'url': 'http: //httpbin.org/delete?id=10000'
# }
print(resp.status_code, resp.json())

# HEAD 请求
resp = requests.head('http://httpbin.org/get')
# 200
# {
#     'Connection': 'keep-alive',
#     'Server': 'gunicorn/19.8.1',
#     'Date': 'Wed, 04Jul201803: 16: 02GMT',
#     'Content-Type': 'application/json',
#     'Content-Length': '209',
#     'Access-Control-Allow-Origin': '*',
#     'Access-Control-Allow-Credentials': 'true',
#     'Via': '1.1vegur'
# }
print(resp.status_code, resp.headers)

resp = requests.options('http://httpbin.org/get')

# 200
# {
#     'Connection': 'keep-alive',
#     'Server': 'gunicorn/19.8.1',
#     'Date': 'Wed, 04Jul201803: 17: 37GMT',
#     'Content-Type': 'text/html;charset=utf-8',
#     'Allow': 'GET, OPTIONS, HEAD',
#     'Access-Control-Allow-Origin': '*',
#     'Access-Control-Allow-Credentials': 'true',
#     'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
#     'Access-Control-Max-Age': '3600',
#     'Content-Length': '0',
#     'Via': '1.1vegur'
# }
print(resp.status_code, resp.headers)
