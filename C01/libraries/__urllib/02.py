# https://docs.python.org/3/library/urllib.request.html#module-urllib.request

from urllib import request

# GET
# resp = request.urlopen(r'http://httpbin.org/get')
resp = request.urlopen(r'http://192.168.0.105/get')
# <class 'http.client.HTTPResponse'> <http.client.HTTPResponse object at 0x0000023DF0911128>
print(type(resp), resp)

# HTTPResponse Attributes
# print(help(resp))
# ['__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__',
# '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '_abc_impl', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable',
# '_check_close', '_close_conn', '_get_chunk_left', '_method', '_peek_chunked', '_read1_chunked',
# '_read_and_discard_trailer', '_read_next_chunk_size', '_read_status', '_readall_chunked',
# '_readinto_chunked', '_safe_read', '_safe_readinto', 'begin', 'chunk_left', 'chunked', 'close',
# 'closed', 'code', 'debuglevel', 'detach', 'fileno', 'flush', 'fp', 'getcode', 'getheader', 'getheaders',
# 'geturl', 'headers', 'info', 'isatty', 'isclosed', 'length', 'msg', 'peek', 'read', 'read1', 'readable',
# 'readinto', 'readinto1', 'readline', 'readlines', 'reason', 'seek', 'seekable', 'status', 'tell',
# 'truncate', 'url', 'version', 'will_close', 'writable', 'write', 'writelines']
# print(dir(resp))

# 200 200 OK OK
print(resp.code, resp.status, resp.reason, resp.msg)
# http://httpbin.org/get
print(resp.url)
# <class 'http.client.HTTPMessage'>
print(type(resp.headers))
# Connection: close
# Server: gunicorn/19.8.1
# Date: Mon, 09 Jul 2018 06:24:41 GMT
# Content-Type: application/json
# Content-Length: 184
# Access-Control-Allow-Origin: *
# Access-Control-Allow-Credentials: true
# Via: 1.1 vegur
print(resp.headers)
# Server: gunicorn/19.9.0
# Date: Mon, 09 Jul 2018 07:10:06 GMT
# Connection: close
# Content-Type: application/json
# Content-Length: 236
# Access-Control-Allow-Origin: *
# Access-Control-Allow-Credentials: true
print('-' * 10 + '>', '\n', resp.info())
# 184
print(resp.length)
# 11 -> HTTP/1.1
print(resp.version)

r = resp.read()
# <class 'bytes'>
# b'{"args":{},"headers":{"Accept-Encoding":"identity","Connection":"close","Host":"httpbin.org","User-Agent":"Python-urllib/3.7"},"origin":"114.94.64.145","url":"http://httpbin.org/get"}\n'
print(type(r), r)
# {"args":{},"headers":{"Accept-Encoding":"identity","Connection":"close","Host":"httpbin.org","User-Agent":"Python-urllib/3.7"},"origin":"114.94.64.145","url":"http://httpbin.org/get"}
print(r.decode('utf-8'))

resp.close()
