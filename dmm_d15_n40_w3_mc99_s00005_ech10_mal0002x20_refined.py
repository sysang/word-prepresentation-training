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
        epochs=10,
        min_alpha=0.0002,
        alpha=0.0002*10*10,
        comment='ech10,mal0002x10,refined',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    pprint.pprint(common_kwargs)

    base.train(
            common_kwargs=common_kwargs,
            saved_fname=saved_fname,
            evaluate=False,
            database='refined'
            )

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech10,mal0002x10,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6)
Save model to: models/dmm_d15_n40_w3_mc99_s00005_ech10_mal0002x20_refined.bin
2020-09-27 20:29:02,043 : INFO : saving Doc2Vec object under models/dmm_d15_n40_w3_mc99_s00005_ech10_mal0002x20_refined.bin, separately None
2020-09-27 20:29:02,043 : INFO : storing np array 'vectors_docs_lockf' to models/dmm_d15_n40_w3_mc99_s00005_ech10_mal0002x20_refined.bin.trainables.vectors_docs_lockf.npy
2020-09-27 20:29:02,122 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n40_w3_mc99_s00005_ech10_mal0002x20_refined.bin.docvecs.vectors_docs.npy
2020-09-27 20:29:03,265 : INFO : saved models/dmm_d15_n40_w3_mc99_s00005_ech10_mal0002x20_refined.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 20268249
[+] index 20268249 -> "that apology had absolutely nothing to do with your slandering me in july"
2020-09-27 20:29:03,275 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 29778948
[+] index 29778948 -> "fuel and air mix downstream of the two fixed orifices mentioned above"
    No any match in top 200 similarities.


.....get random document, tag: 11024303
[+] index 11024303 -> "that 's like saying the brain surgery would have gone great if i 'd known where all those neurons and blobs of tissue were"
    No any match in top 200 similarities.


.....get random document, tag: 12960331
[+] index 12960331 -> "it seems to me you have no idea what rules are in play here"
    No any match in top 200 similarities.


.....get random document, tag: 14057006
[+] index 14057006 -> "and they want to ban conservative speech as well"
    No any match in top 200 similarities.


.....get random document, tag: 4286306
[+] index 4286306 -> "the fact is that there are among the africans of darkest skin those more intelligent than you"
    No any match in top 200 similarities.


.....get random document, tag: 3130872
[+] index 3130872 -> "lastly for any stragglers on sunday we will be meeting for final drinks and brunch before everyone makes their way home"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (23368020): what this fellow bruces wants is to let iraq invades all countries

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech10,mal0002x10,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):

MOST (28307574, 0.9887467622756958): «he is creating a new generation of terrorists in the middle east to threaten us and our national security»

MEDIAN (23802444, 0.8487963676452637): «this is quite different from booking a senior or military fare when you are not entitled to it»

LEAST (37641239, -0.9298444986343384): «it is a crime to steal untold billions from america»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'garcia' model: Doc2Vec("ech10,mal0002x10,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
2020-09-27 20:30:33,642 : INFO : precomputing L2-norms of word weight vectors
     1. 0.98 'jorge'
     2. 0.97 'morgan'
     3. 0.96 'henderson'
     4. 0.96 'theo'
     5. 0.96 'castillo'
     6. 0.95 'reyes'
     7. 0.95 'carlos'


[+] target_word: 'encountered' model: Doc2Vec("ech10,mal0002x10,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.94 'seen'
     2. 0.91 'overlooked'
     3. 0.89 'attracted'
     4. 0.89 'faking'
     5. 0.89 'known'
     6. 0.88 'rife'
     7. 0.88 'similiar'


[+] target_word: 'its' model: Doc2Vec("ech10,mal0002x10,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.82 'fronts'
     2. 0.81 'continental'
     3. 0.79 'divisions'
     4. 0.79 'along'
     5. 0.79 'continents'
     6. 0.79 'across'
     7. 0.78 'mainly'


[+] target_word: 'handguns' model: Doc2Vec("ech10,mal0002x10,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.94 'firearms'
     2. 0.92 'guns'
     3. 0.91 'aliens'
     4. 0.90 'ammunition'
     5. 0.88 'handgun'
     6. 0.88 'hoas'
     7. 0.88 'firearm'


[+] target_word: 'recollect' model: Doc2Vec("ech10,mal0002x10,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 1.00 'nibble'
     2. 1.00 'tease'
     3. 1.00 'mould'
     4. 1.00 'dine'
     5. 1.00 'scold'
     6. 1.00 'irritate'
     7. 1.00 'irrigate'


[+] target_word: 'curiosity' model: Doc2Vec("ech10,mal0002x10,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.91 'curiousity'
     2. 0.88 'pleasure'
     3. 0.87 'perhaps'
     4. 0.87 'abilities'
     5. 0.86 'vibes'
     6. 0.86 'difficulty'
     7. 0.85 'zenworm'


[+] target_word: 'siting' model: Doc2Vec("ech10,mal0002x10,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.89 'forecasting'
     2. 0.82 'tackling'
     3. 0.81 'rollout'
     4. 0.80 'modelers'
     5. 0.80 'signaling'
     6. 0.77 'anticipating'
     7. 0.77 'tricky'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-27 20:30:35,025 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-27 20:30:35,250 : INFO : capital-common-countries: 1.9% (9/462)
2020-09-27 20:30:35,846 : INFO : capital-world: 1.8% (21/1157)
2020-09-27 20:30:35,945 : INFO : currency: 2.2% (4/178)
2020-09-27 20:30:37,264 : INFO : city-in-state: 1.5% (33/2267)
2020-09-27 20:30:37,509 : INFO : family: 20.0% (84/420)
2020-09-27 20:30:38,075 : INFO : gram1-adjective-to-adverb: 2.8% (28/992)
2020-09-27 20:30:38,554 : INFO : gram2-opposite: 2.0% (15/756)
2020-09-27 20:30:39,268 : INFO : gram3-comparative: 4.8% (64/1332)
2020-09-27 20:30:39,806 : INFO : gram4-superlative: 3.4% (36/1056)
2020-09-27 20:30:40,408 : INFO : gram5-present-participle: 14.0% (148/1056)
2020-09-27 20:30:41,232 : INFO : gram6-nationality-adjective: 6.5% (85/1299)
2020-09-27 20:30:42,101 : INFO : gram7-past-tense: 12.7% (198/1560)
2020-09-27 20:30:42,740 : INFO : gram8-plural: 9.6% (114/1190)
2020-09-27 20:30:43,271 : INFO : gram9-plural-verbs: 5.9% (51/870)
2020-09-27 20:30:43,272 : INFO : Quadruplets with out-of-vocabulary words: 25.3%
2020-09-27 20:30:43,272 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-27 20:30:43,272 : INFO : Total accuracy: 6.1% (890/14595)
Doc2Vec("ech10,mal0002x10,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6): 6.10% correct (890 of 14595)


[+] questions-words-narrowed.txt
2020-09-27 20:30:43,311 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-27 20:30:43,558 : INFO : family: 20.0% (84/420)
2020-09-27 20:30:44,123 : INFO : gram1-adjective-to-adverb: 2.8% (28/992)
2020-09-27 20:30:44,602 : INFO : gram2-opposite: 2.0% (15/756)
2020-09-27 20:30:45,322 : INFO : gram3-comparative: 4.8% (64/1332)
2020-09-27 20:30:45,862 : INFO : gram4-superlative: 3.4% (36/1056)
2020-09-27 20:30:46,465 : INFO : gram5-present-participle: 14.0% (148/1056)
2020-09-27 20:30:47,295 : INFO : gram6-nationality-adjective: 6.5% (85/1299)
2020-09-27 20:30:48,786 : INFO : gram7-past-tense: 12.7% (198/1560)
2020-09-27 20:30:49,427 : INFO : gram8-plural: 9.6% (114/1190)
2020-09-27 20:30:49,958 : INFO : gram9-plural-verbs: 5.9% (51/870)
2020-09-27 20:30:49,958 : INFO : Quadruplets with out-of-vocabulary words: 5.8%
2020-09-27 20:30:49,958 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-27 20:30:49,959 : INFO : Total accuracy: 7.8% (823/10531)
Doc2Vec("ech10,mal0002x10,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6): 7.82% correct (823 of 10531)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-27 20:30:50,006 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5007
2020-09-27 20:30:50,006 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5214
2020-09-27 20:30:50,006 : INFO : Pairs with unknown words ratio: 0.6%
((0.5007433354414018, 1.1219287936844289e-23), SpearmanrResult(correlation=0.521440903129636, pvalue=7.278288795924922e-26), 0.56657223796034)


02 - simlex999
2020-09-27 20:30:50,656 : INFO : Pearson correlation coefficient against simlex999.txt: 0.1720
2020-09-27 20:30:50,656 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1679
2020-09-27 20:30:50,656 : INFO : Pairs with unknown words ratio: 0.5%
((0.1719688023923531, 4.879062106895549e-08), SpearmanrResult(correlation=0.1678615766629267, pvalue=1.0181306654899913e-07), 0.5005005005005005)


03 - simverb3500
2020-09-27 20:30:50,717 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1372
2020-09-27 20:30:50,717 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1402
2020-09-27 20:30:50,717 : INFO : Pairs with unknown words ratio: 0.5%
((0.13723763874285155, 4.1608085088655876e-16), SpearmanrResult(correlation=0.14018766339209626, pvalue=9.541421803529298e-17), 0.5142857142857142)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
