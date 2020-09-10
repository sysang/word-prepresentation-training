
# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=15, negative=4, window=2, min_count=23, sample=0.0001,
    dm=1, dm_concat=1, hs=0, epochs=5
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'thefinal'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n4,w2,mc23,s0.0001,t5)
Save model to: models/dmc_d15_n4_w2_mc23_s0001_ech05_thefinal.bin
2020-09-10 14:47:57,805 : INFO : saving Doc2Vec object under models/dmc_d15_n4_w2_mc23_s0001_ech05_thefinal.bin, separately None
2020-09-10 14:47:57,805 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n4_w2_mc23_s0001_ech05_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-10 14:47:57,833 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n4_w2_mc23_s0001_ech05_thefinal.bin.docvecs.vectors_docs.npy
2020-09-10 14:47:58,595 : INFO : saved models/dmc_d15_n4_w2_mc23_s0001_ech05_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 9740336
[+] ... "it covers approximately 539 km² 208 mi² of total area"
2020-09-10 14:47:58,604 : INFO : precomputing L2-norms of doc weight vectors
[(4430538, 0.9281601905822754), (86323, 0.9253445863723755), (6570375, 0.9188328981399536), (1334707, 0.917312502861023), (2246343, 0.9060484766960144)]


.....get random document, tag: 11119229
[+] ... "but having them both face the same way is so much easier they can both watch the dvd which means they both sit motionless and quiet for hours at a time"
[(4031834, 0.9281095862388611), (5446718, 0.9197700023651123), (353667, 0.9194077253341675), (2161942, 0.918820858001709), (6264164, 0.9092439413070679)]


.....get random document, tag: 10220854
[+] ... "as of the census of 2000 there are 601 people 144 households and 127 families residing in the cdp"
[(8021267, 0.9499750137329102), (7917328, 0.9414347410202026), (8519074, 0.9311469793319702), (9208661, 0.9276634454727173), (2908692, 0.9244360327720642)]


.....get random document, tag: 6428751
[+] ... "they sing their song in their first appearance in the film it seems almost to get out of the way"
[(13155113, 0.9363012313842773), (12499785, 0.927750289440155), (12240348, 0.9119596481323242), (1636350, 0.9108033776283264), (10763913, 0.9082059264183044)]


.....get random document, tag: 1860465
[+] ... "the hot controversy on this point is idle and without substance—the idlest controversies are always the hottest—for m60 not only was gordon the last man in all the world to hold himself bound by official instructions but the actual conditions of the case were too little known too shifting too unstable to permit of hard and fast directions beforehand how to solve so desperate a problem"
[(7984609, 0.9392044544219971), (32990, 0.9290211796760559), (5180005, 0.917944073677063), (2789027, 0.9170787930488586), (3663752, 0.9127861261367798)]


.....get random document, tag: 2016321
[+] ... "clemens ' he said nobody seems to have a very good word for you i hadn't referred him to people that i thought were going to whitewash me"
[(8802921, 0.9367828369140625), (10611238, 0.9309858083724976), (1806290, 0.9233275651931763), (5925267, 0.9198850393295288), (2361602, 0.9190340638160706)]


.....get random document, tag: 12354391
[+] ... "she has such a bubble gum voice compared to some of her lyrics"
[(8535738, 0.9224620461463928), (11663434, 0.9174883365631104), (6235767, 0.9113622903823853), (6221477, 0.9002491235733032), (9144168, 0.8998123407363892)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (3275372): you shall have your brother to-morrow if sir jasper can manage it

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n4,w2,mc23,s0.0001,t5):

MOST (2849522, 0.9419495463371277): «if it ever overcomes the strong feeling which exists against it this will only be after the establishment of a systematic national education by which the various grades of politically valuable acquirement may be accurately defined and authenticated»

MEDIAN (9190539, 0.0007985532283782959): «in the following years chicago architecture would become influential throughout the world»

LEAST (612389, -0.9439833760261536): «after having sailed far enough john verrazano discovered the coast of north america which he called a new land never before seen by any man ancient or modern he took possession of it in the name of his king and in order to settle the matter called the whole coast new france»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'millennium' model: Doc2Vec(dm/c,d15,n4,w2,mc23,s0.0001,t5) similar words:
2020-09-10 14:48:25,719 : INFO : precomputing L2-norms of word weight vectors
     1. 0.92 "'90's"
     2. 0.92 '1980’s'
     3. 0.91 '2004|'
     4. 0.91 'hegira'
     5. 0.91 'zu’l'
     6. 0.91 'millenium'
     7. 0.90 'late-1980s'
     8. 0.90 'gregorian'
     9. 0.89 'late-1990s'
     10. 0.89 '1650s'
     11. 0.88 'ides'
     12. 0.88 '1680s'
     13. 0.88 '1470s'
     14. 0.88 'bicentenary'
     15. 0.88 "'30's"
     16. 0.88 'carnaval'
     17. 0.88 'early-1990s'
     18. 0.88 "'60's"
     19. 0.87 "'50's"
     20. 0.87 'showa'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-10 14:48:26,275 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-10 14:48:27,017 : INFO : capital-common-countries: 6.7% (34/506)
2020-09-10 14:48:32,850 : INFO : capital-world: 2.1% (80/3773)
2020-09-10 14:48:33,539 : INFO : currency: 0.7% (3/458)
2020-09-10 14:48:36,976 : INFO : city-in-state: 1.3% (31/2467)
2020-09-10 14:48:37,769 : INFO : family: 28.5% (144/506)
2020-09-10 14:48:39,042 : INFO : gram1-adjective-to-adverb: 3.5% (35/992)
2020-09-10 14:48:40,145 : INFO : gram2-opposite: 4.7% (38/812)
2020-09-10 14:48:41,690 : INFO : gram3-comparative: 26.8% (357/1332)
2020-09-10 14:48:43,195 : INFO : gram4-superlative: 10.3% (116/1122)
2020-09-10 14:48:44,304 : INFO : gram5-present-participle: 18.0% (190/1056)
2020-09-10 14:48:46,698 : INFO : gram6-nationality-adjective: 7.2% (109/1521)
2020-09-10 14:48:48,886 : INFO : gram7-past-tense: 18.1% (283/1560)
2020-09-10 14:48:51,026 : INFO : gram8-plural: 12.7% (169/1332)
2020-09-10 14:48:52,212 : INFO : gram9-plural-verbs: 9.0% (78/870)
2020-09-10 14:48:52,214 : INFO : Quadruplets with out-of-vocabulary words: 6.3%
2020-09-10 14:48:52,215 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-10 14:48:52,216 : INFO : Total accuracy: 9.1% (1667/18307)
Doc2Vec(dm/c,d15,n4,w2,mc23,s0.0001,t5): 9.11% correct (1667 of 18307)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-10 14:48:52,595 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4834
2020-09-10 14:48:52,595 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4709
2020-09-10 14:48:52,595 : INFO : Pairs with unknown words ratio: 0.0%
((0.48336309557430307, 4.557540326652314e-22), SpearmanrResult(correlation=0.4709394524196053, pvalue=6.916355467223665e-21), 0.0)


02 - simlex999
2020-09-10 14:48:52,949 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3143
2020-09-10 14:48:52,949 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2689
2020-09-10 14:48:52,949 : INFO : Pairs with unknown words ratio: 0.2%
((0.314349442722748, 2.6389187630620733e-24), SpearmanrResult(correlation=0.2689163900491926, pvalue=5.6157821604084896e-18), 0.20020020020020018)


03 - simverb3500
2020-09-10 14:48:53,573 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1745
2020-09-10 14:48:53,573 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1623
2020-09-10 14:48:53,573 : INFO : Pairs with unknown words ratio: 0.1%
((0.17451425343274443, 2.5413438053918483e-25), SpearmanrResult(correlation=0.16232359131375973, pvalue=4.408619873157006e-22), 0.05714285714285715)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
