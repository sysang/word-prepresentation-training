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
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*30*5,
        comment='ech05,mal0002*50,refined',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(
            common_kwargs=common_kwargs,
            saved_fname=saved_fname,
            evaluate=False,
            database='refined')

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech05,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6)
Save model to: models/dmc_d15_n72_w2_mc99_s0005_ech05_mal0002x30_refined.bin
2020-09-28 18:20:22,490 : INFO : saving Doc2Vec object under models/dmc_d15_n72_w2_mc99_s0005_ech05_mal0002x30_refined.bin, separately None
2020-09-28 18:20:22,490 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n72_w2_mc99_s0005_ech05_mal0002x30_refined.bin.trainables.vectors_docs_lockf.npy
2020-09-28 18:20:22,570 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n72_w2_mc99_s0005_ech05_mal0002x30_refined.bin.docvecs.vectors_docs.npy
2020-09-28 18:20:23,820 : INFO : saved models/dmc_d15_n72_w2_mc99_s0005_ech05_mal0002x30_refined.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 45539645
[+] index 45539645 -> "the thirteen moon calendar change peace movement is a grassroots movement around the world"
2020-09-28 18:20:23,832 : INFO : precomputing L2-norms of doc weight vectors
[*] Matched with rank 22, score: 0.9132252931594849!


.....get random document, tag: 41460294
[+] index 41460294 -> "get your firstly raining past depending on my network"
    No any match in top 200 similarities.


.....get random document, tag: 28632316
[+] index 28632316 -> "it just shows how natural it is to copy and share the things we like"
    No any match in top 200 similarities.


.....get random document, tag: 28132446
[+] index 28132446 -> "it is the upper caste hindus who fake their degrees that i am talking about"
    No any match in top 200 similarities.


.....get random document, tag: 11017155
[+] index 11017155 -> "this problem has stumped people into believing in reincarnation"
    No any match in top 200 similarities.


.....get random document, tag: 11786179
[+] index 11786179 -> "we can not smell goldsmiths unless dianna will angrily grasp afterwards"
    No any match in top 200 similarities.


.....get random document, tag: 5998530
[+] index 5998530 -> "battery weight is the mass of the container and it 's contents"
[*] Matched with rank 11, score: 0.9220291972160339!




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (28712481): the panel comes on the heels of the ailing leader 's surgery for intestinal bleeding two weeks ago

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):

MOST (28717443, 0.9784305095672607): «the panel comes on the heels of the ailing leader 's surgery for intestinal bleeding two weeks ago»

MEDIAN (27528963, -0.001655464991927147): «one of the big reasons for going was to try to make some progress where bush has failed»

LEAST (5767608, -0.9480517506599426): «british imperialism preserved where earlier islamic imperialism destroyed thousands of hindu temples»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'freeze' model: Doc2Vec("ech05,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):
2020-09-28 18:21:52,112 : INFO : precomputing L2-norms of word weight vectors
     1. 0.98 'plunge'
     2. 0.97 'sweep'
     3. 0.96 'bounce'
     4. 0.96 'float'
     5. 0.96 'squeeze'
     6. 0.96 'tighten'
     7. 0.95 'rebuild'


[+] target_word: 'behavioral' model: Doc2Vec("ech05,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):
     1. 0.98 'behavioural'
     2. 0.98 'epigenetic'
     3. 0.97 'physiological'
     4. 0.96 'sociological'
     5. 0.96 'biologic'
     6. 0.95 'amidase'
     7. 0.95 'biological'


[+] target_word: 'avoids' model: Doc2Vec("ech05,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):
     1. 0.95 'assesses'
     2. 0.94 'provokes'
     3. 0.94 'affords'
     4. 0.94 'resists'
     5. 0.94 'entails'
     6. 0.93 'strengthens'
     7. 0.93 'anticipates'


[+] target_word: 'ppl' model: Doc2Vec("ech05,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):
     1. 0.99 'people'
     2. 0.99 'poeple'
     3. 0.98 'peole'
     4. 0.98 'folks'
     5. 0.98 'peope'
     6. 0.98 'peopel'
     7. 0.97 'englishmen'


[+] target_word: 'altered' model: Doc2Vec("ech05,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):
     1. 0.97 'added'
     2. 0.97 'emulated'
     3. 0.96 'encapsulated'
     4. 0.96 'crafted'
     5. 0.96 'formalized'
     6. 0.96 'defined'
     7. 0.95 'rewritten'


[+] target_word: 'occurrence' model: Doc2Vec("ech05,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):
     1. 0.96 'element'
     2. 0.96 'occurance'
     3. 0.95 'occurence'
     4. 0.94 'demonstration'
     5. 0.93 'usage'
     6. 0.93 'adaptation'
     7. 0.92 'makeover'


[+] target_word: 'illustration' model: Doc2Vec("ech05,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6):
     1. 0.95 'writeup'
     2. 0.94 'screenplay'
     3. 0.94 'synopsis'
     4. 0.94 'quotation'
     5. 0.93 'description'
     6. 0.93 'narration'
     7. 0.93 'snippet'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-28 18:21:53,556 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-28 18:21:53,833 : INFO : capital-common-countries: 5.0% (23/462)
2020-09-28 18:21:54,534 : INFO : capital-world: 1.2% (14/1157)
2020-09-28 18:21:54,642 : INFO : currency: 1.7% (3/178)
2020-09-28 18:21:55,928 : INFO : city-in-state: 0.8% (18/2267)
2020-09-28 18:21:56,205 : INFO : family: 26.2% (110/420)
2020-09-28 18:21:56,759 : INFO : gram1-adjective-to-adverb: 1.6% (16/992)
2020-09-28 18:21:57,233 : INFO : gram2-opposite: 3.8% (29/756)
2020-09-28 18:21:57,908 : INFO : gram3-comparative: 15.4% (205/1332)
2020-09-28 18:21:58,531 : INFO : gram4-superlative: 5.4% (57/1056)
2020-09-28 18:21:59,179 : INFO : gram5-present-participle: 7.3% (77/1056)
2020-09-28 18:21:59,997 : INFO : gram6-nationality-adjective: 3.3% (43/1299)
2020-09-28 18:22:01,004 : INFO : gram7-past-tense: 6.3% (99/1560)
2020-09-28 18:22:01,785 : INFO : gram8-plural: 6.1% (72/1190)
2020-09-28 18:22:02,353 : INFO : gram9-plural-verbs: 11.1% (97/870)
2020-09-28 18:22:02,353 : INFO : Quadruplets with out-of-vocabulary words: 25.3%
2020-09-28 18:22:02,353 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-28 18:22:02,353 : INFO : Total accuracy: 5.9% (863/14595)
Doc2Vec("ech05,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6): 5.91% correct (863 of 14595)


[+] questions-words-narrowed.txt
2020-09-28 18:22:02,392 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-28 18:22:02,672 : INFO : family: 26.2% (110/420)
2020-09-28 18:22:03,233 : INFO : gram1-adjective-to-adverb: 1.6% (16/992)
2020-09-28 18:22:03,707 : INFO : gram2-opposite: 3.8% (29/756)
2020-09-28 18:22:04,384 : INFO : gram3-comparative: 15.4% (205/1332)
2020-09-28 18:22:05,004 : INFO : gram4-superlative: 5.4% (57/1056)
2020-09-28 18:22:05,655 : INFO : gram5-present-participle: 7.3% (77/1056)
2020-09-28 18:22:06,474 : INFO : gram6-nationality-adjective: 3.3% (43/1299)
2020-09-28 18:22:07,491 : INFO : gram7-past-tense: 6.3% (99/1560)
2020-09-28 18:22:08,272 : INFO : gram8-plural: 6.1% (72/1190)
2020-09-28 18:22:08,839 : INFO : gram9-plural-verbs: 11.1% (97/870)
2020-09-28 18:22:08,839 : INFO : Quadruplets with out-of-vocabulary words: 5.8%
2020-09-28 18:22:08,839 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-28 18:22:08,839 : INFO : Total accuracy: 7.6% (805/10531)
Doc2Vec("ech05,mal0002*50,refined",dm/c,d15,n72,w2,mc99,s0.0005,t6): 7.64% correct (805 of 10531)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-28 18:22:09,495 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3901
2020-09-28 18:22:09,495 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.3808
2020-09-28 18:22:09,495 : INFO : Pairs with unknown words ratio: 0.6%
((0.3901318988633248, 3.306029623798655e-14), SpearmanrResult(correlation=0.38075058862396766, pvalue=1.4901044760834779e-13), 0.56657223796034)


02 - simlex999
2020-09-28 18:22:10,143 : INFO : Pearson correlation coefficient against simlex999.txt: 0.1981
2020-09-28 18:22:10,143 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1709
2020-09-28 18:22:10,143 : INFO : Pairs with unknown words ratio: 0.5%
((0.1981479016625654, 2.940455128365322e-10), SpearmanrResult(correlation=0.1709021863229275, pvalue=5.9161843922120866e-08), 0.5005005005005005)


03 - simverb3500
2020-09-28 18:22:10,204 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1338
2020-09-28 18:22:10,204 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1308
2020-09-28 18:22:10,204 : INFO : Pairs with unknown words ratio: 0.5%
((0.13377906826422353, 2.246501041392735e-15), SpearmanrResult(correlation=0.13075643784513877, pvalue=9.464993062387122e-15), 0.5142857142857142)


     ____________     COMPLETED      ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
