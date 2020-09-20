import multiprocessing as mp


class UseCorpus():
    def __iter__(self):
        with open(fname, errors='replace') as f:
            for line in f:
                yield(line)


fname = "/archives/corpus/WestburyLab-NonRedundant-UsenetCorpus/WestburyLab.NonRedundant.UsenetCorpus.txt"
text_corpus = UseCorpus()
volume = 1000
skip = 5000

index = 0
for text in text_corpus:
    index += 1
    if not index > skip:
        continue
    print(text)
    if index > skip + volume:
        break
