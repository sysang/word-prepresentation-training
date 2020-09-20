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
        epochs=20,
        min_alpha=0.0025,
        alpha=0.0025*1*20,
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    corpus = 'thefinal'

    base.train(corpus, common_kwargs, saved_fname)

"""
2020-09-19 16:28:23,584 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-19 16:28:23,584 : INFO : Loading a fresh vocabulary
2020-09-19 16:28:24,058 : INFO : effective_min_count=75 retains 70715 unique words (3% of original 1784839, drops 1714124)
2020-09-19 16:28:24,058 : INFO : effective_min_count=75 leaves 329482258 word corpus (98% of original 336075146, drops 6592888)
2020-09-19 16:28:24,216 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-19 16:28:24,251 : INFO : sample=5e-05 downsamples 730 most-common words
2020-09-19 16:28:24,251 : INFO : downsampling leaves estimated 148046269 word corpus (44.9% of prior 329482258)
2020-09-19 16:28:24,388 : INFO : estimated required memory for 70715 words and 15 dimensions: 866700700 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10)
Save model to: models/dmc_d15_n30_w3_mc75_s00005_mal=0025x1_ech20_thefinal.bin
2020-09-19 20:16:48,575 : INFO : saving Doc2Vec object under models/dmc_d15_n30_w3_mc75_s00005_mal=0025x1_ech20_thefinal.bin, separately None
2020-09-19 20:16:48,575 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n30_w3_mc75_s00005_mal=0025x1_ech20_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-19 20:16:48,604 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n30_w3_mc75_s00005_mal=0025x1_ech20_thefinal.bin.docvecs.vectors_docs.npy
2020-09-19 20:16:49,198 : INFO : saved models/dmc_d15_n30_w3_mc75_s00005_mal=0025x1_ech20_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 2872448
[+] index 2872448 -> "i am very sorry for you and i do not want to seem unfriendly but it is only a week since we met"
2020-09-19 20:16:49,208 : INFO : precomputing L2-norms of doc weight vectors
!! No any match in top 100 similarities


.....get random document, tag: 13256629
[+] index 13256629 -> "club owner line sister in atl with the fifteen names first true love what messed me up on this one was the word true"
** Matched with rank 1, score: 0.9801645278930664


.....get random document, tag: 1350940
[+] index 1350940 -> "your kindness where you have once placed it is inviolable and it is to that only i attribute my happiness in your love"
** Matched with rank 1, score: 0.9563242197036743


.....get random document, tag: 8755179
[+] index 8755179 -> "he then hoisted a red flag signalling huang zhong to attack"
** Matched with rank 1, score: 0.9616934061050415


.....get random document, tag: 5231965
[+] index 5231965 -> "france is great and all-great and at bottom he is france"
** Matched with rank 30, score: 0.8867785334587097


.....get random document, tag: 10906602
[+] index 10906602 -> "this morning we all headed out for breakfast and down to walk along the waterfront and throw rocks in dirty lake ontario then i came home went online and realized that i hadn't blogged in a while and that i have a bad habit of doing that so i decided that when i have nothing to blog about i am going to post the lyrics that the song i currently have on repeat in my cd player and car"
!! No any match in top 100 similarities


.....get random document, tag: 8199094
[+] index 8199094 -> "in the 1966 bbc radio serialization of the hobbit bilbo was played by paul daneman"
** Matched with rank 3, score: 0.9199991822242737




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (1072777): casaubon but of late chiefly with tantripp and their experienced courier

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):

MOST (9534103, 0.9451433420181274): «fuel supplies must be barged in via the oubangui river or trucked overland through cameroon resulting in frequent shortages of gasoline diesel and jet fuel»

MEDIAN (1705234, -0.0023486465215682983): «ve never thought that i had much courage physical courage but when i felt my watch was gone a sort of frenzy came over me»

LEAST (9024934, -0.9386278986930847): «the group of permutations on the rubik 's cube does not form a complete symmetric group of the 20 corner and face cubelets there are some final cube positions which can not be achieved through the legal manipulations of the cube»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'carmen' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
2020-09-19 20:17:13,814 : INFO : precomputing L2-norms of word weight vectors
     1. 0.95 'ravi'
     2. 0.94 'nana'
     3. 0.94 'gigi'
     4. 0.93 'tomas'
     5. 0.93 'coll'
     6. 0.93 'lia'
     7. 0.93 'gino'


[+] target_word: 'remembrance' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.92 'mourning'
     2. 0.91 'recollection'
     3. 0.90 'festivity'
     4. 0.89 'home-coming'
     5. 0.88 'glory'
     6. 0.88 'communion'
     7. 0.88 'tidings'


[+] target_word: 'princes' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.96 'grandees'
     2. 0.96 'nobles'
     3. 0.95 'barons'
     4. 0.95 'priestesses'
     5. 0.94 'potentates'
     6. 0.94 'eunuchs'
     7. 0.94 'templars'


[+] target_word: 'predictions' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.93 'results'
     2. 0.92 'sentence'
     3. 0.92 'diagnosis'
     4. 0.92 'diagnoses'
     5. 0.92 'back-story'
     6. 0.91 'revelations'
     7. 0.91 'backstory'


[+] target_word: 'witchcraft' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.95 'necromancy'
     2. 0.94 'sodomy'
     3. 0.94 'chivalry'
     4. 0.93 'pederasty'
     5. 0.93 'lycan'
     6. 0.92 'polygamy'
     7. 0.92 'satanism'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-19 20:17:14,291 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-19 20:17:14,602 : INFO : capital-common-countries: 4.0% (20/506)
2020-09-19 20:17:15,872 : INFO : capital-world: 3.3% (63/1929)
2020-09-19 20:17:16,036 : INFO : currency: 0.8% (2/236)
2020-09-19 20:17:17,636 : INFO : city-in-state: 2.1% (48/2330)
2020-09-19 20:17:17,977 : INFO : family: 32.6% (137/420)
2020-09-19 20:17:18,614 : INFO : gram1-adjective-to-adverb: 2.7% (27/992)
2020-09-19 20:17:19,147 : INFO : gram2-opposite: 2.7% (19/702)
2020-09-19 20:17:19,900 : INFO : gram3-comparative: 21.7% (289/1332)
2020-09-19 20:17:20,629 : INFO : gram4-superlative: 7.3% (77/1056)
2020-09-19 20:17:21,309 : INFO : gram5-present-participle: 13.3% (140/1056)
2020-09-19 20:17:22,376 : INFO : gram6-nationality-adjective: 7.4% (102/1371)
2020-09-19 20:17:23,467 : INFO : gram7-past-tense: 16.8% (262/1560)
2020-09-19 20:17:24,408 : INFO : gram8-plural: 7.9% (105/1332)
2020-09-19 20:17:25,080 : INFO : gram9-plural-verbs: 6.8% (59/870)
2020-09-19 20:17:25,081 : INFO : Quadruplets with out-of-vocabulary words: 19.7%
2020-09-19 20:17:25,081 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-19 20:17:25,081 : INFO : Total accuracy: 8.6% (1350/15692)
Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10): 8.60% correct (1350 of 15692)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-19 20:17:25,359 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4865
2020-09-19 20:17:25,359 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4862
2020-09-19 20:17:25,359 : INFO : Pairs with unknown words ratio: 0.6%
((0.486526931792038, 2.942324101486039e-22), SpearmanrResult(correlation=0.4861637407678516, pvalue=3.1920843292122356e-22), 0.56657223796034)


02 - simlex999
2020-09-19 20:17:25,415 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2792
2020-09-19 20:17:25,415 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2453
2020-09-19 20:17:25,415 : INFO : Pairs with unknown words ratio: 0.3%
((0.27920062530008394, 2.7194503837167596e-19), SpearmanrResult(correlation=0.24525589168226514, pvalue=4.139486523839522e-15), 0.3003003003003003)


03 - simverb3500
2020-09-19 20:17:25,698 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1647
2020-09-19 20:17:25,698 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1524
2020-09-19 20:17:25,698 : INFO : Pairs with unknown words ratio: 0.7%
((0.16470868523777496, 1.4944970710056815e-22), SpearmanrResult(correlation=0.15236827094634542, pvalue=1.7131919958969837e-19), 0.7428571428571429)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
