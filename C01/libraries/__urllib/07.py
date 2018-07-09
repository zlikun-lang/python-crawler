# parse 是一个工具模块
# https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse

from urllib import parse

# b'name=Ashe&hobbies=%5B%27%E6%91%84%E5%BD%B1%27%2C+%27%E6%97%85%E8%A1%8C%27%5D'
print(parse.urlencode({'name': 'Ashe', 'hobbies': ['摄影', '旅行']}).encode('utf-8'))

o = parse.urlparse('https://zlikun:123456@zlikun.com:8443/python/guide.html')
# ParseResult(scheme='https', netloc='zlikun:123456@zlikun.com:8443', path='/python/guide.html', params='', query='', fragment='')
print(o)

url = parse.urljoin('https://zlikun.com/python/guide.html', 'manual.html')
# https://zlikun.com/python/manual.html
print(url)
