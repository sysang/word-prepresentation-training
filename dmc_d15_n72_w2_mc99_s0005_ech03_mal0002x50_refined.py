import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=72,
        window=2,
        min_count=99,
        sample=0.0005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=3,
        min_alpha=0.0002,
        alpha=0.0002*50*3,
        comment='ech03,mal0002*50,refined',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(
            common_kwargs=common_kwargs,
            saved_fname=saved_fname,
            evaluate=False,
            database='refined')

"""
2020-09-28 09:52:11,725 : INFO : collected 877734 word types and 46020000 unique tags from a corpus of 46020000 examples and 610836932 words
2020-09-28 09:52:11,725 : INFO : Loading a fresh vocabulary
2020-09-28 09:52:11,964 : INFO : effective_min_count=99 retains 53059 unique words (6% of original 877734, drops 824675)
2020-09-28 09:52:11,964 : INFO : effective_min_count=99 leaves 606131238 word corpus (99% of original 610836932, drops 4705694)
2020-09-28 09:52:12,081 : INFO : deleting the raw counts dictionary of 877734 items
2020-09-28 09:52:12,098 : INFO : sample=0.0005 downsamples 88 most-common words
2020-09-28 09:52:12,098 : INFO : downsampling leaves estimated 411853197 word corpus (67.9% of prior 606131238)
2020-09-28 09:52:12,182 : INFO : estimated required memory for 53059 words and 15 dimensions: 2806830740 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech03,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6)
Save model to: models/dmc_d15_n72_w2_mc99_s0005_ech03_mal0002x50_refined.bin
2020-09-28 12:45:13,344 : INFO : saving Doc2Vec object under models/dmc_d15_n72_w2_mc99_s0005_ech03_mal0002x50_refined.bin, separately None
2020-09-28 12:45:13,344 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n72_w2_mc99_s0005_ech03_mal0002x50_refined.bin.trainables.vectors_docs_lockf.npy
2020-09-28 12:45:13,439 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n72_w2_mc99_s0005_ech03_mal0002x50_refined.bin.docvecs.vectors_docs.npy
2020-09-28 12:45:14,680 : INFO : saved models/dmc_d15_n72_w2_mc99_s0005_ech03_mal0002x50_refined.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 44853783
[+] index 44853783 -> "for several years he worked back and forth behind and in front of the microphone"
2020-09-28 12:45:14,694 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 43458619
[+] index 43458619 -> "then giorgio and the others came clattering to overtake them"
    No any match in top 200 similarities.


.....get random document, tag: 3381772
[+] index 3381772 -> "i just sat down and tried to draw it was very difficult"
    No any match in top 200 similarities.


.....get random document, tag: 1370221
[+] index 1370221 -> "it should jump the thin tyrant and cover it before its dorm"
    No any match in top 200 similarities.


.....get random document, tag: 42311713
[+] index 42311713 -> "it takes a disaster for someone to do this crime"
    No any match in top 200 similarities.


.....get random document, tag: 17322215
[+] index 17322215 -> "we can not throw to fancy dancy wars and expect them to pay for themselves yannow"
    No any match in top 200 similarities.


.....get random document, tag: 43202312
[+] index 43202312 -> "you can not patent distribution only a specific process"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (3261708): they are one of the few christian groups that as a whole walk their talk

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech03,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):

MOST (44334283, 0.948916494846344): «if you do not believe me see darkness falls or they»

MEDIAN (24427752, 0.001874077133834362): «other reports detail missions conducted by special operation forces charged with hunting down top insurgent commanders»

LEAST (12478754, -0.9566985964775085): «he will be irrigating about empty jay until his game cares wrongly»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'proposals' model: Doc2Vec("ech03,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):
2020-09-28 12:46:41,728 : INFO : precomputing L2-norms of word weight vectors
     1. 0.96 'directives'
     2. 0.95 'resolutions'
     3. 0.95 'guidelines'
     4. 0.95 'revisions'
     5. 0.94 'procedures'
     6. 0.94 'contracts'
     7. 0.94 'stipulations'


[+] target_word: 'multiply' model: Doc2Vec("ech03,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):
     1. 0.97 'weigh'
     2. 0.97 'characterise'
     3. 0.97 'embody'
     4. 0.97 'reproduce'
     5. 0.97 'inhibit'
     6. 0.97 'transmit'
     7. 0.97 'incorporate'


[+] target_word: 'advocated' model: Doc2Vec("ech03,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):
     1. 0.96 'condoned'
     2. 0.94 'cautioned'
     3. 0.93 'defended'
     4. 0.93 'feared'
     5. 0.92 'denied'
     6. 0.92 'objected'
     7. 0.91 'protested'


[+] target_word: 'arses' model: Doc2Vec("ech03,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):
     1. 0.97 'asses'
     2. 0.95 'butts'
     3. 0.95 'cocks'
     4. 0.94 'dicks'
     5. 0.92 'cats'
     6. 0.92 'privates'
     7. 0.92 'backsides'


[+] target_word: 'wwii' model: Doc2Vec("ech03,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):
     1. 0.99 'wwi'
     2. 0.97 'ww2'
     3. 0.95 'ww1'
     4. 0.94 'qana'
     5. 0.92 'dresden'
     6. 0.92 'samarra'
     7. 0.92 '1930s'


[+] target_word: 'upstairs' model: Doc2Vec("ech03,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):
     1. 0.97 'downstairs'
     2. 0.90 'berserk'
     3. 0.90 'overnight'
     4. 0.90 'silently'
     5. 0.88 'ashore'
     6. 0.88 'thither'
     7. 0.88 'feverishly'


[+] target_word: 'joie' model: Doc2Vec("ech03,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):
     1. 1.00 'sheri'
     2. 1.00 'nelly'
     3. 1.00 'tamara'
     4. 1.00 'selma'
     5. 1.00 'francine'
     6. 1.00 'usha'
     7. 1.00 'linette'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-28 12:46:43,138 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-28 12:46:43,390 : INFO : capital-common-countries: 3.0% (14/462)
2020-09-28 12:46:44,043 : INFO : capital-world: 0.7% (8/1157)
2020-09-28 12:46:44,153 : INFO : currency: 1.7% (3/178)
2020-09-28 12:46:45,430 : INFO : city-in-state: 0.8% (18/2267)
2020-09-28 12:46:45,709 : INFO : family: 37.4% (157/420)
2020-09-28 12:46:46,274 : INFO : gram1-adjective-to-adverb: 1.7% (17/992)
2020-09-28 12:46:46,746 : INFO : gram2-opposite: 3.0% (23/756)
2020-09-28 12:46:47,393 : INFO : gram3-comparative: 16.9% (225/1332)
2020-09-28 12:46:47,918 : INFO : gram4-superlative: 8.6% (91/1056)
2020-09-28 12:46:48,560 : INFO : gram5-present-participle: 8.3% (88/1056)
2020-09-28 12:46:49,364 : INFO : gram6-nationality-adjective: 3.2% (42/1299)
2020-09-28 12:46:50,373 : INFO : gram7-past-tense: 6.0% (93/1560)
2020-09-28 12:46:51,130 : INFO : gram8-plural: 9.3% (111/1190)
2020-09-28 12:46:51,680 : INFO : gram9-plural-verbs: 13.4% (117/870)
2020-09-28 12:46:51,680 : INFO : Quadruplets with out-of-vocabulary words: 25.3%
2020-09-28 12:46:51,681 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-28 12:46:51,681 : INFO : Total accuracy: 6.9% (1007/14595)
Doc2Vec("ech03,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6): 6.90% correct (1007 of 14595)


[+] questions-words-narrowed.txt
2020-09-28 12:46:51,721 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-28 12:46:52,004 : INFO : family: 37.4% (157/420)
2020-09-28 12:46:52,574 : INFO : gram1-adjective-to-adverb: 1.7% (17/992)
2020-09-28 12:46:53,046 : INFO : gram2-opposite: 3.0% (23/756)
2020-09-28 12:46:53,697 : INFO : gram3-comparative: 16.9% (225/1332)
2020-09-28 12:46:54,225 : INFO : gram4-superlative: 8.6% (91/1056)
2020-09-28 12:46:54,867 : INFO : gram5-present-participle: 8.3% (88/1056)
2020-09-28 12:46:55,673 : INFO : gram6-nationality-adjective: 3.2% (42/1299)
2020-09-28 12:46:56,684 : INFO : gram7-past-tense: 6.0% (93/1560)
2020-09-28 12:46:57,443 : INFO : gram8-plural: 9.3% (111/1190)
2020-09-28 12:46:57,994 : INFO : gram9-plural-verbs: 13.4% (117/870)
2020-09-28 12:46:57,995 : INFO : Quadruplets with out-of-vocabulary words: 5.8%
2020-09-28 12:46:57,995 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-28 12:46:57,995 : INFO : Total accuracy: 9.2% (964/10531)
Doc2Vec("ech03,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6): 9.15% correct (964 of 10531)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-28 12:46:58,654 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4160
2020-09-28 12:46:58,654 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4067
2020-09-28 12:46:58,654 : INFO : Pairs with unknown words ratio: 0.6%
((0.416037464677603, 4.0002125318338395e-16), SpearmanrResult(correlation=0.4066916167350337, pvalue=2.056216016795035e-15), 0.56657223796034)


02 - simlex999
2020-09-28 12:46:59,309 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2115
2020-09-28 12:46:59,309 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1851
2020-09-28 12:46:59,309 : INFO : Pairs with unknown words ratio: 0.5%
((0.2114947358846288, 1.6291384594019995e-11), SpearmanrResult(correlation=0.1850983654837329, pvalue=4.1208006995843015e-09), 0.5005005005005005)


03 - simverb3500
2020-09-28 12:46:59,371 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1260
2020-09-28 12:46:59,371 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1268
2020-09-28 12:46:59,371 : INFO : Pairs with unknown words ratio: 0.5%
((0.12596468807497968, 8.64920256001516e-14), SpearmanrResult(correlation=0.12676933847885916, pvalue=5.999748339013885e-14), 0.5142857142857142)


     ____________     COMPLETED      ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
