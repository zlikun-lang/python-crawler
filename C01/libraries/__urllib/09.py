# Proxies
# https://www.cnblogs.com/feng18/p/5749045.html

from urllib import request

proxy_handler = request.ProxyHandler({'sock5': '120.26.110.59:8080'})

opener = request.build_opener(proxy_handler)
request.install_opener(opener)

resp = request.urlopen('http://192.168.0.105/ip')
print(resp.headers)
print(resp.read().decode())
