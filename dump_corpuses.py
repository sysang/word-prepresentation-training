from pymongo import MongoClient
from dump_imdbreviews_to_mongodb import imdb
from dump_blogcorpus_to_mongodb import blog
from dump_enwik8_to_mongodb import enwik8
from dump_gutenberg_to_mongodb import gutenberg

if __name__ == "__main__":
    with MongoClient('172.17.0.1', 27017, username='myUserAdmin', password='111') as client:
        db = client.mycorus
        dbcollection = db.docs

        gutenberg(dbcollection)
        imdb(dbcollection)
        blog(dbcollection)
        enwik8(dbcollection)

        db.command({"reIndex": "docs"})
