import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15, negative=18, window=2, min_count=75, sample=0.0001,
        dm=1, dm_concat=1, hs=0, epochs=5
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    corpus = 'thefinal'

    base.train(corpus, common_kwargs, saved_fname)

"""
2020-09-19 07:29:38,238 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-19 07:29:38,238 : INFO : Loading a fresh vocabulary
2020-09-19 07:29:38,707 : INFO : effective_min_count=75 retains 70715 unique words (3% of original 1784839, drops 1714124)
2020-09-19 07:29:38,708 : INFO : effective_min_count=75 leaves 329482258 word corpus (98% of original 336075146, drops 6592888)
2020-09-19 07:29:38,865 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-19 07:29:38,900 : INFO : sample=0.0001 downsamples 381 most-common words
2020-09-19 07:29:38,900 : INFO : downsampling leaves estimated 170152500 word corpus (51.6% of prior 329482258)
2020-09-19 07:29:39,040 : INFO : estimated required memory for 70715 words and 15 dimensions: 858214900 bytes

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n18,w2,mc75,s0.0001,t10)
Save model to: models/dmc_d15_n18_w2_mc75_s0001_ech05_thefinal.bin
2020-09-19 08:48:14,812 : INFO : saving Doc2Vec object under models/dmc_d15_n18_w2_mc75_s0001_ech05_thefinal.bin, separately None
2020-09-19 08:48:14,812 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n18_w2_mc75_s0001_ech05_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-19 08:48:14,842 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n18_w2_mc75_s0001_ech05_thefinal.bin.docvecs.vectors_docs.npy
2020-09-19 08:48:15,389 : INFO : saved models/dmc_d15_n18_w2_mc75_s0001_ech05_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 12428927
[+] index 12428927 -> "6 months is the amount of time i can write a blog before i decide to scrap the whole thing and start again"
2020-09-19 08:48:15,400 : INFO : precomputing L2-norms of doc weight vectors
!! No any match in top 100 similarities


.....get random document, tag: 11428852
[+] index 11428852 -> "and the majority of americans are on the conservative side of these issues still"
!! No any match in top 100 similarities


.....get random document, tag: 2587290
[+] index 2587290 -> "and so it is he said look at it as you will"
!! No any match in top 100 similarities


.....get random document, tag: 6110203
[+] index 6110203 -> "i just rented this movie last weekend and i can not understand why it only was nominated for a razzie"
!! No any match in top 100 similarities


.....get random document, tag: 8719967
[+] index 8719967 -> "the yazoo river was named by french explorer la salle in 1682 in reference to a native american tribe living near the river 's mouth"
!! No any match in top 100 similarities


.....get random document, tag: 11153650
[+] index 11153650 -> "of course a shadow of a statue of a major world leader is not much to speak about"
** Matched with rank 12, score: 0.8807097673416138


.....get random document, tag: 11010358
[+] index 11010358 -> "finally despite the love he had for his son blake packed his bags walked out the door and attempted to rebuild his life"
!! No any match in top 100 similarities




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (6110607): neither has had major success before or since warner had a lengthy run in family law and to be perfectly frank this movie gives a good idea why they have little charisma and no chemistry despite the fact that they supposedly fall in love during the film the story demands lead players who do not come across as insipid but it does not get them

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n18,w2,mc75,s0.0001,t10):

MOST (7877714, 0.92026287317276): «flood control and use of the colorado river is managed by three agencies established by the texas legislature the upper colorado river authority central colorado river authority and lower colorado river authority»

MEDIAN (12550600, -0.008587844669818878): «so maybe that is why today was harder than i really even thought it would be»

LEAST (10671229, -0.9500885009765625): «i am sorry to have to report the loss of two rochester hills residents that touched many people in our community»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'rectory' model: Doc2Vec(dm/c,d15,n18,w2,mc75,s0.0001,t10):
2020-09-19 08:48:40,276 : INFO : precomputing L2-norms of word weight vectors
     1. 0.98 'vicarage'
     2. 0.98 'plumstead'
     3. 0.97 'parsonage'
     4. 0.96 'limmeridge'
     5. 0.96 'deanery'
     6. 0.96 'aldborough'
     7. 0.95 'lowick'


[+] target_word: 'convince' model: Doc2Vec(dm/c,d15,n18,w2,mc75,s0.0001,t10):
     1. 0.97 'persuade'
     2. 0.95 'disown'
     3. 0.94 'warn'
     4. 0.94 'undeceive'
     5. 0.94 'embarrass'
     6. 0.94 'outdo'
     7. 0.93 'repay'


[+] target_word: 'pointing' model: Doc2Vec(dm/c,d15,n18,w2,mc75,s0.0001,t10):
     1. 0.96 'crumpling'
     2. 0.95 'poising'
     3. 0.94 'undid'
     4. 0.94 'disengaging'
     5. 0.93 'straightens'
     6. 0.93 'pursing'
     7. 0.93 'thrusting'


[+] target_word: 'topped' model: Doc2Vec(dm/c,d15,n18,w2,mc75,s0.0001,t10):
     1. 0.93 'skimmed'
     2. 0.93 'capped'
     3. 0.89 'seeded'
     4. 0.89 'picked'
     5. 0.89 'netted'
     6. 0.88 'raked'
     7. 0.88 'banked'


[+] target_word: 'succeeded' model: Doc2Vec(dm/c,d15,n18,w2,mc75,s0.0001,t10):
     1. 0.93 'overruled'
     2. 0.93 'quashed'
     3. 0.92 'miscarried'
     4. 0.92 'capitulated'
     5. 0.92 'testified'
     6. 0.92 'adjured'
     7. 0.92 'apprehended'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-19 08:48:40,950 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-19 08:48:41,316 : INFO : capital-common-countries: 7.7% (39/506)
2020-09-19 08:48:42,745 : INFO : capital-world: 3.6% (69/1929)
2020-09-19 08:48:42,925 : INFO : currency: 0.8% (2/236)
2020-09-19 08:48:44,501 : INFO : city-in-state: 1.6% (37/2330)
2020-09-19 08:48:44,848 : INFO : family: 36.4% (153/420)
2020-09-19 08:48:45,542 : INFO : gram1-adjective-to-adverb: 4.0% (40/992)
2020-09-19 08:48:46,095 : INFO : gram2-opposite: 4.3% (30/702)
2020-09-19 08:48:46,982 : INFO : gram3-comparative: 27.0% (360/1332)
2020-09-19 08:48:47,765 : INFO : gram4-superlative: 12.6% (133/1056)
2020-09-19 08:48:48,527 : INFO : gram5-present-participle: 20.3% (214/1056)
2020-09-19 08:48:49,610 : INFO : gram6-nationality-adjective: 6.9% (95/1371)
2020-09-19 08:48:50,811 : INFO : gram7-past-tense: 20.8% (325/1560)
2020-09-19 08:48:51,831 : INFO : gram8-plural: 12.1% (161/1332)
2020-09-19 08:48:52,511 : INFO : gram9-plural-verbs: 11.8% (103/870)
2020-09-19 08:48:52,511 : INFO : Quadruplets with out-of-vocabulary words: 19.7%
2020-09-19 08:48:52,511 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-19 08:48:52,511 : INFO : Total accuracy: 11.2% (1761/15692)
Doc2Vec(dm/c,d15,n18,w2,mc75,s0.0001,t10): 11.22% correct (1761 of 15692)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-19 08:48:52,791 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5050
2020-09-19 08:48:52,791 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4956
2020-09-19 08:48:52,791 : INFO : Pairs with unknown words ratio: 0.6%
((0.5049587010461574, 4.134152206627169e-24), SpearmanrResult(correlation=0.49562513413829273, pvalue=3.701586376277248e-23), 0.56657223796034)


02 - simlex999
2020-09-19 08:48:52,847 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3055
2020-09-19 08:48:52,847 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2677
2020-09-19 08:48:52,847 : INFO : Pairs with unknown words ratio: 0.3%
((0.30550665972686036, 5.824070720708776e-23), SpearmanrResult(correlation=0.2677074765729131, pvalue=8.293089816140366e-18), 0.3003003003003003)


03 - simverb3500
2020-09-19 08:48:53,131 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1811
2020-09-19 08:48:53,131 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1676
2020-09-19 08:48:53,131 : INFO : Pairs with unknown words ratio: 0.7%
((0.18110566362860253, 5.3324526173605746e-27), SpearmanrResult(correlation=0.16759085560596368, pvalue=2.657866109897889e-23), 0.7428571428571429)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
