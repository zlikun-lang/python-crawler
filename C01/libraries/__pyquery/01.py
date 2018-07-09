from pyquery import PyQuery as pq
from lxml import etree
from urllib import request

d = pq('<html></html>')
# <class 'pyquery.pyquery.PyQuery'> <html/>
print(type(d), d)

d = pq(etree.fromstring('<html></html>'))
# <class 'pyquery.pyquery.PyQuery'> <html/>
print(type(d), d)

d = pq(url='https://baidu.com/', opener=lambda url, **kwargs: request.urlopen(url).read())
# <class 'pyquery.pyquery.PyQuery'>
# <html> ... </html>
print(type(d), d)
