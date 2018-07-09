# https://docs.python.org/3/library/urllib.request.html#module-urllib.request

from urllib import request

# GET
r = request.Request(url='https://www.oschina.net/',
                    # data={'author': 'zlikun'},
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'},
                    method='GET')

r.add_header('Host', 'www.oschina.net')

# www.oschina.net
print(r.get_header('Host'))
# {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36', 'Host': 'www.oschina.net'}
print(r.headers)
# GET
print(r.get_method())
# https://www.oschina.net/
print(r.get_full_url())
# None
print(r.data)

resp = request.urlopen(r, timeout=1.5)

# <!DOCTYPE HTML>
# ... ...
print(resp.read().decode())

resp.close()
