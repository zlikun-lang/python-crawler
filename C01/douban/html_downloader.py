import requests


class HtmlDownloader(object):

    def download(self, url):
        '''
        下载网页，返回网页内容
        :param url:
        :return:
        '''
        if url is None:
            return None

        r = requests.get(url, timeout=1.0)
        if r.status_code is not requests.codes.ok:
            # 下载失败时抛出异常
            # r.raise_for_status()
            return None
        else:
            return r.text
