import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=40,
        window=2,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=15,
        min_alpha=0.0002,
        alpha=0.0002*8*10,
        comment='ech15,mal0002x8,blogwikgutimdb',
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


Model details: Doc2Vec("ech15,mal0002x8,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6)
Save model to: models/dmc_d15_n40_w2_mc99_s00005_ech15_mal0002x8_blogwikgutimdb.bin
2020-09-29 20:19:48,481 : INFO : saving Doc2Vec object under models/dmc_d15_n40_w2_mc99_s00005_ech15_mal0002x8_blogwikgutimdb.bin, separately None
2020-09-29 20:19:48,481 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n40_w2_mc99_s00005_ech15_mal0002x8_blogwikgutimdb.bin.docvecs.vectors_docs.npy
2020-09-29 20:19:48,844 : INFO : saved models/dmc_d15_n40_w2_mc99_s00005_ech15_mal0002x8_blogwikgutimdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 2337695
-> index 2337695 --> "i think she declared that it is your candor which makes you englishmen so attractive"
2020-09-29 20:19:49,708 : INFO : precomputing L2-norms of doc weight vectors
[*] Matched with rank 146, score: 0.8653686046600342!


.....get random document, tag: 5348045
-> index 5348045 --> "game controllers can be used to govern the movement or actions of elements in a video or computer game"
    No any match in top 200 similarities.


.....get random document, tag: 142351
-> index 142351 --> "i remember i remember said lindau nodding his head slowly up and down"
[*] Matched with rank 1, score: 0.9763016700744629!


.....get random document, tag: 3627411
-> index 3627411 --> "he was a signer of the declaration of independence a continental congressman from delaware a delegate to the u s"
    No any match in top 200 similarities.


.....get random document, tag: 2211430
-> index 2211430 --> "in the adult rabbit they have ossified continuously with the rest of the body"
    No any match in top 200 similarities.


.....get random document, tag: 2000892
-> index 2000892 --> "d like a decent meal chapter i let him take me to a restaurant of his choice but on the way i bought a paper"
    No any match in top 200 similarities.


.....get random document, tag: 264566
-> index 264566 --> "in private life services demand compensation equal to the services rendered a wise economy would dictate the same rule in the government service"
[*] Matched with rank 1, score: 0.9742813110351562!




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (1289746): as soon as he came close i caught the rope

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech15,mal0002x8,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):

MOST (1590880, 0.9342396855354309): «the buoy fell close beside him and he caught it»

MEDIAN (2679513, 0.0005552386865019798): «this last class included not only the most desperate and utterly abandoned villains in london but some who were comparatively innocent»

LEAST (5736956, -0.9288856983184814): «although not a great football fan it was great fun watching the european cup with other different europeans»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'reflection' model: Doc2Vec("ech15,mal0002x8,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
2020-09-29 20:20:11,836 : INFO : precomputing L2-norms of word weight vectors
     1. 0.95 'abstraction'
     2. 0.93 'clarity'
     3. 0.93 'perception'
     4. 0.92 'introspection'
     5. 0.92 'expression'
     6. 0.92 'vision'
     7. 0.92 'vividness'


[+] target_word: 'straw' model: Doc2Vec("ech15,mal0002x8,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.93 'slipper'
     2. 0.93 'knuckle'
     3. 0.92 'belly'
     4. 0.91 'braid'
     5. 0.91 'feather'
     6. 0.90 'sock'
     7. 0.90 'buckskin'


[+] target_word: 'patron' model: Doc2Vec("ech15,mal0002x8,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.91 'franciscan'
     2. 0.90 'jesuit'
     3. 0.89 'devotee'
     4. 0.89 'guardian'
     5. 0.89 'healer'
     6. 0.88 'missionary'
     7. 0.88 'pilgrim'


[+] target_word: 'cardinal' model: Doc2Vec("ech15,mal0002x8,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.90 'abbe'
     2. 0.89 'clement'
     3. 0.88 'ptolemy'
     4. 0.88 'bolingbroke'
     5. 0.87 'successor'
     6. 0.87 'baron'
     7. 0.87 'cato'


[+] target_word: 'instantly' model: Doc2Vec("ech15,mal0002x8,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.95 'involuntarily'
     2. 0.93 'mysteriously'
     3. 0.93 'momentarily'
     4. 0.93 'werper'
     5. 0.93 'stubbornly'
     6. 0.93 'suddenly'
     7. 0.92 'rudely'


[+] target_word: 'pages' model: Doc2Vec("ech15,mal0002x8,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.94 'entries'
     2. 0.92 'headings'
     3. 0.91 'paragraphs'
     4. 0.91 'posts'
     5. 0.91 'chapters'
     6. 0.91 'illustrations'
     7. 0.90 'photographs'


[+] target_word: 'era' model: Doc2Vec("ech15,mal0002x8,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.91 'revival'
     2. 0.89 'renaissance'
     3. 0.87 'revolution'
     4. 0.87 'epoch'
     5. 0.86 'period'
     6. 0.85 'eras'
     7. 0.85 'heyday'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-29 20:20:12,213 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-29 20:20:12,398 : INFO : capital-common-countries: 8.7% (40/462)
2020-09-29 20:20:12,761 : INFO : capital-world: 5.7% (49/862)
2020-09-29 20:20:12,816 : INFO : currency: 0.0% (0/128)
2020-09-29 20:20:13,571 : INFO : city-in-state: 3.1% (63/2009)
2020-09-29 20:20:13,737 : INFO : family: 44.2% (168/380)
2020-09-29 20:20:14,162 : INFO : gram1-adjective-to-adverb: 3.1% (31/992)
2020-09-29 20:20:14,452 : INFO : gram2-opposite: 4.3% (28/650)
2020-09-29 20:20:14,965 : INFO : gram3-comparative: 39.9% (532/1332)
2020-09-29 20:20:15,357 : INFO : gram4-superlative: 11.6% (122/1056)
2020-09-29 20:20:15,756 : INFO : gram5-present-participle: 20.7% (205/992)
2020-09-29 20:20:16,338 : INFO : gram6-nationality-adjective: 11.9% (154/1299)
2020-09-29 20:20:16,996 : INFO : gram7-past-tense: 29.9% (467/1560)
2020-09-29 20:20:17,530 : INFO : gram8-plural: 19.7% (234/1190)
2020-09-29 20:20:17,872 : INFO : gram9-plural-verbs: 18.0% (146/812)
2020-09-29 20:20:17,872 : INFO : Quadruplets with out-of-vocabulary words: 29.8%
2020-09-29 20:20:17,873 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 20:20:17,873 : INFO : Total accuracy: 16.3% (2239/13724)
Doc2Vec("ech15,mal0002x8,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6): 16.31% correct (2239 of 13724)


[+] questions-words-narrowed.txt
2020-09-29 20:20:17,895 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-29 20:20:18,062 : INFO : family: 44.2% (168/380)
2020-09-29 20:20:18,487 : INFO : gram1-adjective-to-adverb: 3.1% (31/992)
2020-09-29 20:20:18,777 : INFO : gram2-opposite: 4.3% (28/650)
2020-09-29 20:20:19,289 : INFO : gram3-comparative: 39.9% (532/1332)
2020-09-29 20:20:19,680 : INFO : gram4-superlative: 11.6% (122/1056)
2020-09-29 20:20:20,079 : INFO : gram5-present-participle: 20.7% (205/992)
2020-09-29 20:20:20,656 : INFO : gram6-nationality-adjective: 11.9% (154/1299)
2020-09-29 20:20:21,318 : INFO : gram7-past-tense: 29.9% (467/1560)
2020-09-29 20:20:21,851 : INFO : gram8-plural: 19.7% (234/1190)
2020-09-29 20:20:22,194 : INFO : gram9-plural-verbs: 18.0% (146/812)
2020-09-29 20:20:22,195 : INFO : Quadruplets with out-of-vocabulary words: 8.2%
2020-09-29 20:20:22,195 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 20:20:22,195 : INFO : Total accuracy: 20.3% (2087/10263)
Doc2Vec("ech15,mal0002x8,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6): 20.34% correct (2087 of 10263)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-29 20:20:22,359 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5579
2020-09-29 20:20:22,359 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5508
2020-09-29 20:20:22,359 : INFO : Pairs with unknown words ratio: 2.5%
((0.5579423428666228, 1.5433040971848452e-29), SpearmanrResult(correlation=0.5507804903558717, pvalue=1.109958595682473e-28), 2.5495750708215295)


02 - simlex999
2020-09-29 20:20:22,384 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3377
2020-09-29 20:20:22,384 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2884
2020-09-29 20:20:22,384 : INFO : Pairs with unknown words ratio: 0.5%
((0.3377137178243185, 6.116883806088421e-28), SpearmanrResult(correlation=0.2883524377676567, pvalue=1.7361452813769557e-20), 0.5005005005005005)


03 - simverb3500
2020-09-29 20:20:22,431 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1759
2020-09-29 20:20:22,431 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1577
2020-09-29 20:20:22,431 : INFO : Pairs with unknown words ratio: 6.0%
((0.1758909935601997, 2.9059005310626515e-24), SpearmanrResult(correlation=0.1577125439745508, pvalue=9.17237239899816e-20), 6.0285714285714285)


     ____________     COMPLETED      ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
