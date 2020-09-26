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
        epochs=3,
        min_alpha=0.0002,
        alpha=0.0002*30*3,
        comment='ech03,mal0002x20,refined',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    pprint.pprint(common_kwargs)

    base.train(
            common_kwargs=common_kwargs,
            saved_fname=saved_fname,
            evaluate=False,
            database='refined')

"""
2020-09-25 19:16:00,801 : INFO : collected 877734 word types and 46020000 unique tags from a corpus of 46020000 examples and 610836932 words
2020-09-25 19:16:00,801 : INFO : Loading a fresh vocabulary
2020-09-25 19:16:01,050 : INFO : effective_min_count=99 retains 53059 unique words (6% of original 877734, drops 824675)
2020-09-25 19:16:01,050 : INFO : effective_min_count=99 leaves 606131238 word corpus (99% of original 610836932, drops 4705694)
2020-09-25 19:16:01,170 : INFO : deleting the raw counts dictionary of 877734 items
2020-09-25 19:16:01,187 : INFO : sample=5e-05 downsamples 822 most-common words
2020-09-25 19:16:01,187 : INFO : downsampling leaves estimated 265856440 word corpus (43.9% of prior 606131238)
2020-09-25 19:16:01,272 : INFO : estimated required memory for 53059 words and 15 dimensions: 2794096580 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech03,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6)
Save model to: models/dmm_d15_n40_w3_mc99_s00005_ech03_mal0002x30_refined.bin
2020-09-26 14:02:20,455 : INFO : saving Doc2Vec object under models/dmm_d15_n40_w3_mc99_s00005_ech03_mal0002x30_refined.bin, separately None
2020-09-26 14:02:20,455 : INFO : storing np array 'vectors_docs_lockf' to models/dmm_d15_n40_w3_mc99_s00005_ech03_mal0002x30_refined.bin.trainables.vectors_docs_lockf.npy
2020-09-26 14:02:20,535 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n40_w3_mc99_s00005_ech03_mal0002x30_refined.bin.docvecs.vectors_docs.npy
2020-09-26 14:02:21,676 : INFO : saved models/dmm_d15_n40_w3_mc99_s00005_ech03_mal0002x30_refined.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 40535521
[+] index 40535521 -> "that 's the most ridiculous lunacy i have ever heard"
2020-09-26 14:02:21,692 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 12923060
[+] index 12923060 -> "resident or currently able to legally work in the"
    No any match in top 200 similarities.


.....get random document, tag: 45461158
[+] index 45461158 -> "for this event they want to sell some of the great urllink gadgets they had in the old studio"
    No any match in top 200 similarities.


.....get random document, tag: 15864130
[+] index 15864130 -> "they knew that my friend did not have any intensive to pretend to be anyone 's friend as accused"
    No any match in top 200 similarities.


.....get random document, tag: 19577218
[+] index 19577218 -> "i do not know the newer ones much but a year ago i did look and it was like an expensive restaurant"
    No any match in top 200 similarities.


.....get random document, tag: 25338733
[+] index 25338733 -> "negotiating with terrorists is almost as criminal as being one"
    No any match in top 200 similarities.


.....get random document, tag: 29675259
[+] index 29675259 -> "bush is left for hstory to see what an idi amin he is"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (1277787): try not to open quickly while you are explaining about a proud shirt

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech03,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):

MOST (4527050, 0.9773986339569092): «all rural sticky teacher talks cards throughout ed 's dull cap»

MEDIAN (36643262, 0.6740894913673401): «then maybe he will kill himself and the world will be a better place»

LEAST (2526718, -0.9721218943595886): «it turns out to be blue according to the lorentz transform»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'infect' model: Doc2Vec("ech03,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
2020-09-26 14:03:49,773 : INFO : precomputing L2-norms of word weight vectors
     1. 0.89 'infecting'
     2. 0.88 'infected'
     3. 0.86 'ingest'
     4. 0.85 'weeding'
     5. 0.85 'cloned'
     6. 0.84 'consumed'
     7. 0.84 'infects'


[+] target_word: 'passionate' model: Doc2Vec("ech03,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.86 'lifelong'
     2. 0.84 'natured'
     3. 0.84 'consummate'
     4. 0.83 'admiration'
     5. 0.82 'haughty'
     6. 0.82 'passion'
     7. 0.82 'manly'


[+] target_word: 'freeway' model: Doc2Vec("ech03,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.93 'ramp'
     2. 0.92 'runway'
     3. 0.91 'motorbike'
     4. 0.90 'subway'
     5. 0.90 'staples'
     6. 0.90 'tractor'
     7. 0.90 'suv'


[+] target_word: 'virtuous' model: Doc2Vec("ech03,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.91 'sinful'
     2. 0.90 'unbelief'
     3. 0.90 'benevolence'
     4. 0.89 'glorify'
     5. 0.89 'unenlightened'
     6. 0.89 'yearning'
     7. 0.89 'righteous'


[+] target_word: 'nova' model: Doc2Vec("ech03,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.98 'scotia'
     2. 0.96 'la'
     3. 0.94 'rio'
     4. 0.92 'vancouver'
     5. 0.92 'brunswick'
     6. 0.91 'grande'
     7. 0.91 'tokyo'


[+] target_word: 'forgive' model: Doc2Vec("ech03,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.92 'confess'
     2. 0.85 'deserve'
     3. 0.84 'repent'
     4. 0.82 'watchman'
     5. 0.81 'swear'
     6. 0.81 'pleases'
     7. 0.80 'redeem'


[+] target_word: 'tract' model: Doc2Vec("ech03,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.94 'digestive'
     2. 0.92 'liver'
     3. 0.91 'iodine'
     4. 0.91 'yeast'
     5. 0.91 'tumors'
     6. 0.90 'pancreas'
     7. 0.90 'tumor'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-26 14:03:51,095 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-26 14:03:51,322 : INFO : capital-common-countries: 4.3% (20/462)
2020-09-26 14:03:51,989 : INFO : capital-world: 1.5% (17/1157)
2020-09-26 14:03:52,076 : INFO : currency: 5.1% (9/178)
2020-09-26 14:03:53,423 : INFO : city-in-state: 1.9% (43/2267)
2020-09-26 14:03:53,684 : INFO : family: 26.2% (110/420)
2020-09-26 14:03:54,240 : INFO : gram1-adjective-to-adverb: 5.0% (50/992)
2020-09-26 14:03:54,698 : INFO : gram2-opposite: 2.1% (16/756)
2020-09-26 14:03:55,318 : INFO : gram3-comparative: 5.3% (70/1332)
2020-09-26 14:03:55,834 : INFO : gram4-superlative: 2.9% (31/1056)
2020-09-26 14:03:56,429 : INFO : gram5-present-participle: 20.7% (219/1056)
2020-09-26 14:03:57,202 : INFO : gram6-nationality-adjective: 7.2% (94/1299)
2020-09-26 14:03:58,091 : INFO : gram7-past-tense: 13.3% (207/1560)
2020-09-26 14:03:58,744 : INFO : gram8-plural: 9.7% (115/1190)
2020-09-26 14:03:59,239 : INFO : gram9-plural-verbs: 7.9% (69/870)
2020-09-26 14:03:59,240 : INFO : Quadruplets with out-of-vocabulary words: 25.3%
2020-09-26 14:03:59,240 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-26 14:03:59,240 : INFO : Total accuracy: 7.3% (1070/14595)
Doc2Vec("ech03,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6): 7.33% correct (1070 of 14595)


[+] questions-words-narrowed.txt
2020-09-26 14:03:59,279 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-26 14:03:59,545 : INFO : family: 26.2% (110/420)
2020-09-26 14:04:00,106 : INFO : gram1-adjective-to-adverb: 5.0% (50/992)
2020-09-26 14:04:00,566 : INFO : gram2-opposite: 2.1% (16/756)
2020-09-26 14:04:01,188 : INFO : gram3-comparative: 5.3% (70/1332)
2020-09-26 14:04:01,706 : INFO : gram4-superlative: 2.9% (31/1056)
2020-09-26 14:04:02,304 : INFO : gram5-present-participle: 20.7% (219/1056)
2020-09-26 14:04:03,079 : INFO : gram6-nationality-adjective: 7.2% (94/1299)
2020-09-26 14:04:03,969 : INFO : gram7-past-tense: 13.3% (207/1560)
2020-09-26 14:04:04,624 : INFO : gram8-plural: 9.7% (115/1190)
2020-09-26 14:04:05,118 : INFO : gram9-plural-verbs: 7.9% (69/870)
2020-09-26 14:04:05,118 : INFO : Quadruplets with out-of-vocabulary words: 5.8%
2020-09-26 14:04:05,118 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-26 14:04:05,118 : INFO : Total accuracy: 9.3% (981/10531)
Doc2Vec("ech03,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6): 9.32% correct (981 of 10531)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-26 14:04:05,772 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4757
2020-09-26 14:04:05,772 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4904
2020-09-26 14:04:05,772 : INFO : Pairs with unknown words ratio: 0.6%
((0.47571661566526763, 3.1918083655620528e-21), SpearmanrResult(correlation=0.4903903143117303, pvalue=1.229356208924146e-22), 0.56657223796034)


02 - simlex999
2020-09-26 14:04:06,420 : INFO : Pearson correlation coefficient against simlex999.txt: 0.1847
2020-09-26 14:04:06,420 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1695
2020-09-26 14:04:06,420 : INFO : Pairs with unknown words ratio: 0.5%
((0.18467866369955813, 4.47229391462214e-09), SpearmanrResult(correlation=0.16945342280586484, pvalue=7.671893739908467e-08), 0.5005005005005005)


03 - simverb3500
2020-09-26 14:04:06,481 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1315
2020-09-26 14:04:06,481 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1264
2020-09-26 14:04:06,481 : INFO : Pairs with unknown words ratio: 0.5%
((0.13146000459236276, 6.7922241661897314e-15), SpearmanrResult(correlation=0.12642194512698904, pvalue=7.028046878817613e-14), 0.5142857142857142)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
