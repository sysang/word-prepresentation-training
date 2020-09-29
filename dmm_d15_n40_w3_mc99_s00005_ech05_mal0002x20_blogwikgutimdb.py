import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=40,
        window=3,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=0,
        hs=0,
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*20*5,
        comment='ech05,mal0002x20,blogwikgutimdb',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(
            common_kwargs=common_kwargs,
            saved_fname=saved_fname,
            evaluate=False,
            database='blogwikgutimdb')

"""
2020-09-29 08:52:48,011 : INFO : collected 605528 word types and 7410000 unique tags from a corpus of 7410000 examples and 121440062 words
2020-09-29 08:52:48,011 : INFO : Loading a fresh vocabulary
2020-09-29 08:52:48,177 : INFO : effective_min_count=99 retains 34983 unique words (5% of original 605528, drops 570545)
2020-09-29 08:52:48,177 : INFO : effective_min_count=99 leaves 118011182 word corpus (97% of original 121440062, drops 3428880)
2020-09-29 08:52:48,255 : INFO : deleting the raw counts dictionary of 605528 items
2020-09-29 08:52:48,267 : INFO : sample=5e-05 downsamples 737 most-common words
2020-09-29 08:52:48,267 : INFO : downsampling leaves estimated 51370242 word corpus (43.5% of prior 118011182)
2020-09-29 08:52:48,317 : INFO : estimated required memory for 34983 words and 15 dimensions: 466289460 bytes
2020-09-29 08:52:48,317 : INFO : resetting layer weights
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/m,d15,n40,w3,mc99,s5e-05,t6)
Save model to: models/dmm_d15_n40_w3_mc99_s00005_ech05_mal0002x20_blogwikgutimdb.bin
2020-09-29 09:53:02,636 : INFO : saving Doc2Vec object under models/dmm_d15_n40_w3_mc99_s00005_ech05_mal0002x20_blogwikgutimdb.bin, separately None
2020-09-29 09:53:02,636 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n40_w3_mc99_s00005_ech05_mal0002x20_blogwikgutimdb.bin.docvecs.vectors_docs.npy
2020-09-29 09:53:02,946 : INFO : saved models/dmm_d15_n40_w3_mc99_s00005_ech05_mal0002x20_blogwikgutimdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 6287970
[+] index 6287970 -> "but poor him to put on hold quite a number of job interviews"
2020-09-29 09:53:05,053 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 1826374
[+] index 1826374 -> "but yet among them all they did not quite see how they were to confute the senator 's logic"
    No any match in top 200 similarities.


.....get random document, tag: 6033366
[+] index 6033366 -> "maybe it 's just another one of those days"
    No any match in top 200 similarities.


.....get random document, tag: 553157
[+] index 553157 -> "in the constant wars with which italy was plagued by the dissensions of her petty states and republics there was a demand for native hardihood"
    No any match in top 200 similarities.


.....get random document, tag: 3412560
[+] index 3412560 -> "my friends and i viewed this a week ago with breathless anticipation"
    No any match in top 200 similarities.


.....get random document, tag: 6402368
[+] index 6402368 -> "i can not see a direction to go in that i want to travel"
    No any match in top 200 similarities.


.....get random document, tag: 1186270
[+] index 1186270 -> "i want some money so soon do not try to crawfish it was agreed you should give me a check whenever i asked for it"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (3115128): as it is in heaven seems to fit the bill

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/m,d15,n40,w3,mc99,s5e-05,t6):

MOST (3237684, 0.9945160746574402): «the greatest asset that kal ho na ho has is its cast»

MEDIAN (7050389, 0.8436815738677979): «some boys on the street were playing monkey in the middle»

LEAST (5255916, -0.9626820087432861): «according to the united states census bureau the cdp has a total area of 10 2 km² 3 9 mi²»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'faded' model: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/m,d15,n40,w3,mc99,s5e-05,t6):
2020-09-29 09:53:31,783 : INFO : precomputing L2-norms of word weight vectors
     1. 0.92 'darkened'
     2. 0.89 'dazzled'
     3. 0.89 'fading'
     4. 0.89 'glowing'
     5. 0.88 'glowed'
     6. 0.88 'sombre'
     7. 0.88 'twinkled'


[+] target_word: 'preferred' model: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.91 'concerned'
     2. 0.90 'share'
     3. 0.90 'prefer'
     4. 0.90 'expects'
     5. 0.89 'entertain'
     6. 0.89 'recognize'
     7. 0.89 'encourage'


[+] target_word: 'friedrich' model: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.96 'wilhelm'
     2. 0.90 'ludwig'
     3. 0.88 'heinrich'
     4. 0.87 'gustav'
     5. 0.87 'karl'
     6. 0.87 'vladimir'
     7. 0.87 'kaiser'


[+] target_word: 'along' model: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.97 'across'
     2. 0.93 'outside'
     3. 0.91 'side'
     4. 0.91 'straight'
     5. 0.90 'near'
     6. 0.90 'around'
     7. 0.89 'close'


[+] target_word: 'highest' model: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.94 'lowest'
     2. 0.86 'higher'
     3. 0.85 'high'
     4. 0.84 'smallest'
     5. 0.83 'greater'
     6. 0.82 'relative'
     7. 0.81 'wider'


[+] target_word: 'perry' model: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.98 'riley'
     2. 0.96 'williamson'
     3. 0.96 'walker'
     4. 0.95 'baker'
     5. 0.95 'bryan'
     6. 0.95 'dixon'
     7. 0.95 'phillip'


[+] target_word: 'beard' model: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.98 'mustache'
     2. 0.97 'whiskers'
     3. 0.96 'moustache'
     4. 0.94 'wig'
     5. 0.92 'curls'
     6. 0.92 'plump'
     7. 0.91 'blond'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-29 09:53:32,200 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-29 09:53:32,400 : INFO : capital-common-countries: 19.0% (88/462)
2020-09-29 09:53:32,789 : INFO : capital-world: 11.6% (100/862)
2020-09-29 09:53:32,847 : INFO : currency: 0.8% (1/128)
2020-09-29 09:53:33,705 : INFO : city-in-state: 4.2% (84/2009)
2020-09-29 09:53:33,837 : INFO : family: 50.5% (192/380)
2020-09-29 09:53:34,192 : INFO : gram1-adjective-to-adverb: 5.6% (56/992)
2020-09-29 09:53:34,439 : INFO : gram2-opposite: 3.1% (20/650)
2020-09-29 09:53:34,989 : INFO : gram3-comparative: 33.5% (446/1332)
2020-09-29 09:53:35,378 : INFO : gram4-superlative: 12.1% (128/1056)
2020-09-29 09:53:35,741 : INFO : gram5-present-participle: 20.6% (204/992)
2020-09-29 09:53:36,337 : INFO : gram6-nationality-adjective: 16.9% (220/1299)
2020-09-29 09:53:36,900 : INFO : gram7-past-tense: 38.1% (595/1560)
2020-09-29 09:53:37,423 : INFO : gram8-plural: 32.4% (385/1190)
2020-09-29 09:53:37,718 : INFO : gram9-plural-verbs: 14.5% (118/812)
2020-09-29 09:53:37,719 : INFO : Quadruplets with out-of-vocabulary words: 29.8%
2020-09-29 09:53:37,719 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 09:53:37,720 : INFO : Total accuracy: 19.2% (2637/13724)
Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/m,d15,n40,w3,mc99,s5e-05,t6): 19.21% correct (2637 of 13724)


[+] questions-words-narrowed.txt
2020-09-29 09:53:37,745 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-29 09:53:37,880 : INFO : family: 50.5% (192/380)
2020-09-29 09:53:38,238 : INFO : gram1-adjective-to-adverb: 5.6% (56/992)
2020-09-29 09:53:38,487 : INFO : gram2-opposite: 3.1% (20/650)
2020-09-29 09:53:39,039 : INFO : gram3-comparative: 33.5% (446/1332)
2020-09-29 09:53:39,430 : INFO : gram4-superlative: 12.1% (128/1056)
2020-09-29 09:53:39,794 : INFO : gram5-present-participle: 20.6% (204/992)
2020-09-29 09:53:40,387 : INFO : gram6-nationality-adjective: 16.9% (220/1299)
2020-09-29 09:53:40,948 : INFO : gram7-past-tense: 38.1% (595/1560)
2020-09-29 09:53:41,470 : INFO : gram8-plural: 32.4% (385/1190)
2020-09-29 09:53:41,764 : INFO : gram9-plural-verbs: 14.5% (118/812)
2020-09-29 09:53:41,765 : INFO : Quadruplets with out-of-vocabulary words: 8.2%
2020-09-29 09:53:41,766 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 09:53:41,767 : INFO : Total accuracy: 23.0% (2364/10263)
Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/m,d15,n40,w3,mc99,s5e-05,t6): 23.03% correct (2364 of 10263)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-29 09:53:41,936 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5394
2020-09-29 09:53:41,936 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5220
2020-09-29 09:53:41,936 : INFO : Pairs with unknown words ratio: 2.5%
((0.5393620451041027, 2.3414703407186805e-27), SpearmanrResult(correlation=0.522005155564426, pvalue=1.9415704420128142e-25), 2.5495750708215295)


02 - simlex999
2020-09-29 09:53:41,961 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2812
2020-09-29 09:53:41,961 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2247
2020-09-29 09:53:41,961 : INFO : Pairs with unknown words ratio: 0.5%
((0.2811857016364033, 1.6110660969907212e-19), SpearmanrResult(correlation=0.22470464911701407, pvalue=7.6450650133827e-13), 0.5005005005005005)


03 - simverb3500
2020-09-29 09:53:42,009 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1313
2020-09-29 09:53:42,009 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1096
2020-09-29 09:53:42,009 : INFO : Pairs with unknown words ratio: 6.0%
((0.1313183560168453, 4.000379080952068e-14), SpearmanrResult(correlation=0.10964768011624565, pvalue=2.8837937616703123e-10), 6.0285714285714285)


     ____________     COMPLETED      ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#


"""
