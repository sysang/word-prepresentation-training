import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=67,
        window=5,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=0,
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


Model details: Doc2Vec("ech05,mal0002x25",dm/m,d15,n67,w5,mc99,s5e-05,t6)
Save model to: models/dmm_d15_n67_w5_mc99_s00005_ech05_mal0002x25_thefinal.bin
2020-09-22 18:05:06,930 : INFO : saving Doc2Vec object under models/dmm_d15_n67_w5_mc99_s00005_ech05_mal0002x25_thefinal.bin, separately None
2020-09-22 18:05:06,930 : INFO : storing np array 'vectors_docs_lockf' to models/dmm_d15_n67_w5_mc99_s00005_ech05_mal0002x25_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-22 18:05:06,959 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n67_w5_mc99_s00005_ech05_mal0002x25_thefinal.bin.docvecs.vectors_docs.npy
2020-09-22 18:05:07,378 : INFO : saved models/dmm_d15_n67_w5_mc99_s00005_ech05_mal0002x25_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 7847117
[+] index 7847117 -> "41 7% of all households are made up of individuals and 22 0% have someone living alone who is 65 years of age or older"
2020-09-22 18:05:07,388 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 100 similarities.


.....get random document, tag: 3444121
[+] index 3444121 -> "they are to be chosen from such as are widows indeed who trust in god and continue in supplications and prayers night and day 1 timothy 5 5"
    No any match in top 100 similarities.


.....get random document, tag: 4611486
[+] index 4611486 -> "they have to be fed with whatever food it may be they crave for and that 's the end of it kendricks motioned with his head across the room to where the little woman with the blackened eyebrows was eating her dinner"
    No any match in top 100 similarities.


.....get random document, tag: 13039354
[+] index 13039354 -> "that 's a great goal for everyone to have live it up psycho shitheads of the world there is a future for you yet"
    No any match in top 100 similarities.


.....get random document, tag: 9490433
[+] index 9490433 -> "physically you can only keep up with everyone for so long"
    No any match in top 100 similarities.


.....get random document, tag: 8508383
[+] index 8508383 -> "they describe an important urban civilization of about one million people living in walled cities under small city kings or magistrates"
    No any match in top 100 similarities.


.....get random document, tag: 12516766
[+] index 12516766 -> "but it 's cool i sipped on some gin and juice sang some country"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (7202429): thus the two distinct notions of the inverse of a function are strongly related in this case while they must be carefully distinguished in the general case see below

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x25",dm/m,d15,n67,w5,mc99,s5e-05,t6):

MOST (3958642, 0.9954465627670288): «a man that has got a character like that is hard to find he might be artful and keep his faults to himself suggested tredgold»

MEDIAN (6944812, 0.9079515933990479): «these agam sutras were orally passed on to future generations»

LEAST (7699108, -0.9760188460350037): «1 06% of the population are hispanic or latino of any race»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'fool' model: Doc2Vec("ech05,mal0002x25",dm/m,d15,n67,w5,mc99,s5e-05,t6):
2020-09-22 18:05:32,414 : INFO : precomputing L2-norms of word weight vectors
     1. 0.95 'dolt'
     2. 0.91 'bastard'
     3. 0.91 'slut'
     4. 0.90 'nigga'
     5. 0.89 'liar'
     6. 0.88 'idiot'
     7. 0.88 'whore'


[+] target_word: 'expand' model: Doc2Vec("ech05,mal0002x25",dm/m,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.90 'expanding'
     2. 0.87 'broaden'
     3. 0.87 'vital'
     4. 0.86 'facilitating'
     5. 0.85 'enabled'
     6. 0.85 'revitalize'
     7. 0.84 'pave'


[+] target_word: 'alphabet' model: Doc2Vec("ech05,mal0002x25",dm/m,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.95 'alphabets'
     2. 0.94 'numerals'
     3. 0.93 'diacritic'
     4. 0.91 'cyrillic'
     5. 0.91 'spellings'
     6. 0.90 'diacritics'
     7. 0.90 'abbreviations'


[+] target_word: 'rite' model: Doc2Vec("ech05,mal0002x25",dm/m,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.93 'liturgy'
     2. 0.92 'communion'
     3. 0.91 'eucharist'
     4. 0.90 'prayer'
     5. 0.90 'hymns'
     6. 0.90 'sacrament'
     7. 0.90 'prayers'


[+] target_word: 'raging' model: Doc2Vec("ech05,mal0002x25",dm/m,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.92 'buffeted'
     2. 0.88 'raged'
     3. 0.88 'braving'
     4. 0.88 'maddened'
     5. 0.87 'erupts'
     6. 0.87 'rages'
     7. 0.87 'drowned'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-22 18:05:33,118 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-22 18:05:33,467 : INFO : capital-common-countries: 9.7% (49/506)
2020-09-22 18:05:34,721 : INFO : capital-world: 7.0% (125/1779)
2020-09-22 18:05:34,850 : INFO : currency: 1.7% (3/178)
2020-09-22 18:05:36,450 : INFO : city-in-state: 3.1% (70/2267)
2020-09-22 18:05:36,766 : INFO : family: 45.0% (189/420)
2020-09-22 18:05:37,447 : INFO : gram1-adjective-to-adverb: 6.1% (61/992)
2020-09-22 18:05:37,904 : INFO : gram2-opposite: 3.7% (26/702)
2020-09-22 18:05:38,782 : INFO : gram3-comparative: 26.5% (353/1332)
2020-09-22 18:05:39,458 : INFO : gram4-superlative: 7.1% (75/1056)
2020-09-22 18:05:40,120 : INFO : gram5-present-participle: 21.2% (224/1056)
2020-09-22 18:05:41,102 : INFO : gram6-nationality-adjective: 15.6% (214/1371)
2020-09-22 18:05:42,118 : INFO : gram7-past-tense: 37.0% (577/1560)
2020-09-22 18:05:43,080 : INFO : gram8-plural: 19.4% (258/1332)
2020-09-22 18:05:43,654 : INFO : gram9-plural-verbs: 12.2% (106/870)
2020-09-22 18:05:43,655 : INFO : Quadruplets with out-of-vocabulary words: 21.1%
2020-09-22 18:05:43,655 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-22 18:05:43,655 : INFO : Total accuracy: 15.1% (2330/15421)
Doc2Vec("ech05,mal0002x25",dm/m,d15,n67,w5,mc99,s5e-05,t6): 15.11% correct (2330 of 15421)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-22 18:05:43,927 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.6021
2020-09-22 18:05:43,927 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.6181
2020-09-22 18:05:43,927 : INFO : Pairs with unknown words ratio: 0.6%
((0.6020791645579721, 5.3738669877063124e-36), SpearmanrResult(correlation=0.6181061174330984, pvalue=2.279802645180626e-38), 0.56657223796034)


02 - simlex999
2020-09-22 18:05:43,975 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3340
2020-09-22 18:05:43,975 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.3028
2020-09-22 18:05:43,975 : INFO : Pairs with unknown words ratio: 0.3%
((0.3339607947911923, 2.246655930025067e-27), SpearmanrResult(correlation=0.30281855923298573, pvalue=1.4385538975960445e-22), 0.3003003003003003)


03 - simverb3500
2020-09-22 18:05:44,254 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.2108
2020-09-22 18:05:44,254 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1950
2020-09-22 18:05:44,254 : INFO : Pairs with unknown words ratio: 1.4%
((0.21079757535390686, 5.687069610227328e-36), SpearmanrResult(correlation=0.19502392673533536, pvalue=6.166633509911564e-31), 1.3714285714285714)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
