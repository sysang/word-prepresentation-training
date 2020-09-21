import re
from pymongo import MongoClient
from dump_master import extract_documents


def gutenberg(dbcollection):
    fnames = ['gutenberg.tar.gz']

    repl = " "
    regex_fname = re.compile(r'Gutenberg/txt/\S+\.txt$')
    regex_newline = re.compile(r"\r\n")
    regex01 = re.compile(r"\[Illustration\:\s.+\]")
    regex02 = re.compile(r"\[Illustration\:\s.+")
    regex03 = re.compile(r"\{\d+\}\s+.+")
    regex04 = re.compile(r"([A-Z]\s*[A-Z\.\,\-\'\[\]]+\s*)+")
    regex05 = re.compile(r"\([A-Z\s]*\)")
    regex06 = re.compile(r"[A-Z]\w+:\s+[A-Z][\w\s]+")

    extrax_regexes = [
            (regex_newline, repl),
            (regex01, repl),
            (regex02, repl),
            (regex03, repl),
            (regex04, repl),
            (regex05, repl),
            (regex06, repl)
            ]

    for fname in fnames:
        extract_documents(fname, dbcollection, regex_fname, extrax_regexes)


if __name__ == "__main__":
    with MongoClient('127.0.0.1', 27017, username='myUserAdmin', password='111') as client:
        db = client.gutenberg
        dbcollection = db.books

        dbcollection.delete_many({})

        gutenberg(dbcollection)

        db.command({"reIndex": "books"})
