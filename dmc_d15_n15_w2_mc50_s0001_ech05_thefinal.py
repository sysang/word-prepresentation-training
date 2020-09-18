# import doc2vec_training_script_mongodb_connect as base
import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15, negative=15, window=2, min_count=50, sample=0.0001,
        dm=1, dm_concat=1, hs=0, epochs=5
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    corpus = 'thefinal'

    base.train(corpus, common_kwargs, saved_fname)

"""
2020-09-18 17:56:41,563 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-18 17:56:41,563 : INFO : Loading a fresh vocabulary
2020-09-18 17:56:42,054 : INFO : effective_min_count=50 retains 87552 unique words (4% of original 1784839, drops 1697287)
2020-09-18 17:56:42,055 : INFO : effective_min_count=50 leaves 330503050 word corpus (98% of original 336075146, drops 5572096)
2020-09-18 17:56:42,252 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-18 17:56:42,290 : INFO : sample=0.0001 downsamples 379 most-common words
2020-09-18 17:56:42,290 : INFO : downsampling leaves estimated 171274015 word corpus (51.8% of prior 330503050)

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n15,w2,mc50,s0.0001,t10)
Save model to: models/dmc_d15_n15_w2_mc50_s0001_ech10_thefinal.bin
2020-09-18 19:16:15,230 : INFO : saving Doc2Vec object under models/dmc_d15_n15_w2_mc50_s0001_ech10_thefinal.bin, separately None
2020-09-18 19:16:15,230 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n15_w2_mc50_s0001_ech10_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-18 19:16:15,259 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n15_w2_mc50_s0001_ech10_thefinal.bin.docvecs.vectors_docs.npy
2020-09-18 19:16:15,854 : INFO : saved models/dmc_d15_n15_w2_mc50_s0001_ech10_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 3752255
[+] index 3752255 -> "i knew her in london he replied 'in the algernon strange set"
2020-09-18 19:16:15,864 : INFO : precomputing L2-norms of doc weight vectors
!! No any match in top 100 similarities


.....get random document, tag: 12815548
[+] index 12815548 -> "phineas says be seeing you miss dvornik on campus"
!! No any match in top 100 similarities


.....get random document, tag: 5119235
[+] index 5119235 -> "though he stood within reach of the gunwale a gulf of three years was between"
!! No any match in top 100 similarities


.....get random document, tag: 7359299
[+] index 7359299 -> "13 4% of the population and 8 3% of families are below the poverty line"
!! No any match in top 100 similarities


.....get random document, tag: 6548937
[+] index 6548937 -> "likewise that the nerdy nebbish woody allen without the fixation on the adopted children of his mate gay guy who unfortunately for him was ten years ahead of the gay geek hotness era we find ourselves in and in any event hot gay geeks are not broadway musical fans much less piano players would be in love in classic hollywood romantic comedies from the 40s and 50s fashion with the gay hunk best pal and ultimately the hunk would for no reason at all without any real basis after turning him down because the neb was clearly not the hunk 's type and after lusting in love with a guy who 's only real thing in common with the neb is that they both have a musical background you might as well say that the hunk fell in love with them because they both breath air"
!! No any match in top 100 similarities


.....get random document, tag: 13247957
[+] index 13247957 -> "i went to ikea on friday night with my coworkers there were four of us just to get myself out of the house"
!! No any match in top 100 similarities


.....get random document, tag: 6579276
[+] index 6579276 -> "two years later esther made the 2nd place at the eurovision song contest with t'en vas pas representing switzerland"
!! No any match in top 100 similarities




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (4964524): i have a letter for you and no end of messages

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n15,w2,mc50,s0.0001,t10):

MOST (12165084, 0.9211899042129517): «hey it beats the fires of heck that heated my office last week that 's for sure oh there 's something i met someone who knows mollx 's girl»

MEDIAN (4715409, -0.006818369030952454): «so he made haste and opened the door quickly and instead of the wooden doll his wife sat in front of the fire»

LEAST (2758196, -0.9320861101150513): «it was a relief when he reappeared in time for supper and after that they set out again»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'guild' model: Doc2Vec(dm/c,d15,n15,w2,mc50,s0.0001,t10):
2020-09-18 19:16:40,825 : INFO : precomputing L2-norms of word weight vectors
     1. 0.93 'mogul'
     2. 0.90 'freeholder'
     3. 0.90 'lobbyist'
     4. 0.89 'stockbroker'
     5. 0.89 'librarian'
     6. 0.88 'organizer'
     7. 0.88 'spokesperson'


[+] target_word: 'speeches' model: Doc2Vec(dm/c,d15,n15,w2,mc50,s0.0001,t10):
     1. 0.94 'conversations'
     2. 0.94 'shenanigans'
     3. 0.93 'editorials'
     4. 0.93 'criticisms'
     5. 0.93 'rants'
     6. 0.92 'remarks'
     7. 0.92 'roles'


[+] target_word: 'seamen' model: Doc2Vec(dm/c,d15,n15,w2,mc50,s0.0001,t10):
     1. 0.98 'sailors'
     2. 0.97 'boatmen'
     3. 0.97 'convicts'
     4. 0.96 'recruits'
     5. 0.96 'conscripts'
     6. 0.96 'soldiers'
     7. 0.95 'dutchmen'


[+] target_word: 'salute' model: Doc2Vec(dm/c,d15,n15,w2,mc50,s0.0001,t10):
     1. 0.88 'salutes'
     2. 0.88 'summons'
     3. 0.85 'dispatches'
     4. 0.85 'tocsin'
     5. 0.85 'messenger'
     6. 0.84 'bodyguard'
     7. 0.84 'parley'


[+] target_word: 'spoof' model: Doc2Vec(dm/c,d15,n15,w2,mc50,s0.0001,t10):
     1. 0.97 'parody'
     2. 0.93 're-imagining'
     3. 0.92 'remake'
     4. 0.92 'spin-off'
     5. 0.91 'untitled'
     6. 0.91 'rap'
     7. 0.91 'fanfic'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-18 19:16:41,814 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-18 19:16:42,313 : INFO : capital-common-countries: 5.7% (29/506)
2020-09-18 19:16:44,803 : INFO : capital-world: 3.1% (77/2474)
2020-09-18 19:16:45,101 : INFO : currency: 1.3% (4/302)
2020-09-18 19:16:47,258 : INFO : city-in-state: 1.9% (45/2394)
2020-09-18 19:16:47,725 : INFO : family: 34.2% (158/462)
2020-09-18 19:16:48,623 : INFO : gram1-adjective-to-adverb: 3.9% (39/992)
2020-09-18 19:16:49,331 : INFO : gram2-opposite: 5.6% (42/756)
2020-09-18 19:16:50,358 : INFO : gram3-comparative: 27.9% (372/1332)
2020-09-18 19:16:51,175 : INFO : gram4-superlative: 10.1% (107/1056)
2020-09-18 19:16:51,933 : INFO : gram5-present-participle: 16.9% (178/1056)
2020-09-18 19:16:53,262 : INFO : gram6-nationality-adjective: 6.2% (85/1371)
2020-09-18 19:16:54,623 : INFO : gram7-past-tense: 20.7% (323/1560)
2020-09-18 19:16:55,976 : INFO : gram8-plural: 13.3% (177/1332)
2020-09-18 19:16:56,797 : INFO : gram9-plural-verbs: 9.2% (80/870)
2020-09-18 19:16:56,798 : INFO : Quadruplets with out-of-vocabulary words: 15.8%
2020-09-18 19:16:56,798 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-18 19:16:56,798 : INFO : Total accuracy: 10.4% (1716/16463)
Doc2Vec(dm/c,d15,n15,w2,mc50,s0.0001,t10): 10.42% correct (1716 of 16463)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-18 19:16:57,096 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5058
2020-09-18 19:16:57,096 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5026
2020-09-18 19:16:57,096 : INFO : Pairs with unknown words ratio: 0.6%
((0.5058015406101283, 3.3804186823608424e-24), SpearmanrResult(correlation=0.5025565146515777, pvalue=7.314836899654978e-24), 0.56657223796034)


02 - simlex999
2020-09-18 19:16:57,381 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3101
2020-09-18 19:16:57,381 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2685
2020-09-18 19:16:57,381 : INFO : Pairs with unknown words ratio: 0.3%
((0.31012978131594726, 1.2028231036832533e-23), SpearmanrResult(correlation=0.26847873248625476, pvalue=6.6271679584401396e-18), 0.3003003003003003)


03 - simverb3500
2020-09-18 19:16:57,692 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1826
2020-09-18 19:16:57,692 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1693
2020-09-18 19:16:57,692 : INFO : Pairs with unknown words ratio: 0.3%
((0.1825641772184722, 1.606999282589168e-27), SpearmanrResult(correlation=0.16928448341281574, pvalue=7.731949170516841e-24), 0.34285714285714286)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
