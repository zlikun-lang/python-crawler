# coding:utf-8
# author:zlikun

from urllib import request
from urllib import parse
import re
from bs4 import BeautifulSoup

# 下载Wiki百科主页
url = 'https://en.wikipedia.org/wiki/Main_Page'
# 读取下载的网页内容，并将其使用utf-8解码
html = request.urlopen(url).read().decode('utf-8')

# 使用bs4库解析网页
soup = BeautifulSoup(html, 'html.parser')

# 获取全部A标签，其href属性值以`/wiki/`开头
a_tags = soup.find_all('a', href=re.compile('^/wiki/'))

for a_tag in a_tags:
    # 过滤以`.png`和`.jpg`结尾的链接(re.I 表示忽略大小写)
    if not re.search(r'\.(png|jpg)$', a_tag['href'], re.I):
        # 打印A标签的href属性值，这里打印其绝对路径
        print(parse.urljoin(url, a_tag['href']))
