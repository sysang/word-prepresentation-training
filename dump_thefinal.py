from pymongo import MongoClient
from dump_imdbreviews_to_mongodb import imdb
from dump_blogcorpus_to_mongodb import blog
from dump_enwik9_to_mongodb import enwik9
from dump_gutenberg_to_mongodb import gutenberg

if __name__ == "__main__":
    with MongoClient('172.17.0.1', 27017, username='myUserAdmin', password='111') as client:
        db = client.thefinal
        dbcollection = db.docs

        dbcollection.delete_many({})

        gutenberg(dbcollection)
        imdb(dbcollection)
        enwik9(dbcollection)
        blog(dbcollection)

        db.command({"reIndex": "docs"})
