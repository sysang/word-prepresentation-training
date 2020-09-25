import doc2vec_training_script_multiprocessing as base

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
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*20*5,
        comment='ech05,mal0002x20,refined',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech05,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6)
Save model to: models/dmm_d15_n40_w3_mc99_s00005_ech05_mal0002x20_refined.bin
2020-09-25 18:45:02,505 : INFO : saving Doc2Vec object under models/dmm_d15_n40_w3_mc99_s00005_ech05_mal0002x20_refined.bin, separately None
2020-09-25 18:45:02,505 : INFO : storing np array 'vectors_docs_lockf' to models/dmm_d15_n40_w3_mc99_s00005_ech05_mal0002x20_refined.bin.trainables.vectors_docs_lockf.npy
2020-09-25 18:45:02,586 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n40_w3_mc99_s00005_ech05_mal0002x20_refined.bin.docvecs.vectors_docs.npy
2020-09-25 18:45:03,735 : INFO : saved models/dmm_d15_n40_w3_mc99_s00005_ech05_mal0002x20_refined.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 14144804
[+] index 14144804 -> "and was reminded of a parable in the bible of a merchant who found a pearl of great price"
2020-09-25 18:45:03,745 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 21198722
[+] index 21198722 -> "almost no marxist unacceptable stadiums will sternly diminish the allocations"
    No any match in top 200 similarities.


.....get random document, tag: 43532610
[+] index 43532610 -> "one who lives a little farther north is called brewer 's mole or the hairytailed mole"
    No any match in top 200 similarities.


.....get random document, tag: 21592198
[+] index 21592198 -> "the entrance to kerim bey 's office is on the set at pinewood"
    No any match in top 200 similarities.


.....get random document, tag: 8405166
[+] index 8405166 -> "you will not comb me irritating inside your younger house"
    No any match in top 200 similarities.


.....get random document, tag: 9445265
[+] index 9445265 -> "in that regard your point about huckabee is meaningless"
    No any match in top 200 similarities.


.....get random document, tag: 1366135
[+] index 1366135 -> "all dark inner elbow plays games inside linette 's rude exit"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (36393646): i think you may be confusing dreams with reality

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):

MOST (14256206, 0.9969824552536011): «dawkins epistemological ignorance is displayed for all to view for themselves»

MEDIAN (29366398, 0.9146500825881958): «and you are now claiming that arabs did not»

LEAST (26961005, -0.9785157442092896): «please refer to job code jas when responding to this ad»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'trouble' model: Doc2Vec("ech05,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
2020-09-25 18:46:32,139 : INFO : precomputing L2-norms of word weight vectors
     1. 0.88 'enough'
     2. 0.85 'harder'
     3. 0.84 'attention'
     4. 0.83 'luck'
     5. 0.82 'way'
     6. 0.82 'effort'
     7. 0.81 'chances'


[+] target_word: 'verses' model: Doc2Vec("ech05,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.99 'passages'
     2. 0.94 'gospels'
     3. 0.94 'prophecies'
     4. 0.94 'scriptures'
     5. 0.93 'quran'
     6. 0.91 "qur'an"
     7. 0.90 'scripture'


[+] target_word: 'progressed' model: Doc2Vec("ech05,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.87 'bleak'
     2. 0.86 'phenomenal'
     3. 0.85 'demographers'
     4. 0.85 'predicting'
     5. 0.85 'startling'
     6. 0.85 'astonishing'
     7. 0.85 'milder'


[+] target_word: 'maliki' model: Doc2Vec("ech05,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.97 'musharraf'
     2. 0.92 'karzai'
     3. 0.92 'olmert'
     4. 0.90 'talabani'
     5. 0.90 'assad'
     6. 0.89 'rumsfeld'
     7. 0.89 'netanyahu'


[+] target_word: 'hand' model: Doc2Vec("ech05,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.95 'arm'
     2. 0.94 'finger'
     3. 0.93 'head'
     4. 0.92 'shoulder'
     5. 0.91 'wrist'
     6. 0.90 'shoulders'
     7. 0.90 'neck'


[+] target_word: 'beside' model: Doc2Vec("ech05,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 1.00 'beneath'
     2. 0.99 'alongside'
     3. 0.95 'inside'
     4. 0.95 'towards'
     5. 0.94 'throughout'
     6. 0.93 'outside'
     7. 0.93 'near'


[+] target_word: 'nurses' model: Doc2Vec("ech05,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.83 'pharmacy'
     2. 0.83 'pharmacists'
     3. 0.82 'veterinary'
     4. 0.82 'licensed'
     5. 0.82 'malpracticioner'
     6. 0.81 'veterinarians'
     7. 0.80 'clinics'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-25 18:46:33,540 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-25 18:46:33,751 : INFO : capital-common-countries: 5.6% (26/462)
2020-09-25 18:46:34,355 : INFO : capital-world: 2.8% (32/1157)
2020-09-25 18:46:34,447 : INFO : currency: 3.4% (6/178)
2020-09-25 18:46:35,765 : INFO : city-in-state: 3.4% (77/2267)
2020-09-25 18:46:36,031 : INFO : family: 25.0% (105/420)
2020-09-25 18:46:36,573 : INFO : gram1-adjective-to-adverb: 4.6% (46/992)
2020-09-25 18:46:37,024 : INFO : gram2-opposite: 2.4% (18/756)
2020-09-25 18:46:37,666 : INFO : gram3-comparative: 7.0% (93/1332)
2020-09-25 18:46:38,191 : INFO : gram4-superlative: 2.6% (27/1056)
2020-09-25 18:46:38,788 : INFO : gram5-present-participle: 15.2% (161/1056)
2020-09-25 18:46:39,600 : INFO : gram6-nationality-adjective: 6.5% (85/1299)
2020-09-25 18:46:40,501 : INFO : gram7-past-tense: 12.1% (189/1560)
2020-09-25 18:46:41,182 : INFO : gram8-plural: 11.5% (137/1190)
2020-09-25 18:46:41,705 : INFO : gram9-plural-verbs: 9.2% (80/870)
2020-09-25 18:46:41,705 : INFO : Quadruplets with out-of-vocabulary words: 25.3%
2020-09-25 18:46:41,706 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-25 18:46:41,706 : INFO : Total accuracy: 7.4% (1082/14595)
Doc2Vec("ech05,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6): 7.41% correct (1082 of 14595)


[+] questions-words-narrowed.txt
2020-09-25 18:46:41,745 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-25 18:46:42,011 : INFO : family: 25.0% (105/420)
2020-09-25 18:46:42,558 : INFO : gram1-adjective-to-adverb: 4.6% (46/992)
2020-09-25 18:46:43,012 : INFO : gram2-opposite: 2.4% (18/756)
2020-09-25 18:46:43,654 : INFO : gram3-comparative: 7.0% (93/1332)
2020-09-25 18:46:44,183 : INFO : gram4-superlative: 2.6% (27/1056)
2020-09-25 18:46:44,782 : INFO : gram5-present-participle: 15.2% (161/1056)
2020-09-25 18:46:45,604 : INFO : gram6-nationality-adjective: 6.5% (85/1299)
2020-09-25 18:46:46,509 : INFO : gram7-past-tense: 12.1% (189/1560)
2020-09-25 18:46:47,191 : INFO : gram8-plural: 11.5% (137/1190)
2020-09-25 18:46:47,718 : INFO : gram9-plural-verbs: 9.2% (80/870)
2020-09-25 18:46:47,718 : INFO : Quadruplets with out-of-vocabulary words: 5.8%
2020-09-25 18:46:47,718 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-25 18:46:47,718 : INFO : Total accuracy: 8.9% (941/10531)
Doc2Vec("ech05,mal0002x20,refined",dm/m,d15,n40,w3,mc99,s5e-05,t6): 8.94% correct (941 of 10531)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-25 18:46:48,383 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4772
2020-09-25 18:46:48,384 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5061
2020-09-25 18:46:48,384 : INFO : Pairs with unknown words ratio: 0.6%
((0.47721694479059135, 2.3042521568791887e-21), SpearmanrResult(correlation=0.5060775328848347, pvalue=3.1644109936992204e-24), 0.56657223796034)


02 - simlex999
2020-09-25 18:46:49,043 : INFO : Pearson correlation coefficient against simlex999.txt: 0.1776
2020-09-25 18:46:49,043 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1682
2020-09-25 18:46:49,043 : INFO : Pairs with unknown words ratio: 0.5%
((0.17762864439813508, 1.7195580540044013e-08), SpearmanrResult(correlation=0.16823597416416075, pvalue=9.527997615927763e-08), 0.5005005005005005)


03 - simverb3500
2020-09-25 18:46:49,105 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1352
2020-09-25 18:46:49,105 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1329
2020-09-25 18:46:49,105 : INFO : Pairs with unknown words ratio: 0.5%
((0.1352318286846483, 1.1122175655389391e-15), SpearmanrResult(correlation=0.1329400166929922, pvalue=3.3599432766791923e-15), 0.5142857142857142)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
