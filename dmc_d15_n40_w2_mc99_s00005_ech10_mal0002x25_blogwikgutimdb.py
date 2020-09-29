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
        epochs=10,
        min_alpha=0.0002,
        alpha=0.0002*10*10,
        comment='ech10,mal0002x10,blogwikgutimdb',
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


Model details: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6)
Save model to: models/dmc_d15_n40_w2_mc99_s00005_ech10_mal0002x25_blogwikgutimdb.bin
2020-09-29 18:37:53,176 : INFO : saving Doc2Vec object under models/dmc_d15_n40_w2_mc99_s00005_ech10_mal0002x25_blogwikgutimdb.bin, separately None
2020-09-29 18:37:53,176 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n40_w2_mc99_s00005_ech10_mal0002x25_blogwikgutimdb.bin.docvecs.vectors_docs.npy
2020-09-29 18:37:53,573 : INFO : saved models/dmc_d15_n40_w2_mc99_s00005_ech10_mal0002x25_blogwikgutimdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 3748572
[+] index 3748572 -> "his pallbearers comprised representatives of literature of science of both houses of parliament of theology anglican and nonconformist and of the universities of oxford and cambridge"
2020-09-29 18:37:54,866 : INFO : precomputing L2-norms of doc weight vectors
[*] Matched with rank 49, score: 0.8695862889289856!


.....get random document, tag: 5422122
[+] index 5422122 -> "the unit included an entire service arm including ground crew and not just pilots"
    No any match in top 200 similarities.


.....get random document, tag: 3942474
[+] index 3942474 -> "however by 1836 the new main building of the university was inaugurated amid extensive building until the end of the century"
    No any match in top 200 similarities.


.....get random document, tag: 6886114
[+] index 6886114 -> "it would be nice to have a job where you did not have files to work"
[*] Matched with rank 4, score: 0.9182670712471008!


.....get random document, tag: 1951860
[+] index 1951860 -> "he thought that he also had a glimpse of his waterman in the green jacket"
[*] Matched with rank 1, score: 0.9438657164573669!


.....get random document, tag: 6525182
[+] index 6525182 -> "todd see below makes the best deserts in town and yes i am having way too much fun with links and photos in this post"
    No any match in top 200 similarities.


.....get random document, tag: 1510648
[+] index 1510648 -> "she would not have been at all happy seeing all this alcohol about"
[*] Matched with rank 77, score: 0.8640607595443726!




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (1879479): pritchett m very much obliged for the trouble you are at in telling me oh i think nothing of the trouble

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):

MOST (4442156, 0.9335314035415649): «a new group of artists among them ol kainry and disiz la peste are very close to contemporary american rap music»

MEDIAN (1478063, -0.0019260793924331665): «shorter with a sigh acknowledged this necessity and escorted honora gallantly through the office and across the sidewalk to the waiting hansom»

LEAST (4382946, -0.9337027072906494): «chinese eggplant are commonly shaped like a narrower slightly pendulous cucumber»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'grown' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
2020-09-29 18:38:21,715 : INFO : precomputing L2-norms of word weight vectors
     1. 0.90 'grew'
     2. 0.89 'covered'
     3. 0.88 'grows'
     4. 0.87 'watered'
     5. 0.86 'inhabited'
     6. 0.85 'matured'
     7. 0.85 'harvested'


[+] target_word: 'uncle' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.98 'cousin'
     2. 0.96 'wife'
     3. 0.95 'nephew'
     4. 0.94 'brother'
     5. 0.94 'husband'
     6. 0.94 'friend'
     7. 0.94 'fiance'


[+] target_word: 'performances' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.92 'collaborations'
     2. 0.92 'cameos'
     3. 0.91 'roles'
     4. 0.91 'solos'
     5. 0.90 'choreography'
     6. 0.89 'skits'
     7. 0.89 'highlights'


[+] target_word: 'bridge' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.94 'tower'
     2. 0.94 'breakwater'
     3. 0.94 'lighthouse'
     4. 0.93 'canal'
     5. 0.93 'causeway'
     6. 0.93 'strand'
     7. 0.93 'quay'


[+] target_word: 'shouting' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.97 'yelling'
     2. 0.95 'screaming'
     3. 0.95 'shrieking'
     4. 0.95 'beating'
     5. 0.94 'bellowing'
     6. 0.94 'cheering'
     7. 0.93 'bawling'


[+] target_word: 'term' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.92 'phonetic'
     2. 0.91 'usage'
     3. 0.91 'concept'
     4. 0.91 'orthography'
     5. 0.90 'derivation'
     6. 0.90 'transcription'
     7. 0.90 'identity'


[+] target_word: 'rhythm' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.96 'melodic'
     2. 0.94 'acoustic'
     3. 0.94 'cadence'
     4. 0.93 'rhythmic'
     5. 0.92 'sonorous'
     6. 0.92 'background'
     7. 0.91 'melody'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-29 18:38:22,049 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-29 18:38:22,234 : INFO : capital-common-countries: 9.3% (43/462)
2020-09-29 18:38:22,594 : INFO : capital-world: 7.3% (63/862)
2020-09-29 18:38:22,648 : INFO : currency: 0.8% (1/128)
2020-09-29 18:38:23,413 : INFO : city-in-state: 2.6% (53/2009)
2020-09-29 18:38:23,578 : INFO : family: 45.0% (171/380)
2020-09-29 18:38:23,989 : INFO : gram1-adjective-to-adverb: 3.0% (30/992)
2020-09-29 18:38:24,271 : INFO : gram2-opposite: 4.2% (27/650)
2020-09-29 18:38:24,787 : INFO : gram3-comparative: 40.2% (535/1332)
2020-09-29 18:38:25,196 : INFO : gram4-superlative: 17.2% (182/1056)
2020-09-29 18:38:25,595 : INFO : gram5-present-participle: 22.4% (222/992)
2020-09-29 18:38:26,191 : INFO : gram6-nationality-adjective: 14.8% (192/1299)
2020-09-29 18:38:26,824 : INFO : gram7-past-tense: 28.9% (451/1560)
2020-09-29 18:38:27,364 : INFO : gram8-plural: 20.3% (242/1190)
2020-09-29 18:38:27,703 : INFO : gram9-plural-verbs: 19.0% (154/812)
2020-09-29 18:38:27,703 : INFO : Quadruplets with out-of-vocabulary words: 29.8%
2020-09-29 18:38:27,704 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 18:38:27,704 : INFO : Total accuracy: 17.2% (2366/13724)
Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6): 17.24% correct (2366 of 13724)


[+] questions-words-narrowed.txt
2020-09-29 18:38:27,725 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-29 18:38:27,890 : INFO : family: 45.0% (171/380)
2020-09-29 18:38:28,304 : INFO : gram1-adjective-to-adverb: 3.0% (30/992)
2020-09-29 18:38:28,586 : INFO : gram2-opposite: 4.2% (27/650)
2020-09-29 18:38:29,104 : INFO : gram3-comparative: 40.2% (535/1332)
2020-09-29 18:38:29,512 : INFO : gram4-superlative: 17.2% (182/1056)
2020-09-29 18:38:29,913 : INFO : gram5-present-participle: 22.4% (222/992)
2020-09-29 18:38:30,502 : INFO : gram6-nationality-adjective: 14.8% (192/1299)
2020-09-29 18:38:31,301 : INFO : gram7-past-tense: 28.9% (451/1560)
2020-09-29 18:38:31,842 : INFO : gram8-plural: 20.3% (242/1190)
2020-09-29 18:38:32,183 : INFO : gram9-plural-verbs: 19.0% (154/812)
2020-09-29 18:38:32,183 : INFO : Quadruplets with out-of-vocabulary words: 8.2%
2020-09-29 18:38:32,184 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 18:38:32,184 : INFO : Total accuracy: 21.5% (2206/10263)
Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6): 21.49% correct (2206 of 10263)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-29 18:38:32,353 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5489
2020-09-29 18:38:32,353 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5468
2020-09-29 18:38:32,353 : INFO : Pairs with unknown words ratio: 2.5%
((0.5489359688952785, 1.830889981984142e-28), SpearmanrResult(correlation=0.546754649684854, pvalue=3.2958965578662055e-28), 2.5495750708215295)


02 - simlex999
2020-09-29 18:38:32,379 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3193
2020-09-29 18:38:32,379 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2707
2020-09-29 18:38:32,379 : INFO : Pairs with unknown words ratio: 0.5%
((0.31929191655219746, 5.411492971006437e-25), SpearmanrResult(correlation=0.2706569293333035, pvalue=3.784757829468776e-18), 0.5005005005005005)


03 - simverb3500
2020-09-29 18:38:32,426 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1663
2020-09-29 18:38:32,426 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1483
2020-09-29 18:38:32,426 : INFO : Pairs with unknown words ratio: 6.0%
((0.16634620269455092, 7.744384190542981e-22), SpearmanrResult(correlation=0.1483202224307343, pvalue=1.2284056624931465e-17), 6.0285714285714285)


     ____________     COMPLETED      ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
