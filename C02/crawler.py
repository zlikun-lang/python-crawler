# 爬虫启动入口

from C02.data import processor
from C02.page import downloader, parser
from C02.url import manager


class Spider(object):

    def __init__(self):
        # self.url_manager = manager.Manager()
        self.url_manager = manager.RedisUrlManager(host='192.168.0.105')
        self.page_downloader = downloader.Downloader()
        self.page_parser = parser.Parser(base_url='https://movie.douban.com/subject/26752088/comments')
        self.data_processor = processor.Processor(host='192.168.0.105', collection='movie_26752088_comments_2')
        # self.data_processor = processor.Processor(host='192.168.0.105', collection='movie_1292052_comments_2')

    def start(self, root_url):
        """
        启动爬虫方法
        :param root_url: 启动URL
        :return: 抓取的URL数量
        """
        nums = 0
        self.url_manager.append_new_urls([root_url])
        while self.url_manager.has_new_url():
            nums += 1
            new_url = self.url_manager.get_new_url()
            print('开始下载第{:03}个URL：{}'.format(nums, new_url))
            html = self.page_downloader.download(new_url)
            if html is None:
                print('html is empty .')
                continue
            links, results = self.page_parser.parse(html)
            if len(links) > 0:
                self.url_manager.append_new_urls(links)
            if len(results) > 0:
                self.data_processor.process(results)
        return nums


if __name__ == "__main__":
    spider = Spider()
    nums = spider.start("https://movie.douban.com/subject/26752088/comments?start=0&limit=20&sort=new_score&status=P")
    # nums = spider.start("https://movie.douban.com/subject/1292052/comments?start=0&limit=20&sort=new_score&status=P")
    print('爬虫执行完成，共抓取{}个URL'.format(nums))
