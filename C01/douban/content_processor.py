import pymongo


class ContentProcessor(object):

    def __init__(self):
        # 创建Mongo连接
        self.client = pymongo.MongoClient(host='192.168.0.200', port=27017)
        # 获取douban库books集合
        self.books = self.client.douban.books

    def __del__(self):
        self.client.close()
        print('Mongo连接已关闭')

    def process(self, content):
        # 这里不做任何处理，直接打印到控制台即可
        if content is None or len(content) == 0:
            return
        # {'href': 'https://book.douban.com/subject/26665230/', 'title': '硅谷之谜: 《浪潮之巅》续集', 'remark': '吴军 / 人民邮电出版社 / 2015-12-1 / 59.00', 'star': '8.5'}
        for i in content:
            self._save_to_mongodb(i)

    def _save_to_mongodb(self, data):
        '''
        将数据写入MongoDB中，这里暂不做优化(不采用批量写入)
        :param data:
        :return:
        '''
        # 执行插入操作
        self.books.insert(data)
