"""
仅抓取一页信息(不完整爬虫)
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

    root_url = 'http://maoyan.com/board/4'
    html = get_one_page(root_url)
    links, datas = parse_one_page(html, root_url)

    print('链接列表：')
    for link in links:
        print(link)

    print('数据列表：')
    for data in datas:
        print(data)

    write_to_file(datas)
