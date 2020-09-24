import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=75,
        window=5,
        min_count=50,
        sample=0.0001,
        dm=1,
        dm_concat=0,
        hs=0,
        epochs=7,
        min_alpha=0.0001,
        alpha=0.0001*70*7,
        comment='ech07,mal0001x70',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(common_kwargs=common_kwargs, saved_fname=saved_fname, evaluate=True)

"""
2020-09-24 21:40:31,843 : INFO : collected 605528 word types and 7410000 unique tags from a corpus of 7410000 examples and 121440062 words
2020-09-24 21:40:31,844 : INFO : Loading a fresh vocabulary
2020-09-24 21:40:32,018 : INFO : effective_min_count=50 retains 49732 unique words (8% of original 605528, drops 555796)
2020-09-24 21:40:32,018 : INFO : effective_min_count=50 leaves 119044697 word corpus (98% of original 121440062, drops 2395365)
2020-09-24 21:40:32,128 : INFO : deleting the raw counts dictionary of 605528 items
2020-09-24 21:40:32,139 : INFO : sample=0.0001 downsamples 383 most-common words
2020-09-24 21:40:32,139 : INFO : downsampling leaves estimated 60609058 word corpus (50.9% of prior 119044697)
2020-09-24 21:40:32,217 : INFO : estimated required memory for 49732 words and 15 dimensions: 475433840 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech07,mal0001x70",dm/m,d15,n75,w5,mc50,s0.0001,t6)
Save model to: models/dmm_d15_n75_w5_mc50_s0001_ech07_mal0001x70_blogwikguiimdb.bin
2020-09-24 22:51:29,001 : INFO : saving Doc2Vec object under models/dmm_d15_n75_w5_mc50_s0001_ech07_mal0001x70_blogwikguiimdb.bin, separately None
2020-09-24 22:51:29,001 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n75_w5_mc50_s0001_ech07_mal0001x70_blogwikguiimdb.bin.docvecs.vectors_docs.npy
2020-09-24 22:51:29,331 : INFO : saved models/dmm_d15_n75_w5_mc50_s0001_ech07_mal0001x70_blogwikguiimdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 2242650
[+] index 2242650 -> "he 's devoted to her and if it were a career to be an excellent father he 'd be very distinguished"
2020-09-24 22:51:30,111 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 7150158
[+] index 7150158 -> "still the same fears the same weaknesses the same doubts"
    No any match in top 200 similarities.


.....get random document, tag: 5458396
[+] index 5458396 -> "1 4 km² 0 6 mi² of it is land and none of it is covered by water"
    No any match in top 200 similarities.


.....get random document, tag: 2052033
[+] index 2052033 -> "you ought to see our men rush one of them"
    No any match in top 200 similarities.


.....get random document, tag: 1774086
[+] index 1774086 -> "on what principle of justice could sir felix come between him and another man i do not understand this kind of thing he said"
    No any match in top 200 similarities.


.....get random document, tag: 6891659
[+] index 6891659 -> "boooo after much hooplah and long waits in line"
    No any match in top 200 similarities.


.....get random document, tag: 3809426
[+] index 3809426 -> "however the bbfc refused to allow the release of the film uncut in britain citing its extreme levels of sexual violence towards women"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (1160696): wherever stirring adventures were to be had jefferson hope had been there in search of them

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech07,mal0001x70",dm/m,d15,n75,w5,mc50,s0.0001,t6):

MOST (5166635, 0.9890158176422119): «mount pleasant township is a township located in wabasha county minnesota in the united states»

MEDIAN (6053709, 0.8199068903923035): «now the cpa have changed it back to arabic»

LEAST (5183077, -0.904852032661438): «for every 100 females there are 85 00 males»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'easily' model: Doc2Vec("ech07,mal0001x70",dm/m,d15,n75,w5,mc50,s0.0001,t6):
2020-09-24 22:51:58,906 : INFO : precomputing L2-norms of word weight vectors
     1. 0.89 'reliably'
     2. 0.89 'normally'
     3. 0.88 'otherwise'
     4. 0.87 'evenly'
     5. 0.86 'completely'
     6. 0.85 'generally'
     7. 0.84 'somehow'


[+] target_word: 'disturbed' model: Doc2Vec("ech07,mal0001x70",dm/m,d15,n75,w5,mc50,s0.0001,t6):
     1. 0.91 'distracted'
     2. 0.89 'aroused'
     3. 0.88 'perturbed'
     4. 0.87 'roused'
     5. 0.87 'marveled'
     6. 0.87 'overwhelmed'
     7. 0.87 'troubled'


[+] target_word: 'deliver' model: Doc2Vec("ech07,mal0001x70",dm/m,d15,n75,w5,mc50,s0.0001,t6):
     1. 0.92 'give'
     2. 0.91 'introduce'
     3. 0.91 'sending'
     4. 0.90 'draw'
     5. 0.90 'rely'
     6. 0.90 'carry'
     7. 0.89 'employ'


[+] target_word: 'startled' model: Doc2Vec("ech07,mal0001x70",dm/m,d15,n75,w5,mc50,s0.0001,t6):
     1. 0.88 'dumbfounded'
     2. 0.88 'awed'
     3. 0.87 'horrified'
     4. 0.86 'climactic'
     5. 0.84 'marvelling'
     6. 0.84 'unmasked'
     7. 0.83 'astonished'


[+] target_word: 'trading' model: Doc2Vec("ech07,mal0001x70",dm/m,d15,n75,w5,mc50,s0.0001,t6):
     1. 0.91 'wholesale'
     2. 0.88 'multinational'
     3. 0.86 'randd'
     4. 0.86 'banking'
     5. 0.85 'realty'
     6. 0.85 'cooperative'
     7. 0.85 'local'


[+] target_word: 'inclined' model: Doc2Vec("ech07,mal0001x70",dm/m,d15,n75,w5,mc50,s0.0001,t6):
     1. 0.82 'constrained'
     2. 0.80 'confident'
     3. 0.79 'reasonable'
     4. 0.78 'surer'
     5. 0.78 'rediculous'
     6. 0.78 'aggrieved'
     7. 0.76 'steadier'


[+] target_word: 'brick' model: Doc2Vec("ech07,mal0001x70",dm/m,d15,n75,w5,mc50,s0.0001,t6):
     1. 0.92 'baize'
     2. 0.92 'stone'
     3. 0.92 'domed'
     4. 0.90 'marble'
     5. 0.90 'atop'
     6. 0.90 'stucco'
     7. 0.89 'pyramid'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-24 22:51:59,514 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-24 22:51:59,808 : INFO : capital-common-countries: 9.3% (47/506)
2020-09-24 22:52:00,799 : INFO : capital-world: 5.5% (93/1681)
2020-09-24 22:52:00,908 : INFO : currency: 1.1% (2/178)
2020-09-24 22:52:02,093 : INFO : city-in-state: 2.5% (57/2267)
2020-09-24 22:52:02,347 : INFO : family: 33.3% (140/420)
2020-09-24 22:52:02,874 : INFO : gram1-adjective-to-adverb: 3.7% (37/992)
2020-09-24 22:52:03,241 : INFO : gram2-opposite: 3.3% (23/702)
2020-09-24 22:52:03,912 : INFO : gram3-comparative: 34.4% (458/1332)
2020-09-24 22:52:04,388 : INFO : gram4-superlative: 6.8% (72/1056)
2020-09-24 22:52:04,934 : INFO : gram5-present-participle: 13.1% (138/1056)
2020-09-24 22:52:05,656 : INFO : gram6-nationality-adjective: 12.9% (167/1299)
2020-09-24 22:52:06,578 : INFO : gram7-past-tense: 27.2% (424/1560)
2020-09-24 22:52:07,389 : INFO : gram8-plural: 15.5% (206/1332)
2020-09-24 22:52:07,868 : INFO : gram9-plural-verbs: 9.9% (86/870)
2020-09-24 22:52:07,868 : INFO : Quadruplets with out-of-vocabulary words: 22.0%
2020-09-24 22:52:07,868 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-24 22:52:07,869 : INFO : Total accuracy: 12.8% (1950/15251)
Doc2Vec("ech07,mal0001x70",dm/m,d15,n75,w5,mc50,s0.0001,t6): 12.79% correct (1950 of 15251)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-24 22:52:07,912 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5930
2020-09-24 22:52:07,912 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5998
2020-09-24 22:52:07,913 : INFO : Pairs with unknown words ratio: 0.6%
((0.5930479979425375, 1.0211687585161894e-34), SpearmanrResult(correlation=0.5998286685115992, pvalue=1.1291665664848386e-35), 0.56657223796034)


02 - simlex999
2020-09-24 22:52:08,082 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3002
2020-09-24 22:52:08,082 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2570
2020-09-24 22:52:08,082 : INFO : Pairs with unknown words ratio: 0.4%
((0.3002335785214556, 3.568000580647286e-22), SpearmanrResult(correlation=0.2569587135173041, pvalue=1.8127342824273363e-16), 0.40040040040040037)


03 - simverb3500
2020-09-24 22:52:08,142 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1690
2020-09-24 22:52:08,142 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1587
2020-09-24 22:52:08,142 : INFO : Pairs with unknown words ratio: 2.1%
((0.16902067083897906, 2.1869012846707222e-23), SpearmanrResult(correlation=0.15868766579132557, pvalue=9.023886630449432e-21), 2.057142857142857)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
