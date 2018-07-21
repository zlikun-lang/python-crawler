# Spring官方文档 5.0.7 版，单词统计爬虫
# https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/core.html#spring-core
# https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/testing.html#testing
# https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/data-access.html#spring-data-tier
# https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/web.html#spring-web
# https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/web-reactive.html#spring-webflux
# https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/integration.html#spring-integration
# https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/languages.html#languages
import jieba
import requests
from pyquery import PyQuery

resp = requests.get(
    'https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/core.html#spring-core')
pq = PyQuery(resp.text)

words = jieba.cut(pq.text())

data = {}
for word in words:
    if word in data:
        data[word] += 1
    else:
        data[word] = 1

# 将统计结果按统计数量倒序排列
for item in sorted(data.items(), key=lambda item: item[-1], reverse=True):
    print(item)
