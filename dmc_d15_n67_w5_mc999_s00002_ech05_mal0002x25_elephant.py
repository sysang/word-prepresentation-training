import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=67,
        window=5,
        min_count=999,
        sample=0.00002,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*25*5,
        comment='ech05,mal0002x25',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc999,s2e-05,t6)
Save model to: models/dmc_d15_n67_w5_mc999_s00002_ech05_mal0002x25_elephant.bin
2020-09-23 22:29:12,131 : INFO : saving Doc2Vec object under models/dmc_d15_n67_w5_mc999_s00002_ech05_mal0002x25_elephant.bin, separately None
2020-09-23 22:29:12,132 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n67_w5_mc999_s00002_ech05_mal0002x25_elephant.bin.trainables.vectors_docs_lockf.npy
2020-09-23 22:29:12,407 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n67_w5_mc999_s00002_ech05_mal0002x25_elephant.bin.docvecs.vectors_docs.npy
2020-09-23 22:29:33,730 : INFO : saved models/dmc_d15_n67_w5_mc999_s00002_ech05_mal0002x25_elephant.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 56575918
[+] index 56575918 -> "nor do i foresee a meaningful conversation with you"
2020-09-23 22:29:33,881 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 100 similarities.


.....get random document, tag: 13533481
[+] index 13533481 -> "how janet 's old elbow scolds, joie calls among closed, proud halls"
    No any match in top 100 similarities.


.....get random document, tag: 48565193
[+] index 48565193 -> "algeria must defeat the united states as at least one condition of advancement"
    No any match in top 100 similarities.


.....get random document, tag: 12423590
[+] index 12423590 -> ".i just do not know what you expect to accomplish..with all of this murder"
    No any match in top 100 similarities.


.....get random document, tag: 112843317
[+] index 112843317 -> "actually, it is quite clear and perhaps just went over your head"
    No any match in top 100 similarities.


.....get random document, tag: 118023584
[+] index 118023584 -> "although i was able to access the snapper file from my own pc, it worked laboriously, at best and on other pc 's - not at all so attempting to access a runtime version from any other pc on the network is not a workable solution"
    No any match in top 100 similarities.


.....get random document, tag: 80433551
[+] index 80433551 -> "thank you, so all of this time, the *gang* has not known the facts"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (60559268): how does mohammed refer so earlier, whenever pam revives the technical taste very relatively

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc999,s2e-05,t6):

MOST (61774454, 0.9530025124549866): «you are trying to confuse the two terms in order to make your point,»

MEDIAN (20984808, 0.00034509599208831787): «he will be shouting around wide dolf until his shopkeeper expects weekly»

LEAST (51919963, -0.9551111459732056): «at least back when i lived in chicago, the new york times was delivered on the morning it was dated»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'scowling' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc999,s2e-05,t6):
2020-09-23 22:35:26,866 : INFO : precomputing L2-norms of word weight vectors
     1. 0.94 'hugging'
     2. 0.93 'kissing'
     3. 0.92 'grinning'
     4. 0.91 'cursing'
     5. 0.91 'giggling'
     6. 0.90 'smirking'
     7. 0.90 'sobbing'


[+] target_word: 'kfc' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc999,s2e-05,t6):
     1. 0.96 'mcdonalds'
     2. 0.95 'hamburgers'
     3. 0.94 'bbq'
     4. 0.94 'rum'
     5. 0.94 'pizza'
     6. 0.94 'hamburger'
     7. 0.93 'safeway'


[+] target_word: 'murders,' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc999,s2e-05,t6):
     1. 0.98 'rapes,'
     2. 0.97 'rapes'
     3. 0.96 'murders'
     4. 0.95 'assaults,'
     5. 0.94 'killings,'
     6. 0.93 'beatings'
     7. 0.93 'slayings'


[+] target_word: 'hi-rel' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc999,s2e-05,t6):
     1. 0.90 '2011'
     2. 0.89 '2010'
     3. 0.88 '2009'
     4. 0.85 '2008'
     5. 0.84 '2007'
     6. 0.84 '2006'
     7. 0.82 'metro'


[+] target_word: 'alt' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc999,s2e-05,t6):
     1. 0.91 '"old"'
     2. 0.90 'soc'
     3. 0.90 'printable'
     4. 0.89 'downloadable'
     5. 0.89 'irc'
     6. 0.89 'froup'
     7. 0.89 'web'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-23 22:35:32,906 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-23 22:35:33,218 : INFO : capital-common-countries: 6.5% (30/462)
2020-09-23 22:35:33,830 : INFO : capital-world: 3.9% (34/877)
2020-09-23 22:35:33,854 : INFO : currency: 5.0% (2/40)
2020-09-23 22:35:34,696 : INFO : city-in-state: 2.0% (31/1520)
2020-09-23 22:35:34,951 : INFO : family: 46.6% (177/380)
2020-09-23 22:35:35,537 : INFO : gram1-adjective-to-adverb: 1.8% (18/992)
2020-09-23 22:35:35,850 : INFO : gram2-opposite: 3.4% (22/650)
2020-09-23 22:35:36,411 : INFO : gram3-comparative: 23.1% (308/1332)
2020-09-23 22:35:36,778 : INFO : gram4-superlative: 10.4% (103/992)
2020-09-23 22:35:37,247 : INFO : gram5-present-participle: 20.9% (221/1056)
2020-09-23 22:35:37,945 : INFO : gram6-nationality-adjective: 21.7% (282/1299)
2020-09-23 22:35:38,814 : INFO : gram7-past-tense: 26.5% (413/1560)
2020-09-23 22:35:39,518 : INFO : gram8-plural: 16.0% (180/1122)
2020-09-23 22:35:39,995 : INFO : gram9-plural-verbs: 18.0% (146/812)
2020-09-23 22:35:40,008 : INFO : Quadruplets with out-of-vocabulary words: 33.0%
2020-09-23 22:35:40,008 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-23 22:35:40,008 : INFO : Total accuracy: 15.0% (1967/13094)
Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc999,s2e-05,t6): 15.02% correct (1967 of 13094)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-23 22:35:40,084 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5091
2020-09-23 22:35:40,084 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5047
2020-09-23 22:35:40,084 : INFO : Pairs with unknown words ratio: 2.0%
((0.5091111594879372, 3.25215307171537e-24), SpearmanrResult(correlation=0.5046622023519081, pvalue=9.317683864133402e-24), 1.9830028328611897)


02 - simlex999
2020-09-23 22:35:41,987 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2797
2020-09-23 22:35:41,987 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2348
2020-09-23 22:35:41,987 : INFO : Pairs with unknown words ratio: 0.6%
((0.27969754325481533, 2.644917599683948e-19), SpearmanrResult(correlation=0.23477310356374245, pvalue=6.690237997198473e-14), 0.6006006006006006)


03 - simverb3500
2020-09-23 22:35:42,087 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1612
2020-09-23 22:35:42,087 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1479
2020-09-23 22:35:42,087 : INFO : Pairs with unknown words ratio: 2.3%
((0.16119441408588336, 2.4464678777490595e-21), SpearmanrResult(correlation=0.1478723483853512, pvalue=3.590094719900631e-18), 2.314285714285714)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
