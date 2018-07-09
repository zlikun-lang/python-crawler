from urllib import robotparser

rp = robotparser.RobotFileParser()
rp.set_url('https://zhihu.com/robots.txt')
rp.read()

# None
print(rp.crawl_delay('*'))
# False
print(rp.can_fetch('*', 'https://zhihu.com/tags'))
