import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=67,
        window=5,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=20,
        min_alpha=0.0002,
        alpha=0.0002*8*20,
        comment='ech20,mal0002x08,blogwikgutimdb',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(
            common_kwargs=common_kwargs,
            saved_fname=saved_fname,
            evaluate=False,
            database='blogwikgutimdb')

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech20,mal0002x08,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6)
Save model to: models/dmc_d15_n67_w5_mc99_s00005_ech20_mal0002x8_blogwikgutimdb.bin
2020-09-29 15:46:17,561 : INFO : saving Doc2Vec object under models/dmc_d15_n67_w5_mc99_s00005_ech20_mal0002x8_blogwikgutimdb.bin, separately None
2020-09-29 15:46:17,561 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n67_w5_mc99_s00005_ech20_mal0002x8_blogwikgutimdb.bin.docvecs.vectors_docs.npy
2020-09-29 15:46:18,009 : INFO : saved models/dmc_d15_n67_w5_mc99_s00005_ech20_mal0002x8_blogwikgutimdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 2154981
[+] index 2154981 -> "the happiest life for her would be one that never forced her to use it i do not know as i understand you exactly said mrs"
2020-09-29 15:46:18,749 : INFO : precomputing L2-norms of doc weight vectors
[*] Matched with rank 1, score: 0.9462931752204895!


.....get random document, tag: 2787671
[+] index 2787671 -> "our hero was one of the first to leap into her and he pulled the bow oar"
[*] Matched with rank 1, score: 0.9582661390304565!


.....get random document, tag: 210438
[+] index 210438 -> "a very old friend my lord the clergyman of his parish and for many years an intimate friend of his father"
[*] Matched with rank 4, score: 0.8984631896018982!


.....get random document, tag: 7107155
[+] index 7107155 -> "bastards says pobble turning to look towards the entrance to cowpunchers"
[*] Matched with rank 5, score: 0.902582585811615!


.....get random document, tag: 2195277
[+] index 2195277 -> "i never committed murder sir said he in an improved tone"
    No any match in top 200 similarities.


.....get random document, tag: 2460320
[+] index 2460320 -> "nothing could be more rigorously simple than the furniture of the parlor"
    No any match in top 200 similarities.


.....get random document, tag: 40143
[+] index 40143 -> "as she did so it seemed to her that something knocked against her door from without"
[*] Matched with rank 3, score: 0.9229564666748047!




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (5063846): the island is mountainous and japan 's largest active volcano aso at 1 592 m is on kyushu

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech20,mal0002x08,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):

MOST (3263768, 0.9453368782997131): «milius did his research well for the most part»

MEDIAN (6617578, 1.6063451766967773e-05): «one was having a birthday so everyone went out on saturday night to celebrate by getting trashed»

LEAST (22203, -0.9334546327590942): «he had a very friendly feeling toward both the girls»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'fascinating' model: Doc2Vec("ech20,mal0002x08,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
2020-09-29 15:46:42,190 : INFO : precomputing L2-norms of word weight vectors
     1. 0.93 'intriguing'
     2. 0.92 'bizarre'
     3. 0.92 'remarkable'
     4. 0.92 'appealing'
     5. 0.91 'comprehensible'
     6. 0.91 'uplifting'
     7. 0.91 'interesting'


[+] target_word: 'help' model: Doc2Vec("ech20,mal0002x08,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.90 'call'
     2. 0.90 'seek'
     3. 0.90 'cooperate'
     4. 0.90 'humiliate'
     5. 0.88 'acquit'
     6. 0.88 'shirk'
     7. 0.88 'withhold'


[+] target_word: 'assigned' model: Doc2Vec("ech20,mal0002x08,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.94 'secured'
     2. 0.93 'procured'
     3. 0.92 'accommodated'
     4. 0.92 'designated'
     5. 0.92 'funded'
     6. 0.92 'relinquished'
     7. 0.92 'held'


[+] target_word: 'ride' model: Doc2Vec("ech20,mal0002x08,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.90 'cab'
     2. 0.87 'hurry'
     3. 0.85 'lookout'
     4. 0.84 'trot'
     5. 0.83 'fast'
     6. 0.82 'sleigh'
     7. 0.82 'elevator'


[+] target_word: '2004' model: Doc2Vec("ech20,mal0002x08,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.99 '1998'
     2. 0.98 '1999'
     3. 0.97 '1997'
     4. 0.97 '2001'
     5. 0.97 '1994'
     6. 0.96 '1995'
     7. 0.96 '1996'


[+] target_word: 'signal' model: Doc2Vec("ech20,mal0002x08,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.92 'photon'
     2. 0.91 'ignition'
     3. 0.91 'doppler'
     4. 0.90 'velocity'
     5. 0.90 'voltage'
     6. 0.89 'synchronization'
     7. 0.89 'acceleration'


[+] target_word: 'spencer' model: Doc2Vec("ech20,mal0002x08,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.96 'sampson'
     2. 0.96 'gardiner'
     3. 0.96 'morley'
     4. 0.95 'searle'
     5. 0.95 'orme'
     6. 0.95 'silvester'
     7. 0.95 'boyle'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-29 15:46:42,552 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-29 15:46:42,704 : INFO : capital-common-countries: 11.3% (52/462)
2020-09-29 15:46:43,021 : INFO : capital-world: 7.8% (67/862)
2020-09-29 15:46:43,076 : INFO : currency: 0.0% (0/128)
2020-09-29 15:46:43,858 : INFO : city-in-state: 2.8% (56/2009)
2020-09-29 15:46:44,015 : INFO : family: 11.3% (43/380)
2020-09-29 15:46:44,404 : INFO : gram1-adjective-to-adverb: 1.0% (10/992)
2020-09-29 15:46:44,690 : INFO : gram2-opposite: 1.2% (8/650)
2020-09-29 15:46:45,211 : INFO : gram3-comparative: 10.4% (139/1332)
2020-09-29 15:46:45,671 : INFO : gram4-superlative: 3.6% (38/1056)
2020-09-29 15:46:46,084 : INFO : gram5-present-participle: 6.9% (68/992)
2020-09-29 15:46:46,681 : INFO : gram6-nationality-adjective: 8.7% (113/1299)
2020-09-29 15:46:47,274 : INFO : gram7-past-tense: 8.2% (128/1560)
2020-09-29 15:46:47,779 : INFO : gram8-plural: 5.5% (66/1190)
2020-09-29 15:46:48,101 : INFO : gram9-plural-verbs: 4.3% (35/812)
2020-09-29 15:46:48,101 : INFO : Quadruplets with out-of-vocabulary words: 29.8%
2020-09-29 15:46:48,102 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 15:46:48,102 : INFO : Total accuracy: 6.0% (823/13724)
Doc2Vec("ech20,mal0002x08,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6): 6.00% correct (823 of 13724)


[+] questions-words-narrowed.txt
2020-09-29 15:46:48,125 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-29 15:46:48,282 : INFO : family: 11.3% (43/380)
2020-09-29 15:46:48,674 : INFO : gram1-adjective-to-adverb: 1.0% (10/992)
2020-09-29 15:46:48,961 : INFO : gram2-opposite: 1.2% (8/650)
2020-09-29 15:46:49,485 : INFO : gram3-comparative: 10.4% (139/1332)
2020-09-29 15:46:49,945 : INFO : gram4-superlative: 3.6% (38/1056)
2020-09-29 15:46:50,359 : INFO : gram5-present-participle: 6.9% (68/992)
2020-09-29 15:46:50,956 : INFO : gram6-nationality-adjective: 8.7% (113/1299)
2020-09-29 15:46:51,549 : INFO : gram7-past-tense: 8.2% (128/1560)
2020-09-29 15:46:52,055 : INFO : gram8-plural: 5.5% (66/1190)
2020-09-29 15:46:52,377 : INFO : gram9-plural-verbs: 4.3% (35/812)
2020-09-29 15:46:52,377 : INFO : Quadruplets with out-of-vocabulary words: 8.2%
2020-09-29 15:46:52,377 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 15:46:52,378 : INFO : Total accuracy: 6.3% (648/10263)
Doc2Vec("ech20,mal0002x08,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6): 6.31% correct (648 of 10263)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-29 15:46:52,408 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5252
2020-09-29 15:46:52,409 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5094
2020-09-29 15:46:52,409 : INFO : Pairs with unknown words ratio: 2.5%
((0.5252289745838902, 8.711638407734137e-26), SpearmanrResult(correlation=0.5093720961336939, pvalue=4.138533303358647e-24), 2.5495750708215295)


02 - simlex999
2020-09-29 15:46:52,563 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2882
2020-09-29 15:46:52,563 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2698
2020-09-29 15:46:52,563 : INFO : Pairs with unknown words ratio: 0.5%
((0.2882482671226787, 1.794117427435329e-20), SpearmanrResult(correlation=0.2697839909135474, pvalue=4.886907191784132e-18), 0.5005005005005005)


03 - simverb3500
2020-09-29 15:46:52,610 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1640
2020-09-29 15:46:52,611 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1532
2020-09-29 15:46:52,611 : INFO : Pairs with unknown words ratio: 6.0%
((0.16395331977240452, 2.9860740976835652e-21), SpearmanrResult(correlation=0.153201343734641, pvalue=1.0016243235885302e-18), 6.0285714285714285)


     ____________     COMPLETED      ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
