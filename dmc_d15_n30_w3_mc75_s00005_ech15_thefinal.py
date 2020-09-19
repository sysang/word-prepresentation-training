import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15, negative=30, window=3, min_count=75, sample=0.00005,
        dm=1, dm_concat=1, hs=0, epochs=15
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    corpus = 'thefinal'

    base.train(corpus, common_kwargs, saved_fname)

"""
2020-09-19 12:51:51,493 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-19 12:51:51,494 : INFO : Loading a fresh vocabulary
2020-09-19 12:51:51,968 : INFO : effective_min_count=75 retains 70715 unique words (3% of original 1784839, drops 1714124)
2020-09-19 12:51:51,968 : INFO : effective_min_count=75 leaves 329482258 word corpus (98% of original 336075146, drops 6592888)
2020-09-19 12:51:52,130 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-19 12:51:52,166 : INFO : sample=5e-05 downsamples 730 most-common words
2020-09-19 12:51:52,166 : INFO : downsampling leaves estimated 148046269 word corpus (44.9% of prior 329482258)
2020-09-19 12:51:52,304 : INFO : estimated required memory for 70715 words and 15 dimensions: 866700700 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10)
Save model to: models/dmc_d15_n30_w3_mc75_s00005_ech15_thefinal.bin
2020-09-19 15:56:37,722 : INFO : saving Doc2Vec object under models/dmc_d15_n30_w3_mc75_s00005_ech15_thefinal.bin, separately None
2020-09-19 15:56:37,722 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n30_w3_mc75_s00005_ech15_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-19 15:56:37,751 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n30_w3_mc75_s00005_ech15_thefinal.bin.docvecs.vectors_docs.npy
2020-09-19 15:56:38,345 : INFO : saved models/dmc_d15_n30_w3_mc75_s00005_ech15_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 1539417
[+] index 1539417 -> "this was on new year 's day when mr"
2020-09-19 15:56:38,356 : INFO : precomputing L2-norms of doc weight vectors
!! No any match in top 100 similarities


.....get random document, tag: 9038469
[+] index 9038469 -> "göodel himself felt and expressed the thought in his paper that his work did not contradict hilbert 's formalistic point of view reid p"
!! No any match in top 100 similarities


.....get random document, tag: 1877445
[+] index 1877445 -> "but he had found out that i was your wife"
!! No any match in top 100 similarities


.....get random document, tag: 4648464
[+] index 4648464 -> "there ought to be a law to protect unfortunate authors said mrs jo one morning soon after emil 's arrival when the mail brought her an unusually large and varied assortment of letters"
!! No any match in top 100 similarities


.....get random document, tag: 7022656
[+] index 7022656 -> "it occurs in all age groups but especially in the elderly"
** Matched with rank 1, score: 0.9809085130691528


.....get random document, tag: 1841421
[+] index 1841421 -> "billy with his teamster judgment admitted that for heavy hauling it was anything but a picnic"
!! No any match in top 100 similarities


.....get random document, tag: 977536
[+] index 977536 -> "i have read it with mingled feelings with keen appreciation of your sympathetic understanding of the problems which confronted the forest service before the western people understood it and with deep regret that i am no longer officially associated with its work although i am as deeply interested and almost as closely in touch as ever"
** Matched with rank 30, score: 0.9053714871406555




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (10917020): because after all there 's many people that go through their entire life without finding that special one with whom to feel identified complete loved secure protective

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):

MOST (11772696, 0.9205530285835266): «it 's so popular i almost wanted to have a look myself just to see what was so attractive about it»

MEDIAN (5849452, 0.00013646483421325684): «when up on bail he jumps and heads to mexico city»

LEAST (818850, -0.9219223260879517): «ah then he has been losing heavily again m afraid so»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'brows' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
2020-09-19 15:57:02,982 : INFO : precomputing L2-norms of word weight vectors
     1. 0.98 'eyebrows'
     2. 0.95 'forehead'
     3. 0.94 'brow'
     4. 0.93 'finger-tips'
     5. 0.93 'eyelashes'
     6. 0.93 'eyelids'
     7. 0.92 'fingertips'


[+] target_word: 'faithfully' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.94 'privately'
     2. 0.92 'wisely'
     3. 0.90 'charitably'
     4. 0.89 'conscientiously'
     5. 0.88 'graciously'
     6. 0.87 'kilcullen'
     7. 0.87 'penwether'


[+] target_word: 'searched' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.94 'laid'
     2. 0.93 'gathered'
     3. 0.93 'rummaged'
     4. 0.92 'tied'
     5. 0.91 'ensconced'
     6. 0.91 'standing'
     7. 0.91 'chalked'


[+] target_word: 'sarcastic' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.97 'deadpan'
     2. 0.96 'playful'
     3. 0.96 'acerbic'
     4. 0.96 'sardonic'
     5. 0.96 'self-deprecating'
     6. 0.95 'flippant'
     7. 0.95 'snarky'


[+] target_word: 'lately' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.90 'we�re'
     2. 0.87 'infrequently'
     3. 0.87 'weren�t'
     4. 0.87 'infact'
     5. 0.86 'though'
     6. 0.85 'yet'
     7. 0.85 'they�re'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-19 15:57:03,539 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-19 15:57:03,850 : INFO : capital-common-countries: 9.9% (50/506)
2020-09-19 15:57:05,053 : INFO : capital-world: 5.0% (96/1929)
2020-09-19 15:57:05,227 : INFO : currency: 2.5% (6/236)
2020-09-19 15:57:06,730 : INFO : city-in-state: 1.9% (44/2330)
2020-09-19 15:57:07,068 : INFO : family: 39.8% (167/420)
2020-09-19 15:57:07,759 : INFO : gram1-adjective-to-adverb: 3.4% (34/992)
2020-09-19 15:57:08,299 : INFO : gram2-opposite: 7.0% (49/702)
2020-09-19 15:57:09,154 : INFO : gram3-comparative: 25.8% (343/1332)
2020-09-19 15:57:09,912 : INFO : gram4-superlative: 12.5% (132/1056)
2020-09-19 15:57:10,560 : INFO : gram5-present-participle: 16.8% (177/1056)
2020-09-19 15:57:11,593 : INFO : gram6-nationality-adjective: 18.8% (258/1371)
2020-09-19 15:57:12,649 : INFO : gram7-past-tense: 26.9% (419/1560)
2020-09-19 15:57:13,612 : INFO : gram8-plural: 13.0% (173/1332)
2020-09-19 15:57:14,246 : INFO : gram9-plural-verbs: 11.3% (98/870)
2020-09-19 15:57:14,247 : INFO : Quadruplets with out-of-vocabulary words: 19.7%
2020-09-19 15:57:14,247 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-19 15:57:14,248 : INFO : Total accuracy: 13.0% (2046/15692)
Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10): 13.04% correct (2046 of 15692)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-19 15:57:14,531 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5273
2020-09-19 15:57:14,531 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5069
2020-09-19 15:57:14,531 : INFO : Pairs with unknown words ratio: 0.6%
((0.5273358470453476, 1.6255195689762857e-26), SpearmanrResult(correlation=0.5069037688375797, pvalue=2.595881750746791e-24), 0.56657223796034)


02 - simlex999
2020-09-19 15:57:14,589 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3227
2020-09-19 15:57:14,589 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2794
2020-09-19 15:57:14,589 : INFO : Pairs with unknown words ratio: 0.3%
((0.32270978137540923, 1.424355519616876e-25), SpearmanrResult(correlation=0.27936311830306254, pvalue=2.588133576674824e-19), 0.3003003003003003)


03 - simverb3500
2020-09-19 15:57:14,875 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1829
2020-09-19 15:57:14,875 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1661
2020-09-19 15:57:14,875 : INFO : Pairs with unknown words ratio: 0.7%
((0.18286915578195193, 1.6683460337571613e-27), SpearmanrResult(correlation=0.1661395670467296, pvalue=6.365832190183668e-23), 0.7428571428571429)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
