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
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*25*5,
        comment='ech05,mal0002x25,blogwikgutimdb',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(
            common_kwargs=common_kwargs,
            saved_fname=saved_fname,
            evaluate=False,
            database='blogwikgutimdb')

"""
2020-09-29 13:08:58,959 : INFO : collected 605528 word types and 7410000 unique tags from a corpus of 7410000 examples and 121440062 words
2020-09-29 13:08:58,959 : INFO : Loading a fresh vocabulary
2020-09-29 13:08:59,126 : INFO : effective_min_count=99 retains 34983 unique words (5% of original 605528, drops 570545)
2020-09-29 13:08:59,126 : INFO : effective_min_count=99 leaves 118011182 word corpus (97% of original 121440062, drops 3428880)
2020-09-29 13:08:59,203 : INFO : deleting the raw counts dictionary of 605528 items
2020-09-29 13:08:59,215 : INFO : sample=5e-05 downsamples 737 most-common words
2020-09-29 13:08:59,215 : INFO : downsampling leaves estimated 51370242 word corpus (43.5% of prior 118011182)
2020-09-29 13:08:59,268 : INFO : estimated required memory for 34983 words and 15 dimensions: 487279260 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6)
Save model to: models/dmc_d15_n67_w5_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin
2020-09-29 13:46:21,025 : INFO : saving Doc2Vec object under models/dmc_d15_n67_w5_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin, separately None
2020-09-29 13:46:21,025 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n67_w5_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin.docvecs.vectors_docs.npy
2020-09-29 13:46:21,475 : INFO : saved models/dmc_d15_n67_w5_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 2756424
[+] index 2756424 -> "yet herman mordaunt went through it with a grace and dignity that i think would have been remarked at a royal banquet"
2020-09-29 13:46:22,408 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 2447720
[+] index 2447720 -> "the literary merit of some of the essays herein is in many respects nowise inferior to that in some of the volumes he collected himself"
    No any match in top 200 similarities.


.....get random document, tag: 5980015
[+] index 5980015 -> "otherwise its name would not be joy it looks forward or backward the direction in this regard is unimportant to the great eucatastrophe"
    No any match in top 200 similarities.


.....get random document, tag: 1980110
[+] index 1980110 -> "in the first place however we must search for something to eat"
    No any match in top 200 similarities.


.....get random document, tag: 6295084
[+] index 6295084 -> "on the borght side i did get distinctions for law and economics"
    No any match in top 200 similarities.


.....get random document, tag: 2535680
[+] index 2535680 -> "burton she said you must please not come near me but i want a kiss he protested"
    No any match in top 200 similarities.


.....get random document, tag: 5331654
[+] index 5331654 -> "in 1971 it was expanded and renamed as the pan am worldport"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (889390): it bodes ill for england it is natural harold said gently

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):

MOST (5588470, 0.9490870237350464): «there is nothing like a bunch of drag queens to make a woman feel inferior»

MEDIAN (4486867, 0.0006433911621570587): «the winner of the race is the person who accumulates the most points and is on the leading lap»

LEAST (2487239, -0.9492571353912354): «while my father remains in his present helpless condition somebody must assume a position of command in this house»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'ability' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
2020-09-29 13:46:48,987 : INFO : precomputing L2-norms of word weight vectors
     1. 0.92 'inability'
     2. 0.89 'incentive'
     3. 0.88 'compulsion'
     4. 0.88 'tendency'
     5. 0.87 'willingness'
     6. 0.86 'ingenuity'
     7. 0.86 'abilities'


[+] target_word: '105' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 1.00 '108'
     2. 1.00 '104'
     3. 0.99 '102'
     4. 0.99 '103'
     5. 0.99 '107'
     6. 0.99 '106'
     7. 0.99 '109'


[+] target_word: 'letting' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.91 'forcing'
     2. 0.90 'helping'
     3. 0.89 'bothering'
     4. 0.87 'hurting'
     5. 0.86 'allowing'
     6. 0.86 "'let"
     7. 0.86 'abusing'


[+] target_word: 'sermon' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.91 'prayer'
     2. 0.90 'ceremony'
     3. 0.90 'sermons'
     4. 0.89 'prayers'
     5. 0.89 'liturgy'
     6. 0.88 'communion'
     7. 0.87 'catechism'


[+] target_word: 'causing' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.93 'inflicting'
     2. 0.89 'crippling'
     3. 0.88 'easing'
     4. 0.88 'racking'
     5. 0.88 'inducing'
     6. 0.87 'resulting'
     7. 0.87 'quicken'


[+] target_word: 'syndrome' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.95 'anemia'
     2. 0.95 'schizophrenia'
     3. 0.94 'syphilis'
     4. 0.93 'dementia'
     5. 0.92 'hypertension'
     6. 0.90 'symptoms'
     7. 0.90 'abnormalities'


[+] target_word: 'river' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.96 'gulch'
     2. 0.95 'tigris'
     3. 0.95 'loire'
     4. 0.93 'islet'
     5. 0.92 'sands'
     6. 0.91 'creek'
     7. 0.91 'bayou'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-29 13:46:49,357 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-29 13:46:49,533 : INFO : capital-common-countries: 9.1% (42/462)
2020-09-29 13:46:49,881 : INFO : capital-world: 7.4% (64/862)
2020-09-29 13:46:49,941 : INFO : currency: 0.0% (0/128)
2020-09-29 13:46:50,729 : INFO : city-in-state: 4.6% (92/2009)
2020-09-29 13:46:50,898 : INFO : family: 42.4% (161/380)
2020-09-29 13:46:51,331 : INFO : gram1-adjective-to-adverb: 3.0% (30/992)
2020-09-29 13:46:51,636 : INFO : gram2-opposite: 5.8% (38/650)
2020-09-29 13:46:52,206 : INFO : gram3-comparative: 33.0% (439/1332)
2020-09-29 13:46:52,668 : INFO : gram4-superlative: 15.4% (163/1056)
2020-09-29 13:46:53,103 : INFO : gram5-present-participle: 20.9% (207/992)
2020-09-29 13:46:53,697 : INFO : gram6-nationality-adjective: 10.2% (133/1299)
2020-09-29 13:46:54,377 : INFO : gram7-past-tense: 26.7% (417/1560)
2020-09-29 13:46:54,913 : INFO : gram8-plural: 15.0% (178/1190)
2020-09-29 13:46:55,264 : INFO : gram9-plural-verbs: 11.6% (94/812)
2020-09-29 13:46:55,264 : INFO : Quadruplets with out-of-vocabulary words: 29.8%
2020-09-29 13:46:55,264 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 13:46:55,264 : INFO : Total accuracy: 15.0% (2058/13724)
Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6): 15.00% correct (2058 of 13724)


[+] questions-words-narrowed.txt
2020-09-29 13:46:55,285 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-29 13:46:55,455 : INFO : family: 42.4% (161/380)
2020-09-29 13:46:55,886 : INFO : gram1-adjective-to-adverb: 3.0% (30/992)
2020-09-29 13:46:56,195 : INFO : gram2-opposite: 5.8% (38/650)
2020-09-29 13:46:56,763 : INFO : gram3-comparative: 33.0% (439/1332)
2020-09-29 13:46:57,227 : INFO : gram4-superlative: 15.4% (163/1056)
2020-09-29 13:46:57,662 : INFO : gram5-present-participle: 20.9% (207/992)
2020-09-29 13:46:58,257 : INFO : gram6-nationality-adjective: 10.2% (133/1299)
2020-09-29 13:46:58,935 : INFO : gram7-past-tense: 26.7% (417/1560)
2020-09-29 13:46:59,473 : INFO : gram8-plural: 15.0% (178/1190)
2020-09-29 13:46:59,823 : INFO : gram9-plural-verbs: 11.6% (94/812)
2020-09-29 13:46:59,823 : INFO : Quadruplets with out-of-vocabulary words: 8.2%
2020-09-29 13:46:59,823 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 13:46:59,823 : INFO : Total accuracy: 18.1% (1860/10263)
Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n67,w5,mc99,s5e-05,t6): 18.12% correct (1860 of 10263)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-29 13:46:59,984 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5687
2020-09-29 13:46:59,985 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5703
2020-09-29 13:46:59,985 : INFO : Pairs with unknown words ratio: 2.5%
((0.5687247701708505, 7.221417816382574e-31), SpearmanrResult(correlation=0.5702785418875319, pvalue=4.601931250031061e-31), 2.5495750708215295)


02 - simlex999
2020-09-29 13:47:00,009 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3415
2020-09-29 13:47:00,009 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2993
2020-09-29 13:47:00,009 : INFO : Pairs with unknown words ratio: 0.5%
((0.34151148028625505, 1.4244628736862328e-28), SpearmanrResult(correlation=0.2992972932918391, pvalue=5.0972330033364e-22), 0.5005005005005005)


03 - simverb3500
2020-09-29 13:47:00,057 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1915
2020-09-29 13:47:00,058 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1721
2020-09-29 13:47:00,058 : INFO : Pairs with unknown words ratio: 6.0%
((0.19154593660930097, 1.5048111036198185e-28), SpearmanrResult(correlation=0.17205550381913115, pvalue=2.8507249496298e-23), 6.0285714285714285)


     ____________     COMPLETED      ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#


"""
