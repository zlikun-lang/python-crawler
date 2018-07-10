import pymongo


class Processor(object):

    def __init__(self, host=None, port=27017, database='douban', collection='movie_26752088_comments'):
        self.client = pymongo.MongoClient(host=host, port=port)
        self.database = database
        self.collection = collection

    def __del__(self):
        self.client.close()

    def process(self, results):
        comments = self.client.get_database(self.database).get_collection(self.collection)
        return comments.insert(results)
