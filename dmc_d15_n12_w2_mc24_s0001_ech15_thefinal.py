# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=15, negative=12, window=2, min_count=24, sample=0.0001,
    dm=1, dm_concat=1, hs=0, epochs=15
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'thefinal'

base.train(corpus, common_kwargs, saved_fname)
