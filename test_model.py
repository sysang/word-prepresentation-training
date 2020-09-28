from gensim.models import Doc2Vec
from gensim.models import KeyedVectors


model_fpath = 'models/dmc_d15_n67_w5_mc999_s00002_ech05_mal0002x25_elephant.bin'
fpath = 'doc2vec-model.bin'


def transform_trained_model():
    model = Doc2Vec.load(model_fpath)
    model.delete_temporary_training_data(keep_doctags_vectors=True, keep_inference=True)
    model.save_word2vec_format(fpath)


# transform_trained_model()

d2vmodel = Doc2Vec.load(fpath)


def eval_similarity(m, first, second):
    similarity = m.similarity(first, second)
    print('%s vs %s, score: %f' % (first, second, similarity))


def get_vector(m, w):
    print(m.get_vector(w))


vectors = d2vmodel.infer_vector(['i', 'am', 'excited'])
print(vectors)





