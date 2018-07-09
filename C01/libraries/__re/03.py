import requests
import re

resp = requests.get('https://en.wikipedia.org/wiki/Main_Page')

# 200 OK
print(resp.status_code, resp.reason)

# 使用正则表达式，提取全部超链接列表
# print(resp.text)

pattern = r'(https://en.wikipedia.org)?/wiki/(\w+(:\w+)?)'
lst = re.findall(pattern, resp.text, re.I)
for o in lst:
    print('/'.join(['https://en.wikipedia.org/wiki', o[1]]), '\t', o)
