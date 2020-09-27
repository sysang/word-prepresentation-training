import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=72,
        window=5,
        min_count=99,
        sample=0.0001,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=3,
        min_alpha=0.0002,
        alpha=0.0002*50*3,
        comment='ech03,mal0002*50,refined',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(
            common_kwargs=common_kwargs,
            saved_fname=saved_fname,
            evaluate=False,
            database='refined')

"""
"""
