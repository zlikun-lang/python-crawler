from urllib.parse import urljoin

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, url, html):
        '''
        解析网页，返回链接列表和内容对象
        :param url:
        :param html:
        :return:
        '''
        if url is None or html is None:
            return
        soup = BeautifulSoup(html, 'html.parser')

        new_urls = self._get_new_urls(soup, url)
        new_data = self._get_new_data(soup, url)
        return new_urls, new_data

    @staticmethod
    def _get_new_urls(soup, url):
        '''
        按href属性特征获取a标签
        :param soup:
        :param url:
        :return:
        '''
        # urljoin() 用于生成URL的绝对值
        r = map(lambda a: urljoin(url, a.get('href')), soup.select('div.paginator > a[href]'))
        return list(r)

    @staticmethod
    def _get_new_data(soup, url):
        '''
        内容部分提取书籍URL和标题，构成一个元组序列
        :param soup:
        :param url:
        :return: [($url, $title),]
        '''
        lst = []
        for t in soup.select('#subject_list li'):
            data = {}
            title_node = t.select_one('h2 > a[href]')
            data['href'] = urljoin(url, title_node.get('href'))
            data['title'] = title_node.get_text(strip=True)
            remark_node = t.select_one('div.pub')
            if remark_node is not None:
                data['remark'] = remark_node.get_text(strip=True)
            star_node = t.select_one('div.star > span.rating_nums')
            if star_node is not None:
                data['star'] = star_node.get_text()
            lst.append(data)
        return lst
