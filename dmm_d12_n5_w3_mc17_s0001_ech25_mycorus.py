import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=12, negative=5, window=3, min_count=17, sample=0.0001,
    dm=1, dm_concat=0, hs=0, epochs=25
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'mycorus'

base.train(corpus, common_kwargs, saved_fname)
