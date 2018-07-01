class ContentProcessor(object):

    def __init__(self):
        self._counter = 1

    def process(self, content):
        # 这里不做任何处理，直接打印到控制台即可
        if content is None or len(content) == 0:
            return
        for m, n in content:
            print('\t{:04} : {} -> {}'.format(self._counter, m, n))
            self._counter += 1
