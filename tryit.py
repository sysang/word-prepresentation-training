from pymongo import MongoClient
from pymongo import UpdateOne
from bson.objectid import ObjectId
import pymongo
import math
import numpy as np
import re

import collections
SentimentDocument = collections.namedtuple('SentimentDocument', 'words tags')

# with MongoClient('172.17.0.1', 27017, username='bottrainer', password='111') as client:

#     db = client.imdb_reviews

#     reviews = db.reviews

#     total = reviews.count_documents({})
#     batch_size = 10000
#     start_index = 0

#     sum = 0
#     for index in range(0, math.ceil(total / batch_size)):
#         start_index = index * batch_size
#         end_index = start_index + batch_size if (start_index + batch_size) < total else total
        
#         cursor = reviews.find(projection={"_id": False})
#         reviews_batch = cursor[start_index:end_index]

#         sum += len(list(reviews_batch))
#         print(sum)


class MyCorpus(object):
    def __iter__(self):
        with MongoClient('172.17.0.1', 27017, username='bottrainer', password='111') as client:
            db = client.imdb_reviews
            reviews = db.reviews

            total = reviews.count_documents({})
            batch_size = 5000
            start_index = 0
            for index in range(0, math.ceil(total / batch_size)):
                start_index = index * batch_size
                end_index = start_index + batch_size if (start_index + batch_size) < total else total
                cursor = reviews.find(projection={"_id": False}).sort('tag', pymongo.ASCENDING)
                reviews_batch = cursor[start_index:end_index]

                for line in list(reviews_batch):
                    index += 1
                    yield SentimentDocument(line['text'].split(' '), [int(line['tag'])])
    
    def get_doc_by_index(self, index):
        with MongoClient('172.17.0.1', 27017, username='bottrainer', password='111') as client:
            db = client.imdb_reviews
            review = db.reviews.find_one({'tag': index})

            return review['text']
            # return list(review)[0]['text']


def finddoc(corpus, doc_index):
    boundary = 1000
    track = 0
    for doc in corpus:
        track += 1
        if doc.tags[0] == doc_index:
            return doc
        if track > boundary:
            raise Exception('Something wrong!')


with MongoClient('172.17.0.1', 27017, username='bottrainer', password='111') as client:
    db = client.mycorus

    cursor = db.docs.find({}, projection={"text": False, "tag": False}, skip=5000000)

    index = 0
    for doc in cursor:
        index += 1
        result = db.docs.delete_one({'_id': doc['_id']})
        if index % 5000 == 0:
            print(index)




