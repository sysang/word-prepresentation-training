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
        dm_concat=1,
        hs=0,
        epochs=10,
        min_alpha=0.0002,
        alpha=0.0002*10*10,
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


Model details: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6)
Save model to: models/dmc_d15_n67_w5_mc99_s00005_ech10_mal0002x10_blogwikgutimdb.bin
2020-09-29 22:47:07,748 : INFO : saving Doc2Vec object under models/dmc_d15_n67_w5_mc99_s00005_ech10_mal0002x10_blogwikgutimdb.bin, separately None
2020-09-29 22:47:07,748 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n67_w5_mc99_s00005_ech10_mal0002x10_blogwikgutimdb.bin.docvecs.vectors_docs.npy
2020-09-29 22:47:08,200 : INFO : saved models/dmc_d15_n67_w5_mc99_s00005_ech10_mal0002x10_blogwikgutimdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 6251388
-> index 6251388 --> "i may seem to be really negative about life but that 's not true"
2020-09-29 22:47:10,311 : INFO : precomputing L2-norms of doc weight vectors
[*] Matched with rank 1, score: 0.9308639168739319!


.....get random document, tag: 7266873
-> index 7266873 --> "we all stand outside waiting for everyone to catch up"
[*] Matched with rank 6, score: 0.9179497957229614!


.....get random document, tag: 82155
-> index 82155 --> "and really it 's a great relief to think he 's going hastings continued my honest friend"
[*] Matched with rank 133, score: 0.8387297987937927!


.....get random document, tag: 6846652
-> index 6846652 --> "visiting hours are over time for our bedside tug of war"
    No any match in top 200 similarities.


.....get random document, tag: 5940372
-> index 5940372 --> "hmmm i think it 's time to start digging through the cookbooks and shaking up the menu a bit"
[*] Matched with rank 1, score: 0.939455509185791!


.....get random document, tag: 7255956
-> index 7255956 --> "what else i also started the overwhelming nightmare of a project of cleaning my room"
[*] Matched with rank 56, score: 0.8642491102218628!


.....get random document, tag: 4876535
-> index 4876535 --> "the foundations were rediscovered in may 2003 revealing a building 80 m long and 41 m wide"
[*] Matched with rank 1, score: 0.9219328761100769!




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (1050882): for the moment my animosity toward the mexican vanished and with it the old hunger to be in the thick of wild western life

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):

MOST (1290739, 0.9182851314544678): «ll give you all the money i can spare»

MEDIAN (2393464, -0.00028248131275177): «silence lads not so bad though says he rubbing his wet hands»

LEAST (4852794, -0.9235734343528748): «udp connections may sometimes be tunnelled with the aid of programs such as netcat»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'designed' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
2020-09-29 22:47:38,276 : INFO : precomputing L2-norms of word weight vectors
     1. 0.90 'used'
     2. 0.90 'devised'
     3. 0.88 'pioneered'
     4. 0.87 'intended'
     5. 0.86 'utilized'
     6. 0.86 'fitted'
     7. 0.85 'engineered'


[+] target_word: 'racing' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.96 'motorcycle'
     2. 0.92 'automobile'
     3. 0.91 'cycling'
     4. 0.90 'bicycle'
     5. 0.89 'scooter'
     6. 0.89 'dinghy'
     7. 0.88 'airplane'


[+] target_word: 'foolish' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.96 'thoughtless'
     2. 0.95 'conceited'
     3. 0.95 'unkind'
     4. 0.94 'ungrateful'
     5. 0.94 'spiteful'
     6. 0.94 'impudent'
     7. 0.94 'selfish'


[+] target_word: '67' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 1.00 '68'
     2. 0.99 '66'
     3. 0.99 '62'
     4. 0.99 '69'
     5. 0.99 '63'
     6. 0.99 '61'
     7. 0.99 '58'


[+] target_word: 'church' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.95 'synagogue'
     2. 0.95 'diocese'
     3. 0.94 'congregation'
     4. 0.91 'convent'
     5. 0.91 'priory'
     6. 0.91 'archbishops'
     7. 0.90 'priesthood'


[+] target_word: 'regime' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.97 'dictatorship'
     2. 0.90 'suharto'
     3. 0.90 'revolution'
     4. 0.90 'junta'
     5. 0.90 'imperialism'
     6. 0.89 'insurrection'
     7. 0.88 'insurgency'


[+] target_word: 'valleys' model: Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.97 'uplands'
     2. 0.96 'plains'
     3. 0.95 'plateaus'
     4. 0.95 'thickets'
     5. 0.95 'slopes'
     6. 0.94 'lowlands'
     7. 0.94 'hillsides'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-29 22:47:38,623 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-29 22:47:38,792 : INFO : capital-common-countries: 8.9% (41/462)
2020-09-29 22:47:39,129 : INFO : capital-world: 6.5% (56/862)
2020-09-29 22:47:39,189 : INFO : currency: 0.8% (1/128)
2020-09-29 22:47:39,945 : INFO : city-in-state: 4.8% (96/2009)
2020-09-29 22:47:40,114 : INFO : family: 44.2% (168/380)
2020-09-29 22:47:40,521 : INFO : gram1-adjective-to-adverb: 3.3% (33/992)
2020-09-29 22:47:40,815 : INFO : gram2-opposite: 3.4% (22/650)
2020-09-29 22:47:41,331 : INFO : gram3-comparative: 39.0% (520/1332)
2020-09-29 22:47:41,766 : INFO : gram4-superlative: 12.6% (133/1056)
2020-09-29 22:47:42,195 : INFO : gram5-present-participle: 21.0% (208/992)
2020-09-29 22:47:42,791 : INFO : gram6-nationality-adjective: 11.6% (151/1299)
2020-09-29 22:47:43,441 : INFO : gram7-past-tense: 27.4% (427/1560)
2020-09-29 22:47:43,982 : INFO : gram8-plural: 17.9% (213/1190)
2020-09-29 22:47:44,328 : INFO : gram9-plural-verbs: 16.0% (130/812)
2020-09-29 22:47:44,329 : INFO : Quadruplets with out-of-vocabulary words: 29.8%
2020-09-29 22:47:44,329 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 22:47:44,329 : INFO : Total accuracy: 16.0% (2199/13724)
Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6): 16.02% correct (2199 of 13724)


[+] questions-words-narrowed.txt
2020-09-29 22:47:44,351 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-29 22:47:44,519 : INFO : family: 44.2% (168/380)
2020-09-29 22:47:44,926 : INFO : gram1-adjective-to-adverb: 3.3% (33/992)
2020-09-29 22:47:45,222 : INFO : gram2-opposite: 3.4% (22/650)
2020-09-29 22:47:45,737 : INFO : gram3-comparative: 39.0% (520/1332)
2020-09-29 22:47:46,175 : INFO : gram4-superlative: 12.6% (133/1056)
2020-09-29 22:47:46,604 : INFO : gram5-present-participle: 21.0% (208/992)
2020-09-29 22:47:47,201 : INFO : gram6-nationality-adjective: 11.6% (151/1299)
2020-09-29 22:47:47,846 : INFO : gram7-past-tense: 27.4% (427/1560)
2020-09-29 22:47:48,390 : INFO : gram8-plural: 17.9% (213/1190)
2020-09-29 22:47:48,736 : INFO : gram9-plural-verbs: 16.0% (130/812)
2020-09-29 22:47:48,737 : INFO : Quadruplets with out-of-vocabulary words: 8.2%
2020-09-29 22:47:48,737 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 22:47:48,737 : INFO : Total accuracy: 19.5% (2005/10263)
Doc2Vec("ech10,mal0002x10,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6): 19.54% correct (2005 of 10263)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-29 22:47:48,898 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5815
2020-09-29 22:47:48,898 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5735
2020-09-29 22:47:48,898 : INFO : Pairs with unknown words ratio: 2.5%
((0.5815331278682088, 1.6369359981257307e-32), SpearmanrResult(correlation=0.5735237706816517, pvalue=1.7818489001971048e-31), 2.5495750708215295)


02 - simlex999
2020-09-29 22:47:48,922 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3541
2020-09-29 22:47:48,922 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.3069
2020-09-29 22:47:48,923 : INFO : Pairs with unknown words ratio: 0.5%
((0.35412042519894743, 9.741203042224882e-31), SpearmanrResult(correlation=0.30689593985840646, pvalue=4.018338739022044e-23), 0.5005005005005005)


03 - simverb3500
2020-09-29 22:47:48,970 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1874
2020-09-29 22:47:48,970 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1719
2020-09-29 22:47:48,970 : INFO : Pairs with unknown words ratio: 6.0%
((0.1873738215889021, 2.276631970885793e-27), SpearmanrResult(correlation=0.1719047327290716, pvalue=3.11509992557801e-23), 6.0285714285714285)


     ____________     COMPLETED      ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
