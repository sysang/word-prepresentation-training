import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=67,
        window=5,
        min_count=999,
        sample=0.00002,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=3,
        min_alpha=0.0002,
        alpha=0.0002*50*3,
        comment='ech03,mal0002x50',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(common_kwargs, saved_fname)

"""
2020-09-24 07:49:19,892 : INFO : collected 8416415 word types and 141275000 unique tags from a corpus of 141275000 examples and 2464282844 words
2020-09-24 07:49:19,892 : INFO : Loading a fresh vocabulary
2020-09-24 07:49:21,705 : INFO : effective_min_count=999 retains 54133 unique words (0% of original 8416415, drops 8362282)
2020-09-24 07:49:21,705 : INFO : effective_min_count=999 leaves 2384652225 word corpus (96% of original 2464282844, drops 79630619)
2020-09-24 07:49:21,836 : INFO : deleting the raw counts dictionary of 8416415 items
2020-09-24 07:49:22,003 : INFO : sample=2e-05 downsamples 2019 most-common words
2020-09-24 07:49:22,003 : INFO : downsampling leaves estimated 904927488 word corpus (37.9% of prior 2384652225)
2020-09-24 07:49:22,106 : INFO : estimated required memory for 54133 words and 15 dimensions: 8542542260 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech03,mal0002x50",dm/c,d15,n67,w5,mc999,s2e-05,t6)
Save model to: models/dmc_d15_n67_w5_mc999_s00002_ech03_mal0002x50_elephant.bin
2020-09-24 17:35:11,336 : INFO : saving Doc2Vec object under models/dmc_d15_n67_w5_mc999_s00002_ech03_mal0002x50_elephant.bin, separately None
2020-09-24 17:35:11,337 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n67_w5_mc999_s00002_ech03_mal0002x50_elephant.bin.trainables.vectors_docs_lockf.npy
2020-09-24 17:35:11,599 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n67_w5_mc999_s00002_ech03_mal0002x50_elephant.bin.docvecs.vectors_docs.npy
2020-09-24 17:35:32,019 : INFO : saved models/dmc_d15_n67_w5_mc999_s00002_ech03_mal0002x50_elephant.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 86147182
[+] index 86147182 -> "yet it does not seem to be much of a problem for stores and other businesses named for families, but without an apostrophe"
2020-09-24 17:35:32,161 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 1000 similarities.


.....get random document, tag: 104413957
[+] index 104413957 -> "i think i will skip the vigil, the last time i went to that was when i was confirmed, and i was not sure the reading of the saints was ever going to stop"
    No any match in top 1000 similarities.


.....get random document, tag: 41634987
[+] index 41634987 -> ""be who you are and say what you feel"
    No any match in top 1000 similarities.


.....get random document, tag: 86045011
[+] index 86045011 -> ""i am not a professional, i am an artist.""
    No any match in top 1000 similarities.


.....get random document, tag: 56155672
[+] index 56155672 -> "nonsense, belief in creationism requires a belief in god"
[*] Matched with rank 6, score: 0.9358531832695007!


.....get random document, tag: 96990896
[+] index 96990896 -> "..the how and why can be found by looking at the shadow party and george soros"
    No any match in top 1000 similarities.


.....get random document, tag: 38774675
[+] index 38774675 -> "whenever i look for something, it 's always in the last place i look"
    No any match in top 1000 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (4609638): my solid cap will not pour before i join it

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech03,mal0002x50",dm/c,d15,n67,w5,mc999,s2e-05,t6):

MOST (140185193, 0.9504772424697876): «i need to do crunches and not sit ups»

MEDIAN (134812204, -0.0009552687406539917): «in the town the population is spread out with 27.6% under the age of 18, 6.8% from 18 to 24, 26.3% from 25 to 44, 27.4% from 45 to 64, and 11.9% who are 65 years of age or older»

LEAST (13528113, -0.9466480612754822): «they are laughing below clever, with sharp, around unique shopkeepers»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'seamlessly' model: Doc2Vec("ech03,mal0002x50",dm/c,d15,n67,w5,mc999,s2e-05,t6):
2020-09-24 17:41:30,420 : INFO : precomputing L2-norms of word weight vectors
     1. 0.88 'flawlessly'
     2. 0.88 'jvm'
     3. 0.86 'internals'
     4. 0.85 'opengl'
     5. 0.85 'parallel,'
     6. 0.85 'platforms'
     7. 0.85 'dimmer'


[+] target_word: 'grynszpan' model: Doc2Vec("ech03,mal0002x50",dm/c,d15,n67,w5,mc999,s2e-05,t6):
     1. 0.91 'lived,'
     2. 0.90 'survived,'
     3. 0.88 'born,'
     4. 0.88 'knew,'
     5. 0.87 'remained,'
     6. 0.87 'seen,'
     7. 0.86 'was'


[+] target_word: 'hating' model: Doc2Vec("ech03,mal0002x50",dm/c,d15,n67,w5,mc999,s2e-05,t6):
     1. 0.91 'obsequious'
     2. 0.91 'detest'
     . 0.91 'disliking'
     4. 0.90 'deceiving'
     5. 0.89 'dissing'
     6. 0.89 'taunt'
     7. 0.89 'behaving'


[+] target_word: 'wrong."' model: Doc2Vec("ech03,mal0002x50",dm/c,d15,n67,w5,mc999,s2e-05,t6):
     1. 0.91 'nothing,'
     2. 0.91 'wrong,'
     3. 0.89 'that;'
     4. 0.89 '.what'
     5. 0.88 'say"'
     6. 0.88 'nothing;'
     7. 0.87 'anything,'


[+] target_word: 'investigating' model: Doc2Vec("ech03,mal0002x50",dm/c,d15,n67,w5,mc999,s2e-05,t6):
     1. 0.94 'implicated'
     2. 0.91 'reporting'
     3. 0.91 'alerted'
     4. 0.90 'investigated'
     5. 0.89 'publicizing'
     6. 0.88 'charged'
     7. 0.88 'alleges'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-24 17:41:37,163 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-24 17:41:37,453 : INFO : capital-common-countries: 5.8% (27/462)
2020-09-24 17:41:38,024 : INFO : capital-world: 4.7% (41/877)
2020-09-24 17:41:38,048 : INFO : currency: 2.5% (1/40)
2020-09-24 17:41:38,769 : INFO : city-in-state: 2.0% (31/1520)
2020-09-24 17:41:39,028 : INFO : family: 44.5% (169/380)
2020-09-24 17:41:39,584 : INFO : gram1-adjective-to-adverb: 2.5% (25/992)
2020-09-24 17:41:39,886 : INFO : gram2-opposite: 3.1% (20/650)
2020-09-24 17:41:40,446 : INFO : gram3-comparative: 23.4% (312/1332)
2020-09-24 17:41:40,788 : INFO : gram4-superlative: 11.0% (109/992)
2020-09-24 17:41:41,248 : INFO : gram5-present-participle: 24.4% (258/1056)
2020-09-24 17:41:41,772 : INFO : gram6-nationality-adjective: 20.2% (262/1299)
2020-09-24 17:41:42,609 : INFO : gram7-past-tense: 29.3% (457/1560)
2020-09-24 17:41:43,343 : INFO : gram8-plural: 17.8% (200/1122)
2020-09-24 17:41:43,789 : INFO : gram9-plural-verbs: 19.7% (160/812)
2020-09-24 17:41:43,813 : INFO : Quadruplets with out-of-vocabulary words: 33.0%
2020-09-24 17:41:43,814 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-24 17:41:43,814 : INFO : Total accuracy: 15.8% (2072/13094)
Doc2Vec("ech03,mal0002x50",dm/c,d15,n67,w5,mc999,s2e-05,t6): 15.82% correct (2072 of 13094)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-24 17:41:43,905 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5261
2020-09-24 17:41:43,905 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5309
2020-09-24 17:41:43,905 : INFO : Pairs with unknown words ratio: 2.0%
((0.5260905826493151, 5.06379537814844e-26), SpearmanrResult(correlation=0.5308578248737833, pvalue=1.5079619033248292e-26), 1.9830028328611897)


02 - simlex999
2020-09-24 17:41:45,834 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3017
2020-09-24 17:41:45,834 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2575
2020-09-24 17:41:45,834 : INFO : Pairs with unknown words ratio: 0.6%
((0.3016969550848627, 2.4175738197140875e-22), SpearmanrResult(correlation=0.25748061194833693, pvalue=1.681514236313469e-16), 0.6006006006006006)


03 - simverb3500
2020-09-24 17:41:45,951 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1713
2020-09-24 17:41:45,952 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1586
2020-09-24 17:41:45,952 : INFO : Pairs with unknown words ratio: 2.3%
((0.1713392393257942, 6.140795100295193e-24), SpearmanrResult(correlation=0.15857515615979695, pvalue=1.0796091169118818e-20), 2.314285714285714)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
