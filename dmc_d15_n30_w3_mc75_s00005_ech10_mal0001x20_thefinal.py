import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=30,
        window=3,
        min_count=75,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=10,
        min_alpha=0.0001,
        alpha=0.0001*20*10
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
2020-09-20 09:48:39,439 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-20 09:48:39,440 : INFO : Loading a fresh vocabulary
2020-09-20 09:48:39,952 : INFO : effective_min_count=75 retains 70715 unique words (3% of original 1784839, drops 1714124)
2020-09-20 09:48:39,953 : INFO : effective_min_count=75 leaves 329482258 word corpus (98% of original 336075146, drops 6592888)
2020-09-20 09:48:40,111 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-20 09:48:40,148 : INFO : sample=5e-05 downsamples 730 most-common words
2020-09-20 09:48:40,149 : INFO : downsampling leaves estimated 148046269 word corpus (44.9% of prior 329482258)
2020-09-20 09:48:40,284 : INFO : estimated required memory for 70715 words and 15 dimensions: 866700700 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10)
Save model to: models/dmc_d15_n30_w3_mc75_s00005_ech10_mal0001x20_thefinal.bin
2020-09-20 11:57:32,968 : INFO : saving Doc2Vec object under models/dmc_d15_n30_w3_mc75_s00005_ech10_mal0001x20_thefinal.bin, separately None
2020-09-20 11:57:32,968 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n30_w3_mc75_s00005_ech10_mal0001x20_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-20 11:57:32,995 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n30_w3_mc75_s00005_ech10_mal0001x20_thefinal.bin.docvecs.vectors_docs.npy
2020-09-20 11:57:33,607 : INFO : saved models/dmc_d15_n30_w3_mc75_s00005_ech10_mal0001x20_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 2487129
[+] index 2487129 -> "amy dear louisa ' rang out olive 's contralto 'do not judge me by appearances"
2020-09-20 11:57:33,617 : INFO : precomputing L2-norms of doc weight vectors
[*] Matched with rank 4, score: 0.9164108633995056!


.....get random document, tag: 134265
[+] index 134265 -> "but go no lower than the gibbon and see how vastly more he differs from the gorilla than the latter does from man even in this structure"
    No any match in top 100 similarities.


.....get random document, tag: 236110
[+] index 236110 -> "then you 'd sing simon like a garden thrush"
[*] Matched with rank 1, score: 0.9187186360359192!


.....get random document, tag: 213451
[+] index 213451 -> "total score miss beighton 1 1 0 0 5 7 21 barr-saggott looked as if the last few arrowheads had been driven into his legs instead of the target 's and the deep stillness was broken by a little snubby mottled half-grown girl saying in a shrill voice of triumph then won mrs"
[*] Matched with rank 68, score: 0.8727812767028809!


.....get random document, tag: 4931830
[+] index 4931830 -> "he knew now that he could not climb the sides of that pail and there was no other way of getting out"
[*] Matched with rank 27, score: 0.8974665403366089!


.....get random document, tag: 12208543
[+] index 12208543 -> "some guy 's probably making millions of bucks putting this very same advice in a book"
[*] Matched with rank 1, score: 0.9475771188735962!


.....get random document, tag: 11128419
[+] index 11128419 -> "cannabis can be also used for stronger ropes yes rope is made of hemp people if you did not know that already"
[*] Matched with rank 34, score: 0.8945674300193787!




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (2124174): i wonder if there is any truth in it at all

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):

MOST (10876098, 0.9474688172340393): «truth is i wonder why pot is not doing it for me»

MEDIAN (7186832, -0.00010962039232254028): «her planes delivered final blows to japanese defenses on the 16th the day before the landings and provided close air support and cap over the island until 28 february»

LEAST (10502219, -0.9582095146179199): «this entry is dedicated to a certain salami hehe so i am killing time waiting for my bro to arrive more on that later so decided to pop in my godfather dvd»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'butt' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
2020-09-20 11:57:58,425 : INFO : precomputing L2-norms of word weight vectors
     1. 0.96 'arse'
     2. 0.94 'ass'
     3. 0.94 'knuckle'
     4. 0.92 'whip'
     5. 0.92 'drumstick'
     6. 0.91 'titty'
     7. 0.91 'whack'


[+] target_word: 'philosophers' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.97 'theologians'
     2. 0.97 'metaphysicians'
     3. 0.97 'thinkers'
     4. 0.95 'realists'
     5. 0.95 'scholars'
     6. 0.95 'humanists'
     7. 0.94 'evolutionists'


[+] target_word: 'to-night' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.93 'to-morrow'
     2. 0.92 'to-day'
     3. 0.92 'by-and-by'
     4. 0.91 'loreley'
     5. 0.90 'torp'
     6. 0.87 'shakhira'
     7. 0.87 'home'


[+] target_word: '1970s' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 1.00 '1960s'
     2. 1.00 '1980s'
     3. 0.99 '1950s'
     4. 0.99 '1990s'
     5. 0.99 '1940s'
     6. 0.98 '1930s'
     7. 0.98 '2000s'


[+] target_word: 'patted' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.98 'patting'
     2. 0.95 'clasping'
     3. 0.94 'shook'
     4. 0.94 'kissed'
     5. 0.93 'hugged'
     6. 0.93 'stroked'
     7. 0.93 'clutched'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-20 11:57:59,016 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-20 11:57:59,364 : INFO : capital-common-countries: 8.3% (42/506)
2020-09-20 11:58:00,714 : INFO : capital-world: 4.5% (87/1929)
2020-09-20 11:58:00,882 : INFO : currency: 3.0% (7/236)
2020-09-20 11:58:02,553 : INFO : city-in-state: 2.0% (46/2330)
2020-09-20 11:58:02,905 : INFO : family: 42.1% (177/420)
2020-09-20 11:58:03,620 : INFO : gram1-adjective-to-adverb: 3.5% (35/992)
2020-09-20 11:58:04,138 : INFO : gram2-opposite: 6.3% (44/702)
2020-09-20 11:58:05,025 : INFO : gram3-comparative: 30.7% (409/1332)
2020-09-20 11:58:05,804 : INFO : gram4-superlative: 13.0% (137/1056)
2020-09-20 11:58:06,465 : INFO : gram5-present-participle: 17.0% (179/1056)
2020-09-20 11:58:07,461 : INFO : gram6-nationality-adjective: 16.1% (221/1371)
2020-09-20 11:58:08,556 : INFO : gram7-past-tense: 24.6% (384/1560)
2020-09-20 11:58:09,453 : INFO : gram8-plural: 16.4% (218/1332)
2020-09-20 11:58:10,077 : INFO : gram9-plural-verbs: 10.8% (94/870)
2020-09-20 11:58:10,078 : INFO : Quadruplets with out-of-vocabulary words: 19.7%
2020-09-20 11:58:10,078 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-20 11:58:10,078 : INFO : Total accuracy: 13.3% (2080/15692)
Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10): 13.26% correct (2080 of 15692)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-20 11:58:10,360 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5526
2020-09-20 11:58:10,360 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5293
2020-09-20 11:58:10,361 : INFO : Pairs with unknown words ratio: 0.6%
((0.5525813987676517, 1.877748367485982e-29), SpearmanrResult(correlation=0.5292628996839972, pvalue=9.894461269527341e-27), 0.56657223796034)


02 - simlex999
2020-09-20 11:58:10,417 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3299
2020-09-20 11:58:10,417 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2817
2020-09-20 11:58:10,417 : INFO : Pairs with unknown words ratio: 0.3%
((0.32987780454580046, 1.0333727743114386e-26), SpearmanrResult(correlation=0.2817367931293612, pvalue=1.2513078171978293e-19), 0.3003003003003003)


03 - simverb3500
2020-09-20 11:58:10,702 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1838
2020-09-20 11:58:10,702 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1676
2020-09-20 11:58:10,703 : INFO : Pairs with unknown words ratio: 0.7%
((0.18381164460728963, 8.922221893177992e-28), SpearmanrResult(correlation=0.1676338333400727, pvalue=2.5896903853390946e-23), 0.7428571428571429)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
