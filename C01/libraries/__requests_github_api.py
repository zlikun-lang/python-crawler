# coding:utf-8
# author:zlikun

import requests, json
from requests import exceptions

URL = 'https://api.github.com'


def build_url(endpoint):
    return '/'.join([URL, endpoint])


def format_json_string(json_string):
    return json.dumps(json.loads(json_string), indent=4)


# 获取用户信息
resp = requests.get(build_url('users/zlikun'))
print(format_json_string(resp.text))

# 获取邮箱信息，需要传入认证信息(这里密码是假的^_^)
# resp = requests.get(build_url('user/emails'), auth=('zlikun', '******'))
# print(format_json_string(resp.text))

# 异常处理
try:
    resp = requests.get(build_url('user/emails'), timeout=0.1)
    resp.raise_for_status()
except exceptions.Timeout as e:
    # HTTPSConnectionPool(host='api.github.com', port=443): Max retries exceeded with url: /user/emails (Caused by ConnectTimeoutError(<urllib3.connection.VerifiedHTTPSConnection object at 0x000002205A1C0A20>, 'Connection to api.github.com timed out. (connect timeout=0.1)'))
    print(e)
except exceptions.HTTPError as e:
    # 401 Client Error: Unauthorized for url: https://api.github.com/user/emails
    print(e)
else:
    print(resp.status_code)
