# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=15, negative=10, window=2, min_count=20, sample=0.0001,
    dm=1, dm_concat=1, hs=0, epochs=5
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'thefinal'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n10,w2,mc20,s0.0001,t5)
Save model to: models/dmc_d15_n10_w2_mc20_s0001_ech05_thefinal.bin
2020-09-10 14:09:47,868 : INFO : saving Doc2Vec object under models/dmc_d15_n10_w2_mc20_s0001_ech05_thefinal.bin, separately None
2020-09-10 14:09:47,868 : INFO : storing np array 'syn1neg' to models/dmc_d15_n10_w2_mc20_s0001_ech05_thefinal.bin.trainables.syn1neg.npy
2020-09-10 14:09:47,890 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n10_w2_mc20_s0001_ech05_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-10 14:09:47,912 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n10_w2_mc20_s0001_ech05_thefinal.bin.docvecs.vectors_docs.npy
2020-09-10 14:09:48,450 : INFO : saved models/dmc_d15_n10_w2_mc20_s0001_ech05_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 741680
[+] ... "the arab was a swarthy sinewy man of forty with all his fibres indurated and worked down to the whip-cord meagreness and rigidity of a racer his frame presenting a perfect picture of the sort of being one would fancy suited to the exhausting motion of a dromedary and to the fare of a desert"
2020-09-10 14:09:48,459 : INFO : precomputing L2-norms of doc weight vectors
[(5028179, 0.9454492926597595), (12158562, 0.937739908695221), (2867818, 0.9325440526008606), (4590629, 0.928946852684021), (10039922, 0.9225900769233704)]


.....get random document, tag: 11088088
[+] ... "i could tell she vaguely remembered that then she said oh yeah i do remember that she asked me how long i have been working there i told her 17 years but normally i am at the dearborn heights store"
[(9555852, 0.9240376949310303), (822143, 0.9199677109718323), (3926389, 0.9197108745574951), (12788099, 0.9193369150161743), (10351368, 0.9134886264801025)]


.....get random document, tag: 9765965
[+] ... "11 76% of the population are hispanic or latino of any race"
[(11753021, 0.9309331774711609), (6028000, 0.930891752243042), (3869103, 0.9287329912185669), (7075568, 0.915237307548523), (12389383, 0.9102058410644531)]


.....get random document, tag: 11708592
[+] ... "perhaps together in that spirit i present a very disturbing top 5 list of other things he meant to say"
[(4319735, 0.9464144706726074), (4581187, 0.9386663436889648), (2877980, 0.9330847263336182), (12640349, 0.9170839786529541), (8387668, 0.9152994155883789)]


.....get random document, tag: 3444591
[+] ... "as many as walk according to this rule what rule the rule by which men are proved new creatures the word of faith and the moral precept"
[(8799980, 0.9449304342269897), (1436047, 0.9342060685157776), (760034, 0.9340985417366028), (6615412, 0.9316697716712952), (10393078, 0.9301645755767822)]


.....get random document, tag: 9057709
[+] ... "the first usaf phantoms in vietnam were f-4cs from 555th tactical fighter squadron triple nickel which arrived in december 1964"
[(1528124, 0.9462746977806091), (4371942, 0.9393647313117981), (10224695, 0.9363200664520264), (3137086, 0.934279203414917), (12854929, 0.9333138465881348)]


.....get random document, tag: 9608604
[+] ... "according to the united states census bureau the city has a total area of 25 0 km² 9 6 mi²"
[(4039415, 0.9263696670532227), (11755887, 0.9138906002044678), (3073875, 0.9031921625137329), (11013340, 0.9031252861022949), (10532659, 0.8980228900909424)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (3126491): so i was introduced to miss penclosa and it did not escape me that as my name was mentioned she glanced across at agatha

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n10,w2,mc20,s0.0001,t5):

MOST (11837712, 0.9469075202941895): «in any event it took another decade or so before katarina took to actually using her legal name and there are still scads of people who call her cathy»

MEDIAN (7305114, -0.004035241901874542): «for example if we have a state consisting of a single variable formula 37 we could define this in vdm-sl as»

LEAST (9655528, -0.9420806765556335): «professor masuyama and assistants will teach the statistical control of quality in the afternoon»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'rehabilitation' model: Doc2Vec(dm/c,d15,n10,w2,mc20,s0.0001,t5) similar words:
2020-09-10 14:10:15,811 : INFO : precomputing L2-norms of word weight vectors
     1. 0.92 'divestment'
     2. 0.92 'overspending'
     3. 0.92 'preparedness'
     4. 0.91 'protection'
     5. 0.91 'procurement'
     6. 0.91 'mobilization'
     7. 0.90 'self-management'
     8. 0.90 'liquidation'
     9. 0.90 'torts'
     10. 0.90 'aid'
     11. 0.90 'sterilization'
     12. 0.89 'resuscitation'
     13. 0.89 'exchange'
     14. 0.89 'expropriation'
     15. 0.89 'health'
     16. 0.89 'bailout'
     17. 0.89 'appropriation'
     18. 0.89 'rescheduling'
     19. 0.89 'revaluation'
     20. 0.89 'financing'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-10 14:10:16,394 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-10 14:10:17,183 : INFO : capital-common-countries: 7.5% (38/506)
2020-09-10 14:10:24,143 : INFO : capital-world: 2.3% (88/3847)
2020-09-10 14:10:25,102 : INFO : currency: 1.3% (6/458)
2020-09-10 14:10:28,900 : INFO : city-in-state: 1.5% (37/2467)
2020-09-10 14:10:29,901 : INFO : family: 33.2% (168/506)
2020-09-10 14:10:31,663 : INFO : gram1-adjective-to-adverb: 3.8% (38/992)
2020-09-10 14:10:33,218 : INFO : gram2-opposite: 4.4% (36/812)
2020-09-10 14:10:35,605 : INFO : gram3-comparative: 23.1% (308/1332)
2020-09-10 14:10:37,436 : INFO : gram4-superlative: 9.7% (109/1122)
2020-09-10 14:10:38,907 : INFO : gram5-present-participle: 15.7% (166/1056)
2020-09-10 14:10:41,106 : INFO : gram6-nationality-adjective: 5.9% (90/1521)
2020-09-10 14:10:43,781 : INFO : gram7-past-tense: 19.9% (310/1560)
2020-09-10 14:10:46,039 : INFO : gram8-plural: 13.8% (184/1332)
2020-09-10 14:10:47,607 : INFO : gram9-plural-verbs: 8.5% (74/870)
2020-09-10 14:10:47,608 : INFO : Quadruplets with out-of-vocabulary words: 6.0%
2020-09-10 14:10:47,608 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-10 14:10:47,608 : INFO : Total accuracy: 9.0% (1652/18381)
Doc2Vec(dm/c,d15,n10,w2,mc20,s0.0001,t5): 8.99% correct (1652 of 18381)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-10 14:10:47,992 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4958
2020-09-10 14:10:47,992 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4844
2020-09-10 14:10:47,992 : INFO : Pairs with unknown words ratio: 0.0%
((0.4958463297317888, 2.644809303043867e-23), SpearmanrResult(correlation=0.4844162345454865, pvalue=3.6005939498788866e-22), 0.0)


02 - simlex999
2020-09-10 14:10:48,619 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3253
2020-09-10 14:10:48,620 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2782
2020-09-10 14:10:48,620 : INFO : Pairs with unknown words ratio: 0.2%
((0.3252860364230067, 5.28608857050929e-26), SpearmanrResult(correlation=0.2781536235271534, pvalue=3.5886842944569157e-19), 0.20020020020020018)


03 - simverb3500
2020-09-10 14:10:49,022 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1731
2020-09-10 14:10:49,022 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1600
2020-09-10 14:10:49,022 : INFO : Pairs with unknown words ratio: 0.1%
((0.17312791156844387, 6.105692176431344e-25), SpearmanrResult(correlation=0.1600144976423921, pvalue=1.7002149938790187e-21), 0.05714285714285715)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
