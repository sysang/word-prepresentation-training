import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15, negative=18, window=2, min_count=60, sample=0.0001,
        dm=1, dm_concat=1, hs=0, epochs=5
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    corpus = 'thefinal'

    base.train(corpus, common_kwargs, saved_fname)

"""
2020-09-18 20:32:58,934 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-18 20:32:58,934 : INFO : Loading a fresh vocabulary
2020-09-18 20:32:59,412 : INFO : effective_min_count=60 retains 79424 unique words (4% of original 1784839, drops 1705415)
2020-09-18 20:32:59,412 : INFO : effective_min_count=60 leaves 330061954 word corpus (98% of original 336075146, drops 6013192)
2020-09-18 20:32:59,589 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-18 20:32:59,626 : INFO : sample=0.0001 downsamples 380 most-common words
2020-09-18 20:32:59,626 : INFO : downsampling leaves estimated 170789420 word corpus (51.7% of prior 330061954)
2020-09-18 20:32:59,783 : INFO : estimated required memory for 79424 words and 15 dimensions: 865704640 bytes

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n18,w2,mc60,s0.0001,t10)
Save model to: models/dmc_d18_n15_w2_mc60_s0001_ech05_thefinal.bin
2020-09-18 21:51:22,598 : INFO : saving Doc2Vec object under models/dmc_d18_n15_w2_mc60_s0001_ech05_thefinal.bin, separately None
2020-09-18 21:51:22,598 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d18_n15_w2_mc60_s0001_ech05_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-18 21:51:22,632 : INFO : storing np array 'vectors_docs' to models/dmc_d18_n15_w2_mc60_s0001_ech05_thefinal.bin.docvecs.vectors_docs.npy
2020-09-18 21:51:23,202 : INFO : saved models/dmc_d18_n15_w2_mc60_s0001_ech05_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 6170799
[+] index 6170799 -> "the characters in this were down to earth and you could just absorb the boys as if they were your own i saw it at the atlanta film festival and hope that it gets a nationwide release eventually"
2020-09-18 21:51:23,211 : INFO : precomputing L2-norms of doc weight vectors
!! No any match in top 100 similarities


.....get random document, tag: 8969822
[+] index 8969822 -> "at european level the pds co-founded the european left alliance of parties and the left party is the largest party in the european parliament 's european united left/nordic green left parliamentary group"
!! No any match in top 100 similarities


.....get random document, tag: 10179950
[+] index 10179950 -> "these plans were disrupted however by at least two distinct factors"
!! No any match in top 100 similarities


.....get random document, tag: 9314446
[+] index 9314446 -> "myth asserts that hasidic couples have intercourse through a sheet with holes in it a false assertion"
!! No any match in top 100 similarities


.....get random document, tag: 656709
[+] index 656709 -> "when the time came for payment he saw her flinch"
!! No any match in top 100 similarities


.....get random document, tag: 6807397
[+] index 6807397 -> "dre was eventually dissed by 2pac because he had not testified for snoop at the rapper 's murder trial because he had left death row and because he had discouraged the west coast-east coast beef"
!! No any match in top 100 similarities


.....get random document, tag: 7229527
[+] index 7229527 -> "which is howard 's contribution curry being committed to the combinator which is more like writing everything in a machine language for which the lambda calculus is a high-level language more recently extensions of the curry-howard correspondence have been formulated which handle classical logic as well by relating classically valid rules such as double negation elimination and peirce 's law to the types of terms which explicitly deal with continuations such as call/cc"
!! No any match in top 100 similarities




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (4510911): the first fruits of this unfortunate leisure were a bitter quarrel with hume one of the most famous and far-resounding of all the quarrels of illustrious men but one about which very little needs now be said

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n18,w2,mc60,s0.0001,t10):

MOST (7793024, 0.9381083250045776): «incidence of back pain in western countries has increased in recent years»

MEDIAN (261833, 0.009427517652511597): «at present those who have power dread a disturbance of the status quo lest their unjust privileges should be taken away»

LEAST (9947277, -0.9500764608383179): «though meaning maybe found in quilts without names as well»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'derives' model: Doc2Vec(dm/c,d15,n18,w2,mc60,s0.0001,t10):
2020-09-18 21:51:47,929 : INFO : precomputing L2-norms of word weight vectors
     1. 0.97 'derived'
     2. 0.95 'originates'
     3. 0.92 'shews'
     4. 0.92 'emanates'
     5. 0.91 'translates'
     6. 0.91 'identified'
     7. 0.90 'distinguishes'


[+] target_word: 'satellites' model: Doc2Vec(dm/c,d15,n18,w2,mc60,s0.0001,t10):
     1. 0.95 'probes'
     2. 0.94 'airships'
     3. 0.94 'radars'
     4. 0.92 'aeroplanes'
     5. 0.92 'planes'
     6. 0.92 'beacons'
     7. 0.91 'shuttles'


[+] target_word: 'fu' model: Doc2Vec(dm/c,d15,n18,w2,mc60,s0.0001,t10):
     1. 0.91 'foo'
     2. 0.89 'mein'
     3. 0.89 'con'
     4. 0.89 'hos'
     5. 0.88 'wo'
     6. 0.88 'puro'
     7. 0.88 'bi'


[+] target_word: 'offered' model: Doc2Vec(dm/c,d15,n18,w2,mc60,s0.0001,t10):
     1. 0.93 'requested'
     2. 0.93 'arranges'
     3. 0.92 'prepared'
     4. 0.92 'prepares'
     5. 0.90 'selects'
     6. 0.90 'ordered'
     7. 0.90 'entitles'


[+] target_word: 'blushed' model: Doc2Vec(dm/c,d15,n18,w2,mc60,s0.0001,t10):
     1. 0.96 'sighed'
     2. 0.96 'smiled'
     3. 0.96 'pouted'
     4. 0.94 'winced'
     5. 0.93 'blushing'
     6. 0.91 'shuddered'
     7. 0.90 'chuckled'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-18 21:51:48,557 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-18 21:51:48,990 : INFO : capital-common-countries: 7.5% (38/506)
2020-09-18 21:51:51,002 : INFO : capital-world: 3.8% (86/2245)
2020-09-18 21:51:51,221 : INFO : currency: 1.3% (3/236)
2020-09-18 21:51:53,129 : INFO : city-in-state: 1.8% (43/2394)
2020-09-18 21:51:53,510 : INFO : family: 37.1% (156/420)
2020-09-18 21:51:54,228 : INFO : gram1-adjective-to-adverb: 3.9% (39/992)
2020-09-18 21:51:54,925 : INFO : gram2-opposite: 4.5% (34/756)
2020-09-18 21:51:56,086 : INFO : gram3-comparative: 26.6% (354/1332)
2020-09-18 21:51:57,104 : INFO : gram4-superlative: 10.4% (110/1056)
2020-09-18 21:51:57,948 : INFO : gram5-present-participle: 17.1% (181/1056)
2020-09-18 21:51:59,239 : INFO : gram6-nationality-adjective: 7.1% (98/1371)
2020-09-18 21:52:00,576 : INFO : gram7-past-tense: 19.6% (305/1560)
2020-09-18 21:52:01,841 : INFO : gram8-plural: 12.8% (170/1332)
2020-09-18 21:52:02,614 : INFO : gram9-plural-verbs: 8.3% (72/870)
2020-09-18 21:52:02,614 : INFO : Quadruplets with out-of-vocabulary words: 17.5%
2020-09-18 21:52:02,615 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-18 21:52:02,615 : INFO : Total accuracy: 10.5% (1689/16126)
Doc2Vec(dm/c,d15,n18,w2,mc60,s0.0001,t10): 10.47% correct (1689 of 16126)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-18 21:52:02,906 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5133
2020-09-18 21:52:02,906 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5075
2020-09-18 21:52:02,906 : INFO : Pairs with unknown words ratio: 0.6%
((0.5132981618435437, 5.503903464971588e-25), SpearmanrResult(correlation=0.5074532286880973, pvalue=2.274879936378469e-24), 0.56657223796034)


02 - simlex999
2020-09-18 21:52:03,185 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3092
2020-09-18 21:52:03,185 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2680
2020-09-18 21:52:03,185 : INFO : Pairs with unknown words ratio: 0.3%
((0.3092098151183613, 1.6500322335591935e-23), SpearmanrResult(correlation=0.2679561653714011, pvalue=7.715220756983893e-18), 0.3003003003003003)


03 - simverb3500
2020-09-18 21:52:03,491 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1785
2020-09-18 21:52:03,491 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1651
2020-09-18 21:52:03,491 : INFO : Pairs with unknown words ratio: 0.7%
((0.17852301733340448, 2.725357607060573e-26), SpearmanrResult(correlation=0.16506244956788976, pvalue=1.1614215798145263e-22), 0.6571428571428571)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
