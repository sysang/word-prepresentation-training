import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=50,
        negative=67,
        window=5,
        min_count=99,
        sample=0.001,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*20*5,
        comment='ech05,mal0002x20,refined',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(
                common_kwargs=common_kwargs,
                saved_fname=saved_fname,
                evaluate=False,
                database='refined'
            )

"""
"""
