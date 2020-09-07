import re
from pymongo import MongoClient
from dump_master import extract_documents


with MongoClient('172.17.0.1', 27017, username='myUserAdmin', password='111') as client:
    fname = 'bloggercom_mkopper.tar.gz'

    dbcollection = client.bloggercom.posts

    regex_fname = re.compile(r'blogs\/(\d+)\.(male|female)\.[2-9][4-9]\.(.+)\.(\w+)\.xml')
    regex_xml_tag = re.compile(r"<date>.*</date>|<blog>|<\/blog>|<post>|<\/post>", re.IGNORECASE)
    extrax_regexes = [regex_xml_tag]

    extract_documents(fname, dbcollection, regex_fname, extrax_regexes)

    dbcollection.reindex()
