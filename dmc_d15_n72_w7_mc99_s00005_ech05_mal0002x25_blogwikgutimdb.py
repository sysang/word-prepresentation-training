import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=72,
        window=7,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*25*5,
        comment='ech05,mal0002x25,blogwikgutimdb',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(
                common_kwargs=common_kwargs,
                saved_fname=saved_fname,
                evaluate=True,
                database="blogwikgutimdb"
            )

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


INFO: Training parameters: {'vector_size': 15, 'negative': 72, 'window': 7, 'min_count': 99, 'sample': 5e-05, 'dm': 1, 'dm_concat': 1, 'hs': 0, 'epochs': 5, 'min_alpha': 0.0002, 'alpha': 0.025, 'comment': 'ech05,mal0002x25,blogwikgutimdb'}
INFO: Model details: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n72,w7,mc99,s5e-05,t6)
INFO: Save model to: models/dmc_d15_n72_w7_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin
2020-10-01 18:40:35,744 : INFO : saving Doc2Vec object under models/dmc_d15_n72_w7_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin, separately None
2020-10-01 18:40:35,744 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n72_w7_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin.docvecs.vectors_docs.npy
2020-10-01 18:40:36,273 : INFO : saved models/dmc_d15_n72_w7_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 4276393
-> index 4276393 --> "it is now before the supreme court to decide"
2020-10-01 18:40:37,708 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 5279522
-> index 5279522 --> "the average household size is 3 24 and the average family size is 4 04"
    No any match in top 200 similarities.


.....get random document, tag: 2698315
-> index 2698315 --> "there are no cows here to give milk or any mice or even grasshoppers"
    No any match in top 200 similarities.


.....get random document, tag: 1967947
-> index 1967947 --> "some of them burst in the action killing their people"
    No any match in top 200 similarities.


.....get random document, tag: 2352901
-> index 2352901 --> "the two men said hardly a word when they met but stood there for a moment grasping each other 's hands"
    No any match in top 200 similarities.


.....get random document, tag: 6759048
-> index 6759048 --> "40 000 won roughly 40 cdn worth of spam"
    No any match in top 200 similarities.


.....get random document, tag: 3000733
-> index 3000733 --> "he had all the qualities for major stardom but sadly it was not to be"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (287113): but their answer to my question is none the less wrong

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n72,w7,mc99,s5e-05,t6):

MOST (7382586, 0.908674418926239): «i have told him to call a dentist but he will not do it»

MEDIAN (4346280, 0.0008781366050243378): «there is also a prequel novella new spring in the legends anthology edited by robert silverberg»

LEAST (2771974, -0.9408191442489624): «chatterton presently in the bustling plaza and the elder lady turned aside from her english companions after a glance at her niece»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'row' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n72,w7,mc99,s5e-05,t6):
2020-10-01 18:41:04,072 : INFO : precomputing L2-norms of word weight vectors
     1. 0.88 'skid'
     2. 0.88 'round'
     3. 0.87 'inning'
     4. 0.86 'marlboro'
     5. 0.86 'notch'
     6. 0.84 'floor'
     7. 0.84 'deck'


[+] target_word: 'specifically' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n72,w7,mc99,s5e-05,t6):
     1. 0.89 'informally'
     2. 0.85 'rightly'
     3. 0.84 'incorrectly'
     4. 0.83 'simply'
     5. 0.83 'collectively'
     6. 0.83 'wrongly'
     7. 0.83 'experts'


[+] target_word: 'ideal' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n72,w7,mc99,s5e-05,t6):
     1. 0.96 'aesthetic'
     2. 0.95 'intellectual'
     3. 0.95 'symbolic'
     4. 0.92 'moral'
     5. 0.92 'artistic'
     6. 0.91 'collective'
     7. 0.91 'physical'


[+] target_word: 'parliament' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n72,w7,mc99,s5e-05,t6):
     1. 0.95 'senate'
     2. 0.95 'duma'
     3. 0.94 'council'
     4. 0.94 'riksdag'
     5. 0.94 'governors'
     6. 0.93 'legislature'
     7. 0.92 'parliaments'


[+] target_word: 'issued' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n72,w7,mc99,s5e-05,t6):
     1. 0.95 'signed'
     2. 0.93 'obtained'
     3. 0.92 'received'
     4. 0.92 'offered'
     5. 0.91 'delivered'
     6. 0.91 'procured'
     7. 0.91 'filed'


[+] target_word: 'eventually' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n72,w7,mc99,s5e-05,t6):
     1. 0.91 'successfully'
     2. 0.90 'speedily'
     3. 0.89 'inadvertently'
     4. 0.88 'finally'
     5. 0.87 'never'
     6. 0.87 'accidentally'
     7. 0.85 'allegedly'


[+] target_word: 'mountain' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n72,w7,mc99,s5e-05,t6):
     1. 0.92 'upland'
     2. 0.91 'turf'
     3. 0.90 'glacier'
     4. 0.90 'rivulet'
     5. 0.90 'cliffs'
     6. 0.90 'oceanic'
     7. 0.90 'waterfall'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-10-01 18:41:04,297 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-10-01 18:41:04,474 : INFO : capital-common-countries: 13.6% (63/462)
2020-10-01 18:41:04,814 : INFO : capital-world: 7.5% (65/862)
2020-10-01 18:41:04,871 : INFO : currency: 0.0% (0/128)
2020-10-01 18:41:05,657 : INFO : city-in-state: 4.0% (81/2009)
2020-10-01 18:41:05,830 : INFO : family: 37.9% (144/380)
2020-10-01 18:41:06,255 : INFO : gram1-adjective-to-adverb: 2.7% (27/992)
2020-10-01 18:41:06,556 : INFO : gram2-opposite: 4.5% (29/650)
2020-10-01 18:41:07,098 : INFO : gram3-comparative: 33.0% (439/1332)
2020-10-01 18:41:07,537 : INFO : gram4-superlative: 12.4% (131/1056)
2020-10-01 18:41:07,971 : INFO : gram5-present-participle: 28.7% (285/992)
2020-10-01 18:41:08,561 : INFO : gram6-nationality-adjective: 12.4% (161/1299)
2020-10-01 18:41:09,238 : INFO : gram7-past-tense: 26.0% (405/1560)
2020-10-01 18:41:09,792 : INFO : gram8-plural: 16.8% (200/1190)
2020-10-01 18:41:10,150 : INFO : gram9-plural-verbs: 12.4% (101/812)
2020-10-01 18:41:10,151 : INFO : Quadruplets with out-of-vocabulary words: 29.8%
2020-10-01 18:41:10,151 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-10-01 18:41:10,151 : INFO : Total accuracy: 15.5% (2131/13724)
Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n72,w7,mc99,s5e-05,t6): 15.53% correct (2131 of 13724)


[+] questions-words-narrowed.txt
2020-10-01 18:41:10,311 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-10-01 18:41:10,487 : INFO : family: 37.9% (144/380)
2020-10-01 18:41:10,912 : INFO : gram1-adjective-to-adverb: 2.7% (27/992)
2020-10-01 18:41:11,213 : INFO : gram2-opposite: 4.5% (29/650)
2020-10-01 18:41:11,756 : INFO : gram3-comparative: 33.0% (439/1332)
2020-10-01 18:41:12,198 : INFO : gram4-superlative: 12.4% (131/1056)
2020-10-01 18:41:12,633 : INFO : gram5-present-participle: 28.7% (285/992)
2020-10-01 18:41:13,223 : INFO : gram6-nationality-adjective: 12.4% (161/1299)
2020-10-01 18:41:13,903 : INFO : gram7-past-tense: 26.0% (405/1560)
2020-10-01 18:41:14,447 : INFO : gram8-plural: 16.8% (200/1190)
2020-10-01 18:41:14,804 : INFO : gram9-plural-verbs: 12.4% (101/812)
2020-10-01 18:41:14,804 : INFO : Quadruplets with out-of-vocabulary words: 8.2%
2020-10-01 18:41:14,804 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-10-01 18:41:14,805 : INFO : Total accuracy: 18.7% (1922/10263)
Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n72,w7,mc99,s5e-05,t6): 18.73% correct (1922 of 10263)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-10-01 18:41:14,837 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5677
2020-10-01 18:41:14,837 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5648
2020-10-01 18:41:14,838 : INFO : Pairs with unknown words ratio: 2.5%
((0.5677054876855584, 9.692352906813545e-31), SpearmanrResult(correlation=0.5647987821164916, pvalue=2.230857287043205e-30), 2.5495750708215295)


02 - simlex999
2020-10-01 18:41:15,004 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3491
2020-10-01 18:41:15,004 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.3083
2020-10-01 18:41:15,004 : INFO : Pairs with unknown words ratio: 0.5%
((0.34909696567505033, 7.295052501882898e-30), SpearmanrResult(correlation=0.3083301629461438, pvalue=2.4667520388769572e-23), 0.5005005005005005)


03 - simverb3500
2020-10-01 18:41:15,052 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1855
2020-10-01 18:41:15,052 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1697
2020-10-01 18:41:15,052 : INFO : Pairs with unknown words ratio: 6.0%
((0.1855447424336539, 7.343011839391223e-27), SpearmanrResult(correlation=0.16972001216549887, pvalue=1.1159575223615485e-22), 6.0285714285714285)


-----------------------------------------------------
Benchmark similarity score with respect to theme word
-----------------------------------------------------




_____  COMPLETED  _________________________________
###~~~~~~~~#~~~~~~~#~~~~~~~#~~~~~~~~~~#~~~~~~~~~###
"""
