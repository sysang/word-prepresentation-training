import doc2vec_training_script_multiprocessing as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=40,
        window=2,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=0,
        hs=0,
        epochs=5,
        min_alpha=0.0001,
        alpha=0.0001*100*5,
        comment='ech05,mal0001x100',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech05,mal0001x100",dm/m,d15,n40,w2,mc99,s5e-05,t6)
Save model to: models/dmm_d15_n40_w2_mc99_s00005_ech05_mal0001x100_thefinal.bin
2020-09-21 19:53:14,134 : INFO : saving Doc2Vec object under models/dmm_d15_n40_w2_mc99_s00005_ech05_mal0001x100_thefinal.bin, separately None
2020-09-21 19:53:14,134 : INFO : storing np array 'vectors_docs_lockf' to models/dmm_d15_n40_w2_mc99_s00005_ech05_mal0001x100_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-21 19:53:14,163 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n40_w2_mc99_s00005_ech05_mal0001x100_thefinal.bin.docvecs.vectors_docs.npy
2020-09-21 19:53:14,595 : INFO : saved models/dmm_d15_n40_w2_mc99_s00005_ech05_mal0001x100_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 4714351
[+] index 4714351 -> "then go quite alone down a road that you will find on your right hand looking southwards"
2020-09-21 19:53:14,604 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 100 similarities.


.....get random document, tag: 8687336
[+] index 8687336 -> "the softball team has won six ncaa women 's college world series titles in 1991 1993 1994 1996 1997 and 2001 under head coach mike candrea ncaa softball championship"
    No any match in top 100 similarities.


.....get random document, tag: 12843679
[+] index 12843679 -> "this does worry me as a librarian i will be required to do some book lifting from time to time"
    No any match in top 100 similarities.


.....get random document, tag: 1084805
[+] index 1084805 -> "go my lord remember your promise to seek at your cousin 's hand the gonfalon and may god and his blessed saints prosper your excellency the old man caught the young man 's hand and bending his head until his face was hidden in his long white hair he imprinted a kiss of fealty upon it"
    No any match in top 100 similarities.


.....get random document, tag: 12282067
[+] index 12282067 -> "okay so friday started out as a normal day"
    No any match in top 100 similarities.


.....get random document, tag: 12467807
[+] index 12467807 -> "you may be thinking right about now gawd you 'd think she was the only person to ever start working full time do not get me wrong as far as jobs go i have a good one but sometimes i do not feel there is a lot of scope for uni graduates in particular to be able to adjust"
    No any match in top 100 similarities.


.....get random document, tag: 8117330
[+] index 8117330 -> "the supreme court has never ruled that any specific form of execution has violated the eight amendment clause prohibiting cruel and unusual punishment"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (12925602): perhaps there is something in all this after all

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0001x100",dm/m,d15,n40,w2,mc99,s5e-05,t6):

MOST (11647138, 0.9980602264404297): «the rest of the day is kind of a blur»

MEDIAN (1751013, 0.7897081971168518): «it was not consistent with cautious sounding that norman was always looking appealingly towards her and indeed she could not wait long with such a question on her mind»

LEAST (10056247, -0.9620526432991028): «the per capita income for the county is $18 050»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'demo' model: Doc2Vec("ech05,mal0001x100",dm/m,d15,n40,w2,mc99,s5e-05,t6):
2020-09-21 19:53:40,830 : INFO : precomputing L2-norms of word weight vectors
     1. 0.95 'promo'
     2. 0.92 'walkman'
     3. 0.92 'cd'
     4. 0.91 'playlist'
     5. 0.91 'cassette'
     6. 0.91 'clip'
     7. 0.89 'recorder'


[+] target_word: '92' model: Doc2Vec("ech05,mal0001x100",dm/m,d15,n40,w2,mc99,s5e-05,t6):
     1. 1.00 '91'
     2. 1.00 '93'
     3. 1.00 '94'
     4. 1.00 '89'
     5. 0.99 '87'
     6. 0.99 '86'
     7. 0.98 '83'


[+] target_word: 'winters' model: Doc2Vec("ech05,mal0001x100",dm/m,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.93 'summers'
     2. 0.91 'mid-winter'
     3. 0.86 'twenties'
     4. 0.86 'thirties'
     5. 0.85 'forties'
     6. 0.85 'humid'
     7. 0.84 '20s'


[+] target_word: 'senor' model: Doc2Vec("ech05,mal0001x100",dm/m,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.97 'alonzo'
     2. 0.97 'herrera'
     3. 0.96 'dom'
     4. 0.95 'anselmo'
     5. 0.95 'senhor'
     6. 0.95 'gaston'
     7. 0.95 'raoul'


[+] target_word: 'colleagues' model: Doc2Vec("ech05,mal0001x100",dm/m,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.91 'counselors'
     2. 0.89 'staffers'
     3. 0.88 'advisors'
     4. 0.88 'classmates'
     5. 0.87 'collaborators'
     6. 0.86 'advisers'
     7. 0.86 'mentors'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-21 19:53:41,480 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-21 19:53:41,793 : INFO : capital-common-countries: 8.5% (43/506)
2020-09-21 19:53:43,022 : INFO : capital-world: 5.4% (96/1779)
2020-09-21 19:53:43,143 : INFO : currency: 1.1% (2/178)
2020-09-21 19:53:44,842 : INFO : city-in-state: 2.4% (55/2267)
2020-09-21 19:53:45,142 : INFO : family: 39.3% (165/420)
2020-09-21 19:53:45,939 : INFO : gram1-adjective-to-adverb: 2.1% (21/992)
2020-09-21 19:53:46,326 : INFO : gram2-opposite: 5.0% (35/702)
2020-09-21 19:53:47,035 : INFO : gram3-comparative: 25.7% (342/1332)
2020-09-21 19:53:47,684 : INFO : gram4-superlative: 7.3% (77/1056)
2020-09-21 19:53:48,284 : INFO : gram5-present-participle: 21.8% (230/1056)
2020-09-21 19:53:49,293 : INFO : gram6-nationality-adjective: 8.0% (110/1371)
2020-09-21 19:53:50,354 : INFO : gram7-past-tense: 22.3% (348/1560)
2020-09-21 19:53:51,400 : INFO : gram8-plural: 17.3% (230/1332)
2020-09-21 19:53:51,951 : INFO : gram9-plural-verbs: 6.9% (60/870)
2020-09-21 19:53:51,951 : INFO : Quadruplets with out-of-vocabulary words: 21.1%
2020-09-21 19:53:51,951 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-21 19:53:51,952 : INFO : Total accuracy: 11.8% (1814/15421)
Doc2Vec("ech05,mal0001x100",dm/m,d15,n40,w2,mc99,s5e-05,t6): 11.76% correct (1814 of 15421)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-21 19:53:52,224 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5470
2020-09-21 19:53:52,224 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5458
2020-09-21 19:53:52,224 : INFO : Pairs with unknown words ratio: 0.6%
((0.5470066291737895, 8.785855116208255e-29), SpearmanrResult(correlation=0.5458267553848163, pvalue=1.2134326185346217e-28), 0.56657223796034)


02 - simlex999
2020-09-21 19:53:52,272 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2998
2020-09-21 19:53:52,272 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2639
2020-09-21 19:53:52,272 : INFO : Pairs with unknown words ratio: 0.3%
((0.299759723075353, 3.9792858200462944e-22), SpearmanrResult(correlation=0.2638695608205883, pvalue=2.5040865723573995e-17), 0.3003003003003003)


03 - simverb3500
2020-09-21 19:53:52,551 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1765
2020-09-21 19:53:52,551 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1619
2020-09-21 19:53:52,551 : INFO : Pairs with unknown words ratio: 1.4%
((0.17650416754616716, 1.486196585021297e-25), SpearmanrResult(correlation=0.16186793112174025, pvalue=1.0682957570782386e-21), 1.3714285714285714)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
