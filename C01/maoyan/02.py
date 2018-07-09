"""
修改为一个完整的爬虫(循环队列，将Top100的数据全部抓取下来)
"""

import json
import requests
from requests import RequestException
from urllib import parse
from bs4 import BeautifulSoup


def get_one_page(url):
    """
    下载单个网页
    :param url:
    :return:
    """
    try:
        resp = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        })
        if resp.status_code == 200:
            return resp.text
    except RequestException as e:
        print(e.errno, e.strerror)


def parse_one_page(html, url):
    """
    解析单个网页(用正则太复杂，还是用第三方库得了)
    :param html:
    :return:
    """

    # 工具函数，处理字符串两端空白
    def trim(string):
        if string is not None:
            return string.strip()
        else:
            return string

    bs = BeautifulSoup(html, 'html.parser')

    # 获取链接列表
    links = []
    for a in bs.select('ul.list-pager a'):
        href = a.get('href')
        if href.startswith('javascript'):
            continue
        links.append(parse.urljoin(url, href))

    # 获取内容信息
    lst = []
    for dd in bs.select('dl.board-wrapper > dd'):
        img = dd.select_one('img.board-img').get('data-src')
        title = dd.select_one('p.name > a').get_text()
        href = dd.select_one('a.image-link').get('href')
        star = dd.select_one('p.star').get_text()
        time = dd.select_one('p.releasetime').get_text()
        score = dd.select_one('p.score').get_text()
        lst.append(tuple(map(lambda s: trim(s), [img, title, parse.urljoin(url, href), star, time, score])))

    return links, lst


def write_to_file(lst):
    """
    将数据转换为JSON，写入到本地文件中
    :param lst:
    :return:
    """
    with open('.data', 'a', encoding='utf-8') as f:
        for content in lst:
            f.writelines(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


if __name__ == '__main__':
    print('猫眼电影 Top100', 'http://maoyan.com/board/4')

    root_url = 'http://maoyan.com/board/4?offset=0'

    # 声明一个URL队列，使用启动URL初始化
    new_urls = [root_url]
    old_urls = []

    while len(new_urls) > 0:

        # 从队列中取出一个URL，并将其加入到已完成队列中(这里暂不考虑失败的情况)
        new_url = new_urls.pop()
        old_urls.append(new_url)

        # 下载取出的URL标识的网页
        print('正在下载：{}'.format(new_url))
        html = get_one_page(new_url)

        # 解析网页内容
        links, datas = parse_one_page(html, root_url)

        # 将网页中包含的有效超链接加入到待抓取URL队列中
        for link in links:
            # 处理特殊情况：http://maoyan.com/board/4 == http://maoyan.com/board/4?offset=0
            if 'offset=' not in link:
                link += '?offset=0'
            if link in new_urls or link in old_urls:
                continue
            else:
                new_urls.append(link)

        # 将解析的数据写入到文件
        write_to_file(datas)

    print('Top100 爬虫任务完成 !')
