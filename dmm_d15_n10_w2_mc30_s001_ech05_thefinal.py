# coding: utf-8
# import doc2vec_training_script_mongodb_connect as base
import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15, negative=10, window=2, min_count=30, sample=0.001,
        dm=1, dm_concat=0, hs=0, epochs=5
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    corpus = 'thefinal'

    base.train(corpus, common_kwargs, saved_fname)
