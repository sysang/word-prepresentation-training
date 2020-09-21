import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=50,
        window=3,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=0,
        hs=0,
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*20*5,
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
2020-09-20 21:19:39,951 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-20 21:19:39,951 : INFO : Loading a fresh vocabulary
2020-09-20 21:19:40,421 : INFO : effective_min_count=99 retains 61077 unique words (3% of original 1784839, drops 1723762)
2020-09-20 21:19:40,421 : INFO : effective_min_count=99 leaves 328657804 word corpus (97% of original 336075146, drops 7417342)
2020-09-20 21:19:40,562 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-20 21:19:40,597 : INFO : sample=5e-05 downsamples 733 most-common words
2020-09-20 21:19:40,597 : INFO : downsampling leaves estimated 147142569 word corpus (44.8% of prior 328657804)
2020-09-20 21:19:40,714 : INFO : estimated required memory for 61077 words and 15 dimensions: 835267740 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/m,d15,n50,w3,mc99,s5e-05,t10)
Save model to: models/dmm_d15_n50_w3_mc99_s00005_ech05_mal0002x20_thefinal.bin
2020-09-21 11:21:16,027 : INFO : saving Doc2Vec object under models/dmm_d15_n50_w3_mc99_s00005_ech05_mal0002x20_thefinal.bin, separately None
2020-09-21 11:21:16,028 : INFO : storing np array 'vectors_docs_lockf' to models/dmm_d15_n50_w3_mc99_s00005_ech05_mal0002x20_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-21 11:21:16,053 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n50_w3_mc99_s00005_ech05_mal0002x20_thefinal.bin.docvecs.vectors_docs.npy
2020-09-21 11:21:16,460 : INFO : saved models/dmm_d15_n50_w3_mc99_s00005_ech05_mal0002x20_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 6288920
[+] index 6288920 -> "in effect the passage of time and the seasons serve to illustrate the townspeople maturing and adapting to life as the world and its ideals evolve"
2020-09-21 11:21:16,472 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 100 similarities.


.....get random document, tag: 6683169
[+] index 6683169 -> "this image is from the national oceanic and atmospheric administration noaa"
[*] Matched with rank 35, score: 0.9703636169433594!


.....get random document, tag: 12791876
[+] index 12791876 -> "it did not take long unfortunately to realize that it was just a dream"
    No any match in top 100 similarities.


.....get random document, tag: 12372369
[+] index 12372369 -> "new bishop of scranton says he is banned from active ministry"
    No any match in top 100 similarities.


.....get random document, tag: 2778080
[+] index 2778080 -> "as they were sitting together in lady grant 's bedroom cecilia 's ears were suddenly wounded by the mention of the name of sir francis geraldine"
    No any match in top 100 similarities.


.....get random document, tag: 4119251
[+] index 4119251 -> "he includes amental suggestion taking place even at a distance ' a man can transmit an almost compulsive command it appears nowadays by a simple tension of his will if this be so if will can affect matter from a distance obviously the relations of will and matter are not what popular science tells us that they are"
    No any match in top 100 similarities.


.....get random document, tag: 12088920
[+] index 12088920 -> "k you are a human being are not you so i am saying all human beings suffer whether they live in russia america china india pakistan wherever all human beings suffer"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (7555902): this timeline of the big bang describes the events that have occurred and will occur according to the scientific theory of the big bang

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/m,d15,n50,w3,mc99,s5e-05,t10):

MOST (7670735, 0.9762378931045532): «this scenario allows the big bang to have been immediately preceded by the big crunch of a preceding universe»

MEDIAN (12921945, 0.804361879825592): «however they managed to keep things somewhat sane at least until the supreme court stopped the florida recount back in 2000»

LEAST (10301516, -0.9446969032287598): «the per capita income for the city is $16 660»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'flat' model: Doc2Vec(dm/m,d15,n50,w3,mc99,s5e-05,t10):
2020-09-21 11:21:41,825 : INFO : precomputing L2-norms of word weight vectors
     1. 0.92 'chalk'
     2. 0.92 'patch'
     3. 0.89 'edge'
     4. 0.89 'bottom'
     5. 0.88 'gravel'
     6. 0.87 'edges'
     7. 0.87 'underneath'


[+] target_word: 'deny' model: Doc2Vec(dm/m,d15,n50,w3,mc99,s5e-05,t10):
    1. 0.96 'deem'
     2. 0.94 'concede'
     3. 0.94 'prove'
     4. 0.94 'err'
     5. 0.94 'reject'
     6. 0.93 'acknowledge'
     7. 0.93 'assert'


[+] target_word: 'discussion' model: Doc2Vec(dm/m,d15,n50,w3,mc99,s5e-05,t10):
     1. 0.96 'topic'
     2. 0.95 'discussions'
     3. 0.91 'discourse'
     4. 0.91 'debate'
     5. 0.91 'details'
     6. 0.90 'inquiry'
     7. 0.90 'enquiries'


[+] target_word: 'imagined' model: Doc2Vec(dm/m,d15,n50,w3,mc99,s5e-05,t10):
     1. 0.91 'aware'
     2. 0.91 'fancied'
     3. 0.89 'doubtful'
     4. 0.88 'mattered'
     5. 0.88 'imagining'
     6. 0.88 'wondered'
     7. 0.87 'realized'


[+] target_word: 'remorse' model: Doc2Vec(dm/m,d15,n50,w3,mc99,s5e-05,t10):
     1. 0.95 'anguish'
     2. 0.95 'grief'
     3. 0.95 'pang'
     4. 0.95 'pangs'
     5. 0.94 'self-reproach'
     6. 0.94 'bitterness'
     7. 0.93 'agony'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-21 11:21:42,380 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-21 11:21:42,728 : INFO : capital-common-countries: 12.8% (65/506)
2020-09-21 11:21:44,050 : INFO : capital-world: 7.1% (127/1779)
2020-09-21 11:21:44,174 : INFO : currency: 1.1% (2/178)
2020-09-21 11:21:45,918 : INFO : city-in-state: 3.2% (72/2267)
2020-09-21 11:21:46,232 : INFO : family: 44.3% (186/420)
2020-09-21 11:21:47,099 : INFO : gram1-adjective-to-adverb: 5.6% (56/992)
2020-09-21 11:21:47,849 : INFO : gram2-opposite: 5.0% (35/702)
2020-09-21 11:21:49,025 : INFO : gram3-comparative: 30.6% (407/1332)
2020-09-21 11:21:50,275 : INFO : gram4-superlative: 13.2% (139/1056)
2020-09-21 11:21:51,115 : INFO : gram5-present-participle: 18.9% (200/1056)
2020-09-21 11:21:52,112 : INFO : gram6-nationality-adjective: 16.3% (223/1371)
2020-09-21 11:21:53,462 : INFO : gram7-past-tense: 42.4% (661/1560)
2020-09-21 11:21:54,731 : INFO : gram8-plural: 25.0% (333/1332)
2020-09-21 11:21:55,637 : INFO : gram9-plural-verbs: 12.4% (108/870)
2020-09-21 11:21:55,638 : INFO : Quadruplets with out-of-vocabulary words: 21.1%
2020-09-21 11:21:55,638 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-21 11:21:55,638 : INFO : Total accuracy: 17.0% (2614/15421)
Doc2Vec(dm/m,d15,n50,w3,mc99,s5e-05,t10): 16.95% correct (2614 of 15421)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-21 11:21:55,909 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5622
2020-09-21 11:21:55,909 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5590
2020-09-21 11:21:55,909 : INFO : Pairs with unknown words ratio: 0.6%
((0.5621928091079844, 1.225325274585301e-30), SpearmanrResult(correlation=0.5590290545708649, pvalue=3.038794327714104e-30), 0.56657223796034)


02 - simlex999
2020-09-21 11:21:55,958 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3460
2020-09-21 11:21:55,958 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2960
2020-09-21 11:21:55,958 : INFO : Pairs with unknown words ratio: 0.3%
((0.34600262617721134, 2.1777054442100586e-29), SpearmanrResult(correlation=0.2959862932777114, pvalue=1.3729496434033802e-21), 0.3003003003003003)


03 - simverb3500
2020-09-21 11:21:56,238 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1944
2020-09-21 11:21:56,238 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1767
2020-09-21 11:21:56,238 : INFO : Pairs with unknown words ratio: 1.4%
((0.1944063787328045, 9.52076136354036e-31), SpearmanrResult(correlation=0.17668479694249442, pvalue=1.3252810369216644e-25), 1.3714285714285714)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
 
"""
