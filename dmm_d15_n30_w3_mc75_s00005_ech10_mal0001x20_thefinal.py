import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=30,
        window=3,
        min_count=75,
        sample=0.00005,
        dm=1,
        dm_concat=0,
        hs=0,
        epochs=10,
        min_alpha=0.0001,
        alpha=0.0001*20*10
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
2020-09-20 15:32:26,065 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-20 15:32:26,065 : INFO : Loading a fresh vocabulary
2020-09-20 15:32:26,566 : INFO : effective_min_count=75 retains 70715 unique words (3% of original 1784839, drops 1714124)
2020-09-20 15:32:26,566 : INFO : effective_min_count=75 leaves 329482258 word corpus (98% of original 336075146, drops 6592888)
2020-09-20 15:32:26,727 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-20 15:32:26,765 : INFO : sample=5e-05 downsamples 730 most-common words
2020-09-20 15:32:26,765 : INFO : downsampling leaves estimated 148046269 word corpus (44.9% of prior 329482258)
2020-09-20 15:32:26,899 : INFO : estimated required memory for 70715 words and 15 dimensions: 841243300 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/m,d15,n30,w3,mc75,s5e-05,t10)
Save model to: models/dmm_d15_n30_w3_mc75_s00005_ech10_mal0001x20_thefinal.bin
2020-09-20 19:30:12,886 : INFO : saving Doc2Vec object under models/dmm_d15_n30_w3_mc75_s00005_ech10_mal0001x20_thefinal.bin, separately None
2020-09-20 19:30:12,887 : INFO : storing np array 'vectors_docs_lockf' to models/dmm_d15_n30_w3_mc75_s00005_ech10_mal0001x20_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-20 19:30:12,918 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n30_w3_mc75_s00005_ech10_mal0001x20_thefinal.bin.docvecs.vectors_docs.npy
2020-09-20 19:30:13,405 : INFO : saved models/dmm_d15_n30_w3_mc75_s00005_ech10_mal0001x20_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 12676295
[+] index 12676295 -> "first though my options in the evening were spiining followed by pumo however it 's buffy time by 9pm so"
2020-09-20 19:30:13,418 : INFO : precomputing L2-norms of doc weight vectors
[*] Matched with rank 19, score: 0.9646066427230835!


.....get random document, tag: 4959280
[+] index 4959280 -> "accumulations of the public revenue lying within them had been seized for the same object"
    No any match in top 100 similarities.


.....get random document, tag: 170043
[+] index 170043 -> "she enchanted my sword as i said and then my troubles began"
    No any match in top 100 similarities.


.....get random document, tag: 8051156
[+] index 8051156 -> "the next spring however he left the city and took its garrison with him"
    No any match in top 100 similarities.


.....get random document, tag: 7322658
[+] index 7322658 -> "according to the united states census bureau the village has a total area of 5 1 km² 2 0 mi²"
    No any match in top 100 similarities.


.....get random document, tag: 9841134
[+] index 9841134 -> "the population density is 477 9/km² 1 240 9/mi²"
    No any match in top 100 similarities.


.....get random document, tag: 6762384
[+] index 6762384 -> "steering wheels are the precision racing wheel and the force feedback wheel variants which include throttle and brake pedals"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (1309252): but how describe it since the poets have not taught me the painters manage these things better but even their prince rossetti has nothing on his canvases to compare with this delicate feature

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/m,d15,n30,w3,mc75,s5e-05,t10):

MOST (1112149, 0.98487389087677): «the theme is better suited for verse than prose and when i go home to america i will suggest it to one of our poets»

MEDIAN (10575801, 0.7386178970336914): «i drive him around while we get him shoes his final paycheck from the theatre and to go order a corsage for his prom date»

LEAST (9805253, -0.91512131690979): «the per capita income for the city is $27 093»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'user' model: Doc2Vec(dm/m,d15,n30,w3,mc75,s5e-05,t10):
2020-09-20 19:30:38,540 : INFO : precomputing L2-norms of word weight vectors
     1. 0.95 'bios'
     2. 0.94 'authentication'
     3. 0.94 'sql'
     4. 0.93 'permissions'
     5. 0.93 'filesystem'
     6. 0.92 'dns'
     7. 0.92 'login'


[+] target_word: 'brow' model: Doc2Vec(dm/m,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.94 'forehead'
     2. 0.93 'cheek'
     3. 0.91 'brows'
     4. 0.90 'eyelids'
     5. 0.90 'eyes'
     6. 0.89 'cheeks'
     7. 0.89 'visage'


[+] target_word: 'coherent' model: Doc2Vec(dm/m,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.93 'logial'
     2. 0.93 'repeatable'
     3. 0.92 'perceptual'
     4. 0.92 'non-linear'
     5. 0.91 'precise'
     6. 0.90 'simultaneity'
     7. 0.89 'regression'


[+] target_word: 'closely' model: Doc2Vec(dm/m,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.89 'characters'
     2. 0.89 'plots'
     3. 0.88 'identities'
     4. 0.88 'imperfectly'
     5. 0.87 'similarly'
     6. 0.86 'clues'
     7. 0.86 'distantly'


[+] target_word: 'jude' model: Doc2Vec(dm/m,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.91 'matthew'
     2. 0.90 'ezra'
     3. 0.90 'lennon'
     4. 0.90 'gregory'
     5. 0.89 'uriah'
     6. 0.89 'beckett'
     7. 0.89 'terence'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-20 19:30:39,284 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-20 19:30:39,663 : INFO : capital-common-countries: 13.4% (68/506)
2020-09-20 19:30:41,151 : INFO : capital-world: 6.4% (123/1929)
2020-09-20 19:30:41,322 : INFO : currency: 1.3% (3/236)
2020-09-20 19:30:42,921 : INFO : city-in-state: 2.3% (54/2330)
2020-09-20 19:30:43,259 : INFO : family: 40.0% (168/420)
2020-09-20 19:30:43,982 : INFO : gram1-adjective-to-adverb: 3.1% (31/992)
2020-09-20 19:30:44,563 : INFO : gram2-opposite: 6.0% (42/702)
2020-09-20 19:30:45,485 : INFO : gram3-comparative: 25.8% (343/1332)
2020-09-20 19:30:46,190 : INFO : gram4-superlative: 9.3% (98/1056)
2020-09-20 19:30:46,931 : INFO : gram5-present-participle: 17.1% (181/1056)
2020-09-20 19:30:47,968 : INFO : gram6-nationality-adjective: 13.3% (182/1371)
2020-09-20 19:30:49,082 : INFO : gram7-past-tense: 37.5% (585/1560)
2020-09-20 19:30:50,070 : INFO : gram8-plural: 16.2% (216/1332)
2020-09-20 19:30:50,715 : INFO : gram9-plural-verbs: 10.1% (88/870)
2020-09-20 19:30:50,715 : INFO : Quadruplets with out-of-vocabulary words: 19.7%
2020-09-20 19:30:50,716 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-20 19:30:50,716 : INFO : Total accuracy: 13.9% (2182/15692)
Doc2Vec(dm/m,d15,n30,w3,mc75,s5e-05,t10): 13.91% correct (2182 of 15692)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-20 19:30:50,996 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5683
2020-09-20 19:30:50,996 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5750
2020-09-20 19:30:50,996 : INFO : Pairs with unknown words ratio: 0.6%
((0.5682782518892172, 2.0773908371627234e-31), SpearmanrResult(correlation=0.5750374840642037, pvalue=2.7700999211088305e-32), 0.56657223796034)


02 - simlex999
2020-09-20 19:30:51,268 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3158
2020-09-20 19:30:51,269 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2865
2020-09-20 19:30:51,269 : INFO : Pairs with unknown words ratio: 0.3%
((0.31579592784117927, 1.6743792184037503e-24), SpearmanrResult(correlation=0.28649215265999145, pvalue=2.8563276985047886e-20), 0.3003003003003003)


03 - simverb3500
2020-09-20 19:30:51,350 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.2043
2020-09-20 19:30:51,350 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1899
2020-09-20 19:30:51,350 : INFO : Pairs with unknown words ratio: 0.7%
((0.20434157121316396, 4.585372783108563e-34), SpearmanrResult(correlation=0.1898976509660314, pvalue=1.4446054336553356e-29), 0.7428571428571429)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
