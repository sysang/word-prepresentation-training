import re
from pymongo import MongoClient
from dump_master import extract_documents


def enwik9(dbcollection):
    fnames = ['enwik9_MattMahoney.tar.gz']

    regex_fname = re.compile(r'enwik9-preprocessed\/[A-Z][A-Z]\/wiki_\d\d')
    regex_xml_tag = re.compile(r"<doc\s.*>|<\/doc>|<br.*>|\[\[.*\]\]|<pre>", re.IGNORECASE)
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
    with MongoClient('127.0.0.1', 27017, username='myUserAdmin', password='111') as client:
        db = client.enwik9
        dbcollection = db.docs
        dbcollection.delete_many({})

        enwik9(dbcollection)

        db.command({"reIndex": "docs"})
