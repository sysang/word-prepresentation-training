import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=50,
        negative=67,
        window=5,
        min_count=99,
        sample=0.001,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*20*5,
        comment='ech05,mal0002x20,refined',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(
                common_kwargs=common_kwargs,
                saved_fname=saved_fname,
                evaluate=False,
                database='refined'
            )

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


INFO: Training parameters: {'vector_size': 50, 'negative': 67, 'window': 5, 'min_count': 99, 'sample': 0.001, 'dm': 1, 'dm_concat': 1, 'hs': 0, 'epochs': 5, 'min_alpha': 0.0002, 'alpha': 0.02, 'comment': 'ech05,mal0002x20,refined'}
INFO: Model details: Doc2Vec("ech05,mal0002x20,refined",dm/c,d50,n67,w5,mc99,s0.001,t6)
INFO: Save model to: models/dmc_d50_n67_w5_mc99_s001_ech05_mal0002x20_refined.bin
2020-10-03 15:12:28,838 : INFO : saving Doc2Vec object under models/dmc_d50_n67_w5_mc99_s001_ech05_mal0002x20_refined.bin, separately None
2020-10-03 15:12:28,838 : INFO : storing np array 'syn1neg' to models/dmc_d50_n67_w5_mc99_s001_ech05_mal0002x20_refined.bin.trainables.syn1neg.npy
2020-10-03 15:12:28,888 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d50_n67_w5_mc99_s001_ech05_mal0002x20_refined.bin.trainables.vectors_docs_lockf.npy
2020-10-03 15:12:28,964 : INFO : storing np array 'vectors_docs' to models/dmc_d50_n67_w5_mc99_s001_ech05_mal0002x20_refined.bin.docvecs.vectors_docs.npy
2020-10-03 15:12:48,225 : INFO : saved models/dmc_d50_n67_w5_mc99_s001_ech05_mal0002x20_refined.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 16382047
-> index 16382047 --> "i do not know if you get my point"
2020-10-03 15:12:48,243 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 3534168
-> index 3534168 --> "many proud inner drapers totally recollect as the pathetic diets judge"
    No any match in top 200 similarities.


.....get random document, tag: 40964746
-> index 40964746 --> "they are godless enemies of life who wish to steal the title of jew from christ"
    No any match in top 200 similarities.


.....get random document, tag: 12989799
-> index 12989799 --> "yes but then we are not talking about gov"
    No any match in top 200 similarities.


.....get random document, tag: 21436662
-> index 21436662 --> "was there something in the movie press release that negated the possibility of the puny earthlings seeing it coming"
    No any match in top 200 similarities.


.....get random document, tag: 31860823
-> index 31860823 --> "every bushite death is a mercy on our souls so says the son to god as man of men"
    No any match in top 200 similarities.


.....get random document, tag: 44306322
-> index 44306322 --> "go get some czw ecw or xpw dvds instead"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (36814460): that 's a fine example of burrying your head in the sand

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x20,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):

MOST (39003444, 0.7272059917449951): «your pal diddler is a satanist or somethin weird like that»

MEDIAN (9002961, -0.0008566901087760925): «now there 's another interesting set of words coming from you»

LEAST (43725617, -0.7090765237808228): «then it came to pass that hodder carried back with him another armful of books»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'substance' model: Doc2Vec("ech05,mal0002x20,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):
2020-10-03 15:15:22,770 : INFO : precomputing L2-norms of word weight vectors
     1. 0.73 'inhibition'
     2. 0.71 'glutamate'
     3. 0.70 'smegma'
     4. 0.70 'neurotransmitter'
     5. 0.69 'residue'
     6. 0.69 'toxin'
     7. 0.69 'alchohol'


[+] target_word: 'rash' model: Doc2Vec("ech05,mal0002x20,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):
     1. 0.72 'sunburn'
     2. 0.71 'concussion'
     3. 0.71 'whiplash'
     4. 0.70 'impulsive'
     5. 0.69 'stuttering'
     6. 0.69 'sprain'
     7. 0.69 'relapse'


[+] target_word: 'buckets' model: Doc2Vec("ech05,mal0002x20,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):
     1. 1.00 'jugs'
     2. 1.00 'jars'
     3. 0.99 'powders'
     4. 0.99 'pens'
     5. 0.99 'envelopes'
     6. 0.99 'dusts'
     7. 0.99 'spoons'


[+] target_word: 'prohibited' model: Doc2Vec("ech05,mal0002x20,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):
     1. 0.88 'disallowed'
     2. 0.87 'banned'
     3. 0.84 'excluded'
     4. 0.80 'restricted'
     5. 0.79 'exempted'
     6. 0.79 'barred'
     7. 0.77 'exempt'


[+] target_word: 'narcissistic' model: Doc2Vec("ech05,mal0002x20,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):
     1. 0.87 'sociopathic'
     2. 0.83 'delusional'
     3. 0.81 'demented'
     4. 0.81 'deranged'
     5. 0.81 'psychotic'
     6. 0.80 'egotistical'
     7. 0.79 'masochistic'


[+] target_word: 'endorsement' model: Doc2Vec("ech05,mal0002x20,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):
     1. 0.80 'approval'
     2. 0.78 'recommendation'
     3. 0.77 'ultimatum'
     4. 0.76 'resignation'
     5. 0.75 'concession'
     6. 0.75 'apology'
     7. 0.74 'dismissal'


[+] target_word: 'borough' model: Doc2Vec("ech05,mal0002x20,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):
     1. 0.88 'terrace'
     2. 0.88 'parish'
     3. 0.87 'reservation'
     4. 0.87 'suburb'
     5. 0.85 'chapel'
     6. 0.83 'villa'
     7. 0.83 'neighbourhood'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words-narrowed.txt
2020-10-03 15:15:24,330 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-10-03 15:15:24,605 : INFO : family: 45.5% (191/420)
2020-10-03 15:15:25,211 : INFO : gram1-adjective-to-adverb: 8.1% (80/992)
2020-10-03 15:15:25,734 : INFO : gram2-opposite: 16.3% (123/756)
2020-10-03 15:15:26,610 : INFO : gram3-comparative: 40.5% (539/1332)
2020-10-03 15:15:27,159 : INFO : gram4-superlative: 31.7% (335/1056)
2020-10-03 15:15:27,840 : INFO : gram5-present-participle: 63.3% (668/1056)
2020-10-03 15:15:28,591 : INFO : gram6-nationality-adjective: 21.6% (280/1299)
2020-10-03 15:15:29,805 : INFO : gram7-past-tense: 48.6% (758/1560)
2020-10-03 15:15:30,630 : INFO : gram8-plural: 43.2% (514/1190)
2020-10-03 15:15:31,156 : INFO : gram9-plural-verbs: 67.1% (584/870)
2020-10-03 15:15:31,156 : INFO : Quadruplets with out-of-vocabulary words: 5.8%
2020-10-03 15:15:31,156 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-10-03 15:15:31,157 : INFO : Total accuracy: 38.7% (4072/10531)
Doc2Vec("ech05,mal0002x20,refined",dm/c,d50,n67,w5,mc99,s0.001,t6): 38.67% correct (4072 of 10531)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-10-03 15:15:31,240 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5348
2020-10-03 15:15:31,240 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5407
2020-10-03 15:15:31,240 : INFO : Pairs with unknown words ratio: 0.6%
((0.5347843852275528, 2.3439055521388364e-27), SpearmanrResult(correlation=0.5406939221265032, pvalue=4.87145216447811e-28), 0.56657223796034)


02 - simlex999
2020-10-03 15:15:31,920 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3512
2020-10-03 15:15:31,920 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.3434
2020-10-03 15:15:31,920 : INFO : Pairs with unknown words ratio: 0.5%
((0.3511634536829847, 3.200641338699655e-30), SpearmanrResult(correlation=0.34337765531489384, pvalue=6.909189914728092e-29), 0.5005005005005005)


03 - simverb3500
2020-10-03 15:15:32,000 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.2783
2020-10-03 15:15:32,000 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.2708
2020-10-03 15:15:32,000 : INFO : Pairs with unknown words ratio: 0.5%
((0.2782847930775759, 5.940312041491406e-63), SpearmanrResult(correlation=0.2707622333149607, pvalue=1.4493537915962e-59), 0.5142857142857142)


-----------------------------------------------------
Assess stability of inferencing vector
-----------------------------------------------------


Epochs=5 - nsamples=300
Execution time: 0.247802
Difference - avg: 11.381886; deviation: 1.049342
Difference over vector length: 7.1; avg length: 160.326019
Difference - min: 8.978155; max: 14.298186


-----------------------------------------------------
Benchmark similarity score with respect to theme word
-----------------------------------------------------


<EPOCHS: 3 - THRESHOLD: 00.25> - SCORE=52.00 - CONFIDENCE=96.00


<EPOCHS: 3 - THRESHOLD: 00.30> - SCORE=50.00 - CONFIDENCE=92.00




_____  COMPLETED  _________________________________
###~~~~~~~~#~~~~~~~#~~~~~~~#~~~~~~~~~~#~~~~~~~~~###

"""
