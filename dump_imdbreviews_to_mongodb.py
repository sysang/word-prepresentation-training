import re
from pymongo import MongoClient
from dump_master import extract_documents


def imdb(dbcollection):
    fnames = ['aclImdb_v1.tar.gz']

    regex_fname = re.compile(r'aclImdb/(train|test)/(pos|neg|unsup)/\d+_\d+.txt$')
    extrax_regexes = []

    for fname in fnames:
        extract_documents(
                dbcollection=dbcollection,
                regex_fname=regex_fname,
                fname=fname,
                extrax_regexes=extrax_regexes
                )


if __name__ == "__main__":
    with MongoClient('127.0.0.1', 27017, username='myUserAdmin', password='111') as client:
        db = client.imdb_reviews
        dbcollection = db.reviews

        dbcollection.delete_many({})

        imdb(dbcollection)

        db.command({"reIndex": "reviews"})
