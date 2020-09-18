import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15, negative=18, window=2, min_count=60, sample=0.0001,
        dm=1, dm_concat=1, hs=0, epochs=5
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    corpus = 'thefinal'

    base.train(corpus, common_kwargs, saved_fname)

"""
2020-09-18 20:32:58,934 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-18 20:32:58,934 : INFO : Loading a fresh vocabulary
2020-09-18 20:32:59,412 : INFO : effective_min_count=60 retains 79424 unique words (4% of original 1784839, drops 1705415)
2020-09-18 20:32:59,412 : INFO : effective_min_count=60 leaves 330061954 word corpus (98% of original 336075146, drops 6013192)
2020-09-18 20:32:59,589 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-18 20:32:59,626 : INFO : sample=0.0001 downsamples 380 most-common words
2020-09-18 20:32:59,626 : INFO : downsampling leaves estimated 170789420 word corpus (51.7% of prior 330061954)
2020-09-18 20:32:59,783 : INFO : estimated required memory for 79424 words and 15 dimensions: 865704640 bytes

"""
