import re
from pymongo import MongoClient
from dump_master import extract_documents


def gutenberg(dbcollection):
    fnames = ['gutenberg.tar.gz']

    regex_fname = re.compile(r'gutenberg/txt/\S+\.txt$')
    extrax_regexes = []

    for fname in fnames:
        extract_documents(fname, dbcollection, regex_fname, extrax_regexes)


with MongoClient('172.17.0.1', 27017, username='myUserAdmin', password='111') as client:
    db = client.gutenberg
    dbcollection = db.books
    dbcollection.delete_many({})
    gutenberg(dbcollection)
    db.command({"reIndex": "books"})
