# coding:utf-8
# author:zlikun

"""
模拟登录 www.oschina.net ，并获取用户信息
"""

# 1. 模拟表单登录
import requests, hashlib
from bs4 import BeautifulSoup


def sha1(str):
    hash = hashlib.sha1()
    hash.update(str.encode('utf-8'))
    return hash.hexdigest()


resp = requests.post('https://www.oschina.net/action/user/hash_login?from=',
                     {
                         'email': 'likun_zhang@yeah.net',
                         'pwd': sha1('********'),
                         'verifyCode': '',
                         'save_login': '1'
                     },
                     headers={
                         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
                     })

# 200 OK
print(resp.status_code, resp.reason)

# {
#     'Date': 'Wed,
#     04Jul201805: 23: 54GMT',
#     'Content-Type': 'text/html;charset=utf-8',
#     'Content-Length': '0',
#     'Connection': 'keep-alive',
#     'Set-Cookie': 'aliyungf_tc=AQAAAB93K3HTQgEAdcgbGxLRRIvp6sYt;Path=/;HttpOnly,
#     _user_behavior_=b3949e01-411f-49a0-943d-5aa94ea7aa6c;Domain=.oschina.net;Expires=Thu,
#     04-Jul-201905: 23: 54GMT;Path=/;HttpOnly,
#     oscid="";Domain=.oschina.net;Expires=Thu,
#     01-Jan-197000: 00: 10GMT;Path=/;HttpOnly,
#     oscid=18%2B24OHTNObWgBnHCgtLk300eOsXufOKvWH7QK2Ay9CElLuXYaxAILHsw%2BFaKg1sLYF4ctpQCHNH%2BrEVO5i8kDlaPRwV68o%2FZgXFYP8mJ7p7fD8brHM9KOVh5oGPTcpkrkjTQJ8BIzFzpcx8Ui%2F6OYLDVZRQij8K%2BsTtFiMNfnM%3D;Domain=.oschina.net;Expires=Thu,
#     04-Jul-201905: 23: 54GMT;Path=/;HttpOnly',
#     'Server': 'Tengine'
# }
print(resp.headers)

# <Cookie _user_behavior_=4f4e830c-cdd0-4247-9198-e0820d8cbbff for .oschina.net/>
# <Cookie oscid=18%2B24OHTNObWgBnHCgtLk300eOsXufOKvWH7QK2Ay9CElLuXYaxAILHsw%2BFaKg1sLYF4ctpQCHNH%2BrEVO5i8kDlaPRwV68o%2FZgXFYP8mJ7r5Qg9t%2B0LmAOVh5oGPTcpkrkjTQJ8BIzFzpcx8Ui%2F6OYLDVZRQij8K%2BsTtFiMNfnM%3D for .oschina.net/>
# <Cookie aliyungf_tc=AQAAADNPp08BEwkAdcgbG3NPN29nRd3+ for www.oschina.net/>
# type(cookie) = <class 'http.cookiejar.Cookie'>
# type(resp.cookies) = <class 'requests.cookies.RequestsCookieJar'>
cookies = resp.cookies
for cookie in cookies:
    print(cookie)

# 2. 携带cookie信息访问首页，获取右上角的用户信息
resp = requests.get('https://my.oschina.net',
                    headers={
                        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
                    },
                    cookies=cookies)

print(resp.status_code, resp.reason)

# 解析网页
soup = BeautifulSoup(resp.text, "html.parser")

# 登录用户：zlikun
print('登录用户：{}'.format(soup.select_one('h2').text))
