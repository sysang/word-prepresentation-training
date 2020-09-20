import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=30,
        window=3,
        min_count=75,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=10,
        min_alpha=0.001,
        alpha=0.001*5*10,
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
2020-09-19 12:51:51,493 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-19 12:51:51,494 : INFO : Loading a fresh vocabulary
2020-09-19 12:51:51,968 : INFO : effective_min_count=75 retains 70715 unique words (3% of original 1784839, drops 1714124)
2020-09-19 12:51:51,968 : INFO : effective_min_count=75 leaves 329482258 word corpus (98% of original 336075146, drops 6592888)
2020-09-19 12:51:52,130 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-19 12:51:52,166 : INFO : sample=5e-05 downsamples 730 most-common words
2020-09-19 12:51:52,166 : INFO : downsampling leaves estimated 148046269 word corpus (44.9% of prior 329482258)
2020-09-19 12:51:52,304 : INFO : estimated required memory for 70715 words and 15 dimensions: 866700700 bytes

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10)
Save model to: models/dmc_d15_n30_w3_mc75_s00005_ech10_mal001x5_thefinal.bin
2020-09-19 22:46:29,602 : INFO : saving Doc2Vec object under models/dmc_d15_n30_w3_mc75_s00005_ech10_mal001x5_thefinal.bin, separately None
2020-09-19 22:46:29,602 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n30_w3_mc75_s00005_ech10_mal001x5_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-19 22:46:29,630 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n30_w3_mc75_s00005_ech10_mal001x5_thefinal.bin.docvecs.vectors_docs.npy
2020-09-19 22:46:30,228 : INFO : saved models/dmc_d15_n30_w3_mc75_s00005_ech10_mal001x5_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 5610790
[+] index 5610790 -> "paris in his pharmacologia 221 “to find a word which is used to express general characters subsequently become the name of a specific substance in which such characters are predominant and we shall find that some important anomalies in nomenclature may be thus explained"
2020-09-19 22:46:30,239 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 100 similarities.


.....get random document, tag: 5711572
[+] index 5711572 -> "i am starting to get upset just remembering what a tragedy it was"
    No any match in top 100 similarities.


.....get random document, tag: 9078095
[+] index 9078095 -> "like napier he laments the dearth of physical evidence but bourne does not dismiss sasquatch or yeti as impossible"
[*] Matched with rank 1, score: 0.9503947496414185!


.....get random document, tag: 4897029
[+] index 4897029 -> "before i had decided somebody knocked at the door"
[*] Matched with rank 1, score: 0.9353540539741516!


.....get random document, tag: 6456876
[+] index 6456876 -> "i am sorry when a punk documentary includes these bands you know its complete bullshit"
[*] Matched with rank 20, score: 0.8887341022491455!


.....get random document, tag: 6261195
[+] index 6261195 -> "in a bombed-out vienna just after wwii novelist holly martins joseph cotten arrives from america to renew a friendship with his childhood buddy harry lime orson welles"
[*] Matched with rank 4, score: 0.9062916040420532!


.....get random document, tag: 6772452
[+] index 6772452 -> "doug kelly now a former team member joined the team shortly afterwards"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (9757540): the average household size is 2 65 and the average family size is 3 07

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):

MOST (10309294, 0.9731310606002808): «the average household size is 2 65 and the average family size is 3 18»

MEDIAN (5064191, 0.0001499652862548828): «it would only have said in a manner which you yourself could not possibly have mistaken that i had reason to know you were in debt and that it was in my experience and in my mother 's experience of you that you were not very discreet or very scrupulous about how you got money when you wanted it»

LEAST (9638339, -0.9425886273384094): «for every 100 females age 18 and over there are 92 8 males»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'arranged' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
2020-09-19 22:46:54,427 : INFO : precomputing L2-norms of word weight vectors
     1. 0.95 'linked'
     2. 0.95 'employed'
     3. 0.93 'gathered'
     4. 0.93 'examined'
     5. 0.93 'supplemented'
     6. 0.93 'handled'
     7. 0.93 'monitored'


[+] target_word: 'bates' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.98 'davies'
     2. 0.98 'morton'
     3. 0.98 'donaldson'
     4. 0.98 'butler'
     5. 0.98 'parker'
     6. 0.98 'carr'
     7. 0.98 'lockwood'


[+] target_word: 'maybe' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.96 'guess'
     2. 0.95 'b/c'
     3. 0.95 'eventhough'
     4. 0.95 'if'
     5. 0.95 'becuase'
     6. 0.95 'ok'
     7. 0.95 'i'


[+] target_word: 'avenge' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.94 'disinherit'
     2. 0.93 'supplicate'
     3. 0.93 'surrender'
     4. 0.93 'depose'
     5. 0.92 'excommunicate'
     6. 0.92 'dethrone'
     7. 0.92 'vanquish'


[+] target_word: 'run' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.95 'drive'
     2. 0.95 'fly'
     3. 0.94 'go'
     4. 0.94 'pass'
     5. 0.93 'move'
     6. 0.91 'come'
     7. 0.90 'jump'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-19 22:46:55,054 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-19 22:46:55,383 : INFO : capital-common-countries: 6.7% (34/506)
2020-09-19 22:46:56,685 : INFO : capital-world: 4.0% (77/1929)
2020-09-19 22:46:56,853 : INFO : currency: 1.7% (4/236)
2020-09-19 22:46:58,388 : INFO : city-in-state: 1.8% (42/2330)
2020-09-19 22:46:58,721 : INFO : family: 36.0% (151/420)
2020-09-19 22:46:59,336 : INFO : gram1-adjective-to-adverb: 3.5% (35/992)
2020-09-19 22:46:59,865 : INFO : gram2-opposite: 3.0% (21/702)
2020-09-19 22:47:00,664 : INFO : gram3-comparative: 24.1% (321/1332)
2020-09-19 22:47:01,431 : INFO : gram4-superlative: 7.1% (75/1056)
2020-09-19 22:47:02,141 : INFO : gram5-present-participle: 13.1% (138/1056)
2020-09-19 22:47:03,160 : INFO : gram6-nationality-adjective: 8.8% (121/1371)
2020-09-19 22:47:04,284 : INFO : gram7-past-tense: 20.3% (317/1560)
2020-09-19 22:47:05,172 : INFO : gram8-plural: 9.5% (127/1332)
2020-09-19 22:47:05,853 : INFO : gram9-plural-verbs: 8.5% (74/870)
2020-09-19 22:47:05,853 : INFO : Quadruplets with out-of-vocabulary words: 19.7%
2020-09-19 22:47:05,853 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-19 22:47:05,853 : INFO : Total accuracy: 9.8% (1537/15692)
Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10): 9.79% correct (1537 of 15692)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-19 22:47:06,133 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4888
2020-09-19 22:47:06,133 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4782
2020-09-19 22:47:06,133 : INFO : Pairs with unknown words ratio: 0.6%
((0.48879624513792996, 1.7645945848900724e-22), SpearmanrResult(correlation=0.4781506458619819, pvalue=1.8798086010044882e-21), 0.56657223796034)


02 - simlex999
2020-09-19 22:47:06,190 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2842
2020-09-19 22:47:06,190 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2464
2020-09-19 22:47:06,190 : INFO : Pairs with unknown words ratio: 0.3%
((0.28417880094619175, 5.881020946356702e-20), SpearmanrResult(correlation=0.24641060227745326, pvalue=3.051726588460587e-15), 0.3003003003003003)


03 - simverb3500
2020-09-19 22:47:06,475 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1713
2020-09-19 22:47:06,475 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1578
2020-09-19 22:47:06,475 : INFO : Pairs with unknown words ratio: 0.7%
((0.17131973264938263, 2.717671175096123e-24), SpearmanrResult(correlation=0.15783540832590576, pvalue=8.103950539182815e-21), 0.7428571428571429)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
