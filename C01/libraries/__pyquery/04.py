from pyquery import PyQuery as pq
from urllib import request

d = pq(url='https://zhihu.com', opener=lambda url, **kwargs: request.urlopen(url).read())

# 第一条热门内容正文
print(d('main.App-main div.Card.HomeMainItem:first div.ContentItem.AnswerItem:first').text())
