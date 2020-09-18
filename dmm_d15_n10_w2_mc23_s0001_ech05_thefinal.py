# coding: utf-8
# import doc2vec_training_script_mongodb_connect as base
import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15, negative=10, window=2, min_count=23, sample=0.0001,
        dm=1, dm_concat=0, hs=0, epochs=5
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    corpus = 'thefinal'

    base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/m,d15,n10,w2,mc23,s0.0001,t10)
Save model to: models/dmm_d15_n10_w2_mc23_s0001_ech05_thefinal.bin
2020-09-18 14:03:06,616 : INFO : saving Doc2Vec object under models/dmm_d15_n10_w2_mc23_s0001_ech05_thefinal.bin, separately None
2020-09-18 14:03:06,616 : INFO : storing np array 'vectors_docs_lockf' to models/dmm_d15_n10_w2_mc23_s0001_ech05_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-18 14:03:06,643 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n10_w2_mc23_s0001_ech05_thefinal.bin.docvecs.vectors_docs.npy
2020-09-18 14:03:07,175 : INFO : saved models/dmm_d15_n10_w2_mc23_s0001_ech05_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 8826212
[+] index 8826212 -> "maverick records is an record label owned by warner music group and distributed through warner bros"
2020-09-18 14:03:07,191 : INFO : precomputing L2-norms of doc weight vectors
!! No any match in top 100 similarities


.....get random document, tag: 6507183
[+] index 6507183 -> "contributing to the made-for-television feel is an extremely artificial production design on about the authenticity level of television 's the time tunnel"
!! No any match in top 100 similarities


.....get random document, tag: 13000435
[+] index 13000435 -> "they had one great starter in pettitte a bunch of veterans that won more than they lost but in most cases not much and a bullpen filled with blue collar guys who could shut down the other team"
** Matched with rank 10, score: 0.9031088352203369


.....get random document, tag: 2429883
[+] index 2429883 -> "he turned to leave the room and was met by mrs bones"
!! No any match in top 100 similarities


.....get random document, tag: 2631536
[+] index 2631536 -> "going to brazil and do mrs clare like the notion of such a journey she asked"
!! No any match in top 100 similarities


.....get random document, tag: 3689109
[+] index 3689109 -> "thereupon they brought him into a mosque where they promised him great store of money and preferments in case he would forsake the law of jesus christ and take up that of their prophet mahomet"
!! No any match in top 100 similarities


.....get random document, tag: 6190288
[+] index 6190288 -> "jackson would let his good name be associated with such a poor quality movie"
!! No any match in top 100 similarities




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (13208772): it 's sad but ya know that is not such a bad thing sometimes either

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/m,d15,n10,w2,mc23,s0.0001,t10):

MOST (10489127, 0.9887716770172119): «it is the same town he went to high school in incidentally»

MEDIAN (5592050, 0.6519376039505005): «suddenly we saw on the right bank the black silhouette of a house standing high and lone in its clearing and we made fast to a good landing-place an inclined plane of corduroy»

LEAST (10218749, -0.966805100440979): «as of the 2000 census the cdp had a total population of 9 325»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'actions' model: Doc2Vec(dm/m,d15,n10,w2,mc23,s0.0001,t10):
2020-09-18 14:03:31,720 : INFO : precomputing L2-norms of word weight vectors
     1. 0.95 'convictions'
     2. 0.94 'shortcomings'
     3. 0.94 'motives'
     4. 0.93 'objections'
     5. 0.93 'circumstances'
     6. 0.93 'stratagem'
     7. 0.93 'arguments'


[+] target_word: 'passage' model: Doc2Vec(dm/m,d15,n10,w2,mc23,s0.0001,t10):
     1. 0.89 'line'
     2. 0.88 'vacancy'
     3. 0.88 'threshold'
     4. 0.87 'steps'
     5. 0.87 'entrance'
     6. 0.86 'space'
     7. 0.85 'premises'


[+] target_word: 'pumping' model: Doc2Vec(dm/m,d15,n10,w2,mc23,s0.0001,t10):
     1. 0.92 'leaking'
     2. 0.92 'pumped'
     3. 0.89 'cutting'
     4. 0.89 'churning'
     5. 0.88 'scooping'
     6. 0.88 'hauling'
     7. 0.87 'drying'


[+] target_word: 'possessing' model: Doc2Vec(dm/m,d15,n10,w2,mc23,s0.0001,t10):
     1. 0.90 'possessed'
     2. 0.90 'possesses'
     3. 0.89 'human'
     4. 0.89 'exploiting'
     5. 0.88 'preserving'
     6. 0.88 'dealing'
     7. 0.87 'bonding'


[+] target_word: 'defeated' model: Doc2Vec(dm/m,d15,n10,w2,mc23,s0.0001,t10):
     1. 0.94 'fought'
     2. 0.90 'attacked'
     3. 0.89 'surrendered'
     4. 0.89 'defeating'
     5. 0.88 'overthrown'
     6. 0.88 'recaptured'
     7. 0.87 'assassinated'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-18 14:03:33,571 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-18 14:03:34,340 : INFO : capital-common-countries: 9.1% (46/506)
2020-09-18 14:03:40,046 : INFO : capital-world: 3.4% (129/3773)
2020-09-18 14:03:40,701 : INFO : currency: 2.0% (9/458)
2020-09-18 14:03:44,174 : INFO : city-in-state: 2.6% (65/2467)
2020-09-18 14:03:44,773 : INFO : family: 37.5% (190/506)
2020-09-18 14:03:46,107 : INFO : gram1-adjective-to-adverb: 5.4% (54/992)
2020-09-18 14:03:47,121 : INFO : gram2-opposite: 4.7% (38/812)
2020-09-18 14:03:48,443 : INFO : gram3-comparative: 36.0% (480/1332)
2020-09-18 14:03:49,687 : INFO : gram4-superlative: 13.9% (156/1122)
2020-09-18 14:03:50,559 : INFO : gram5-present-participle: 15.7% (166/1056)
2020-09-18 14:03:52,913 : INFO : gram6-nationality-adjective: 12.3% (187/1521)
2020-09-18 14:03:54,175 : INFO : gram7-past-tense: 40.6% (633/1560)
2020-09-18 14:03:55,821 : INFO : gram8-plural: 21.1% (281/1332)
2020-09-18 14:03:56,594 : INFO : gram9-plural-verbs: 14.9% (130/870)
2020-09-18 14:03:56,595 : INFO : Quadruplets with out-of-vocabulary words: 6.3%
2020-09-18 14:03:56,595 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-18 14:03:56,595 : INFO : Total accuracy: 14.0% (2564/18307)
Doc2Vec(dm/m,d15,n10,w2,mc23,s0.0001,t10): 14.01% correct (2564 of 18307)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-18 14:03:56,954 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4646
2020-09-18 14:03:56,954 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4590
2020-09-18 14:03:56,954 : INFO : Pairs with unknown words ratio: 0.0%
((0.4645877822662906, 2.663147038566355e-20), SpearmanrResult(correlation=0.4589504662273158, pvalue=8.608564711298447e-20), 0.0)


02 - simlex999
2020-09-18 14:03:57,530 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3096
2020-09-18 14:03:57,530 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2566
2020-09-18 14:03:57,530 : INFO : Pairs with unknown words ratio: 0.2%
((0.3096399205533182, 1.3529005813106446e-23), SpearmanrResult(correlation=0.25664792492774285, pvalue=1.8436439880746082e-16), 0.20020020020020018)


03 - simverb3500
2020-09-18 14:03:57,898 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1444
2020-09-18 14:03:57,899 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1237
2020-09-18 14:03:57,899 : INFO : Pairs with unknown words ratio: 0.1%
((0.14435465827600835, 9.518969269769153e-18), SpearmanrResult(correlation=0.12366315024699885, pvalue=2.1440478830194513e-13), 0.05714285714285715)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#


"""
