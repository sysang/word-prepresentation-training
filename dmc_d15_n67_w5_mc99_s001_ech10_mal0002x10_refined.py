import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=67,
        window=5,
        min_count=99,
        sample=0.001,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=10,
        min_alpha=0.0002,
        alpha=0.0002*10*10,
        comment='ech10,mal0002x10,refined',
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
2020-09-30 13:07:37,723 : INFO : collected 877734 word types and 46020000 unique tags from a corpus of 46020000 examples and 610836932 words
2020-09-30 13:07:37,723 : INFO : Loading a fresh vocabulary
2020-09-30 13:07:37,965 : INFO : effective_min_count=99 retains 53059 unique words (6% of original 877734, drops 824675)
2020-09-30 13:07:37,966 : INFO : effective_min_count=99 leaves 606131238 word corpus (99% of original 610836932, drops 4705694)
2020-09-30 13:07:38,083 : INFO : deleting the raw counts dictionary of 877734 items
2020-09-30 13:07:38,100 : INFO : sample=0.001 downsamples 47 most-common words
2020-09-30 13:07:38,100 : INFO : downsampling leaves estimated 459319807 word corpus (75.8% of prior 606131238)
2020-09-30 13:07:38,185 : INFO : estimated required memory for 53059 words and 15 dimensions: 2825931980 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


INFO: Training parameters: {'vector_size': 15, 'negative': 67, 'window': 5, 'min_count': 99, 'sample': 0.001, 'dm': 1, 'dm_concat': 1, 'hs': 0, 'epochs': 10, 'min_alpha': 0.0002, 'alpha': 0.02, 'comment': 'ech10,mal0002x10,refined'}
INFO: Model details: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6)
INFO: Save model to: models/dmc_d15_n67_w5_mc99_s001_ech10_mal0002x10_refined.bin
2020-10-02 16:06:47,456 : INFO : saving Doc2Vec object under models/dmc_d15_n67_w5_mc99_s001_ech10_mal0002x10_refined.bin, separately None
2020-10-02 16:06:47,456 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n67_w5_mc99_s001_ech10_mal0002x10_refined.bin.trainables.vectors_docs_lockf.npy
2020-10-02 16:06:47,537 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n67_w5_mc99_s001_ech10_mal0002x10_refined.bin.docvecs.vectors_docs.npy
2020-10-02 16:06:49,172 : INFO : saved models/dmc_d15_n67_w5_mc99_s001_ech10_mal0002x10_refined.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 6085987
-> index 6085987 --> "he is of course a strong critic of israel and all those who exploit the holocaust in order to promote zionism"
2020-10-02 16:06:49,188 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 38288339
-> index 38288339 --> "she wants to recommend blank pins under sue 's fog"
    No any match in top 200 similarities.


.....get random document, tag: 24740923
-> index 24740923 --> "you are saying that someone must choose a side when faced with black and dark gray morality"
    No any match in top 200 similarities.


.....get random document, tag: 16031309
-> index 16031309 --> "he can dine the pathetic draper and taste it around its summer"
    No any match in top 200 similarities.


.....get random document, tag: 10196876
-> index 10196876 --> "bynum 's actions would have violated the right of expression granted mr"
    No any match in top 200 similarities.


.....get random document, tag: 26807333
-> index 26807333 --> "it may be cooler not to bring written notes but it 's not cheating"
    No any match in top 200 similarities.


.....get random document, tag: 33043062
-> index 33043062 --> "this case is eerily similar to the one where buddha was asked why he gave contradictory advice"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (15700137): you will not change me behaving through your sad sunshine

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):

MOST (15533049, 0.9384425282478333): «how did nell hate in back of all the carpenters»

MEDIAN (31715527, -0.0004780292510986328): «the opposite of gravitational pull is centrifugal push it 's as simple as that»

LEAST (22555880, -0.9611291289329529): «it would probably avert a certain amount of embarrassment and perhaps a little covert eye rolling by the duty officer but that 's about it»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'twat' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
2020-10-02 16:08:20,305 : INFO : precomputing L2-norms of word weight vectors
     1. 0.97 'gobshite'
     2. 0.97 'twit'
     3. 0.97 'bitch'
     4. 0.96 'skank'
     5. 0.96 'twerp'
     6. 0.96 'putz'
     7. 0.96 'clod'


[+] target_word: 'ann' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 1.00 'jay'
     2. 1.00 'neil'
     3. 1.00 'janet'
     4. 0.99 'charlie'
     5. 0.99 'anthony'
     6. 0.99 'jason'
     7. 0.99 'gregory'


[+] target_word: 'policeman' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.97 'waiter'
     2. 0.96 'landlord'
     3. 0.95 'homeowner'
     4. 0.95 'medic'
     5. 0.95 'chiropractor'
     6. 0.94 'trapper'
     7. 0.94 'counsellor'


[+] target_word: 'calcium' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.98 'iodine'
     2. 0.98 'sodium'
     3. 0.98 'potassium'
     4. 0.98 'ammonia'
     5. 0.97 'magnesium'
     6. 0.96 'yeast'
     7. 0.96 'chromium'


[+] target_word: 'zealand' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.99 'hampshire'
     2. 0.98 'jersey'
     3. 0.97 'york'
     4. 0.97 'orleans'
     5. 0.96 'brunswick'
     6. 0.95 'zealander'
     7. 0.95 'delhi'


[+] target_word: 'denver' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.98 'hampton'
     2. 0.98 'oakland'
     3. 0.98 'jacksonville'
     4. 0.98 'birmingham'
     5. 0.97 'valencia'
     6. 0.97 'memphis'
     7. 0.97 'syracuse'


[+] target_word: 'cases' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.97 'contexts'
     2. 0.96 'usages'
     3. 0.96 'professions'
     4. 0.96 'avenues'
     5. 0.96 'flavours'
     6. 0.96 'disciplines'
     7. 0.96 'inventions'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words-narrowed.txt
2020-10-02 16:08:21,739 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-10-02 16:08:22,020 : INFO : family: 21.4% (90/420)
2020-10-02 16:08:22,587 : INFO : gram1-adjective-to-adverb: 1.9% (19/992)
2020-10-02 16:08:23,053 : INFO : gram2-opposite: 2.8% (21/756)
2020-10-02 16:08:23,753 : INFO : gram3-comparative: 9.9% (132/1332)
2020-10-02 16:08:24,338 : INFO : gram4-superlative: 4.0% (42/1056)
2020-10-02 16:08:25,036 : INFO : gram5-present-participle: 5.5% (58/1056)
2020-10-02 16:08:25,793 : INFO : gram6-nationality-adjective: 2.2% (28/1299)
2020-10-02 16:08:26,802 : INFO : gram7-past-tense: 7.0% (109/1560)
2020-10-02 16:08:27,584 : INFO : gram8-plural: 4.6% (55/1190)
2020-10-02 16:08:28,141 : INFO : gram9-plural-verbs: 8.4% (73/870)
2020-10-02 16:08:28,141 : INFO : Quadruplets with out-of-vocabulary words: 5.8%
2020-10-02 16:08:28,141 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-10-02 16:08:28,142 : INFO : Total accuracy: 6.0% (627/10531)
Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6): 5.95% correct (627 of 10531)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-10-02 16:08:28,191 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3356
2020-10-02 16:08:28,191 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.3712
2020-10-02 16:08:28,191 : INFO : Pairs with unknown words ratio: 0.6%
((0.335603540863674, 1.095047950759857e-10), SpearmanrResult(correlation=0.37120372305888705, pvalue=6.568441826071431e-13), 0.56657223796034)


02 - simlex999
2020-10-02 16:08:28,853 : INFO : Pearson correlation coefficient against simlex999.txt: 0.1962
2020-10-02 16:08:28,853 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1831
2020-10-02 16:08:28,853 : INFO : Pairs with unknown words ratio: 0.5%
((0.19617670021399586, 4.433682178136421e-10), SpearmanrResult(correlation=0.1831381518375, pvalue=6.029863046817443e-09), 0.5005005005005005)


03 - simverb3500
2020-10-02 16:08:28,917 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1329
2020-10-02 16:08:28,917 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1344
2020-10-02 16:08:28,917 : INFO : Pairs with unknown words ratio: 0.5%
((0.1328917035229529, 3.4384666357778763e-15), SpearmanrResult(correlation=0.13444666787139378, pvalue=1.6278493452997294e-15), 0.5142857142857142)


-----------------------------------------------------
Assess stability of inferencing vector
-----------------------------------------------------


Epochs=50
Difference - min: 0.039943; max: 0.252041; avg: 0.113062
Average length: 0.784004
Difference over vector length: 14.4


-----------------------------------------------------
Benchmark similarity score with respect to theme word
-----------------------------------------------------




_____  COMPLETED  _________________________________
###~~~~~~~~#~~~~~~~#~~~~~~~#~~~~~~~~~~#~~~~~~~~~###

"""
