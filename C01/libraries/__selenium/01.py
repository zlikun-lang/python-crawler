# https://seleniumhq.github.io/selenium/docs/api/py/
from selenium import webdriver

browser = webdriver.Firefox()
try:
    session = browser.get('https://zhihu.com')
    print(session)
finally:
    browser.close()
