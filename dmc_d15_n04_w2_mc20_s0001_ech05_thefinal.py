# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=15, negative=4, window=2, min_count=20, sample=0.0001,
    dm=1, dm_concat=1, hs=0, epochs=5
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'thefinal'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n4,w2,mc20,s0.0001,t10)
Save model to: models/dmc_d15_n4_w2_mc20_s0001_ech05_thefinal.bin
2020-09-09 23:42:50,848 : INFO : saving Doc2Vec object under models/dmc_d15_n4_w2_mc20_s0001_ech05_thefinal.bin, separately None
2020-09-09 23:42:50,848 : INFO : storing np array 'syn1neg' to models/dmc_d15_n4_w2_mc20_s0001_ech05_thefinal.bin.trainables.syn1neg.npy
2020-09-09 23:42:50,872 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n4_w2_mc20_s0001_ech05_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-09 23:42:50,897 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n4_w2_mc20_s0001_ech05_thefinal.bin.docvecs.vectors_docs.npy
2020-09-09 23:42:51,423 : INFO : saved models/dmc_d15_n4_w2_mc20_s0001_ech05_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 2114711
[+] ... "beware i am here for death and life take up thy long-fanged sathanas said the voice or i will conjure him with a bolt from my arblast at the same time was heard the sound of a spring or check as when a crossbow is bent"
2020-09-09 23:42:51,432 : INFO : precomputing L2-norms of doc weight vectors
[(13268648, 0.9377913475036621), (3180037, 0.9346758723258972), (7119657, 0.9328857660293579), (5541209, 0.925058126449585), (12823910, 0.9247540235519409)]


.....get random document, tag: 11882604
[+] ... "tofu also is available in a silken form which is used for desserts sauces or flans"
[(2548009, 0.9384892582893372), (3709659, 0.937356173992157), (7737457, 0.9155327677726746), (8359979, 0.9140442609786987), (7288894, 0.9080686569213867)]


.....get random document, tag: 7429093
[+] ... "the average household size is 2 09 and the average family size is 2 58"
[(5774421, 0.9399994611740112), (4612904, 0.9321809411048889), (6011290, 0.9309190511703491), (10496492, 0.9282371997833252), (11798743, 0.9242072701454163)]


.....get random document, tag: 8724276
[+] ... "the montessori method is described as a way of thinking about who children are"
[(299894, 0.9264805316925049), (5364967, 0.9148910045623779), (7728313, 0.9091639518737793), (10156884, 0.9063040614128113), (4687745, 0.9014256596565247)]


.....get random document, tag: 7986210
[+] ... "on march 30 1806 napoleon i of france declared ferdinand deposed again and replaced him with his own brother joseph bonaparte"
[(8030190, 0.9190830588340759), (10245531, 0.916736900806427), (10463580, 0.9134662747383118), (9207810, 0.9123257994651794), (8897906, 0.9025651216506958)]


.....get random document, tag: 5308338
[+] ... "sometimes the present writer appears as its substitute sometimes the modest author adopts the style of royalty swelling and multiplying himself into we and sometimes to escape the egotistic phrases of in my opinion or as i think he utters dogmas and positively asserts exempli gratia it is a work which etc you deem me inconsistent because having written in praise of the metaphysician i afterwards appear to condemn the essay on political justice"
[(11841190, 0.9449491500854492), (5127939, 0.9438984394073486), (11379648, 0.9359697103500366), (12526462, 0.9354590177536011), (12353168, 0.9338769912719727)]


.....get random document, tag: 11902522
[+] ... "did not i tell you that i was royalty reborn - cheers"
[(4725389, 0.9696727395057678), (9469275, 0.9475998282432556), (10454440, 0.9449492692947388), (9476264, 0.9419791102409363), (11464490, 0.9401870965957642)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (4371524): festus derriman with all his money is nothing to us at all ' but said anne what has made you change all of a sudden from what you have said before amy feelings and my reason which i am thankful for ' anne knew that her mother 's sentiments were naturally so versatile that they could not be depended on for two days together but it did not occur to her for the moment that a change had been helped on in the present case by a romantic talk between mrs

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n4,w2,mc20,s0.0001,t10):

MOST (4937651, 0.9257211685180664): «harrod but to the public that will be the chief difference and if she does not like her service she will be able to criticize and remedy it just as one can now criticize and remedy any inefficiency in one 's local post-office»

MEDIAN (2747848, -0.009692326188087463): «i can not face mother without you she will be glad enough to get you»

LEAST (7701472, -0.944881021976471): «23 3% of all households are made up of individuals and 1 4% have someone living alone who is 65 years of age or older»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'delirious' model: Doc2Vec(dm/c,d15,n4,w2,mc20,s0.0001,t10) similar words:
2020-09-09 23:43:16,660 : INFO : precomputing L2-norms of word weight vectors
     1. 0.93 'lethargic'
     2. 0.92 'hung-over'
     3. 0.92 'depressed'
     4. 0.92 'unbearable'
     5. 0.92 'feverish'
     6. 0.92 'wakeful'
     7. 0.91 'restless'
     8. 0.91 'stupefied'
     9. 0.91 'fitful'
     10. 0.91 'heart-sick'
     11. 0.91 'light-headed'
     12. 0.91 'sullen'
     13. 0.90 'angrier'
     14. 0.90 'queasy'
     15. 0.90 'torpid'
     16. 0.90 'directionless'
     17. 0.90 'stifled'
     18. 0.89 'bloodier'
     19. 0.89 'unendurable'
     20. 0.89 'remorseful'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-09 23:43:17,270 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-09 23:43:17,984 : INFO : capital-common-countries: 6.7% (34/506)
2020-09-09 23:43:23,905 : INFO : capital-world: 2.2% (83/3847)
2020-09-09 23:43:24,574 : INFO : currency: 0.7% (3/458)
2020-09-09 23:43:27,821 : INFO : city-in-state: 1.2% (29/2467)
2020-09-09 23:43:28,628 : INFO : family: 29.2% (148/506)
2020-09-09 23:43:30,036 : INFO : gram1-adjective-to-adverb: 3.7% (37/992)
2020-09-09 23:43:31,179 : INFO : gram2-opposite: 3.7% (30/812)
2020-09-09 23:43:33,006 : INFO : gram3-comparative: 24.9% (332/1332)
2020-09-09 23:43:34,359 : INFO : gram4-superlative: 9.4% (105/1122)
2020-09-09 23:43:35,730 : INFO : gram5-present-participle: 16.6% (175/1056)
2020-09-09 23:43:37,526 : INFO : gram6-nationality-adjective: 7.6% (116/1521)
2020-09-09 23:43:39,905 : INFO : gram7-past-tense: 19.5% (304/1560)
2020-09-09 23:43:41,967 : INFO : gram8-plural: 13.2% (176/1332)
2020-09-09 23:43:43,247 : INFO : gram9-plural-verbs: 6.3% (55/870)
2020-09-09 23:43:43,248 : INFO : Quadruplets with out-of-vocabulary words: 6.0%
2020-09-09 23:43:43,248 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-09 23:43:43,248 : INFO : Total accuracy: 8.9% (1627/18381)
Doc2Vec(dm/c,d15,n4,w2,mc20,s0.0001,t10): 8.85% correct (1627 of 18381)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-09 23:43:43,620 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4882
2020-09-09 23:43:43,620 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4739
2020-09-09 23:43:43,621 : INFO : Pairs with unknown words ratio: 0.0%
((0.4882335478810148, 1.5218884857356285e-22), SpearmanrResult(correlation=0.4739005850982895, pvalue=3.6535107707457805e-21), 0.0)


02 - simlex999
2020-09-09 23:43:44,206 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3137
2020-09-09 23:43:44,206 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2671
2020-09-09 23:43:44,206 : INFO : Pairs with unknown words ratio: 0.2%
((0.31372057905512485, 3.288162714773185e-24), SpearmanrResult(correlation=0.2671467089398764, pvalue=9.398023990486174e-18), 0.20020020020020018)


03 - simverb3500
2020-09-09 23:43:44,586 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1714
2020-09-09 23:43:44,586 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1590
2020-09-09 23:43:44,586 : INFO : Pairs with unknown words ratio: 0.1%
((0.1713924331249961, 1.810549722467829e-24), SpearmanrResult(correlation=0.15904618812567953, pvalue=2.976779118543953e-21), 0.05714285714285715)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
