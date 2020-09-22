import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=67,
        window=5,
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

    pprint.pprint(common_kwargs)

    base.train(common_kwargs, saved_fname)

"""
2020-09-22 18:28:58,387 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-22 18:28:58,387 : INFO : Loading a fresh vocabulary
2020-09-22 18:28:58,826 : INFO : effective_min_count=99 retains 61077 unique words (3% of original 1784839, drops 1723762)
2020-09-22 18:28:58,826 : INFO : effective_min_count=99 leaves 328657804 word corpus (97% of original 336075146, drops 7417342)
2020-09-22 18:28:58,965 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-22 18:28:59,002 : INFO : sample=5e-05 downsamples 733 most-common words
2020-09-22 18:28:59,003 : INFO : downsampling leaves estimated 147142569 word corpus (44.8% of prior 328657804)
2020-09-22 18:28:59,112 : INFO : estimated required memory for 61077 words and 15 dimensions: 871913940 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc99,s5e-05,t6)
Save model to: models/dmc_d15_n67_w5_mc99_s00005_ech05_mal0002x25_thefinal.bin
2020-09-22 19:50:32,517 : INFO : saving Doc2Vec object under models/dmc_d15_n67_w5_mc99_s00005_ech05_mal0002x25_thefinal.bin, separately None
2020-09-22 19:50:32,517 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n67_w5_mc99_s00005_ech05_mal0002x25_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-22 19:50:32,546 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n67_w5_mc99_s00005_ech05_mal0002x25_thefinal.bin.docvecs.vectors_docs.npy
2020-09-22 19:50:33,230 : INFO : saved models/dmc_d15_n67_w5_mc99_s00005_ech05_mal0002x25_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 1584816
[+] index 1584816 -> "not if that peace be just and reasonable the bishop replied not if that peace can bring to an end this horrible and bloody struggle we shall see to that fenn declared with a self-satisfied air"
2020-09-22 19:50:33,241 : INFO : precomputing L2-norms of doc weight vectors
[*] Matched with rank 12, score: 0.8971623182296753!


.....get random document, tag: 6347537
[+] index 6347537 -> "i supposed it was classical music since it was not on the official score of jerry goldsmith"
    No any match in top 100 similarities.


.....get random document, tag: 12813277
[+] index 12813277 -> "the expression on her face is locked into isostasis lips pressed tremblingly hard against each other"
    No any match in top 100 similarities.


.....get random document, tag: 878029
[+] index 878029 -> "this one indispensable and at the same time sufficient expedient which meets at once the demands of justice and the growing exigencies of policy is to open the service of government in all its departments and in every part of the empire on perfectly equal terms to the inhabitants of the colonies"
    No any match in top 100 similarities.


.....get random document, tag: 6234809
[+] index 6234809 -> "other than that there 's pretty much nothing else to recommend"
    No any match in top 100 similarities.


.....get random document, tag: 5920743
[+] index 5920743 -> "there is no doubt about it al gore certainly presents his case very well and it is no wonder that this movie got the praise that it got"
    No any match in top 100 similarities.


.....get random document, tag: 7975292
[+] index 7975292 -> "dean was born in new york city to howard brush dean jr a former corporate executive and andrée belden maitland an art appraiser"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (8227976): economic growth has been further slowed by a largely dysfunctional banking system which has impeded access to capital-state-owned banks which control about three-fourths of deposits and loans and carry classified loan burdens of about 50%

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc99,s5e-05,t6):

MOST (4021126, 0.9357141256332397): «laud 's such at least had he been and so was he still called though his parish had been taken away from him and his place filled by a constitutional pastor that is by a priest who had taken the oath to the constitution required by the national assembly father jerome was banished from his church and deprived of the small emoluments of his office but he was not silenced for he still continued to perform the ceremonies of his religion sometimes in some gentleman 's drawing-room sometimes in a farmer 's house or a peasant 's cottage but oftener out in the open air under the shadow of a spreading beech on a rude altar hastily built for him with rocks and stones»

MEDIAN (3355999, 0.002624116837978363): «i do not grasp the connection between the last two remarks neither do vane admitted»

LEAST (2928360, -0.93410724401474): «denayrouze and company have a tank for the same purpose»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'dolphins' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc99,s5e-05,t6):
2020-09-22 19:50:58,910 : INFO : precomputing L2-norms of word weight vectors
     1. 0.95 'raptors'
     2. 0.95 'sharks'
     3. 0.95 'tigers'
     4. 0.93 'penguins'
     5. 0.92 'jaguars'
     6. 0.92 'caribou'
     7. 0.92 'falcons'


[+] target_word: 'ear' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.92 'finger'
     2. 0.92 'ears'
     3. 0.91 'fingertips'
     4. 0.91 'eyelid'
     5. 0.90 'eyebrow'
     6. 0.90 'lashes'
     7. 0.89 'lips'


[+] target_word: 'shelley' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.94 'fleeming'
     2. 0.94 'wollstonecraft'
     3. 0.92 'southey'
     4. 0.91 'wordsworth'
     5. 0.91 'keats'
     6. 0.90 'loren'
     7. 0.90 'flannery'


[+] target_word: 'lonesome' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.91 'lonely'
     2. 0.87 'dryad'
     3. 0.86 'sleepy'
     4. 0.84 'houseless'
     5. 0.84 'barefoot'
     6. 0.84 'merrier'
     7. 0.83 'blithe'


[+] target_word: 'pose' model: Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc99,s5e-05,t6):
     1. 0.91 'distracts'
     2. 0.89 'overact'
     3. 0.88 'interferes'
     4. 0.88 'balk'
     5. 0.87 'distort'
     6. 0.87 'amplify'
     7. 0.87 'simulating'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-22 19:50:59,479 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-22 19:50:59,821 : INFO : capital-common-countries: 9.3% (47/506)
2020-09-22 19:51:01,081 : INFO : capital-world: 6.7% (120/1779)
2020-09-22 19:51:01,196 : INFO : currency: 1.7% (3/178)
2020-09-22 19:51:02,627 : INFO : city-in-state: 3.1% (71/2267)
2020-09-22 19:51:02,929 : INFO : family: 36.2% (152/420)
2020-09-22 19:51:03,559 : INFO : gram1-adjective-to-adverb: 3.8% (38/992)
2020-09-22 19:51:03,934 : INFO : gram2-opposite: 6.0% (42/702)
2020-09-22 19:51:04,562 : INFO : gram3-comparative: 30.7% (409/1332)
2020-09-22 19:51:05,088 : INFO : gram4-superlative: 11.0% (116/1056)
2020-09-22 19:51:05,729 : INFO : gram5-present-participle: 21.4% (226/1056)
2020-09-22 19:51:06,614 : INFO : gram6-nationality-adjective: 16.0% (219/1371)
2020-09-22 19:51:07,613 : INFO : gram7-past-tense: 27.9% (435/1560)
2020-09-22 19:51:08,570 : INFO : gram8-plural: 15.6% (208/1332)
2020-09-22 19:51:09,167 : INFO : gram9-plural-verbs: 10.8% (94/870)
2020-09-22 19:51:09,168 : INFO : Quadruplets with out-of-vocabulary words: 21.1%
2020-09-22 19:51:09,168 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-22 19:51:09,168 : INFO : Total accuracy: 14.1% (2180/15421)
Doc2Vec("ech05,mal0002x25",dm/c,d15,n67,w5,mc99,s5e-05,t6): 14.14% correct (2180 of 15421)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-22 19:51:09,439 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5921
2020-09-22 19:51:09,439 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5706
2020-09-22 19:51:09,439 : INFO : Pairs with unknown words ratio: 0.6%
((0.5920592211955715, 1.4017453506364403e-34), SpearmanrResult(correlation=0.5706233511792246, pvalue=1.0380492528039562e-31), 0.56657223796034)


02 - simlex999
2020-09-22 19:51:09,489 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3375
2020-09-22 19:51:09,489 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2987
2020-09-22 19:51:09,489 : INFO : Pairs with unknown words ratio: 0.3%
((0.33750876746901587, 5.854373949220476e-28), SpearmanrResult(correlation=0.29869869667626203, pvalue=5.647390262299668e-22), 0.3003003003003003)


03 - simverb3500
2020-09-22 19:51:09,769 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1941
2020-09-22 19:51:09,769 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1787
2020-09-22 19:51:09,769 : INFO : Pairs with unknown words ratio: 1.4%
((0.19407803016980676, 1.1986797219760473e-30), SpearmanrResult(correlation=0.1786957556227481, pvalue=3.669723630743129e-26), 1.3714285714285714)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
