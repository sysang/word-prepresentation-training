import re
from pymongo import MongoClient
from dump_master import extract_documents


def enwik8(dbcollection):
    fnames = ['enwik8_MattMahoney.tar.gz']

    regex_fname = re.compile(r'enwik8\/wiki_\d\d')
    regex_xml_tag = re.compile(r"<doc\s.*>|<\/doc>|<br.*>|\[\[.*\]\]|<pre>", re.IGNORECASE)
    extrax_regexes = [regex_xml_tag]

    for fname in fnames:
        extract_documents(fname, dbcollection, regex_fname, extrax_regexes)


with MongoClient('172.17.0.1', 27017, username='myUserAdmin', password='111') as client:
    db = client.enwik8
    dbcollection = db.docs
    dbcollection.delete_many({})
    enwik8(dbcollection)
    db.command({"reIndex": "docs"})
