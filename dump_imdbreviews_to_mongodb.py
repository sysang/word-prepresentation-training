import re
from pymongo import MongoClient
from dump_master import extract_documents


with MongoClient('172.17.0.1', 27017, username='myUserAdmin', password='111') as client:
    fname = 'aclImdb_v1.tar.gz'

    dbcollection = client.imdb_reviews.reviews

    regex_fname = re.compile(r'aclImdb/(train|test)/(pos|neg|unsup)/\d+_\d+.txt$')
    extrax_regexes = []

    extract_documents(fname, dbcollection, regex_fname, extrax_regexes)

    dbcollection.reindex()

