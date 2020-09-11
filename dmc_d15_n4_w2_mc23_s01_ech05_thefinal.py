# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=15, negative=4, window=2, min_count=23, sample=0.01,
    dm=1, dm_concat=1, hs=0, epochs=5
)

print("kwargs: %s" % (str(common_kwargs)))
saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'thefinal'

base.train(corpus, common_kwargs, saved_fname)
