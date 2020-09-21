# coding: utf-8
# import doc2vec_training_script_mongodb_connect as base
import doc2vec_training_script_rpc_connect as base
# import doc2vec_training_script_v0 as base

common_kwargs = dict(
    vector_size=15, negative=4, window=2, min_count=23, sample=0.0001,
    dm=1, dm_concat=0, hs=0, epochs=5
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'thefinal'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/m,d15,n4,w2,mc23,s0.0001,t5)
Save model to: models/dmm_d15_n4_w2_mc23_s0001_ech05_thefinal.bin
2020-09-13 19:50:26,412 : INFO : saving Doc2Vec object under models/dmm_d15_n4_w2_mc23_s0001_ech05_thefinal.bin, separately None
2020-09-13 19:50:26,412 : INFO : storing np array 'vectors_docs_lockf' to models/dmm_d15_n4_w2_mc23_s0001_ech05_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-13 19:50:26,441 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n4_w2_mc23_s0001_ech05_thefinal.bin.docvecs.vectors_docs.npy
2020-09-13 19:50:26,971 : INFO : saved models/dmm_d15_n4_w2_mc23_s0001_ech05_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 1035348
[+] index 1035348 -> "to affect a spurious ignorance is to disclose a genuine"
2020-09-13 19:50:26,984 : INFO : precomputing L2-norms of doc weight vectors
!! No any match in top 100 similarities


.....get random document, tag: 5897943
[+] index 5897943 -> "the idiotic comments people made at the time of its release about how quaint it was to see old-fashioned hand-drawn animation again as if the last pencil-animated cartoon had been released twenty years ago and the even more idiotic comments about how computers had now made the old techniques obsolete had got my blood up"
!! No any match in top 100 similarities


.....get random document, tag: 5331047
[+] index 5331047 -> "the doctrine of state rights can be so handled by an adroit demagogue as easily to confound the distinction between liberty and lawlessness in the minds of ignorant persons accustomed always to be influenced by the sound of certain words rather than to reflect upon the principles which give them meaning"
!! No any match in top 100 similarities


.....get random document, tag: 10980005
[+] index 10980005 -> "there 's absolutely no evidence that our president was absent from service for more than a month at a time"
!! No any match in top 100 similarities


.....get random document, tag: 2421568
[+] index 2421568 -> "she said that what she wanted was something more like lancelot or sir galahad and would i look on the episode as closed did you explain about the trousers yes"
!! No any match in top 100 similarities


.....get random document, tag: 8198203
[+] index 8198203 -> "the towers on the nativity facade are crowned with geometrically shaped tops that were probably influenced by cubism they were finished around 1920"
!! No any match in top 100 similarities


.....get random document, tag: 10376924
[+] index 10376924 -> "0 00% of the population are hispanic or latino of any race"
!! No any match in top 100 similarities




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (7512579): as of the census of 2000 there are 5 369 people 1 884 households and 1 537 families residing in the town

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/m,d15,n4,w2,mc23,s0.0001,t5):

MOST (10158391, 0.9436109066009521): «there are 6 205 housing units at an average density of 1 104 0/km² 2 857 3/mi²»

MEDIAN (7876514, -0.1704375296831131): «as the war drew to a close their hoped-for plan to return to cockade was achieved but they were disappointed in both the state of the house and the attitude of their one-time servants»

LEAST (10727001, -0.9173303246498108): «it 's really difficult to get big-shot dealers and critics and collectors into your gallery if you are a junior member of the art world in new york city»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'amid' model: Doc2Vec(dm/m,d15,n4,w2,mc23,s0.0001,t5):
2020-09-13 19:50:52,098 : INFO : precomputing L2-norms of word weight vectors
     1. 0.99 'amidst'
     2. 0.90 'tumultuous'
     3. 0.90 'midst'
     4. 0.86 'wildest'
     5. 0.86 'ghostly'
     6. 0.84 'distant'
     7. 0.84 'never-ending'


[+] target_word: 'monitor' model: Doc2Vec(dm/m,d15,n4,w2,mc23,s0.0001,t5):
     1. 0.94 'search'
     2. 0.93 'switch'
     3. 0.92 'setup'
     4. 0.90 'counter'
     5. 0.89 'tracking'
     6. 0.89 'monitors'
     7. 0.89 'computer'


[+] target_word: 'sitting' model: Doc2Vec(dm/m,d15,n4,w2,mc23,s0.0001,t5):
     1. 0.97 'sat'
     2. 0.94 'walking'
     3. 0.93 'walked'
     4. 0.91 'standing'
     5. 0.91 'walks'
     6. 0.91 'rides'
     7. 0.90 'locked'


[+] target_word: 'expect' model: Doc2Vec(dm/m,d15,n4,w2,mc23,s0.0001,t5):
     1. 0.97 'do'
     2. 0.97 'suppose'
     3. 0.97 'know'
     4. 0.96 'think'
     5. 0.95 'wish'
     6. 0.94 'mean'
     7. 0.94 'say'


[+] target_word: 'railroads' model: Doc2Vec(dm/m,d15,n4,w2,mc23,s0.0001,t5):
     1. 0.97 'railways'
     2. 0.89 'shipping'
     3. 0.89 'airports'
     4. 0.89 'routes'
     5. 0.89 'roads'
     6. 0.88 'offshore'
     7. 0.88 'highways'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-13 19:50:53,273 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-13 19:50:53,820 : INFO : capital-common-countries: 7.5% (38/506)
2020-09-13 19:50:58,072 : INFO : capital-world: 2.7% (103/3773)
2020-09-13 19:50:58,662 : INFO : currency: 0.4% (2/458)
2020-09-13 19:51:00,488 : INFO : city-in-state: 2.1% (53/2467)
2020-09-13 19:51:01,260 : INFO : family: 38.5% (195/506)
2020-09-13 19:51:02,492 : INFO : gram1-adjective-to-adverb: 4.0% (40/992)
2020-09-13 19:51:03,628 : INFO : gram2-opposite: 3.7% (30/812)
2020-09-13 19:51:05,082 : INFO : gram3-comparative: 34.2% (455/1332)
2020-09-13 19:51:06,058 : INFO : gram4-superlative: 11.6% (130/1122)
2020-09-13 19:51:07,050 : INFO : gram5-present-participle: 18.5% (195/1056)
2020-09-13 19:51:08,736 : INFO : gram6-nationality-adjective: 11.6% (177/1521)
2020-09-13 19:51:10,304 : INFO : gram7-past-tense: 36.9% (575/1560)
2020-09-13 19:51:11,973 : INFO : gram8-plural: 18.5% (246/1332)
2020-09-13 19:51:12,911 : INFO : gram9-plural-verbs: 12.3% (107/870)
2020-09-13 19:51:12,912 : INFO : Quadruplets with out-of-vocabulary words: 6.3%
2020-09-13 19:51:12,912 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-13 19:51:12,912 : INFO : Total accuracy: 12.8% (2346/18307)
Doc2Vec(dm/m,d15,n4,w2,mc23,s0.0001,t5): 12.81% correct (2346 of 18307)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-13 19:51:13,272 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4793
2020-09-13 19:51:13,272 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4712
2020-09-13 19:51:13,272 : INFO : Pairs with unknown words ratio: 0.0%
((0.4792982042191215, 1.1233177785127701e-21), SpearmanrResult(correlation=0.4711630242115881, pvalue=6.592414289803181e-21), 0.0)


02 - simlex999
2020-09-13 19:51:13,612 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3170
2020-09-13 19:51:13,612 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2661
2020-09-13 19:51:13,612 : INFO : Pairs with unknown words ratio: 0.2%
((0.3169767892662565, 1.0467270390162366e-24), SpearmanrResult(correlation=0.2660543374858714, pvalue=1.2889724801270495e-17), 0.20020020020020018)


03 - simverb3500
2020-09-13 19:51:14,202 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1511
2020-09-13 19:51:14,202 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1276
2020-09-13 19:51:14,202 : INFO : Pairs with unknown words ratio: 0.1%
((0.15105330533642902, 2.6523411374553475e-19), SpearmanrResult(correlation=0.12761817238648673, pvalue=3.560059006553775e-14), 0.05714285714285715)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
