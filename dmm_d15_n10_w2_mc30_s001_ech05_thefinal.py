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

"""
2020-09-18 17:44:42,617 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-18 17:44:42,617 : INFO : Loading a fresh vocabulary
2020-09-18 17:44:43,178 : INFO : effective_min_count=30 retains 115175 unique words (6% of original 1784839, drops 1669664)
2020-09-18 17:44:43,178 : INFO : effective_min_count=30 leaves 331558488 word corpus (98% of original 336075146, drops 4516658)
2020-09-18 17:44:43,443 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-18 17:44:43,477 : INFO : sample=0.001 downsamples 47 most-common words
2020-09-18 17:44:43,477 : INFO : downsampling leaves estimated 249829581 word corpus (75.4% of prior 331558488)


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/m,d15,n10,w2,mc30,s0.001,t10)
Save model to: models/dmm_d15_n10_w2_mc30_s001_ech05_thefinal.bin
2020-09-18 17:08:14,474 : INFO : saving Doc2Vec object under models/dmm_d15_n10_w2_mc30_s001_ech05_thefinal.bin, separately None
2020-09-18 17:08:14,474 : INFO : storing np array 'vectors_docs_lockf' to models/dmm_d15_n10_w2_mc30_s001_ech05_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-18 17:08:14,503 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n10_w2_mc30_s001_ech05_thefinal.bin.docvecs.vectors_docs.npy
2020-09-18 17:08:14,999 : INFO : saved models/dmm_d15_n10_w2_mc30_s001_ech05_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 8593938
[+] index 8593938 -> "some systems unimodal ford research 's prism have found that the weight and cost difference between these sizes of vehicles is so low that two seats is optimum with tandem seating and a low drag shape"
2020-09-18 17:08:15,009 : INFO : precomputing L2-norms of doc weight vectors
!! No any match in top 100 similarities


.....get random document, tag: 2504756
[+] index 2504756 -> "indeed he was hardly aware that he was awake for he first came to the consciousness that he was lying on the ground with a number of wild-looking figures around him some of whom bore torches while hugh held by two of them was close by"
!! No any match in top 100 similarities


.....get random document, tag: 7969946
[+] index 7969946 -> "the per capita income for the city is $16 535"
!! No any match in top 100 similarities


.....get random document, tag: 3281735
[+] index 3281735 -> "the dawn is not nigh and the trees are bare and the waterways sigh that a year has drawn by and two are out there"
!! No any match in top 100 similarities


.....get random document, tag: 5447765
[+] index 5447765 -> "lyle by worse luck was young and strong and took an unconscionable time dying i do not know that i did well when i took the pistol from him"
!! No any match in top 100 similarities


.....get random document, tag: 7555232
[+] index 7555232 -> "if you are in a disaster help might be days or even weeks away"
!! No any match in top 100 similarities


.....get random document, tag: 8142628
[+] index 8142628 -> "corte was the capital of the corsican independent state during the period of pasquale paoli"
!! No any match in top 100 similarities




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (2028497): he went out the other way some time ago

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/m,d15,n10,w2,mc30,s0.001,t10):

MOST (12219388, 0.9862269163131714): «i came home early after my conversation with the boss»

MEDIAN (6682538, 0.7103794813156128): «during his tenure as senator he was selected by the philippine free press magazine as one of the outstanding senators»

LEAST (9651260, -0.9397100806236267): «3 06% of the population are hispanic or latino of any race»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'affirmed' model: Doc2Vec(dm/m,d15,n10,w2,mc30,s0.001,t10):
2020-09-18 17:08:41,014 : INFO : precomputing L2-norms of word weight vectors
     1. 0.97 'asserted'
     2. 0.97 'acknowledged'
     3. 0.96 'contradicted'
     4. 0.96 'decreed'
     5. 0.96 'refuted'
     6. 0.95 'expounded'
     7. 0.95 'contended'


[+] target_word: 'contact' model: Doc2Vec(dm/m,d15,n10,w2,mc30,s0.001,t10):
     1. 0.91 'readiness'
     2. 0.89 'ease'
     3. 0.89 'rheumatism'
     4. 0.88 'bloodstream'
     5. 0.88 'strength'
     6. 0.88 'intent'
     7. 0.87 'control'


[+] target_word: 'baron' model: Doc2Vec(dm/m,d15,n10,w2,mc30,s0.001,t10):
     1. 0.96 'marquis'
     2. 0.96 'abbot'
     3. 0.95 'chevalier'
     4. 0.95 'baroness'
     5. 0.95 'vicar'
     6. 0.95 'bishop'
     7. 0.95 'freedman'


[+] target_word: 'contrived' model: Doc2Vec(dm/m,d15,n10,w2,mc30,s0.001,t10):
     1. 0.95 'disposed'
     2. 0.93 'careful'
     3. 0.93 'seemed'
     4. 0.92 'determined'
     5. 0.92 'constrained'
     6. 0.92 'desired'
     7. 0.91 'calculated'


[+] target_word: 'disorder' model: Doc2Vec(dm/m,d15,n10,w2,mc30,s0.001,t10):
     1. 0.96 'generalities'
     2. 0.95 'disease'
     3. 0.94 'vigour'
     4. 0.94 'psychosis'
     5. 0.94 'asthma'
     6. 0.94 'self-consciousness'
     7. 0.94 'emotion'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-18 17:08:42,304 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-18 17:08:42,849 : INFO : capital-common-countries: 6.9% (35/506)
2020-09-18 17:08:46,646 : INFO : capital-world: 1.9% (65/3352)
2020-09-18 17:08:47,122 : INFO : currency: 0.5% (2/376)
2020-09-18 17:08:49,881 : INFO : city-in-state: 1.1% (26/2394)
2020-09-18 17:08:50,535 : INFO : family: 42.9% (217/506)
2020-09-18 17:08:51,853 : INFO : gram1-adjective-to-adverb: 2.5% (25/992)
2020-09-18 17:08:52,949 : INFO : gram2-opposite: 3.7% (30/812)
2020-09-18 17:08:54,959 : INFO : gram3-comparative: 16.1% (214/1332)
2020-09-18 17:08:56,763 : INFO : gram4-superlative: 7.0% (74/1056)
2020-09-18 17:08:58,124 : INFO : gram5-present-participle: 5.9% (62/1056)
2020-09-18 17:09:00,063 : INFO : gram6-nationality-adjective: 5.7% (83/1445)
2020-09-18 17:09:02,168 : INFO : gram7-past-tense: 8.9% (139/1560)
2020-09-18 17:09:03,796 : INFO : gram8-plural: 8.5% (113/1332)
2020-09-18 17:09:04,986 : INFO : gram9-plural-verbs: 11.8% (103/870)
2020-09-18 17:09:04,987 : INFO : Quadruplets with out-of-vocabulary words: 10.0%
2020-09-18 17:09:04,987 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-18 17:09:04,987 : INFO : Total accuracy: 6.8% (1188/17589)
Doc2Vec(dm/m,d15,n10,w2,mc30,s0.001,t10): 6.75% correct (1188 of 17589)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-18 17:09:05,322 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4126
2020-09-18 17:09:05,323 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4002
2020-09-18 17:09:05,323 : INFO : Pairs with unknown words ratio: 0.3%
((0.41258582236179575, 6.70090177877961e-16), SpearmanrResult(correlation=0.40020561707561236, pvalue=5.689229101935931e-15), 0.28328611898017)


02 - simlex999
2020-09-18 17:09:05,642 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2601
2020-09-18 17:09:05,642 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2227
2020-09-18 17:09:05,642 : INFO : Pairs with unknown words ratio: 0.3%
((0.2600906999389758, 7.30470913412936e-17), SpearmanrResult(correlation=0.2226850027250247, pvalue=1.1736493765076138e-12), 0.3003003003003003)


03 - simverb3500
2020-09-18 17:09:06,211 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1271
2020-09-18 17:09:06,212 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1227
2020-09-18 17:09:06,212 : INFO : Pairs with unknown words ratio: 0.1%
((0.12708506708658504, 4.549829459908244e-14), SpearmanrResult(correlation=0.12268846944355624, pvalue=3.3085852470521353e-13), 0.05714285714285715)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
