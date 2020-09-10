# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=15, negative=4, window=2, min_count=20, sample=0.0001,
    dm=1, dm_concat=1, hs=0, epochs=12
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'thefinal'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n4,w2,mc20,s0.0001,t10)
Save model to: models/dmc_d15_n4_w2_mc20_s0001_ech12_thefinal.bin
2020-09-10 11:40:34,749 : INFO : saving Doc2Vec object under models/dmc_d15_n4_w2_mc20_s0001_ech12_thefinal.bin, separately None
2020-09-10 11:40:34,749 : INFO : storing np array 'syn1neg' to models/dmc_d15_n4_w2_mc20_s0001_ech12_thefinal.bin.trainables.syn1neg.npy
2020-09-10 11:40:34,775 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n4_w2_mc20_s0001_ech12_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-10 11:40:34,796 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n4_w2_mc20_s0001_ech12_thefinal.bin.docvecs.vectors_docs.npy
2020-09-10 11:40:35,300 : INFO : saved models/dmc_d15_n4_w2_mc20_s0001_ech12_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 1789765
[+] ... "we do not want to harm you if you will leave us alone but we have guns enough to blow a whole fleet out of water and will use them if we are driven to it thank you for your warning a voice shouted back from the boats and then an order was given and they rowed back to the ships"
2020-09-10 11:40:35,312 : INFO : precomputing L2-norms of doc weight vectors
[(2437443, 0.9227359890937805), (11662842, 0.9223897457122803), (11662669, 0.9210842847824097), (9818898, 0.9197491407394409), (5338295, 0.9190889000892639)]


.....get random document, tag: 8002243
[+] ... "its loss gave the persians control as far as the isthmus of corinth and the opportunity to sack athens"
[(2527638, 0.9342809915542603), (5465526, 0.9330708980560303), (2717479, 0.9325765371322632), (12555886, 0.9294513463973999), (100624, 0.9290505051612854)]


.....get random document, tag: 10426836
[+] ... "so their alarm went into sleep mode which meant no email reminding them to do their reports no emails sending information no phone call reminders no post it reminders no nothing simply i was not here but i was but i acted as if i wasn’t get it"
[(12764765, 0.9365453720092773), (10426836, 0.9215483069419861), (316334, 0.9213671088218689), (7661820, 0.9198648929595947), (1946461, 0.9195173978805542)]


.....get random document, tag: 3124129
[+] ... "if my turn comes again sahib i will not hang you nor cut your throat ' thank you said the subaltern gravely as he looked along the line of guns that could pound the city to powder in half an hour"
[(6478310, 0.931425154209137), (12332096, 0.9129136800765991), (11778316, 0.912711501121521), (9321836, 0.9106304049491882), (7933474, 0.9094534516334534)]


.....get random document, tag: 6827457
[+] ... "the universal powerline association upa aligns industry leaders in the global powerline communications plc market and covers all markets and both access and an in-home plc technology to ensure a level playing field for the deployment of interoperable and coexisting plc products to the benefit of consumer’s worldwide"
[(12212877, 0.9426183700561523), (9387883, 0.9411211013793945), (10822489, 0.934417724609375), (9387055, 0.9335635900497437), (5982952, 0.9280893802642822)]


.....get random document, tag: 8566238
[+] ... "the next 16 bits is the length of the packet"
[(9693831, 0.9490801095962524), (4229187, 0.9392130374908447), (3233913, 0.9232543110847473), (11756038, 0.9164950847625732), (1463821, 0.9153333306312561)]


.....get random document, tag: 8590733
[+] ... "the reformation made the region around montreux and vevey an attractive haven for huguenots from italy who brought their artisanal skills and set up workshops and businesses"
[(2963936, 0.9507102966308594), (6751464, 0.9400808811187744), (1369051, 0.9263091087341309), (4571304, 0.926095724105835), (1425002, 0.925060510635376)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (428888): could afford me upon the topic in question but i felt they would be entirely sufficient

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n4,w2,mc20,s0.0001,t10):

MOST (4562064, 0.9202669858932495): «they owned now that a person interested with them had been out to look at the property and that they were satisfied with the appearance of things»

MEDIAN (7314842, 0.001440286636352539): «evolution represents a genealogy of regimes that come into existence through adoption by populations of economic agents»

LEAST (202947, -0.9367072582244873): «as he neared the bridge he reduced the speed of the car to fifteen miles an hour and set the hand throttle to hold it there»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'marquise' model: Doc2Vec(dm/c,d15,n4,w2,mc20,s0.0001,t10) similar words:
2020-09-10 11:41:00,310 : INFO : precomputing L2-norms of word weight vectors
     1. 0.97 'duchesse'
     2. 0.96 'darrien'
     3. 0.95 'comtesse'
     4. 0.95 'barère'
     5. 0.94 'kaku'
     6. 0.94 'santini'
     7. 0.93 'bracy'
     8. 0.93 'valentina'
     9. 0.93 'antoinette'
     10. 0.93 'rondel'
     11. 0.93 'theresa'
     12. 0.93 'bellegarde'
     13. 0.93 'vicomte'
     14. 0.93 'conrad'
     15. 0.92 'dellius'
     16. 0.92 'malpertuis'
     17. 0.92 'arana'
     18. 0.92 'berthier'
     19. 0.92 'ignacio'
     20. 0.92 'lackland'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-10 11:41:00,851 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-10 11:41:01,525 : INFO : capital-common-countries: 6.5% (33/506)
2020-09-10 11:41:07,025 : INFO : capital-world: 1.9% (75/3847)
2020-09-10 11:41:07,688 : INFO : currency: 0.7% (3/458)
2020-09-10 11:41:11,111 : INFO : city-in-state: 1.0% (25/2467)
2020-09-10 11:41:11,926 : INFO : family: 26.1% (132/506)
2020-09-10 11:41:13,380 : INFO : gram1-adjective-to-adverb: 2.3% (23/992)
2020-09-10 11:41:14,535 : INFO : gram2-opposite: 4.2% (34/812)
2020-09-10 11:41:16,401 : INFO : gram3-comparative: 24.0% (320/1332)
2020-09-10 11:41:17,879 : INFO : gram4-superlative: 12.9% (145/1122)
2020-09-10 11:41:19,180 : INFO : gram5-present-participle: 13.4% (141/1056)
2020-09-10 11:41:20,838 : INFO : gram6-nationality-adjective: 9.6% (146/1521)
2020-09-10 11:41:23,209 : INFO : gram7-past-tense: 16.5% (257/1560)
2020-09-10 11:41:25,269 : INFO : gram8-plural: 12.2% (162/1332)
2020-09-10 11:41:26,539 : INFO : gram9-plural-verbs: 9.1% (79/870)
2020-09-10 11:41:26,539 : INFO : Quadruplets with out-of-vocabulary words: 6.0%
2020-09-10 11:41:26,540 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-10 11:41:26,540 : INFO : Total accuracy: 8.6% (1575/18381)
Doc2Vec(dm/c,d15,n4,w2,mc20,s0.0001,t10): 8.57% correct (1575 of 18381)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-10 11:41:26,912 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4830
2020-09-10 11:41:26,912 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4703
2020-09-10 11:41:26,912 : INFO : Pairs with unknown words ratio: 0.0%
((0.4830456306046067, 4.892334476319268e-22), SpearmanrResult(correlation=0.47027951323131184, pvalue=7.966774435256134e-21), 0.0)


02 - simlex999
2020-09-10 11:41:27,501 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3179
2020-09-10 11:41:27,501 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2718
2020-09-10 11:41:27,501 : INFO : Pairs with unknown words ratio: 0.2%
((0.31793065762692646, 7.465140693439743e-25), SpearmanrResult(correlation=0.27175099785817836, pvalue=2.441937875148342e-18), 0.20020020020020018)


03 - simverb3500
2020-09-10 11:41:27,883 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1828
2020-09-10 11:41:27,883 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1681
2020-09-10 11:41:27,883 : INFO : Pairs with unknown words ratio: 0.1%
((0.18277484326928264, 1.1772228976985905e-27), SpearmanrResult(correlation=0.16814670362850578, pvalue=1.3409314589006894e-23), 0.05714285714285715)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
