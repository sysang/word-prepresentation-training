import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=67,
        window=2,
        min_count=200,
        sample=0.00004,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=3,
        min_alpha=0.0002,
        alpha=0.0002*100*3,
        comment='ech03,mal0002x100',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(common_kwargs, saved_fname)

"""
2020-09-24 18:11:43,829 : INFO : collected 877734 word types and 46020000 unique tags from a corpus of 46020000 examples and 610836932 words
2020-09-24 18:11:43,829 : INFO : Loading a fresh vocabulary
2020-09-24 18:11:44,059 : INFO : effective_min_count=200 retains 38743 unique words (4% of original 877734, drops 838991)
2020-09-24 18:11:44,059 : INFO : effective_min_count=200 leaves 604107507 word corpus (98% of original 610836932, drops 6729425)
2020-09-24 18:11:44,147 : INFO : deleting the raw counts dictionary of 877734 items
2020-09-24 18:11:44,164 : INFO : sample=4e-05 downsamples 1051 most-common words
2020-09-24 18:11:44,164 : INFO : downsampling leaves estimated 249289843 word corpus (41.3% of prior 604107507)
2020-09-24 18:11:44,218 : INFO : estimated required memory for 38743 words and 15 dimensions: 2794518980 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech03,mal0002x100",dm/c,d15,n67,w2,mc200,s4e-05,t6)
Save model to: models/dmc_d15_n67_w2_mc200_s00004_ech03_mal0002x100_refined.bin
2020-09-24 21:08:58,680 : INFO : saving Doc2Vec object under models/dmc_d15_n67_w2_mc200_s00004_ech03_mal0002x100_refined.bin, separately None
2020-09-24 21:08:58,680 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n67_w2_mc200_s00004_ech03_mal0002x100_refined.bin.trainables.vectors_docs_lockf.npy
2020-09-24 21:08:58,759 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n67_w2_mc200_s00004_ech03_mal0002x100_refined.bin.docvecs.vectors_docs.npy
2020-09-24 21:08:59,963 : INFO : saved models/dmc_d15_n67_w2_mc200_s00004_ech03_mal0002x100_refined.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 35010865
[+] index 35010865 -> "you have completely different realities in each frame of reference"
2020-09-24 21:08:59,973 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 1000 similarities.


.....get random document, tag: 9326223
[+] index 9326223 -> "it should tax even if anastasia 's elbow is not tragic"
    No any match in top 1000 similarities.


.....get random document, tag: 3452909
[+] index 3452909 -> "we buy our oil in the norm al manner without the loss of our lower socioeconomic group 's lives"
    No any match in top 1000 similarities.


.....get random document, tag: 19164685
[+] index 19164685 -> "which all have an abundant supply of sea water"
    No any match in top 1000 similarities.


.....get random document, tag: 19039775
[+] index 19039775 -> "do not pay any attention to anything you are told on this newsgroup"
    No any match in top 1000 similarities.


.....get random document, tag: 24795555
[+] index 24795555 -> "by wednesday it discovered it was on its own"
    No any match in top 1000 similarities.


.....get random document, tag: 19785903
[+] index 19785903 -> "you do not seem to be reading what i wrote"
[*] Matched with rank 386, score: 0.8559703826904297!




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (2383403): i was also afforded the opportunity to meet amjad ali from the iraq freedom congress and a member of the planning committee of the conference

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech03,mal0002x100",dm/c,d15,n67,w2,mc200,s4e-05,t6):

MOST (7482107, 0.9595510959625244): «mary 's draper loves through our wrinkle after we measure before it»

MEDIAN (22080237, -0.001561598852276802): «my smart walnut will not dine before i climb it»

LEAST (45982381, -0.937039315700531): «aleks started to cry and say that he did not want to go»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'flesh' model: Doc2Vec("ech03,mal0002x100",dm/c,d15,n67,w2,mc200,s4e-05,t6):
2020-09-24 21:10:28,610 : INFO : precomputing L2-norms of word weight vectors
     1. 0.94 'foreskin'
     2. 0.93 'genitals'
     3. 0.92 'impurity'
     4. 0.91 'bones'
     5. 0.91 'womb'
     6. 0.91 'nectar'
     7. 0.90 'skin'


[+] target_word: 'boehner' model: Doc2Vec("ech03,mal0002x100",dm/c,d15,n67,w2,mc200,s4e-05,t6):
     1. 0.97 'kerry'
     2. 0.94 'mccain'
     3. 0.94 'francois'
     4. 0.94 'chirac'
     5. 0.93 'prescott'
     6. 0.93 'huckabee'
     7. 0.93 'truman'


[+] target_word: 'between' model: Doc2Vec("ech03,mal0002x100",dm/c,d15,n67,w2,mc200,s4e-05,t6):
     1. 0.93 'throughout'
     2. 0.93 'within'
     3. 0.93 'from'
     4. 0.91 'surrounding'
     5. 0.90 'in'
     6. 0.89 'according'
     7. 0.88 'among'


[+] target_word: 'watch' model: Doc2Vec("ech03,mal0002x100",dm/c,d15,n67,w2,mc200,s4e-05,t6):
     1. 0.95 'see'
     2. 0.94 'listen'
     3. 0.92 'chatting'
     4. 0.92 'talk'
     5. 0.91 'hear'
     6. 0.91 'seeing'
     7. 0.90 'play'


[+] target_word: 'flow' model: Doc2Vec("ech03,mal0002x100",dm/c,d15,n67,w2,mc200,s4e-05,t6):
     1. 0.93 'drain'
     2. 0.90 'overflow'
     3. 0.90 'conduction'
     4. 0.89 'footprint'
     5. 0.89 'radiating'
     6. 0.89 'radiated'
     7. 0.89 'buildup'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-24 21:10:29,276 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-24 21:10:29,463 : INFO : capital-common-countries: 4.5% (21/462)
2020-09-24 21:10:29,814 : INFO : capital-world: 1.2% (10/821)
2020-09-24 21:10:29,839 : INFO : currency: 1.9% (1/54)
2020-09-24 21:10:30,434 : INFO : city-in-state: 1.0% (18/1825)
2020-09-24 21:10:30,610 : INFO : family: 34.5% (131/380)
2020-09-24 21:10:31,033 : INFO : gram1-adjective-to-adverb: 2.9% (29/992)
2020-09-24 21:10:31,333 : INFO : gram2-opposite: 2.6% (17/650)
2020-09-24 21:10:31,785 : INFO : gram3-comparative: 16.3% (217/1332)
2020-09-24 21:10:32,106 : INFO : gram4-superlative: 5.1% (54/1056)
2020-09-24 21:10:32,505 : INFO : gram5-present-participle: 17.8% (188/1056)
2020-09-24 21:10:33,013 : INFO : gram6-nationality-adjective: 8.1% (99/1229)
2020-09-24 21:10:33,668 : INFO : gram7-past-tense: 20.1% (313/1560)
2020-09-24 21:10:34,174 : INFO : gram8-plural: 13.6% (153/1122)
2020-09-24 21:10:34,539 : INFO : gram9-plural-verbs: 19.6% (159/812)
2020-09-24 21:10:34,539 : INFO : Quadruplets with out-of-vocabulary words: 31.7%
2020-09-24 21:10:34,539 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-24 21:10:34,539 : INFO : Total accuracy: 10.6% (1410/13351)
Doc2Vec("ech03,mal0002x100",dm/c,d15,n67,w2,mc200,s4e-05,t6): 10.56% correct (1410 of 13351)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-24 21:10:35,183 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4768
2020-09-24 21:10:35,184 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4715
2020-09-24 21:10:35,184 : INFO : Pairs with unknown words ratio: 1.7%
((0.4767587762405245, 4.2879262532368494e-21), SpearmanrResult(correlation=0.4715045710956902, pvalue=1.3135545764894756e-20), 1.69971671388102)


02 - simlex999
2020-09-24 21:10:35,210 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2179
2020-09-24 21:10:35,210 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1854
2020-09-24 21:10:35,210 : INFO : Pairs with unknown words ratio: 0.6%
((0.21789535172771807, 3.8873904731536924e-12), SpearmanrResult(correlation=0.18540762807879496, pvalue=3.949466335466784e-09), 0.6006006006006006)


03 - simverb3500
2020-09-24 21:10:35,875 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1391
2020-09-24 21:10:35,875 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1295
2020-09-24 21:10:35,875 : INFO : Pairs with unknown words ratio: 2.1%
((0.13914155865297334, 2.8128349235581005e-16), SpearmanrResult(correlation=0.12951873615644807, pvalue=2.734519840183265e-14), 2.1142857142857143)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
