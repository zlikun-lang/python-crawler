from C01.douban import url_manager, html_downloader, html_parser, content_processor


class Crawler(object):

    def __init__(self):
        # 初始化URL管理器
        self.urls = url_manager.UrlManager()
        # 初化HTML下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 初化HTML解析器
        self.parser = html_parser.HtmlParser()
        # 初始化内容处理器
        self.processor = content_processor.ContentProcessor()

    def crawl(self, root_url):
        # 初始化URL管理器(给定一个启动URL)
        self.urls.add_new_url(root_url)
        counter = 0
        # 循环获取URL，使用爬虫连续爬取网页内容
        while self.urls.has_new_url():
            # 从URL管理器中获取一个URL
            new_url = self.urls.get_new_url()
            print('{:02} - 开始下载：{}'.format(counter + 1, new_url))
            try:
                # 使用下载器下载HTML文件
                new_html = self.downloader.download(new_url)
                # 使用HTML解析器解析HTML文档，返回链接列表、文档内容
                new_urls, new_content = self.parser.parse(new_url, new_html)
                # 将链接列表加入到URL管理器中
                self.urls.add_new_urls(new_urls)
                # 将解析文档内容将由内容处理器处理
                self.processor.process(new_content)
            except IOError as e:
                print('爬取[{}]出错：{}'.format(new_url, e))
            finally:
                # 爬虫执行计数(成功、失败都计数，因为这里失败没有重试)
                counter += 1

        print("爬虫程序运行结束，共爬取 {} 个网页".format(counter))


if __name__ == '__main__':
    # 启动URL
    root_url = 'https://book.douban.com/tag/%E4%BA%92%E8%81%94%E7%BD%91'
    # 构造调度器
    crawler = Crawler()
    # 启动爬虫
    crawler.crawl(root_url)
