import doc2vec_training_script_multiprocessing as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=12,
        negative=50,
        window=2,
        min_count=109,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*25*5,
        comment='ech05,mal0002x25',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)
