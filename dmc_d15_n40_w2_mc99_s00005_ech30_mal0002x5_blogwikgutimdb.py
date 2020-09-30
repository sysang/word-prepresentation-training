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
        epochs=30,
        min_alpha=0.0002,
        alpha=0.0002*5*30,
        comment='ech30,mal0002x5,blogwikgutimdb',
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


INFO: Training parameters: {'vector_size': 15, 'negative': 40, 'window': 2, 'min_count': 99, 'sample': 5e-05, 'dm': 1, 'dm_concat': 1, 'hs': 0, 'epochs': 30, 'min_alpha': 0.0002, 'alpha': 0.03, 'comment': 'ech30,mal0002x5,blogwikgutimdb'}
INFO: Model details: Doc2Vec("ech30,mal0002x5,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6)
INFO: Save model to: models/dmc_d15_n40_w2_mc99_s00005_ech30_mal0002x5_blogwikgutimdb.bin
2020-09-30 12:50:27,343 : INFO : saving Doc2Vec object under models/dmc_d15_n40_w2_mc99_s00005_ech30_mal0002x5_blogwikgutimdb.bin, separately None
2020-09-30 12:50:27,344 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n40_w2_mc99_s00005_ech30_mal0002x5_blogwikgutimdb.bin.docvecs.vectors_docs.npy
2020-09-30 12:50:27,709 : INFO : saved models/dmc_d15_n40_w2_mc99_s00005_ech30_mal0002x5_blogwikgutimdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 5032876
-> index 5032876 --> "they had never meant to give themselves a master and they chafed under his hand which grew continually heavier"
2020-09-30 12:50:29,399 : INFO : precomputing L2-norms of doc weight vectors
[*] Matched with rank 1, score: 0.9686651229858398!


.....get random document, tag: 5971669
-> index 5971669 --> "she said never mind what they said i told her i already knew what they told her the same thing they told us"
[*] Matched with rank 1, score: 0.9593676924705505!


.....get random document, tag: 4662927
-> index 4662927 --> "in a dream pericles is instructed to go to the temple of diana"
    No any match in top 200 similarities.


.....get random document, tag: 7162976
-> index 7162976 --> "you see this bright gentleman had a 357 magnum loaded in his coat pocket"
[*] Matched with rank 1, score: 0.9850108623504639!


.....get random document, tag: 1592084
-> index 1592084 --> "miss brown he said please take your pencil i am quite ready sir she answered"
[*] Matched with rank 1, score: 0.9414892792701721!


.....get random document, tag: 7222973
-> index 7222973 --> "we din even get to enter the pub 'coz yanling din bring her id along"
[*] Matched with rank 136, score: 0.8476731777191162!


.....get random document, tag: 4439637
-> index 4439637 --> "the seeds are embedded in the common flesh of the ovary"
[*] Matched with rank 1, score: 0.976651132106781!




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (1819514): m not sure that the obvious people are not the most fortunate he said with a little laugh

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech30,mal0002x5,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):

MOST (3637034, 0.9527906179428101): «the team 's findings reveal that the recurrence of earthquakes is strongly dependent on the recurrence times of previous earthquakes»

MEDIAN (1918646, -0.001875162124633789): «i took off my shoes and went down to the edge»

LEAST (467683, -0.9305126667022705): «but before he signed them he spoke you are a business man mr»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'site' model: Doc2Vec("ech30,mal0002x5,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
2020-09-30 12:50:56,150 : INFO : precomputing L2-norms of word weight vectors
     1. 0.94 'website'
     2. 0.93 'journal'
     3. 0.92 'suite'
     4. 0.92 'library'
     5. 0.92 'newsletter'
     6. 0.91 'weblog'
     7. 0.91 'webpage'


[+] target_word: 'shine' model: Doc2Vec("ech30,mal0002x5,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.92 'conjure'
     2. 0.92 'melt'
     3. 0.91 'stirs'
     4. 0.91 'harden'
     5. 0.90 'swallow'
     6. 0.90 'swallowing'
     7. 0.90 'kindle'


[+] target_word: 'impressed' model: Doc2Vec("ech30,mal0002x5,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.94 'intrigued'
     2. 0.93 'annoyed'
     3. 0.93 'shocked'
     4. 0.93 'fascinated'
     5. 0.92 'hinted'
     6. 0.92 'captivated'
     7. 0.91 'remembered'


[+] target_word: 'session' model: Doc2Vec("ech30,mal0002x5,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.95 'sessions'
     2. 0.92 'interview'
     3. 0.91 'semester'
     4. 0.91 'exam'
     5. 0.90 'rehearsal'
     6. 0.89 'meeting'
     7. 0.89 'exams'


[+] target_word: 'emails' model: Doc2Vec("ech30,mal0002x5,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.95 'messages'
     2. 0.92 'photos'
     3. 0.92 'posts'
     4. 0.92 'promotions'
     5. 0.91 'submissions'
     6. 0.90 'interviews'
     7. 0.90 'telegrams'


[+] target_word: 'bull' model: Doc2Vec("ech30,mal0002x5,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.98 'lion'
     2. 0.97 'dragon'
     3. 0.95 'camel'
     4. 0.95 'crocodile'
     5. 0.95 'viper'
     6. 0.95 'boar'
     7. 0.94 'panda'


[+] target_word: '98' model: Doc2Vec("ech30,mal0002x5,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 1.00 '97'
     2. 1.00 '95'
     3. 1.00 '99'
     4. 1.00 '96'
     5. 1.00 '87'
     6. 1.00 '89'
     7. 1.00 '88'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-30 12:50:56,565 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-30 12:50:56,756 : INFO : capital-common-countries: 9.7% (45/462)
2020-09-30 12:50:57,128 : INFO : capital-world: 5.7% (49/862)
2020-09-30 12:50:57,184 : INFO : currency: 0.0% (0/128)
2020-09-30 12:50:57,990 : INFO : city-in-state: 2.7% (55/2009)
2020-09-30 12:50:58,155 : INFO : family: 42.4% (161/380)
2020-09-30 12:50:58,565 : INFO : gram1-adjective-to-adverb: 2.1% (21/992)
2020-09-30 12:50:58,859 : INFO : gram2-opposite: 2.3% (15/650)
2020-09-30 12:50:59,380 : INFO : gram3-comparative: 28.8% (383/1332)
2020-09-30 12:50:59,805 : INFO : gram4-superlative: 13.5% (143/1056)
2020-09-30 12:51:00,178 : INFO : gram5-present-participle: 15.1% (150/992)
2020-09-30 12:51:00,768 : INFO : gram6-nationality-adjective: 11.5% (150/1299)
2020-09-30 12:51:01,384 : INFO : gram7-past-tense: 25.4% (396/1560)
2020-09-30 12:51:01,898 : INFO : gram8-plural: 16.2% (193/1190)
2020-09-30 12:51:02,244 : INFO : gram9-plural-verbs: 11.6% (94/812)
2020-09-30 12:51:02,244 : INFO : Quadruplets with out-of-vocabulary words: 29.8%
2020-09-30 12:51:02,244 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-30 12:51:02,245 : INFO : Total accuracy: 13.5% (1855/13724)
Doc2Vec("ech30,mal0002x5,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6): 13.52% correct (1855 of 13724)


[+] questions-words-narrowed.txt
2020-09-30 12:51:02,266 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-30 12:51:02,431 : INFO : family: 42.4% (161/380)
2020-09-30 12:51:02,844 : INFO : gram1-adjective-to-adverb: 2.1% (21/992)
2020-09-30 12:51:03,141 : INFO : gram2-opposite: 2.3% (15/650)
2020-09-30 12:51:03,662 : INFO : gram3-comparative: 28.8% (383/1332)
2020-09-30 12:51:04,102 : INFO : gram4-superlative: 13.5% (143/1056)
2020-09-30 12:51:04,474 : INFO : gram5-present-participle: 15.1% (150/992)
2020-09-30 12:51:05,068 : INFO : gram6-nationality-adjective: 11.5% (150/1299)
2020-09-30 12:51:05,687 : INFO : gram7-past-tense: 25.4% (396/1560)
2020-09-30 12:51:06,207 : INFO : gram8-plural: 16.2% (193/1190)
2020-09-30 12:51:06,546 : INFO : gram9-plural-verbs: 11.6% (94/812)
2020-09-30 12:51:06,546 : INFO : Quadruplets with out-of-vocabulary words: 8.2%
2020-09-30 12:51:06,546 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-30 12:51:06,547 : INFO : Total accuracy: 16.6% (1706/10263)
Doc2Vec("ech30,mal0002x5,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6): 16.62% correct (1706 of 10263)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-30 12:51:06,707 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5234
2020-09-30 12:51:06,707 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5204
2020-09-30 12:51:06,707 : INFO : Pairs with unknown words ratio: 2.5%
((0.5234155161347186, 1.3688116943260813e-25), SpearmanrResult(correlation=0.5204454057756547, pvalue=2.852457202355088e-25), 2.5495750708215295)


02 - simlex999
2020-09-30 12:51:06,730 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3051
2020-09-30 12:51:06,731 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2707
2020-09-30 12:51:06,731 : INFO : Pairs with unknown words ratio: 0.5%
((0.30513037899875106, 7.299882330665882e-23), SpearmanrResult(correlation=0.27065324535282204, pvalue=3.788849676575565e-18), 0.5005005005005005)


03 - simverb3500
2020-09-30 12:51:06,777 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1765
2020-09-30 12:51:06,777 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1604
2020-09-30 12:51:06,777 : INFO : Pairs with unknown words ratio: 6.0%
((0.1765460357178353, 1.9572015617280324e-24), SpearmanrResult(correlation=0.16037920177083023, pvalue=2.1587790061691547e-20), 6.0285714285714285)


-----------------------------------------------------
Benchmark similarity score with respect to theme word
-----------------------------------------------------


[*] a beautiful girl - a pretty girl, distance score: 0.425150, with respect to theme: beautiful
 ~  a beautiful girl - a pretty woman, distance score: 0.569541, with respect to theme: female
[*] a beautiful girl - a ugly girl, distance score: 1.765190, with respect to theme: beautiful
 ~  a new car - an old car, distance score: 0.874492, with respect to theme: car
 ~  a new car - an old car, distance score: 0.364260, with respect to theme: new
 ~  a new car - an huge car, distance score: 0.883925, with respect to theme: car
[*] girl - boy, distance score: 1.656205, with respect to theme: gender
 ~  girl - boy, distance score: 1.422825, with respect to theme: young
 ~  girl - woman, distance score: 2.671885, with respect to theme: gender
[*] man - woman, distance score: 3.967470, with respect to theme: gender
[*] boy - man, distance score: 0.451987, with respect to theme: gender
 ~  son - daughter, distance score: 0.084880, with respect to theme: boy
[*] son - daughter, distance score: 0.003047, with respect to theme: children
[*] sea - mountain, distance score: 0.403294, with respect to theme: nature
 ~  sea - house, distance score: 0.179001, with respect to theme: nature
 ~  sea - software, distance score: 0.365220, with respect to theme: nature
 ~  sea - mountain, distance score: 0.021024, with respect to theme: climbing
 ~  human - dog, distance score: 1.506202, with respect to theme: mammal
[*] human - dog, distance score: 1.010348, with respect to theme: intelligence
[*] human - plant, distance score: 0.856115, with respect to theme: mobility
 ~  dog - plant, distance score: 0.187856, with respect to theme: mobility
[*] dog - human, distance score: 0.048409, with respect to theme: mobility
<EPOCHS>: 10 - <SCORE>: 45.45


 ~  a beautiful girl - a pretty girl, distance score: 2.170020, with respect to theme: beautiful
[*] a beautiful girl - a pretty woman, distance score: 0.420809, with respect to theme: female
[*] a beautiful girl - a ugly girl, distance score: 1.267242, with respect to theme: beautiful
 ~  a new car - an old car, distance score: 0.814730, with respect to theme: car
 ~  a new car - an old car, distance score: 0.178374, with respect to theme: new
 ~  a new car - an huge car, distance score: 1.846927, with respect to theme: car
[*] girl - boy, distance score: 2.056557, with respect to theme: gender
[*] girl - boy, distance score: 0.012432, with respect to theme: young
 ~  girl - woman, distance score: 0.788958, with respect to theme: gender
[*] man - woman, distance score: 4.102818, with respect to theme: gender
[*] boy - man, distance score: 0.423668, with respect to theme: gender
 ~  son - daughter, distance score: 0.033734, with respect to theme: boy
[*] son - daughter, distance score: 0.006477, with respect to theme: children
 ~  sea - mountain, distance score: 0.549457, with respect to theme: nature
 ~  sea - house, distance score: 0.208500, with respect to theme: nature
 ~  sea - software, distance score: 0.075759, with respect to theme: nature
 ~  sea - mountain, distance score: 0.103993, with respect to theme: climbing
 ~  human - dog, distance score: 1.019836, with respect to theme: mammal
[*] human - dog, distance score: 4.180975, with respect to theme: intelligence
[*] human - plant, distance score: 1.651158, with respect to theme: mobility
 ~  dog - plant, distance score: 0.384076, with respect to theme: mobility
[*] dog - human, distance score: 0.459046, with respect to theme: mobility
<EPOCHS>: 20 - <SCORE>: 45.45


 ~  a beautiful girl - a pretty girl, distance score: 4.305598, with respect to theme: beautiful
 ~  a beautiful girl - a pretty woman, distance score: 0.555975, with respect to theme: female
[*] a beautiful girl - a ugly girl, distance score: 3.714255, with respect to theme: beautiful
 ~  a new car - an old car, distance score: 1.665797, with respect to theme: car
 ~  a new car - an old car, distance score: 0.099753, with respect to theme: new
[*] a new car - an huge car, distance score: 0.385312, with respect to theme: car
[*] girl - boy, distance score: 1.898250, with respect to theme: gender
[*] girl - boy, distance score: 0.359331, with respect to theme: young
[*] girl - woman, distance score: 0.397200, with respect to theme: gender
[*] man - woman, distance score: 5.456227, with respect to theme: gender
[*] boy - man, distance score: 0.070101, with respect to theme: gender
 ~  son - daughter, distance score: 0.042107, with respect to theme: boy
[*] son - daughter, distance score: 0.000119, with respect to theme: children
[*] sea - mountain, distance score: 0.358280, with respect to theme: nature
 ~  sea - house, distance score: 0.079683, with respect to theme: nature
 ~  sea - software, distance score: 0.188161, with respect to theme: nature
 ~  sea - mountain, distance score: 0.122735, with respect to theme: climbing
 ~  human - dog, distance score: 0.992622, with respect to theme: mammal
[*] human - dog, distance score: 4.186474, with respect to theme: intelligence
[*] human - plant, distance score: 0.639670, with respect to theme: mobility
 ~  dog - plant, distance score: 0.392194, with respect to theme: mobility
[*] dog - human, distance score: 0.178196, with respect to theme: mobility
<EPOCHS>: 50 - <SCORE>: 54.55


 ~  a beautiful girl - a pretty girl, distance score: 2.678066, with respect to theme: beautiful
 ~  a beautiful girl - a pretty woman, distance score: 1.314260, with respect to theme: female
[*] a beautiful girl - a ugly girl, distance score: 1.611300, with respect to theme: beautiful
 ~  a new car - an old car, distance score: 0.966076, with respect to theme: car
 ~  a new car - an old car, distance score: 0.468983, with respect to theme: new
 ~  a new car - an huge car, distance score: 1.278820, with respect to theme: car
[*] girl - boy, distance score: 1.183010, with respect to theme: gender
[*] girl - boy, distance score: 0.234563, with respect to theme: young
[*] girl - woman, distance score: 0.160952, with respect to theme: gender
[*] man - woman, distance score: 2.482445, with respect to theme: gender
 ~  boy - man, distance score: 4.728304, with respect to theme: gender
 ~  son - daughter, distance score: 0.003428, with respect to theme: boy
[*] son - daughter, distance score: 0.024734, with respect to theme: children
[*] sea - mountain, distance score: 0.302440, with respect to theme: nature
 ~  sea - house, distance score: 0.191513, with respect to theme: nature
 ~  sea - software, distance score: 0.086828, with respect to theme: nature
 ~  sea - mountain, distance score: 0.090450, with respect to theme: climbing
 ~  human - dog, distance score: 1.577937, with respect to theme: mammal
[*] human - dog, distance score: 0.713581, with respect to theme: intelligence
[*] human - plant, distance score: 2.075010, with respect to theme: mobility
 ~  dog - plant, distance score: 0.022613, with respect to theme: mobility
 ~  dog - human, distance score: 0.636893, with respect to theme: mobility
<EPOCHS>: 100 - <SCORE>: 40.91


 ~  a beautiful girl - a pretty girl, distance score: 0.651087, with respect to theme: beautiful
 ~  a beautiful girl - a pretty woman, distance score: 1.999146, with respect to theme: female
[*] a beautiful girl - a ugly girl, distance score: 2.004800, with respect to theme: beautiful
 ~  a new car - an old car, distance score: 0.918381, with respect to theme: car
 ~  a new car - an old car, distance score: 0.258163, with respect to theme: new
 ~  a new car - an huge car, distance score: 1.266851, with respect to theme: car
[*] girl - boy, distance score: 1.169462, with respect to theme: gender
[*] girl - boy, distance score: 0.217516, with respect to theme: young
 ~  girl - woman, distance score: 0.801747, with respect to theme: gender
[*] man - woman, distance score: 1.229818, with respect to theme: gender
 ~  boy - man, distance score: 3.382540, with respect to theme: gender
 ~  son - daughter, distance score: 0.035797, with respect to theme: boy
[*] son - daughter, distance score: 0.006117, with respect to theme: children
[*] sea - mountain, distance score: 0.192275, with respect to theme: nature
[*] sea - house, distance score: 0.994373, with respect to theme: nature
 ~  sea - software, distance score: 0.215500, with respect to theme: nature
 ~  sea - mountain, distance score: 0.009116, with respect to theme: climbing
[*] human - dog, distance score: 0.367456, with respect to theme: mammal
[*] human - dog, distance score: 1.495131, with respect to theme: intelligence
 ~  human - plant, distance score: 0.342776, with respect to theme: mobility
 ~  dog - plant, distance score: 0.056818, with respect to theme: mobility
[*] dog - human, distance score: 0.246309, with respect to theme: mobility
<EPOCHS>: 200 - <SCORE>: 45.45




_____  COMPLETED  _________________________________
###~~~~~~~~#~~~~~~~#~~~~~~~#~~~~~~~~~~#~~~~~~~~~###

"""
