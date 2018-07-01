class UrlManager(object):

    def __init__(self):
        # 待爬取URL集合
        self.new_urls = set()
        # 已爬取URL集合
        self.old_urls = set()

    def add_new_url(self, url):
        '''
        添加一个新URL
        :param url:
        :return: None
        '''
        if url is None:
            return
        # 两个URL集合都不存在，说明是一个新的URL，将其加入到待爬取URL集合中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        '''
        添加多个新URL
        :param urls:
        :return: None
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        '''
        判断URL管理器中是否还有未爬取URL
        :return: None
        '''
        return len(self.new_urls) != 0

    def get_new_url(self):
        '''
        从待爬取URL合集中取出一个URL
        :return: str
        '''
        url = self.new_urls.pop()
        if url is None:
            return None
        # 将取出的URL加入到已处理URL集合中(这里不考虑失败的情况)
        self.old_urls.add(url)
        return url
