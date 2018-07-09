from pyquery import PyQuery as pq
from urllib import request

d = pq(url='https://zhihu.com', opener=lambda url, **kwargs: request.urlopen(url).read())
# print(d)

# 使用伪类选择器
# http://pyquery.readthedocs.io/en/latest/pseudo_classes.html
print(d(':button'))
print(d(':checkbox'))
print(d(':checked'))
print(d('div:contains("a")'))
print(d('div:even'))
print(d('div:first'))
print(d('div:eq(0)'))

# ... ...
