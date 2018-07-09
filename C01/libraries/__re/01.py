import re

# 完全匹配(域名)
pattern = r'^https?://(\w+:\w+@)?(\w+\.)?\w+\.\w+$'
# <re.Match object; span=(0, 17), match='http://zlikun.com'>
print(re.match(pattern, 'http://zlikun.com', flags=re.I))
# <re.Match object; span=(0, 18), match='https://zlikun.com'>
print(re.match(pattern, 'https://zlikun.com', flags=re.I))
# <re.Match object; span=(0, 22), match='https://www.zlikun.com'>
print(re.match(pattern, 'https://www.zlikun.com', flags=re.I))
# <re.Match object; span=(0, 32), match='https://zlikun:123456@zlikun.com'>
print(re.match(pattern, 'https://zlikun:123456@zlikun.com', flags=re.I))
# <re.Match object; span=(0, 38), match='https://zlikun:123456@admin.zlikun.com'>
print(re.match(pattern, 'https://zlikun:123456@admin.zlikun.com', flags=re.I))
# <re.Match object; span=(0, 38), match='HTTPs://zlikun:123456@admin.zlikun.com'>
print(re.match(pattern, 'HTTPs://zlikun:123456@admin.zlikun.com', flags=re.I))
# None
print(re.match(pattern, 'HTTPs://zlikun:123456@api.admin.zlikun.com', flags=re.I))

# 匹配目标
pattern = r'(\w+\s)+'

matcher = re.match(pattern, 'Jetty Nginx Tomcat Apache Undertow IIS Redis', flags=re.I)
# <re.Match object; span=(0, 44), match='Jetty Nginx Tomcat Apache Undertow IIS Redis'>
print(matcher)
# ('Apache',)
print(matcher.groups())
# Jetty Nginx Tomcat Apache Undertow IIS Redis
print(matcher.group())
# Jetty Nginx Tomcat Apache Undertow IIS Redis
print(matcher.group(0))
# Apache
print(matcher.group(1))

# 非贪婪模式
pattern = r'This is a .*(\w+) example'
pattern = r'This is a .*?(\w+) example'

matcher = re.match(pattern, 'This is a regex example')
print(matcher)
# 贪婪模式，前面的匹配的尽可能多的字符，留给后面只剩下一个字符：('x',)
# 非贪婪模式，前面匹配最小字符，剩下的都留给后面的模式匹配：('regex',)
print(matcher.groups())

# 匹配模式
# re.I == re.IGNORECASE，不区分大小写
s = 'Hello World \n Hello Python'
# None
print(re.match(r'[a-z]+ [a-z]+ \n [a-z]+ [a-z]+', s))
# <re.Match object; span=(0, 26), match='Hello World \n Hello Python'>
print(re.match(r'[a-z]+ [a-z]+ \n [a-z]+ [a-z]+', s, re.I))
