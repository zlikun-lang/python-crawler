# coding:utf-8
# author:zlikun

import requests

# ================ 基础用法 ================

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

# ================ 进阶用法 ================
from requests import Request, Session

session = Session()
req = Request(method='GET',
              url='http://httpbin.org/basic-auth/zlikun/123456',
              headers={'user-agent': 'zlikun'},
              data={'name': 'zlikun', 'age': 18},
              auth=('zlikun', '123456'))

# 准备
# prepped = req.prepare()
prepped = session.prepare_request(req)
# http://httpbin.org/basic-auth/zlikun/123456
print(prepped.url)
# {'user-agent': 'zlikun', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '18', 'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic emxpa3VuOjEyMzQ1Ng=='}
print(prepped.headers)
# name=zlikun&age=18
print(prepped.body)
# {'response': []}
print(prepped.hooks)

# 发送
resp = session.send(prepped, timeout=3.0)
# 200
print(resp.status_code)
# {'Connection': 'keep-alive', 'Server': 'gunicorn/19.8.1', 'Date': 'Wed, 04 Jul 2018 03:59:37 GMT', 'Content-Type': 'application/json', 'Content-Length': '39', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true', 'Via': '1.1 vegur'}
print(resp.headers)
# {"authenticated":true,"user":"zlikun"}
print(resp.text)
# 0:00:00.495369，请求-响应耗时
print(resp.elapsed)
# []
print(resp.history)

# dir()函数可以查看 response 对象的属性列表(字段、方法)
# ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
print(dir(resp))

# 下载图片和文件
resp = requests.get(
    url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530687702405&di=76705e518f32d2594495915690a6be59&imgtype=0&src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F01d43f58f1863ba8012049ef11b861.jpg%401280w_1l_2o_100sh.jpg',
    stream=True)
# 将图片保存本地
with open('wallpaper.jpg', 'wb') as fd:
    for chunk in resp.iter_content(128):
        fd.write(chunk)


# Hooks，当请求完成时，触发hooks['response']，从而执行钩子函数
def resp_hook(resp, *args, **kwargs):
    print(resp.status_code, resp.reason)


# 200 OK
requests.get('http://httpbin.org/ip', hooks=dict(response=resp_hook))
