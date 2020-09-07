import re
from pymongo import MongoClient
from dump_master import extract_documents


with MongoClient('172.17.0.1', 27017, username='myUserAdmin', password='111') as client:
    fname = 'enwik8_MattMahoney.tar.gz'

    dbcollection = client.enwik8.docs

    regex_fname = re.compile(r'enwik8\/wiki_\d\d')
    regex_xml_tag = re.compile(r"<doc\s.*>|<\/doc>|<br.*>|\[\[.*\]\]|<pre>", re.IGNORECASE)
    extrax_regexes = [regex_xml_tag]

    extract_documents(fname, dbcollection, regex_fname, extrax_regexes)

    dbcollection.reindex()

