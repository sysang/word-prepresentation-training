import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=40,
        window=2,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=12,
        min_alpha=0.0002,
        alpha=0.0002*10*12,
        comment='ech10,mal0002x10,blogwikgutimdb',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(
            common_kwargs=common_kwargs,
            saved_fname=saved_fname,
            evaluate=False,
            database='blogwikgutimdb')

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


INFO: Training parameters: {'vector_size': 15, 'negative': 40, 'window': 2, 'min_count': 99, 'sample': 5e-05, 'dm': 1, 'dm_concat': 1, 'hs': 0, 'epochs': 12, 'min_alpha': 0.0002, 'alpha': 0.024, 'comment': 'ech10,mal0002x10,blogwikgutimdb'}
INFO: Model details: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6)
INFO: Save model to: models/dmc_d15_n40_w2_mc99_s00005_ech12_mal0002x10_blogwikgutimdb.bin
2020-09-30 10:17:37,114 : INFO : saving Doc2Vec object under models/dmc_d15_n40_w2_mc99_s00005_ech12_mal0002x10_blogwikgutimdb.bin, separately None
2020-09-30 10:17:37,114 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n40_w2_mc99_s00005_ech12_mal0002x10_blogwikgutimdb.bin.docvecs.vectors_docs.npy
2020-09-30 10:17:37,478 : INFO : saved models/dmc_d15_n40_w2_mc99_s00005_ech12_mal0002x10_blogwikgutimdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 6878284
-> index 6878284 --> "sometimes i like to be naked and paint my whole body blue"
2020-09-30 10:17:39,795 : INFO : precomputing L2-norms of doc weight vectors
[*] Matched with rank 5, score: 0.9205693006515503!


.....get random document, tag: 7293580
-> index 7293580 --> "if you have been avoiding this show because of the overabundance of hype surrounding it do yourself a favor and check it out"
    No any match in top 200 similarities.


.....get random document, tag: 5140292
-> index 5140292 --> "for every 100 females age 18 and over there are 92 7 males"
    No any match in top 200 similarities.


.....get random document, tag: 3949252
-> index 3949252 --> "the bizarros are a group that resemble the main sealab characters only with black uniforms and other noticeable features"
[*] Matched with rank 44, score: 0.873051106929779!


.....get random document, tag: 2476547
-> index 2476547 --> "the boy probably sold us or your friend dom clemente was too clever for him"
[*] Matched with rank 2, score: 0.9314831495285034!


.....get random document, tag: 1079197
-> index 1079197 --> "all you have got to think of is your wife and your daughter"
[*] Matched with rank 1, score: 0.9596059918403625!


.....get random document, tag: 6520936
-> index 6520936 --> "ill start with baby steps that is ill just motivate my body to welcome physical activities"
[*] Matched with rank 2, score: 0.9491410255432129!




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (3928372): according to the united states census bureau the town has a total area of 4 4 km² 1 7 mi²

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):

MOST (5907183, 0.9461067914962769): «i have taken two showers since i got out of the pool and my skin still smells like chlorine»

MEDIAN (3733903, -0.0009266156703233719): «as a village it is located in the town of pelham»

LEAST (6571708, -0.9069458246231079): «4 the silence due to the lag time on a very long distance telephone call hello»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'numbers' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
2020-09-30 10:18:09,238 : INFO : precomputing L2-norms of word weight vectors
     1. 0.93 'points'
     2. 0.92 'designations'
     3. 0.92 'variables'
     4. 0.92 'prefixes'
     5. 0.91 'fractions'
     6. 0.90 'dimensions'
     7. 0.90 'constants'


[+] target_word: 'worried' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.97 'annoyed'
     2. 0.97 'excited'
     3. 0.95 'disappointed'
     4. 0.94 'upset'
     5. 0.94 'surprised'
     6. 0.94 'bored'
     7. 0.93 'suprised'


[+] target_word: 'fathers' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.95 'wives'
     2. 0.95 'parishioners'
     3. 0.94 'disciples'
     4. 0.94 'husbands'
     5. 0.93 'saints'
     6. 0.93 'relatives'
     7. 0.93 'mistresses'


[+] target_word: 'stuff' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.93 'goodies'
     2. 0.90 'yarns'
     3. 0.90 'pictures'
     4. 0.90 'quizzes'
     5. 0.89 'stuffs'
     6. 0.89 'pics'
     7. 0.89 'accessories'


[+] target_word: 'opera' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.95 'cabaret'
     2. 0.93 'ballet'
     3. 0.92 'revue'
     4. 0.90 'theatre'
     5. 0.89 'repertory'
     6. 0.89 'rhapsody'
     7. 0.88 'festival'


[+] target_word: 'lantern' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.96 'lamp'
     2. 0.94 'curtain'
     3. 0.94 'torch'
     4. 0.92 'candle'
     5. 0.92 'pipe'
     6. 0.92 'candlestick'
     7. 0.91 'knob'


[+] target_word: 'entertained' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.94 'reconciled'
     2. 0.92 'indebted'
     3. 0.91 'engrossed'
     4. 0.90 'shunned'
     5. 0.90 'welcomed'
     6. 0.90 'alienated'
     7. 0.90 'appreciated'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-30 10:18:09,623 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-30 10:18:09,811 : INFO : capital-common-countries: 8.2% (38/462)
2020-09-30 10:18:10,179 : INFO : capital-world: 5.6% (48/862)
2020-09-30 10:18:10,235 : INFO : currency: 0.0% (0/128)
2020-09-30 10:18:11,047 : INFO : city-in-state: 3.9% (78/2009)
2020-09-30 10:18:11,212 : INFO : family: 49.2% (187/380)
2020-09-30 10:18:11,641 : INFO : gram1-adjective-to-adverb: 3.2% (32/992)
2020-09-30 10:18:11,939 : INFO : gram2-opposite: 3.7% (24/650)
2020-09-30 10:18:12,491 : INFO : gram3-comparative: 39.3% (524/1332)
2020-09-30 10:18:12,919 : INFO : gram4-superlative: 10.8% (114/1056)
2020-09-30 10:18:13,309 : INFO : gram5-present-participle: 17.0% (169/992)
2020-09-30 10:18:13,893 : INFO : gram6-nationality-adjective: 12.4% (161/1299)
2020-09-30 10:18:14,542 : INFO : gram7-past-tense: 30.3% (473/1560)
2020-09-30 10:18:15,077 : INFO : gram8-plural: 20.1% (239/1190)
2020-09-30 10:18:15,411 : INFO : gram9-plural-verbs: 15.3% (124/812)
2020-09-30 10:18:15,411 : INFO : Quadruplets with out-of-vocabulary words: 29.8%
2020-09-30 10:18:15,412 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-30 10:18:15,412 : INFO : Total accuracy: 16.1% (2211/13724)
Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6): 16.11% correct (2211 of 13724)


[+] questions-words-narrowed.txt
2020-09-30 10:18:15,435 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-30 10:18:15,600 : INFO : family: 49.2% (187/380)
2020-09-30 10:18:16,032 : INFO : gram1-adjective-to-adverb: 3.2% (32/992)
2020-09-30 10:18:16,329 : INFO : gram2-opposite: 3.7% (24/650)
2020-09-30 10:18:16,882 : INFO : gram3-comparative: 39.3% (524/1332)
2020-09-30 10:18:17,313 : INFO : gram4-superlative: 10.8% (114/1056)
2020-09-30 10:18:17,704 : INFO : gram5-present-participle: 17.0% (169/992)
2020-09-30 10:18:18,294 : INFO : gram6-nationality-adjective: 12.4% (161/1299)
2020-09-30 10:18:18,945 : INFO : gram7-past-tense: 30.3% (473/1560)
2020-09-30 10:18:19,480 : INFO : gram8-plural: 20.1% (239/1190)
2020-09-30 10:18:19,815 : INFO : gram9-plural-verbs: 15.3% (124/812)
2020-09-30 10:18:19,815 : INFO : Quadruplets with out-of-vocabulary words: 8.2%
2020-09-30 10:18:19,815 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-30 10:18:19,815 : INFO : Total accuracy: 19.9% (2047/10263)
Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6): 19.95% correct (2047 of 10263)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-30 10:18:19,979 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5558
2020-09-30 10:18:19,979 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5539
2020-09-30 10:18:19,979 : INFO : Pairs with unknown words ratio: 2.5%
((0.5557665125769136, 2.824642156341102e-29), SpearmanrResult(correlation=0.5539358072835061, pvalue=4.681099557607971e-29), 2.5495750708215295)


02 - simlex999
2020-09-30 10:18:20,004 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3295
2020-09-30 10:18:20,004 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2834
2020-09-30 10:18:20,004 : INFO : Pairs with unknown words ratio: 0.5%
((0.3295406891191696, 1.314873032454402e-26), SpearmanrResult(correlation=0.28342214164069535, pvalue=8.09467450205974e-20), 0.5005005005005005)


03 - simverb3500
2020-09-30 10:18:20,051 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1719
2020-09-30 10:18:20,051 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1530
2020-09-30 10:18:20,051 : INFO : Pairs with unknown words ratio: 6.0%
((0.17185952086562256, 3.1990067543568444e-23), SpearmanrResult(correlation=0.1530428470689885, pvalue=1.0879785630136051e-18), 6.0285714285714285)


-----------------------------------------------------
Benchmark similarity score with respect to theme word
-----------------------------------------------------


 ~  a beautiful girl - a pretty girl, distance score: 3.241482, with respect to theme: beautiful
 ~  a beautiful girl - a pretty woman, distance score: 1.617558, with respect to theme: female
[*] a beautiful girl - a ugly girl, distance score: 0.741780, with respect to theme: beautiful
 ~  a new car - an old car, distance score: 0.948903, with respect to theme: car
 ~  a new car - an old car, distance score: 0.228886, with respect to theme: new
[*] a new car - an huge car, distance score: 0.217776, with respect to theme: car
[*] girl - boy, distance score: 0.829277, with respect to theme: gender
[*] girl - boy, distance score: 0.178754, with respect to theme: young
 ~  son - daughter, distance score: 0.011854, with respect to theme: boy
[*] son - daughter, distance score: 0.042371, with respect to theme: children
 ~  sea - mountain, distance score: 1.615803, with respect to theme: nature
 ~  sea - mountain, distance score: 0.420611, with respect to theme: climbing
<EPOCHS>: 10 - <SCORE>: 41.67


 ~  a beautiful girl - a pretty girl, distance score: 0.879853, with respect to theme: beautiful
 ~  a beautiful girl - a pretty woman, distance score: 1.021649, with respect to theme: female
 ~  a beautiful girl - a ugly girl, distance score: 0.107238, with respect to theme: beautiful
[*] a new car - an old car, distance score: 0.021120, with respect to theme: car
 ~  a new car - an old car, distance score: 0.200141, with respect to theme: new
[*] a new car - an huge car, distance score: 0.075903, with respect to theme: car
[*] girl - boy, distance score: 0.619575, with respect to theme: gender
[*] girl - boy, distance score: 0.138470, with respect to theme: young
 ~  son - daughter, distance score: 0.162046, with respect to theme: boy
[*] son - daughter, distance score: 0.036792, with respect to theme: children
 ~  sea - mountain, distance score: 1.690012, with respect to theme: nature
 ~  sea - mountain, distance score: 0.183249, with respect to theme: climbing
<EPOCHS>: 20 - <SCORE>: 41.67


 ~  a beautiful girl - a pretty girl, distance score: 2.157762, with respect to theme: beautiful
[*] a beautiful girl - a pretty woman, distance score: 0.369324, with respect to theme: female
[*] a beautiful girl - a ugly girl, distance score: 1.626124, with respect to theme: beautiful
 ~  a new car - an old car, distance score: 1.212367, with respect to theme: car
 ~  a new car - an old car, distance score: 0.072439, with respect to theme: new
[*] a new car - an huge car, distance score: 0.040930, with respect to theme: car
 ~  girl - boy, distance score: 0.327227, with respect to theme: gender
[*] girl - boy, distance score: 0.002660, with respect to theme: young
 ~  son - daughter, distance score: 0.137583, with respect to theme: boy
[*] son - daughter, distance score: 0.102445, with respect to theme: children
[*] sea - mountain, distance score: 0.026803, with respect to theme: nature
 ~  sea - mountain, distance score: 0.021366, with respect to theme: climbing
<EPOCHS>: 50 - <SCORE>: 50.00


 ~  a beautiful girl - a pretty girl, distance score: 1.551053, with respect to theme: beautiful
 ~  a beautiful girl - a pretty woman, distance score: 0.949609, with respect to theme: female
[*] a beautiful girl - a ugly girl, distance score: 1.226005, with respect to theme: beautiful
[*] a new car - an old car, distance score: 0.085957, with respect to theme: car
 ~  a new car - an old car, distance score: 0.067215, with respect to theme: new
[*] a new car - an huge car, distance score: 0.210807, with respect to theme: car
[*] girl - boy, distance score: 0.550668, with respect to theme: gender
[*] girl - boy, distance score: 0.011953, with respect to theme: young
 ~  son - daughter, distance score: 0.159347, with respect to theme: boy
[*] son - daughter, distance score: 0.038663, with respect to theme: children
[*] sea - mountain, distance score: 0.209393, with respect to theme: nature
 ~  sea - mountain, distance score: 0.114711, with respect to theme: climbing
<EPOCHS>: 100 - <SCORE>: 58.33


[*] a beautiful girl - a pretty girl, distance score: 0.262424, with respect to theme: beautiful
 ~  a beautiful girl - a pretty woman, distance score: 0.539195, with respect to theme: female
[*] a beautiful girl - a ugly girl, distance score: 2.278840, with respect to theme: beautiful
[*] a new car - an old car, distance score: 0.037501, with respect to theme: car
 ~  a new car - an old car, distance score: 0.047813, with respect to theme: new
[*] a new car - an huge car, distance score: 0.165698, with respect to theme: car
 ~  girl - boy, distance score: 0.019881, with respect to theme: gender
[*] girl - boy, distance score: 0.014150, with respect to theme: young
 ~  son - daughter, distance score: 0.006779, with respect to theme: boy
[*] son - daughter, distance score: 0.003859, with respect to theme: children
[*] sea - mountain, distance score: 0.176371, with respect to theme: nature
 ~  sea - mountain, distance score: 0.120013, with respect to theme: climbing
<EPOCHS>: 200 - <SCORE>: 58.33




_____  COMPLETED  _________________________________
###~~~~~~~~#~~~~~~~#~~~~~~~#~~~~~~~~~~#~~~~~~~~~###
"""
