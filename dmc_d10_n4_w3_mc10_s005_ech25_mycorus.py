# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=10, negative=4, window=3, min_count=10, sample=0.005,
    dm=1, dm_concat=1, hs=0, epochs=5
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'mycorus'

base.train(corpus, common_kwargs, saved_fname)
