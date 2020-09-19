import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=30,
        window=3,
        min_count=75,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        min_alpha=0.0025,
        alpha=0.0025*20*1,
        epochs=20,
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    corpus = 'thefinal'

    base.train(corpus, common_kwargs, saved_fname)
