from pymongo import MongoClient
from pymongo import UpdateOne
from bson.objectid import ObjectId
import pymongo

with MongoClient('172.17.0.1', 27017, username='bottrainer', password='111') as client:
    db = client.mycorus

    cursor = db.docs.find({}, projection={"text": False, "tag": False})

    index = 0
    requests = []
    for doc in cursor:

        requests.append(UpdateOne({'_id': doc['_id']}, {"$set": {'tag': index}}))
        index += 1

        if len(requests) >= 10000:
            result = db.docs.bulk_write(requests)
            print(result.bulk_api_result)
            requests.clear()

    db.docs.create_index([("tag", pymongo.ASCENDING)], unique=True))

