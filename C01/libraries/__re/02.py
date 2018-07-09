import re

pattern = r'^https?://'

# <re.Match object; span=(0, 8), match='https://'>
print(re.search(pattern, 'https://zlikun.com'))
# <re.Match object; span=(0, 8), match='https://'>
print(re.search(pattern, 'https://zlikun.com/python/guide.html'))
# None
print(re.search(pattern, 'ftp://ftp.zlikun.com'))
# None
print(re.search(pattern, '  https://zlikun.com'))

