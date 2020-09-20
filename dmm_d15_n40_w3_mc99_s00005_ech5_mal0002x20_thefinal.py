import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=40,
        window=3,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=0,
        hs=0,
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*20*5
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
2020-09-20 21:19:39,951 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-20 21:19:39,951 : INFO : Loading a fresh vocabulary
2020-09-20 21:19:40,421 : INFO : effective_min_count=99 retains 61077 unique words (3% of original 1784839, drops 1723762)
2020-09-20 21:19:40,421 : INFO : effective_min_count=99 leaves 328657804 word corpus (97% of original 336075146, drops 7417342)
2020-09-20 21:19:40,562 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-20 21:19:40,597 : INFO : sample=5e-05 downsamples 733 most-common words
2020-09-20 21:19:40,597 : INFO : downsampling leaves estimated 147142569 word corpus (44.8% of prior 328657804)
2020-09-20 21:19:40,714 : INFO : estimated required memory for 61077 words and 15 dimensions: 835267740 bytes

"""
