import multiprocessing as mp
import re
import time


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
        with open(self.fname, errors='replace') as f:
            for line in f:
                if line.strip().replace("\n", "").replace("\r\n", "") and verify_line(self.verify_regexes, line.strip()):
                    yield(line)


if __name__ == "__main__":
    fname = "/archives/corpus/WestburyLab-NonRedundant-UsenetCorpus/WestburyLab.NonRedundant.UsenetCorpus.txt"
    text_corpus = UsenetCorpus(fname)
    volume = 4000
    skip = 200000

    index = 0
    for text in text_corpus:
        index += 1
        if not index > skip:
            continue
        print(text)
        if index > skip + volume:
            break
