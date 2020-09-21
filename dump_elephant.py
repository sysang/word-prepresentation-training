from pymongo import MongoClient
from dump_imdbreviews_to_mongodb import imdb
from dump_blogcorpus_to_mongodb import blog
from dump_enwik9_to_mongodb import enwik9
from dump_gutenberg_to_mongodb import gutenberg
from dump_usenet_to_mongodb import usenet

if __name__ == "__main__":
    with MongoClient('127.0.0.1', 27017, username='myUserAdmin', password='111') as client:
        db = client.elephant
        dbcollection = db.docs

        usenet(dbcollection)
        gutenberg(dbcollection)
        imdb(dbcollection)
        enwik9(dbcollection)
        blog(dbcollection)

        print('Almost done, re-indexing database...')
        db.command({"reIndex": "docs"})
