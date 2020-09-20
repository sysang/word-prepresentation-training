from pymongo import MongoClient
import tarfile
import re
import math


class TextCorpus():
    def __init__(self, fname, regex_fname):
        self.fname = fname
        self.regex_fname = regex_fname

    def __iter__(self):
        with tarfile.open(self.fname, mode='r:gz') as tar:
            for member in tar.getmembers():
                # print(member.name)
                if self.regex_fname.match(member.name):
                    # print(member.name)
                    member_bytes = tar.extractfile(member).read()
                    yield member_bytes.decode('utf-8', errors='replace')


def repl_process_prime_s(matchobj):
    return matchobj.group(1) + matchobj.group(2) + ' ' + matchobj.group(3)


def repl_process_letter_dash(matchobj):
    return matchobj.group(1) + matchobj.group(2) + ' '


def repl_process_quote(matchobj):
    return ' ' + matchobj.group(1) + ' '


def recursively_replace(__regex, repl, str):
    old_str = ""
    while old_str != str:
        old_str = str
        str = __regex.sub(repl, str)

    return str


def extract_documents(dbcollection, regex_fname=None, fname=None, corpus=None, extrax_regexes=[]):
    regex = re.compile(r"\(|\)|\<|\>|\{|\}|\_|\.|\,|\-\-|(^|\s)\-\s|\;|\:|\*|\#|\?|\!|\~|\[|\]|\\|\"|”|\=|\+|\\x85|\\x91|\\x96|urllink|nbsp|andnbsp|�|:-)", re.IGNORECASE)
    regex_special_expression = re.compile("<.+>")
    regex_prime = re.compile(r"(^|\s)(\w+)(\'s|\'d)", re.IGNORECASE)
    regex_dash = re.compile(r"(^|\s)(\w+)(\-\s)", re.IGNORECASE)
    regex_quote = re.compile(r"\s\'\s*(\w[\w\s]*\w)\s*\'(\s|$)", re.IGNORECASE)
    regex_url = re.compile(r"\s(\w+)\.(\w+)(\s|$)")
    regex_double_spaces = re.compile(r"\s\s")
    regex_min_eight = re.compile(r"\S(\s\S+){8}")

    if not fname and not corpus:
        raise Exception("No corpus!")

    if corpus:
        text_corpus = corpus
    else:
        text_corpus = TextCorpus(fname, regex_fname)

    bulk_vol = 0
    docs = []
    tag = dbcollection.count_documents({})
    batch_size = 100000
    batch_index = math.floor(tag / batch_size)
    max_length = 1

    for member_text in text_corpus:
        for xRegex, xRepl in extrax_regexes:
            member_text = xRegex.sub(xRepl, member_text)

        member_text = (
                member_text.lower()
                .replace('<br />', ' ').replace('<br/>', ' ').replace('...', '.')
                .replace("\\", " ").replace(" / ", " ").replace(" ' ", " ")
                .replace('&', 'and').replace("'n'", " and ").replace(" 'n ", " and ")
                .replace("isn't", "is not").replace("'m", " am")
                .replace("aren't", "are not").replace("'re", " are").replace("ain't", "are not")
                .replace("aren�t", " are not").replace("�re", " are").replace("weren�t", " were not")
                .replace("doesn't", "does not").replace("dosen't", "does not").replace("doesnt", "does not").replace("doesn`t", "does not") 
                .replace("don't", "do not").replace("don`t", "do not").replace("don´t", "do not").replace("dont", "do not")
                .replace("didn't", "did not").replace("didn´t", "did not") .replace("did'nt", "did not").replace("didn´t", "did not")
                .replace("didn´t", "did not").replace("did't", "did not").replace("didn`t", "did not").replace("didnt", "did not") 
                .replace("wasn't", "was not").replace("weren't", "were not") .replace("wasn´t", "was not")
                .replace("wasnt", "was not").replace("werent", "were not") .replace("wasnt", "was not")
                .replace("haven't", "have not").replace("hasn't", "has not").replace("hasn�t", "has not")
                .replace("'ve", " have").replace(" ' ve", " have").replace("�ve", " have").replace(" � ve", " have")
                .replace("won't", "will not").replace("'ll", " will").replace("wont", "will not").replace("won`t'", "will not")
                .replace("won�t", "will not").replace("�ll", " will")
                .replace("wouldn't", "would not").replace("shouldn't", "should not").replace("mustn't", "must not").replace("wouldnt", "would not")
                .replace("wouldn�t", "would not").replace("shouldn�t", "should not").replace("mustn�t", "must not")
                .replace("cannot", "can not").replace("couldn't", "could not").replace("can't", "can not").replace("cant", "can not")
                .replace("could'nt", "could not").replace("couldnt", "could not").replace("could`nt", "could not")
                .replace("couldn�t", "could not").replace("can�t", "can not")
                .replace("doin'", "doing").replace("goin'", "going").replace("'em", "them")
                .replace("doin�", "doing").replace("goin�", "going").replace("�em", "them")
                .replace("'bout", "about").replace("�bout", "about")
        )

        paragraphs = member_text.splitlines()

        for pgraph in paragraphs:
            for sentence in pgraph.split('. '):
                text = regex.sub(" ", sentence)
                text = regex_special_expression.sub(" ", sentence)
                text = regex_url.sub(" ", text)
                text = regex_prime.sub(repl_process_prime_s, text)
                text = regex_dash.sub(repl_process_letter_dash, text)
                text = regex_quote.sub(repl_process_quote, text)
                text = text.strip()

                text = recursively_replace(regex_double_spaces, " ", text)

                # drop sentence that's too short
                if not regex_min_eight.search(text):
                    continue

                length = len(text)
                if length > max_length:
                    max_length = length

                doc = {'text': text, 'tag': tag, 'batch_index': batch_index}
                docs.append(doc)
                bulk_vol += 1
                tag += 1

                if tag % batch_size == 0:
                    batch_index += 1
                    print("\n")
                    print('-----------  BATCH INDEX: %s' % (batch_index) + '  --------------')

                if bulk_vol >= 10000:
                    print(doc['text'])
                    dbcollection.insert_many(docs)
                    docs.clear()
                    bulk_vol = 0

    print("*** MAXIMUM SENTENCE LENGTH: " + str(max_length))
