import re
from pymongo import MongoClient
from dump_master import extract_documents
import os
import time
import tarfile


def filter_line(regexes, str, repl=" "):
    if len(regexes):
        layer = regexes.pop()
        return filter_line(regexes, layer.sub(repl, str), repl)
    return str


def verify_line(regexes, str):
    for regex in regexes:
        if regex.search(str):
            return False
    return True


class UsenetCorpus():
    def __init__(self, fname):
        self.fname = fname
        self.regex_fname = re.compile(r'splits/\w\w\w$')
        self.verify_regexes = [
                re.compile(r"\-\-\-END\.OF\.DOCUMENT\-\-\-", re.IGNORECASE),
                re.compile(r"\<.*\>", re.IGNORECASE),
                # Fri, 30 Sep 2005 02:47:26 GMT
                re.compile(r"\d\d\s\w\w\w\s\d\d\d\d\s\d\d\:\d\d\:\d\d", re.IGNORECASE),
                re.compile(r"\(.*\W*.*\)", re.IGNORECASE),
                re.compile(r"^[^.]+$", re.IGNORECASE),
                re.compile(r"\d+.*\s+", re.IGNORECASE),
                re.compile(r"\S{20}", re.IGNORECASE),
                re.compile(r"(��)*\s*(��){2,}", re.IGNORECASE),
                ]

    def __iter__(self):
        # f is an install of bz2.BZ2File class
        with tarfile.open(self.fname, mode='r:gz') as tar:
            for member in tar.getmembers():
                # print(member.name)
                if self.regex_fname.match(member.name):
                    member_text = tar.extractfile(member).readlines()
                    for line in member_text:
                        line = line.decode('utf-8', errors='replace')
                        if line.strip().replace("\n", "").replace("\r\n", "") and verify_line(self.verify_regexes, line.strip()):
                            yield line


def usenet(dbcollection):
    fname = "/archives/corpus/usenet_westburylab.splits.tar.gz"

    corpus = UsenetCorpus(fname)

    extract_documents(dbcollection, corpus=corpus)


if __name__ == "__main__":
    with MongoClient('127.0.0.1', 27017, username='myUserAdmin', password='111') as client:
        db = client.usenet
        dbcollection = db.docs

        usenet(dbcollection)

        print('Almost done, re-indexing database...')
        db.command({"reIndex": "docs"})
