from urllib import request, parse

# POST
with request.urlopen(request.Request(url='http://httpbin.org/post',
                                     data=parse.urlencode({'name': 'Ashe', 'age': 17}).encode('utf-8'),
                                     headers={'User-Agent': 'python/zlikun', 'Host': 'httpbin.org'},
                                     method='POST'), timeout=3.0) as resp:
    # 200 OK
    print(resp.code, resp.msg)
    # Connection: close
    # Server: gunicorn/19.8.1
    # Date: Mon, 09 Jul 2018 07:01:42 GMT
    # Content-Type: application/json
    # Content-Length: 321
    # Access-Control-Allow-Origin: *
    # Access-Control-Allow-Credentials: true
    # Via: 1.1 vegur
    print(resp.headers)
    # {
    #     "args": {
    #
    #     },
    #     "data": "",
    #     "files": {
    #
    #     },
    #     "form": {
    #         "age": "17",
    #         "name": "Ashe"
    #     },
    #     "headers": {
    #         "Accept-Encoding": "identity",
    #         "Connection": "close",
    #         "Content-Length": "16",
    #         "Content-Type": "application/x-www-form-urlencoded",
    #         "Host": "httpbin.org",
    #         "User-Agent": "python/zlikun"
    #     },
    #     "json": null,
    #     "origin": "114.94.64.145",
    #     "url": "http://httpbin.org/post"
    # }
    print(resp.read().decode())
