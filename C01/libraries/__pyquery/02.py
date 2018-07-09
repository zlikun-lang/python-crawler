from pyquery import PyQuery as pq
from urllib import request

d = pq(url='https://zhihu.com', opener=lambda url, **kwargs: request.urlopen(url).read())
# print(d)

# 获取文档属性
# <title data-react-helmet="true">知乎 - 发现更大的世界</title>
print(d('title:eq(0)'))
# 知乎 - 发现更大的世界
print(d('title:eq(0)').text())

# 获取 class 属性
# Entry-body
print(d('body').attr('class'))
# Entry-body
print(d('body').attr.class_)

# 获取 href 属性
for a in d('a'):
    print(a.text, ' -> ', a.get('href'))
