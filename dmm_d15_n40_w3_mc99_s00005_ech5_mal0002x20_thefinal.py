import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=40,
        window=3,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=0,
        hs=0,
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*20*5
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
2020-09-20 21:19:39,951 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-20 21:19:39,951 : INFO : Loading a fresh vocabulary
2020-09-20 21:19:40,421 : INFO : effective_min_count=99 retains 61077 unique words (3% of original 1784839, drops 1723762)
2020-09-20 21:19:40,421 : INFO : effective_min_count=99 leaves 328657804 word corpus (97% of original 336075146, drops 7417342)
2020-09-20 21:19:40,562 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-20 21:19:40,597 : INFO : sample=5e-05 downsamples 733 most-common words
2020-09-20 21:19:40,597 : INFO : downsampling leaves estimated 147142569 word corpus (44.8% of prior 328657804)
2020-09-20 21:19:40,714 : INFO : estimated required memory for 61077 words and 15 dimensions: 835267740 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/m,d15,n40,w3,mc99,s5e-05,t10)
Save model to: models/dmm_d15_n40_w3_mc99_s00005_ech5_mal0002x20_thefinal.bin
2020-09-20 23:30:35,725 : INFO : saving Doc2Vec object under models/dmm_d15_n40_w3_mc99_s00005_ech5_mal0002x20_thefinal.bin, separately None
2020-09-20 23:30:35,725 : INFO : storing np array 'vectors_docs_lockf' to models/dmm_d15_n40_w3_mc99_s00005_ech5_mal0002x20_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-20 23:30:35,754 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n40_w3_mc99_s00005_ech5_mal0002x20_thefinal.bin.docvecs.vectors_docs.npy
2020-09-20 23:30:36,151 : INFO : saved models/dmm_d15_n40_w3_mc99_s00005_ech5_mal0002x20_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 9291249
[+] index 9291249 -> "as such he was regarded by berengar himself and by his opponents dietwin of liege durand of troarne and humbert"
2020-09-20 23:30:36,160 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 100 similarities.


.....get random document, tag: 7725959
[+] index 7725959 -> "he stated that these paranormal abilities were something anyone could learn"
    No any match in top 100 similarities.


.....get random document, tag: 6649461
[+] index 6649461 -> "in 1996 hirst wrote and directed the short film hanging around starring eddie izzard"
    No any match in top 100 similarities.


.....get random document, tag: 9479185
[+] index 9479185 -> "when those three fundamental components fit together they sustain one another in explaining the whole of a social order hence constituting the theoretical account of a system"
    No any match in top 100 similarities.


.....get random document, tag: 11395812
[+] index 11395812 -> "i will be adding the rest of the lyrics as i have time"
    No any match in top 100 similarities.


.....get random document, tag: 5784785
[+] index 5784785 -> "the film comments on many other topics from big industry to police surveys spectatorship especially in relation to tragedies and on and on"
    No any match in top 100 similarities.


.....get random document, tag: 11614030
[+] index 11614030 -> "in other news i am putting out an apb on living space in pdx"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (6117894): is the child 's disease a physical manifestation of the family 's spiritual dis-ease following the father 's adultery good question to ponder

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/m,d15,n40,w3,mc99,s5e-05,t10):

MOST (2441126, 0.9813418388366699): «there is visible everywhere a simple and tender effort to recover some of the form of the temples which they had loved and to do honor to god by that which they were erecting while distress and humiliation prevented the desire and prudence precluded the admission either of luxury of ornament or magnificence of plan»

MEDIAN (3018698, 0.8028365969657898): «time you have not confessed i will not only sell all four of you»

LEAST (9646375, -0.9369908571243286): «the average household size is 2 44 and the average family size is 2 88»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'european' model: Doc2Vec(dm/m,d15,n40,w3,mc99,s5e-05,t10):
2020-09-20 23:31:02,453 : INFO : precomputing L2-norms of word weight vectors
     1. 0.90 'australian'
     2. 0.89 'continental'
     3. 0.88 'independent'
     4. 0.87 'nordic'
     5. 0.86 'commonwealth'
     6. 0.86 'indian'
     7. 0.86 'exception'


[+] target_word: 'await' model: Doc2Vec(dm/m,d15,n40,w3,mc99,s5e-05,t10):
     1. 0.94 'hasten'
     2. 0.89 'hastened'
     3. 0.89 'renew'
     4. 0.88 'reopen'
     5. 0.88 'depart'
     6. 0.87 'commence'
     7. 0.87 'purposed'


[+] target_word: 'volunteered' model: Doc2Vec(dm/m,d15,n40,w3,mc99,s5e-05,t10):
     1. 0.90 'advised'
     2. 0.88 'contacted'
     3. 0.87 'informed'
     4. 0.87 'requested'
     5. 0.87 'notified'
     6. 0.87 'pressured'
     7. 0.86 'advising'


[+] target_word: 'resolute' model: Doc2Vec(dm/m,d15,n40,w3,mc99,s5e-05,t10):
     1. 0.88 'coquette'
     2. 0.86 'courageous'
     3. 0.86 'imperious'
     4. 0.85 'defiant'
     5. 0.85 'fearless'
     6. 0.85 'instinctively'
     7. 0.85 'impetuous'


[+] target_word: 'character' model: Doc2Vec(dm/m,d15,n40,w3,mc99,s5e-05,t10):
     1. 0.96 'persona'
     2. 0.90 'protagonist'
     3. 0.86 'anti-hero'
     4. 0.85 'personality'
     5. 0.83 'genius'
     6. 0.83 'role'
     7. 0.83 'resemblance'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-20 23:31:03,000 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-20 23:31:03,317 : INFO : capital-common-countries: 11.7% (59/506)
2020-09-20 23:31:04,470 : INFO : capital-world: 6.0% (106/1779)
2020-09-20 23:31:04,579 : INFO : currency: 2.8% (5/178)
2020-09-20 23:31:06,105 : INFO : city-in-state: 2.5% (57/2267)
2020-09-20 23:31:06,401 : INFO : family: 44.3% (186/420)
2020-09-20 23:31:07,105 : INFO : gram1-adjective-to-adverb: 6.1% (61/992)
2020-09-20 23:31:07,656 : INFO : gram2-opposite: 4.1% (29/702)
2020-09-20 23:31:08,557 : INFO : gram3-comparative: 35.7% (475/1332)
2020-09-20 23:31:09,258 : INFO : gram4-superlative: 13.8% (146/1056)
2020-09-20 23:31:09,979 : INFO : gram5-present-participle: 20.3% (214/1056)
2020-09-20 23:31:10,937 : INFO : gram6-nationality-adjective: 16.9% (232/1371)
2020-09-20 23:31:11,996 : INFO : gram7-past-tense: 43.7% (682/1560)
2020-09-20 23:31:13,075 : INFO : gram8-plural: 26.4% (351/1332)
2020-09-20 23:31:13,690 : INFO : gram9-plural-verbs: 12.0% (104/870)
2020-09-20 23:31:13,690 : INFO : Quadruplets with out-of-vocabulary words: 21.1%
2020-09-20 23:31:13,690 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-20 23:31:13,690 : INFO : Total accuracy: 17.6% (2707/15421)
Doc2Vec(dm/m,d15,n40,w3,mc99,s5e-05,t10): 17.55% correct (2707 of 15421)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-20 23:31:13,960 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5463
2020-09-20 23:31:13,960 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5500
2020-09-20 23:31:13,960 : INFO : Pairs with unknown words ratio: 0.6%
((0.5463210793958542, 1.060062029982947e-28), SpearmanrResult(correlation=0.5499915500497499, pvalue=3.8594652814644523e-29), 0.56657223796034)


02 - simlex999
2020-09-20 23:31:14,007 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3404
2020-09-20 23:31:14,007 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2909
2020-09-20 23:31:14,007 : INFO : Pairs with unknown words ratio: 0.3%
((0.34035026993944695, 1.9687801805827845e-28), SpearmanrResult(correlation=0.29091955049763624, pvalue=7.036079846548258e-21), 0.3003003003003003)


03 - simverb3500
2020-09-20 23:31:14,284 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1929
2020-09-20 23:31:14,284 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1732
2020-09-20 23:31:14,284 : INFO : Pairs with unknown words ratio: 1.4%
((0.192888682023713, 2.7512729294952258e-30), SpearmanrResult(correlation=0.17318159087418827, pvalue=1.1968649447177272e-24), 1.3714285714285714)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#


"""
