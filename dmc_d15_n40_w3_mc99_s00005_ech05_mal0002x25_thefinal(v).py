import doc2vec_training_script_multiprocessing as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=40,
        window=3,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*25*5,
        comment='ech05,mal0002x25',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
2020-09-22 08:52:56,572 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-22 08:52:56,572 : INFO : Loading a fresh vocabulary
2020-09-22 08:52:57,005 : INFO : effective_min_count=99 retains 61077 unique words (3% of original 1784839, drops 1723762)
2020-09-22 08:52:57,005 : INFO : effective_min_count=99 leaves 328657804 word corpus (97% of original 336075146, drops 7417342)
2020-09-22 08:52:57,143 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-22 08:52:57,180 : INFO : sample=5e-05 downsamples 733 most-common words
2020-09-22 08:52:57,180 : INFO : downsampling leaves estimated 147142569 word corpus (44.8% of prior 328657804)
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6)
Save model to: models/dmc_d15_n40_w3_mc99_s00005_ech05_mal0002x25_thefinal.bin
2020-09-22 10:07:09,748 : INFO : saving Doc2Vec object under models/dmc_d15_n40_w3_mc99_s00005_ech05_mal0002x25_thefinal.bin, separately None
2020-09-22 10:07:09,748 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n40_w3_mc99_s00005_ech05_mal0002x25_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-22 10:07:09,776 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n40_w3_mc99_s00005_ech05_mal0002x25_thefinal.bin.docvecs.vectors_docs.npy
2020-09-22 10:07:10,392 : INFO : saved models/dmc_d15_n40_w3_mc99_s00005_ech05_mal0002x25_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 7511852
[+] index 7511852 -> "according to the united states census bureau the town has a total area of 91 9 km² 35 5 mi²"
2020-09-22 10:07:10,405 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 100 similarities.


.....get random document, tag: 8707787
[+] index 8707787 -> "the controversial land reform program that was kicked off in zimbabwe followed by the september 11 2001 attacks propelled it to its weakest historical level of r13 84 to the dollar in december 2001"
[*] Matched with rank 33, score: 0.8844872713088989!


.....get random document, tag: 5562419
[+] index 5562419 -> "it does not matter now in the least if we are ruined"
    No any match in top 100 similarities.


.....get random document, tag: 8389357
[+] index 8389357 -> "brünnow thinks that the rock in question was the sacred mountain en-nejr above but buhl suggests a conspicuous height about 16 miles north of petra shobak the mont-royal of the crusaders"
    No any match in top 100 similarities.


.....get random document, tag: 8856877
[+] index 8856877 -> "nixon to china during his breakthrough trip in january 1972"
    No any match in top 100 similarities.


.....get random document, tag: 12331101
[+] index 12331101 -> "i will probably have an extended post about our trip sometime this week"
    No any match in top 100 similarities.


.....get random document, tag: 8297848
[+] index 8297848 -> "the temple was the most common and best-known form of greek public architecture"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (9903624): the median income for a household in the cdp is $41 875 and the median income for a family is $46 250

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6):

MOST (11879210, 0.932208240032196): «art can range from simple painted stickers on lamp posts to elaborate silk screen techniques lithography and even pieces that involve ceramics»

MEDIAN (11661354, 0.0050731077790260315): «goodbye july almost where did this month go it went by so quickly»

LEAST (6490621, -0.9239216446876526): «there 's really no point in commenting on the dialogue moronic or acting what acting»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'assume' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6):
2020-09-22 10:07:35,895 : INFO : precomputing L2-norms of word weight vectors
     1. 0.96 'prove'
     2. 0.94 'imply'
     3. 0.93 'contradict'
     4. 0.92 'substantiate'
     5. 0.92 'affirm'
     6. 0.92 'deny'
     7. 0.92 'invalidate'


[+] target_word: 'canyon' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.94 'coulee'
     2. 0.93 'rapids'
     3. 0.92 'gorge'
     4. 0.92 'brook'
     5. 092 'light-house'
     6. 0.92 'beacon'
     7. 0.91 'lighthouse'


[+] target_word: 'ornamental' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.96 'decorative'
     2. 0.94 'antique'
     3. 0.93 'free-standing'
     4. 0.92 'unpolished'
     5. 0.91 'segmented'
     6. 0.91 'floral'
     7. 0.90 'variegated'


[+] target_word: 'savages' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.95 'barbarians'
     2. 0.95 'mountaineers'
     3. 0.94 'zulus'
     4. 0.94 'bedouins'
     5. 0.94 'tribesmen'
     6. 0.94 'amahagger'
     7. 0.94 'nomads'


[+] target_word: 'bits' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.92 'blanks'
     2. 0.91 'pieces'
     3. 0.91 'bytes'
     4. 0.91 'samples'
     5. 0.90 'discs'
     6. 0.90 'frames'
     7. 0.90 'digits'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-22 10:07:36,618 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-22 10:07:36,965 : INFO : capital-common-countries: 8.7% (44/506)
2020-09-22 10:07:38,214 : INFO : capital-world: 4.4% (78/1779)
2020-09-22 10:07:38,339 : INFO : currency: 1.7% (3/178)
2020-09-22 10:07:39,792 : INFO : city-in-state: 2.1% (47/2267)
2020-09-22 10:07:40,094 : INFO : family: 38.6% (162/420)
2020-09-22 10:07:40,743 : INFO : gram1-adjective-to-adverb: 3.8% (38/992)
2020-09-22 10:07:41,149 : INFO : gram2-opposite: 5.7% (40/702)
2020-09-22 10:07:41,863 : INFO : gram3-comparative: 30.3% (404/1332)
2020-09-22 10:07:42,432 : INFO : gram4-superlative: 11.6% (123/1056)
2020-09-22 10:07:43,014 : INFO : gram5-present-participle: 25.0% (264/1056)
2020-09-22 10:07:43,823 : INFO : gram6-nationality-adjective: 12.7% (174/1371)
2020-09-22 10:07:44,873 : INFO : gram7-past-tense: 26.7% (416/1560)
2020-09-22 10:07:45,827 : INFO : gram8-plural: 14.9% (198/1332)
2020-09-22 10:07:46,425 : INFO : gram9-plural-verbs: 10.0% (87/870)
2020-09-22 10:07:46,426 : INFO : Quadruplets with out-of-vocabulary words: 21.1%
2020-09-22 10:07:46,426 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-22 10:07:46,426 : INFO : Total accuracy: 13.5% (2078/15421)
Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6): 13.48% correct (2078 of 15421)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-22 10:07:46,700 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5555
2020-09-22 10:07:46,701 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5515
2020-09-22 10:07:46,701 : INFO : Pairs with unknown words ratio: 0.6%
((0.5554954896022042, 8.285064596805521e-30), SpearmanrResult(correlation=0.5515428028600498, pvalue=2.5086601109218227e-29), 0.56657223796034)


02 - simlex999
2020-09-22 10:07:46,750 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3158
2020-09-22 10:07:46,750 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2729
2020-09-22 10:07:46,750 : INFO : Pairs with unknown words ratio: 0.3%
((0.3158078892874557, 1.667348434591329e-24), SpearmanrResult(correlation=0.2729193202064526, pvalue=1.796533692268697e-18), 0.3003003003003003)


03 - simverb3500
2020-09-22 10:07:47,029 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1829
2020-09-22 10:07:47,029 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1684
2020-09-22 10:07:47,029 : INFO : Pairs with unknown words ratio: 1.4%
((0.1828506110580292, 2.462820140020321e-27), SpearmanrResult(correlation=0.16837467894144761, pvalue=2.2750305587794313e-23), 1.3714285714285714)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
