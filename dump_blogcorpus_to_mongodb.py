import re
from pymongo import MongoClient
from dump_master import extract_documents


def blog(dbcollection):
    fnames = ['bloggercom_mkopper.tar.gz']

    regex_fname = re.compile(r'blogs\/(\d+)\.(male|female)\.[2-9][4-9]\.(.+)\.(\w+)\.xml')
    regex_xml_tag = re.compile(r"<date>.*</date>|<blog>|<\/blog>|<post>|<\/post>", re.IGNORECASE)
    repl = " "
    extrax_regexes = [(regex_xml_tag, repl)]

    for fname in fnames:
        extract_documents(
                dbcollection=dbcollection,
                regex_fname=regex_fname,
                fname=fname,
                extrax_regexes=extrax_regexes
                )


if __name__ == "__main__":
    with MongoClient('172.17.0.1', 27017, username='myUserAdmin', password='111') as client:
        db = client.bloggercom
        dbcollection = db.posts
        dbcollection.delete_many({})

        blog(dbcollection)

        db.command({"reIndex": "posts"})
