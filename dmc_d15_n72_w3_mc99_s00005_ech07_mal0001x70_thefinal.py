import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=72,
        window=3,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=7,
        min_alpha=0.0001,
        alpha=0.0001*70*7,
        comment='ech07,mal0001*70',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    pprint.pprint(common_kwargs)

    base.train(common_kwargs, saved_fname)

"""
2020-09-22 20:55:09,720 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-22 20:55:09,720 : INFO : Loading a fresh vocabulary
2020-09-22 20:55:10,150 : INFO : effective_min_count=99 retains 61077 unique words (3% of original 1784839, drops 1723762)
2020-09-22 20:55:10,150 : INFO : effective_min_count=99 leaves 328657804 word corpus (97% of original 336075146, drops 7417342)
2020-09-22 20:55:10,287 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-22 20:55:10,323 : INFO : sample=5e-05 downsamples 733 most-common words
2020-09-22 20:55:10,323 : INFO : downsampling leaves estimated 147142569 word corpus (44.8% of prior 328657804)
2020-09-22 20:55:10,434 : INFO : estimated required memory for 61077 words and 15 dimensions: 857255460 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech07,mal0001*70",dm/c,d15,n72,w3,mc99,s5e-05,t6)
Save model to: models/dmc_d15_n72_w3_mc99_s00005_ech07_mal0001x70_thefinal.bin
2020-09-22 22:31:47,989 : INFO : saving Doc2Vec object under models/dmc_d15_n72_w3_mc99_s00005_ech07_mal0001x70_thefinal.bin, separately None
2020-09-22 22:31:47,989 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n72_w3_mc99_s00005_ech07_mal0001x70_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-22 22:31:48,019 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n72_w3_mc99_s00005_ech07_mal0001x70_thefinal.bin.docvecs.vectors_docs.npy
2020-09-22 22:31:48,597 : INFO : saved models/dmc_d15_n72_w3_mc99_s00005_ech07_mal0001x70_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 614813
[+] index 614813 -> "seeing the young girl curiously watching him with an expectant smile he regretted it"
2020-09-22 22:31:48,611 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 100 similarities.


.....get random document, tag: 2004379
[+] index 2004379 -> "i have in short followed different plans but in every case have taken all the precautions which i could think of so that the two lots should be equally favoured"
[*] Matched with rank 3, score: 0.9299097657203674!


.....get random document, tag: 9271438
[+] index 9271438 -> "can halakha live by rabbi edward feld the reconstructionist vol 59 2 fall 1994 p 64-72"
    No any match in top 100 similarities.


.....get random document, tag: 5005739
[+] index 5005739 -> "francis made a detour so as to avoid being noticed by the gondoliers and then again followed"
    No any match in top 100 similarities.


.....get random document, tag: 479261
[+] index 479261 -> "it was like that i remember when you was a girl"
    No any match in top 100 similarities.


.....get random document, tag: 2381986
[+] index 2381986 -> "and could you reconcile it to your conscience to supplant your friend isaac"
    No any match in top 100 similarities.


.....get random document, tag: 10967368
[+] index 10967368 -> "i 'd say we need a good programmer regardless of gender or race"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (8228962): he often issued letters to the main scholars of the time not only in europe asking for solutions to questions of science mathematics and physics

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech07,mal0001*70",dm/c,d15,n72,w3,mc99,s5e-05,t6):

MOST (9391529, 0.9334895610809326): «historians obtain information about the past from various kinds of sources including written or printed records coins or other artifacts buildings and monuments and interviews oral history»

MEDIAN (2578183, 0.0008459612727165222): «lord john contrasted this language of lord althorp simple plain emphatic and decided with the language of the government of sir robert peel and held up to admiration the whig policy of 1833 certainly coercive but with remedial measures a measure for the abolition of church cess introduced ten days before the coercion bill and a promise of municipal reform made simultaneously with the proclamation of martial law»

LEAST (5165200, -0.9247994422912598): «engage the man by all means she left the room for the second time»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'up-stairs' model: Doc2Vec("ech07,mal0001*70",dm/c,d15,n72,w3,mc99,s5e-05,t6):
2020-09-22 22:32:13,822 : INFO : precomputing L2-norms of word weight vectors
     1. 0.99 'upstairs'
     2. 0.98 'down-stairs'
     3. 0.98 'downtairs'
     4. 0.90 'toll-gate'
     5. 0.89 'homeward'
     6. 0.89 'back'
     7. 0.88 'home'


[+] target_word: 'wagon' model: Doc2Vec("ech07,mal0001*70",dm/c,d15,n72,w3,mc99,s5e-05,t6):
     1. 0.95 'raft'
     2. 0.95 'jeep'
     3. 0.94 'dinghy'
     4. 0.94 'truck'
     5. 0.93 'sedan'
     6. 0.92 'minivan'
     7. 0.92 'buggy'


[+] target_word: 'stated' model: Doc2Vec("ech07,mal0001*70",dm/c,d15,n72,w3,mc99,s5e-05,t6):
     1. 0.96 'argued'
     2. 0.94 'asserted'
     3. 0.94 'alleges'
     4. 0.94 'formulated'
     5. 0.93 'explained'
     6. 0.93 'endorsed'
     7. 0.93 'concluded'


[+] target_word: 'linking' model: Doc2Vec("ech07,mal0001*70",dm/c,d15,n72,w3,mc99,s5e-05,t6):
     1. 0.94 'connecting'
     2. 0.91 'merging'
     3. 0.91 'connect'
     4. 0.90 'conjunction'
     5. 0.90 'connects'
     6. 0.90 'reconstructing'
     7. 0.89 'bypassing'


[+] target_word: 'edifice' model: Doc2Vec("ech07,mal0001*70",dm/c,d15,n72,w3,mc99,s5e-05,t6):
     1. 0.94 'monument'
     2. 0.93 'façade'
     3. 0.92 'pediment'
     4. 0.91 'spire'
     5. 0.91 'edifices'
     6. 0.90 'portico'
     7. 0.90 'sculpture'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-22 22:32:14,485 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-22 22:32:14,812 : INFO : capital-common-countries: 7.3% (37/506)
2020-09-22 22:32:16,008 : INFO : capital-world: 5.8% (103/1779)
2020-09-22 22:32:16,123 : INFO : currency: 0.6% (1/178)
2020-09-22 22:32:17,406 : INFO : city-in-state: 3.0% (67/2267)
2020-09-22 22:32:17,743 : INFO : family: 34.0% (143/420)
2020-09-22 22:32:18,349 : INFO : gram1-adjective-to-adverb: 4.3% (43/992)
2020-09-22 22:32:18,756 : INFO : gram2-opposite: 5.7% (40/702)
2020-09-22 22:32:19,412 : INFO : gram3-comparative: 27.1% (361/1332)
2020-09-22 22:32:20,006 : INFO : gram4-superlative: 9.8% (104/1056)
2020-09-22 22:32:20,608 : INFO : gram5-present-participle: 14.6% (154/1056)
2020-09-22 22:32:21,479 : INFO : gram6-nationality-adjective: 11.7% (161/1371)
2020-09-22 22:32:22,503 : INFO : gram7-past-tense: 21.1% (329/1560)
2020-09-22 22:32:23,463 : INFO : gram8-plural: 13.1% (174/1332)
2020-09-22 22:32:24,050 : INFO : gram9-plural-verbs: 10.3% (90/870)
2020-09-22 22:32:24,051 : INFO : Quadruplets with out-of-vocabulary words: 21.1%
2020-09-22 22:32:24,051 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-22 22:32:24,051 : INFO : Total accuracy: 11.7% (1807/15421)
Doc2Vec("ech07,mal0001*70",dm/c,d15,n72,w3,mc99,s5e-05,t6): 11.72% correct (1807 of 15421)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-22 22:32:24,322 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5333
2020-09-22 22:32:24,322 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5117
2020-09-22 22:32:24,322 : INFO : Pairs with unknown words ratio: 0.6%
((0.5332699915202915, 3.488429953525166e-27), SpearmanrResult(correlation=0.5116792132000204, pvalue=8.176430431320424e-25), 0.56657223796034)


02 - simlex999
2020-09-22 22:32:24,371 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3115
2020-09-22 22:32:24,371 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2746
2020-09-22 22:32:24,371 : INFO : Pairs with unknown words ratio: 0.3%
((0.31148500606352364, 7.534748133506488e-24), SpearmanrResult(correlation=0.274551647117372, pvalue=1.1050885088962558e-18), 0.3003003003003003)


03 - simverb3500
2020-09-22 22:32:24,649 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1801
2020-09-22 22:32:24,649 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1654
2020-09-22 22:32:24,649 : INFO : Pairs with unknown words ratio: 1.4%
((0.180095676018028, 1.4876587019966436e-26), SpearmanrResult(correlation=0.16544259369795283, pvalue=1.3144422625306574e-22), 1.3714285714285714)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
