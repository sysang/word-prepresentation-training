from pymongo import MongoClient
import re
import math
import time

DB_HOST = '127.0.0.1'
DB_PORT = 27017
DB_USER = 'myUserAdmin'
DB_UPASS = '111'

BATCH_SIZE = 100000


class DatabaseIterator():
    def __init__(self, database, collection='docs'):
        self.database = database
        self.dbcollection = collection
        # self.total = self.count_total()
        self.total = 141275000

    def __iter__(self):
        with MongoClient(DB_HOST, DB_PORT, username=DB_USER, password=DB_UPASS) as client:
            db = client.get_database(self.database)
            collection = db.get_collection(self.dbcollection)
            total = self.total

            sanitizing_filter = re.compile(r"^((\w|\'\w)+\s){8,25}(\w+)$")
            # sanitizing_filter = re.compile(r"^(\w+\s){8,25}(\w+)$")

            for index in range(0, math.ceil(total / BATCH_SIZE)):
                # print("<MONGO CLIENT> Query batch index: %d" % (index))

                cursor = collection.find({'batch_index': index}, projection={"_id": False, 'batch_index': False, 'tag': False}, no_cursor_timeout=True)

                for doc in cursor:

                    if not sanitizing_filter.match(doc['text']):
                        continue

                    yield doc['text']

    def count_total(self):
        with MongoClient(DB_HOST, DB_PORT, username=DB_USER, password=DB_UPASS) as client:
            db = client.get_database(self.database)
            collection = db.get_collection(self.dbcollection)

            return collection.count_documents({})


def db_refine(from_db, to_db, from_collection='docs', to_collection='docs'):
    db_iterable = DatabaseIterator(database=from_db, collection=from_collection)

    with MongoClient(DB_HOST, DB_PORT, username=DB_USER, password=DB_UPASS) as client:
        db = client.get_database(to_db)
        collection = db.get_collection(to_collection)

        tag = 0
        bulk_vol = 0
        batch_index = 0
        docs = []
        for text in db_iterable:

            doc = {'text': text, 'tag': tag, 'batch_index': batch_index}
            docs.append(doc)
            bulk_vol += 1
            tag += 1

            if tag % BATCH_SIZE == 0:
                batch_index += 1
                print("\n")
                print('-----------  BATCH INDEX: %s' % (batch_index) + '  --------------')

            if bulk_vol >= 10000:
                collection.insert_many(docs)
                time.sleep(0.1)
                docs.clear()
                bulk_vol = 0
                print("[%d] %s" % (tag, text))


if __name__ == '__main__':
    raise Exception("Check configuration again!!!")
    db_refine(
            from_db='thefinal',
            from_collection='docs',
            to_db='blogwikgutimdb',
            to_collection='docs'
            )
