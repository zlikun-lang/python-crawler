from bs4 import BeautifulSoup
from urllib import parse


class Parser(object):

    def __init__(self, base_url=None):
        self.base_url = base_url

    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        # 超链接列表
        links = []
        for a in soup.select('#paginator > a'):
            if self.base_url is not None:
                links.append(parse.urljoin(self.base_url, a.get('href')))
            else:
                links.append(a.get('href'))

        # 数据列表
        results = []
        for div in soup.select('#comments > div.comment-item'):
            author = div.select_one('h3 > span.comment-info > a').get_text(strip=True)
            date = div.select_one('h3 > span.comment-info > span.comment-time').get_text(strip=True)
            rating = div.select_one('h3 > span.comment-info > span.rating')
            star = None
            if rating is not None:
                star = rating.get('class')[0].replace('allstar', '')
            vote = div.select_one('h3 > span.comment-vote > span.votes').get_text(strip=True)
            comment = div.select_one('div.comment > p').get_text(strip=True)
            results.append({
                'author': author,
                'date': date,
                'star': star,
                'vote': vote,
                'comment': comment
            })

        return links, results
