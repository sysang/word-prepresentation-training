# coding: utf-8
# import doc2vec_training_script_rabbitmq_connect as base
import doc2vec_training_script_mongodb_connect as base

common_kwargs = dict(
    vector_size=15, negative=4, window=2, min_count=23, sample=0.005,
    dm=1, dm_concat=1, hs=0, epochs=5
)

print("kwargs: %s" % (str(common_kwargs)))
saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'thefinal'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n4,w2,mc23,s0.005,t8)
Save model to: models/dmc_d15_n4_w2_mc23_s005_ech05_thefinal.bin
2020-09-12 21:40:22,803 : INFO : saving Doc2Vec object under models/dmc_d15_n4_w2_mc23_s005_ech05_thefinal.bin, separately None
2020-09-12 21:40:22,804 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n4_w2_mc23_s005_ech05_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-12 21:40:22,833 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n4_w2_mc23_s005_ech05_thefinal.bin.docvecs.vectors_docs.npy
2020-09-12 21:40:23,572 : INFO : saved models/dmc_d15_n4_w2_mc23_s005_ech05_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 1665320
[+] ... "tempelhof 's account of these two people and their underground wrestle here is really curious reading clear as daylight to those that will study but of endless expansion as usual in tempelhof and fit only to be indicated here"
2020-09-12 21:40:23,585 : INFO : precomputing L2-norms of doc weight vectors
[(643458, 0.9202306270599365), (11362596, 0.9158936738967896), (6031188, 0.9148982167243958), (8860059, 0.9140604734420776), (11181519, 0.9137141704559326), (9326656, 0.9132027626037598), (2919279, 0.9122188687324524), (4806841, 0.9120038747787476), (5239711, 0.9106546640396118), (11798861, 0.9071406126022339)]


.....get random document, tag: 5947304
[+] ... "stefan 's job is a heroin delivery from germany to sweden which should go easily"
[(3590277, 0.9263380765914917), (1748228, 0.9257031679153442), (5462941, 0.914707362651825), (4792021, 0.912186324596405), (2669920, 0.9120613932609558), (7299818, 0.9111981391906738), (12548995, 0.9058766961097717), (11883422, 0.9003767371177673), (657930, 0.8984774351119995), (8415832, 0.897474467754364)]


.....get random document, tag: 3327748
[+] ... "this manoeuvre excited disagreeable suspicions in the minds of several on board for the lawless character of their pilot had been more than suspected in the course of their short acquaintance and the coast towards which they were furiously rushing known to be iron-bound and in such a gale fatal to all who came rudely upon its rocks"
[(1731545, 0.9565012454986572), (8407132, 0.9459700584411621), (11218490, 0.9399029612541199), (5575134, 0.9344833493232727), (3283256, 0.9331061840057373), (4333922, 0.9287392497062683), (2329684, 0.9261744618415833), (6683941, 0.9253013730049133), (4886419, 0.9246333837509155), (2443752, 0.9230644702911377)]


.....get random document, tag: 11639298
[+] ... "they are seemingly posting every image the rovers capture and are even including screenshots to show the controller-eye view of the rollout on mars"
[(10725806, 0.9411671757698059), (13262902, 0.9195100665092468), (8642079, 0.9030346870422363), (3068403, 0.8987158536911011), (6118677, 0.8980660438537598), (1152818, 0.8920188546180725), (10934744, 0.8905899524688721), (9968617, 0.8891111612319946), (847414, 0.8876539468765259), (7500146, 0.8874019384384155)]


.....get random document, tag: 12618966
[+] ... "shift who i think are out of business again ran an article on youth political apathy back in april"
[(7789017, 0.9189779758453369), (3668805, 0.911986768245697), (11495283, 0.9103438258171082), (548639, 0.9092570543289185), (10469469, 0.9015161991119385), (10065638, 0.8990182876586914), (3827736, 0.8968495726585388), (11392359, 0.894826352596283), (2382958, 0.8938670754432678), (8063259, 0.8918014764785767)]


.....get random document, tag: 6009967
[+] ... "when he decides to play olivia newton john in a local talent show for whom he is very passionate gary 's actions show that he is at odds with the conservative social environment in which he lives"
[(11227092, 0.9270994663238525), (5223212, 0.9213128089904785), (4024793, 0.9197973012924194), (4611238, 0.9180179834365845), (12272078, 0.9133660793304443), (1542794, 0.9123613238334656), (6231644, 0.9121387004852295), (1169271, 0.9102405309677124), (10620509, 0.9061201214790344), (9946528, 0.9042336940765381)]


.....get random document, tag: 7322073
[+] ... "beachwood has one of the highest estate tax distribution in the state 1998-2003 receiving over $16 000 000"
[(2479105, 0.9513025283813477), (5424885, 0.9322566390037537), (6990602, 0.9246989488601685), (10421176, 0.9238943457603455), (6938521, 0.9220954179763794), (4281589, 0.9215434193611145), (1367090, 0.9193768501281738), (5692633, 0.9171366691589355), (9500425, 0.9159146547317505), (1371082, 0.9131767153739929)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (11699650): generally i do not bother to argue with people who say they are doing what they do because god told them to

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n4,w2,mc23,s0.005,t8):

MOST (11785614, 0.9327507615089417): «i have just been messing around killing people and stealing cars crashing the cars is more like it»

MEDIAN (11483576, 0.001318756490945816): «i sat there -naked- on my bed with a paper towel beneath sal to cushion his fall»

LEAST (3911124, -0.919641375541687): «miss eliza grogworthy now tom i know you are joking why can not you be serious i am as serious as were that couple»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'penn' model: Doc2Vec(dm/c,d15,n4,w2,mc23,s0.005,t8) similar words:
2020-09-12 21:40:50,085 : INFO : precomputing L2-norms of word weight vectors
     1. 0.97 'stoughton'
     2. 0.97 'donner'
     3. 0.96 'marriott'
     4. 0.96 'carleton'
     5. 0.96 'callaway'
     6. 0.96 'wolfson'
     7. 0.96 'calder'
target_word: 'grapes' model: Doc2Vec(dm/c,d15,n4,w2,mc23,s0.005,t8) similar words:
     1. 0.97 'beads'
     2. 0.97 'pearls'
     3. 0.97 'flocks'
     4. 0.97 'serpents'
     5. 0.97 'snakes'
     6. 0.97 'vines'
     7. 0.97 'antlers'
target_word: 'file' model: Doc2Vec(dm/c,d15,n4,w2,mc23,s0.005,t8) similar words:
     1. 0.97 'config'
     2. 0.96 'folder'
     3. 0.96 'interface'
     4. 0.96 'header'
     5. 0.96 'firmware'
     6. 0.95 'firewall'
     7. 0.95 'browser'
target_word: 'washington' model: Doc2Vec(dm/c,d15,n4,w2,mc23,s0.005,t8) similar words:
     1. 0.97 'nebraska'
     2. 0.97 'georgetown'
     3. 0.97 'birmingham'
     4. 0.96 'princeton'
     5. 0.96 'truro'
     6. 0.96 'brampton'
     7. 0.96 'montreal'
target_word: '1500' model: Doc2Vec(dm/c,d15,n4,w2,mc23,s0.005,t8) similar words:
     1. 0.98 '12-15'
     2. 0.97 '1200'
     3. 0.97 '1400'
     4. 0.97 '1100'
     5. 0.97 '1300'
     6. 0.96 '7000'
     7. 0.96 '3500'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-12 21:40:51,917 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-12 21:40:52,645 : INFO : capital-common-countries: 2.6% (13/506)
2020-09-12 21:40:58,120 : INFO : capital-world: 1.0% (36/3773)
2020-09-12 21:40:58,794 : INFO : currency: 0.0% (0/458)
2020-09-12 21:41:02,494 : INFO : city-in-state: 1.1% (28/2467)
2020-09-12 21:41:03,249 : INFO : family: 27.7% (140/506)
2020-09-12 21:41:04,490 : INFO : gram1-adjective-to-adverb: 1.6% (16/992)
2020-09-12 21:41:05,637 : INFO : gram2-opposite: 1.0% (8/812)
2020-09-12 21:41:07,699 : INFO : gram3-comparative: 12.3% (164/1332)
2020-09-12 21:41:10,063 : INFO : gram4-superlative: 8.9% (100/1122)
2020-09-12 21:41:11,546 : INFO : gram5-present-participle: 4.5% (48/1056)
2020-09-12 21:41:13,782 : INFO : gram6-nationality-adjective: 3.2% (48/1521)
2020-09-12 21:41:15,840 : INFO : gram7-past-tense: 4.7% (73/1560)
2020-09-12 21:41:17,866 : INFO : gram8-plural: 3.8% (51/1332)
2020-09-12 21:41:18,848 : INFO : gram9-plural-verbs: 4.7% (41/870)
2020-09-12 21:41:18,849 : INFO : Quadruplets with out-of-vocabulary words: 6.3%
2020-09-12 21:41:18,849 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-12 21:41:18,849 : INFO : Total accuracy: 4.2% (766/18307)
Doc2Vec(dm/c,d15,n4,w2,mc23,s0.005,t8): 4.18% correct (766 of 18307)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-12 21:41:19,708 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3427
2020-09-12 21:41:19,708 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.3515
2020-09-12 21:41:19,708 : INFO : Pairs with unknown words ratio: 0.0%
((0.34272583383519406, 3.6436077511594926e-11), SpearmanrResult(correlation=0.35149018652361913, pvalue=1.0562149705068575e-11), 0.0)


02 - simlex999
2020-09-12 21:41:20,550 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2576
2020-09-12 21:41:20,550 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2293
2020-09-12 21:41:20,550 : INFO : Pairs with unknown words ratio: 0.2%
((0.2575887471096737, 1.4197162870943568e-16), SpearmanrResult(correlation=0.2293077125230963, pvalue=2.314373880474762e-13), 0.20020020020020018)


03 - simverb3500
2020-09-12 21:41:22,144 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1370
2020-09-12 21:41:22,144 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1377
2020-09-12 21:41:22,144 : INFO : Pairs with unknown words ratio: 0.1%
((0.13704470507415364, 3.923604926726144e-16), SpearmanrResult(correlation=0.13765069301659486, pvalue=2.9041859558779776e-16), 0.05714285714285715)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
