import redis as redis


def url_checker(fn):
    """
    URL合法性检查器
    :param fn:
    :return:
    """

    def wrapper(obj, urls):
        # url 格式检查，这里主要检查url部分是否是：
        # https://movie.douban.com/subject/26752088/comments
        # 本次任务只抓取该电影影评，所以忽略其它URL
        # 直接在原urls列表上修改遇到问题(&percent_type=部分移除不掉)，所以直接用一个新列表重新装入url列表
        lst = []
        for url in urls:
            # 将不匹配的URL从列表中删除
            if '/subject/26752088/comments' not in url:
                continue
            # 将url中的 &percent_type= 参数移除，避免造成重复抓取(有些链接带这个参数有些不带)
            if '&percent_type=' in url:
                url = url.replace('&percent_type=', '')
            lst.append(url)

        return fn(obj, lst)

    return wrapper


class Manager(object):
    """
    单机URL管理器
    """

    def __init__(self):
        self.new_urls = []
        self.old_urls = []

    @url_checker
    def append_new_urls(self, urls):
        if len(urls) == 0:
            return
        for url in urls:
            if url in self.new_urls or url in self.old_urls:
                continue
            else:
                self.new_urls.append(url)

    def has_new_url(self):
        return len(self.new_urls) > 0

    def get_new_url(self):
        """
        获取一个新的URL，内部隐含了URL抓取过后加入已抓取队列操作(所以这里不考虑实际抓取过程中的失败情况)
        :return:
        """
        url = self.new_urls.pop()
        self.old_urls.append(url)
        return url


class RedisUrlManager(Manager):
    """
    使用Redis实现URL管理器
    """

    def __init__(self, host=None, port=6379):
        self.pool = redis.ConnectionPool(host=host, port=port, db=0, decode_responses=True)

    @url_checker
    def append_new_urls(self, urls):
        if len(urls) == 0:
            return
        for url in urls:
            r = redis.Redis(connection_pool=self.pool)
            if r.sismember('urls:new', url) or r.sismember('urls:old', url):
                continue
            else:
                # 传入的是一个列表，所以需要解包
                # 实际测试发现有重复URL？！
                r.sadd('urls:new', *urls)

    def has_new_url(self):
        r = redis.Redis(connection_pool=self.pool)
        return r.exists('urls:new')

    def get_new_url(self):
        """
        获取一个新的URL，内部隐含了URL抓取过后加入已抓取队列操作(所以这里不考虑实际抓取过程中的失败情况)
        :return:
        """
        r = redis.Redis(connection_pool=self.pool)
        url = r.spop('urls:new')
        r.sadd('urls:old', url)
        return url
