import doc2vec_training_script_multiprocessing as base

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
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*25*5,
        comment='ech05,mal0002x25',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
2020-09-21 20:12:22,267 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-21 20:12:22,267 : INFO : Loading a fresh vocabulary
2020-09-21 20:12:22,701 : INFO : effective_min_count=99 retains 61077 unique words (3% of original 1784839, drops 1723762)
2020-09-21 20:12:22,701 : INFO : effective_min_count=99 leaves 328657804 word corpus (97% of original 336075146, drops 7417342)
2020-09-21 20:12:22,842 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-21 20:12:22,878 : INFO : sample=5e-05 downsamples 733 most-common words
2020-09-21 20:12:22,878 : INFO : downsampling leaves estimated 147142569 word corpus (44.8% of prior 328657804)
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w2,mc99,s5e-05,t6)
Save model to: models/dmc_d15_n40_w2_mc99_s00005_ech05_mal0002x25_thefinal.bin
2020-09-21 21:26:22,859 : INFO : saving Doc2Vec object under models/dmc_d15_n40_w2_mc99_s00005_ech05_mal0002x25_thefinal.bin, separately None
2020-09-21 21:26:22,860 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n40_w2_mc99_s00005_ech05_mal0002x25_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-21 21:26:22,887 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n40_w2_mc99_s00005_ech05_mal0002x25_thefinal.bin.docvecs.vectors_docs.npy
2020-09-21 21:26:23,423 : INFO : saved models/dmc_d15_n40_w2_mc99_s00005_ech05_mal0002x25_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 7623401
[+] index 7623401 -> "the origin of a tendon is where it joins to a muscle"
2020-09-21 21:26:23,433 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 100 similarities.


.....get random document, tag: 4962476
[+] index 4962476 -> "an artifice to keep on your legs said the pursuivants"
    No any match in top 100 similarities.


.....get random document, tag: 2678495
[+] index 2678495 -> "much was said against you by uncle at first and then by aunt mildred"
    No any match in top 100 similarities.


.....get random document, tag: 5735942
[+] index 5735942 -> "the script was a bit weak i am not sure why every time something bad happens the main character says oh my god every time"
    No any match in top 100 similarities.


.....get random document, tag: 10930689
[+] index 10930689 -> "you get extra credit for the slightest act of thoughtfulness"
    No any match in top 100 similarities.


.....get random document, tag: 5867490
[+] index 5867490 -> "they had a brief encounter which includes the drunk calling him a loser and the scarecrow rebounding with takes one to know one loser the scarecrow flips off the building calls him daddy-o and then beheads the poor man"
    No any match in top 100 similarities.


.....get random document, tag: 9525684
[+] index 9525684 -> "it can also be considered allegorically in a number of frameworks for example emotional"
[*] Matched with rank 81, score: 0.8580591678619385!




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (12146665): others will be offended as if i have insulted harry hermione and ron themselves by criticizing the actors who play them

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w2,mc99,s5e-05,t6):

MOST (8142270, 0.9376518726348877): «for the second performance kim pettersson guitar and johan defarfalla bass joined the group»

MEDIAN (1585912, -0.0014670789241790771): «the princess liked to entertain her guests in a fashion of her own»

LEAST (1640572, -0.9239090085029602): «a face came up out of the sea and brooded over the waters as in that picture of vedder 's which he calls memory but the hair was not blond it was the colour of those phosphorescent flames and the eyes were like it»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'collapsed' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w2,mc99,s5e-05,t6):
2020-09-21 21:26:49,173 : INFO : precomputing L2-norms of word weight vectors
     1. 0.94 'sunk'
     2. 0.92 'sank'
     3. 0.91 'halted'
     4. 0.91 'disintegrated'
     5. 0.90 'toppled'
     6. 0.90 'disappeared'
     7. 0.89 'receded'


[+] target_word: 'driving' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.95 'running'
     2. 0.95 'rowing'
     3. 0.94 'cruising'
     4. 0.93 'paddling'
     5. 0.93 'jogging'
     6. 0.93 'speeding'
     7. 0.93 'riding'


[+] target_word: 'flashed' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.94 'disappears'
     2. 0.92 'flared'
     3. 0.91 'vanishes'
     4. 0.91 'flickered'
     5. 0.91 'glared'
     6. 0.91 'gleamed'
     7. 0.91 'welling'


[+] target_word: 'wars' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.93 'massacre'
     2. 0.92 'combats'
     3. 0.90 'invasions'
     4. 0.89 'attacks'
     5. 0.89 'apocalypse'
     6. 0.89 'battles'
     7. 0.89 'bloodbath'


[+] target_word: 'cynthia' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.99 'annette'
     2. 0.99 'ethel'
     3. 0.99 'eliza'
     4. 0.98 'ellen'
     5. 0.98 'ruth'
     6. 0.98 'sylvia'
     7. 0.98 'rebecca'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-21 21:26:49,759 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-21 21:26:50,075 : INFO : capital-common-countries: 7.3% (37/506)
2020-09-21 21:26:51,330 : INFO : capital-world: 4.6% (82/1779)
2020-09-21 21:26:51,452 : INFO : currency: 3.4% (6/178)
2020-09-21 21:26:52,936 : INFO : city-in-state: 2.3% (53/2267)
2020-09-21 21:26:53,242 : INFO : family: 38.1% (160/420)
2020-09-21 21:26:53,864 : INFO : gram1-adjective-to-adverb: 4.4% (44/992)
2020-09-21 21:26:54,354 : INFO : gram2-opposite: 5.6% (39/702)
2020-09-21 21:26:55,142 : INFO : gram3-comparative: 28.3% (377/1332)
2020-09-21 21:26:55,626 : INFO : gram4-superlative: 12.5% (132/1056)
2020-09-21 21:26:56,390 : INFO : gram5-present-participle: 21.2% (224/1056)
2020-09-21 21:26:57,272 : INFO : gram6-nationality-adjective: 11.0% (151/1371)
2020-09-21 21:26:58,530 : INFO : gram7-past-tense: 29.9% (466/1560)
2020-09-21 21:26:59,635 : INFO : gram8-plural: 16.8% (224/1332)
2020-09-21 21:27:00,257 : INFO : gram9-plural-verbs: 12.2% (106/870)
2020-09-21 21:27:00,258 : INFO : Quadruplets with out-of-vocabulary words: 21.1%
2020-09-21 21:27:00,258 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-21 21:27:00,258 : INFO : Total accuracy: 13.6% (2101/15421)
Doc2Vec("ech05,mal0002x25",dm/c,d15,n40,w2,mc99,s5e-05,t6): 13.62% correct (2101 of 15421)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-21 21:27:00,530 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5520
2020-09-21 21:27:00,531 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5470
2020-09-21 21:27:00,531 : INFO : Pairs with unknown words ratio: 0.6%
((0.5520136203420518, 2.2002220872061477e-29), SpearmanrResult(correlation=0.5469502342761399, pvalue=8.922763512995732e-29), 0.56657223796034)


02 - simlex999
2020-09-21 21:27:00,585 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3235
2020-09-21 21:27:00,585 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2807
2020-09-21 21:27:00,585 : INFO : Pairs with unknown words ratio: 0.3%
((0.3234893064430234, 1.074458406024661e-25), SpearmanrResult(correlation=0.28065538672263274, pvalue=1.7439589926784067e-19), 0.3003003003003003)


03 - simverb3500
2020-09-21 21:27:00,866 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1805
2020-09-21 21:27:00,866 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1641
2020-09-21 21:27:00,866 : INFO : Pairs with unknown words ratio: 1.4%
((0.1805218323574807, 1.1284840423109273e-26), SpearmanrResult(correlation=0.16406691078828375, pvalue=2.9604878294551534e-22), 1.3714285714285714)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#


"""
