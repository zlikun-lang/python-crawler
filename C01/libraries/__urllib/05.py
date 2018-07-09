# 异常处理

from urllib import request, error

try:
    resp = request.urlopen('http://192.168.0.105/ip', timeout=0.001)
    # 200 OK
    print(resp.code, resp.msg)
    # {
    #   "origin": "192.168.0.9"
    # }
    print(resp.read().decode())
except error.HTTPError as e:
    # HTTPError 继承自 URLError，所以需要先于 URLError 捕获
    print('请求出错!', e.errno, e.code, e.msg)
except error.URLError as e:
    print('URL不合法!', e.errno, e.reason)
except Exception as e:
    # 超时属于客户端的问题(未得到服务端响应，所以error模块中不包含相应的异常)
    print('请求超时!', e.errno)
else:
    print('-- nothing --')

print('-' * 30 + '>')

with request.urlopen('http://192.168.0.105/ip', timeout=0.001) as resp:
    print(resp.code, resp.msg)
