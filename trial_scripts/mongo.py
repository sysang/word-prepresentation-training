import math
from pymongo import MongoClient
from pymongo.cursor import CursorType

DB_HOST = '172.17.0.1'
DB_PORT = 27017
DB_USER = 'bottrainer'
DB_UPASS = '111'

batch_size = 100000  # must be appropriated with the 'batch_index' key in db


def count_documents(dbcollection):
    return dbcollection.count_documents({})


def data_buf():
    with MongoClient(DB_HOST, DB_PORT, username=DB_USER, password=DB_UPASS) as client:

        dbcollection = client.thefinal.docs
        total = count_documents(dbcollection)

        while True:
            count = 1
            for index in range(0, math.ceil(total / batch_size)):
                print("Caching batch index: %d" % (index))

                cursor = dbcollection.find({'batch_index': index}, projection={"_id": False}).batch_size(10)

                result = ''
                for line in cursor:
                    concatenated = str(line['tag']) + ']~[' + line['text']
                    result += '>|<' + concatenated
                    count += 1
                    yield result[3:]

            print('<END>: %d documents have been served.' % (count))

            yield ('<!END!>')


if __name__ == '__main__':
    iterable = data_buf()
    for i in iterable:
        print(i)
