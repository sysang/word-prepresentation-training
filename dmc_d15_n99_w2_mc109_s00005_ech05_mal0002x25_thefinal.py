import doc2vec_training_script_multiprocessing as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=99,
        window=2,
        min_count=109,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*25*5,
        comment='ech05,mal0002x25',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
2020-09-21 22:09:14,297 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-21 22:09:14,297 : INFO : Loading a fresh vocabulary
2020-09-21 22:09:14,748 : INFO : effective_min_count=109 retains 58154 unique words (3% of original 1784839, drops 1726685)
2020-09-21 22:09:14,748 : INFO : effective_min_count=109 leaves 328355457 word corpus (97% of original 336075146, drops 7719689)
2020-09-21 22:09:14,882 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-21 22:09:14,916 : INFO : sample=5e-05 downsamples 734 most-common words
2020-09-21 22:09:14,916 : INFO : downsampling leaves estimated 146811086 word corpus (44.7% of prior 328355457)
2020-09-21 22:09:15,018 : INFO : estimated required memory for 58154 words and 15 dimensions: 847412440 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech05,mal0002x25",dm/c,d15,n99,w2,mc109,s5e-05,t6)
Save model to: models/dmc_d15_n99_w2_mc109_s00005_ech05_mal0002x25_thefinal.bin
2020-09-21 23:30:21,991 : INFO : saving Doc2Vec object under models/dmc_d15_n99_w2_mc109_s00005_ech05_mal0002x25_thefinal.bin, separately None
2020-09-21 23:30:21,992 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n99_w2_mc109_s00005_ech05_mal0002x25_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-21 23:30:22,021 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n99_w2_mc109_s00005_ech05_mal0002x25_thefinal.bin.docvecs.vectors_docs.npy
2020-09-21 23:30:22,548 : INFO : saved models/dmc_d15_n99_w2_mc109_s00005_ech05_mal0002x25_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 13012747
[+] index 13012747 -> "i support our military 100% and just recently got my own cell phone thank you honey which i am now in love with"
2020-09-21 23:30:22,559 : INFO : precomputing L2-norms of doc weight vectors
[*] Matched with rank 79, score: 0.8639085292816162!


.....get random document, tag: 2018184
[+] index 2018184 -> "but with the advance of wealth and the decay of faith among us the conscience seems to be simply conscientious or if it is otherwise it is social"
    No any match in top 100 similarities.


.....get random document, tag: 8567254
[+] index 8567254 -> "many of the concepts of science and philosophy are often defined culturally and socially"
    No any match in top 100 similarities.


.....get random document, tag: 4209896
[+] index 4209896 -> "he had himself been too busily engaged in satisfying the demands of the customers to look up and had not noticed that one of them was a white man"
    No any match in top 100 similarities.


.....get random document, tag: 5070624
[+] index 5070624 -> "again he was puzzled and did not know what to make of it"
    No any match in top 100 similarities.


.....get random document, tag: 6772780
[+] index 6772780 -> "other new styles such as cumbia pop and rock have seen increased popularity as the music of mexico faces a new generation of young people"
    No any match in top 100 similarities.


.....get random document, tag: 7260577
[+] index 7260577 -> "the racial makeup of the township is 95 54% white 2 29% african american 0 06% native american 1 09% asian 0 00% pacific islander 0 13% from other races and 0 90% from two or more races"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (12439554): the tongass a west virginia-size swath of rock and timber in southeastern alaska had been exempted from the clinton rule 's protections by an earlier decision

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x25",dm/c,d15,n99,w2,mc109,s5e-05,t6):

MOST (6928502, 0.9244863986968994): «quantum link or q-link was an american online service for commodore 64 and 128 personal computers that operated from november 5 1985 to november 1 1994»

MEDIAN (7745179, -0.003811746835708618): «in the city the population is spread out with 24 9% under the age of 18 9 1% from 18 to 24 31 3% from 25 to 44 19 9% from 45 to 64 and 14 8% who are 65 years of age or older»

LEAST (744152, -0.9321500062942505): «green would sooner part with life than part with a prejudice and he shook his head in the negative in a way to show that his mind was made up»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'obscured' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n99,w2,mc109,s5e-05,t6):
2020-09-21 23:30:49,057 : INFO : precomputing L2-norms of word weight vectors
     1. 0.93 'obliterated'
     2. 0.92 'blurred'
     3. 0.91 'illumined'
     4. 0.91 'glimpsed'
     5. 0.91 'accentuated'
     6. 0.91 'shadowed'
     7. 0.91 'irradiated'


[+] target_word: 'stead' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n99,w2,mc109,s5e-05,t6):
     1. 0.89 'death-bed'
     2. 0.88 'numerian'
     3. 0.88 'throne'
     4. 0.88 'bier'
     5. 0.87 'guardianship'
     6. 0.87 'marshalsea'
     7. 0.87 'majesty'


[+] target_word: 'tour' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n99,w2,mc109,s5e-05,t6):
     1. 0.96 'excursion'
     2. 0.92 'jamboree'
     3. 0.92 'voyage'
     4. 0.91 'roadtrip'
     5. 0.91 'trip'
     6. 0.90 'palaver'
     7. 0.90 'parade'


[+] target_word: 'supposing' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n99,w2,mc109,s5e-05,t6):
     1. 0.90 'justifies'
     2. 0.90 'compels'
     3. 0.89 'secondly'
     4. 0.88 'obliges'
     5. 0.88 'thirdly'
     6. 0.88 'believing'
     7. 0.87 "'even"


[+] target_word: 'book' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n99,w2,mc109,s5e-05,t6):
     1. 0.94 'diary'
     2. 0.94 'booklet'
     3. 0.94 'discography'
     4. 0.93 'blurb'
     5. 0.93 'fanzine'
     6. 0.92 'photo'
     7. 0.92 'love-letter'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-21 23:30:49,575 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-21 23:30:49,941 : INFO : capital-common-countries: 9.3% (47/506)
2020-09-21 23:30:51,137 : INFO : capital-world: 5.7% (93/1637)
2020-09-21 23:30:51,249 : INFO : currency: 3.4% (6/178)
2020-09-21 23:30:52,537 : INFO : city-in-state: 2.3% (53/2267)
2020-09-21 23:30:52,837 : INFO : family: 37.9% (159/420)
2020-09-21 23:30:53,500 : INFO : gram1-adjective-to-adverb: 3.8% (38/992)
2020-09-21 23:30:53,961 : INFO : gram2-opposite: 5.1% (36/702)
2020-09-21 23:30:54,636 : INFO : gram3-comparative: 31.4% (418/1332)
2020-09-21 23:30:55,313 : INFO : gram4-superlative: 11.0% (116/1056)
2020-09-21 23:30:55,814 : INFO : gram5-present-participle: 24.7% (261/1056)
2020-09-21 23:30:56,937 : INFO : gram6-nationality-adjective: 12.7% (174/1371)
2020-09-21 23:30:57,807 : INFO : gram7-past-tense: 28.1% (439/1560)
2020-09-21 23:30:58,762 : INFO : gram8-plural: 13.5% (180/1332)
2020-09-21 23:30:59,310 : INFO : gram9-plural-verbs: 12.8% (111/870)
2020-09-21 23:30:59,311 : INFO : Quadruplets with out-of-vocabulary words: 21.8%
2020-09-21 23:30:59,311 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-21 23:30:59,311 : INFO : Total accuracy: 13.9% (2131/15279)
Doc2Vec("ech05,mal0002x25",dm/c,d15,n99,w2,mc109,s5e-05,t6): 13.95% correct (2131 of 15279)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-21 23:30:59,581 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5639
2020-09-21 23:30:59,581 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5583
2020-09-21 23:30:59,581 : INFO : Pairs with unknown words ratio: 0.6%
((0.5638553465846134, 7.572997753605884e-31), SpearmanrResult(correlation=0.5583429235201554, pvalue=3.695647424502264e-30), 0.56657223796034)


02 - simlex999
2020-09-21 23:30:59,626 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3205
2020-09-21 23:30:59,626 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2835
2020-09-21 23:30:59,626 : INFO : Pairs with unknown words ratio: 0.3%
((0.32047241440704505, 3.184347013178733e-25), SpearmanrResult(correlation=0.283507656315918, pvalue=7.242660941371214e-20), 0.3003003003003003)


03 - simverb3500
2020-09-21 23:30:59,902 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1810
2020-09-21 23:30:59,902 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1683
2020-09-21 23:30:59,902 : INFO : Pairs with unknown words ratio: 1.5%
((0.18103155057961828, 8.66473281900546e-27), SpearmanrResult(correlation=0.16828298661484753, pvalue=2.5481153308661618e-23), 1.4857142857142858)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
