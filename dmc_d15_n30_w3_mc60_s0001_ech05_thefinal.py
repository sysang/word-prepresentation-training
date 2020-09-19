import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15, negative=30, window=3, min_count=60, sample=0.0001,
        dm=1, dm_concat=1, hs=0, epochs=5
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    corpus = 'thefinal'

    base.train(corpus, common_kwargs, saved_fname)

"""
2020-09-19 10:52:51,318 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-19 10:52:51,318 : INFO : Loading a fresh vocabulary
2020-09-19 10:52:51,804 : INFO : effective_min_count=60 retains 79424 unique words (4% of original 1784839, drops 1705415)
2020-09-19 10:52:51,804 : INFO : effective_min_count=60 leaves 330061954 word corpus (98% of original 336075146, drops 6013192)
2020-09-19 10:52:51,984 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-19 10:52:52,022 : INFO : sample=0.0001 downsamples 380 most-common words
2020-09-19 10:52:52,022 : INFO : downsampling leaves estimated 170789420 word corpus (51.7% of prior 330061954)
2020-09-19 10:52:52,175 : INFO : estimated required memory for 79424 words and 15 dimensions: 875235520 by
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n30,w3,mc60,s0.0001,t10)
Save model to: models/dmc_d15_n30_w3_mc60_s0001_ech05_thefinal.bin
2020-09-19 10:39:04,732 : INFO : saving Doc2Vec object under models/dmc_d15_n30_w3_mc60_s0001_ech05_thefinal.bin, separately None
2020-09-19 10:39:04,732 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n30_w3_mc60_s0001_ech05_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-19 10:39:04,758 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n30_w3_mc60_s0001_ech05_thefinal.bin.docvecs.vectors_docs.npy
2020-09-19 10:39:05,384 : INFO : saved models/dmc_d15_n30_w3_mc60_s0001_ech05_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 3105944
[+] index 3105944 -> "as soon as on the 12th of april 1861 the first gun was fired in charleston harbor on the union flag upon fort sumter the call was sounded and the northern people rushed to arms"
2020-09-19 10:39:05,393 : INFO : precomputing L2-norms of doc weight vectors
** Matched with rank 85, score: 0.8823883533477783


.....get random document, tag: 10696686
[+] index 10696686 -> "i have been finding harder to deal with life because i have so much free time because school is out and all"
!! No any match in top 100 similarities


.....get random document, tag: 11649922
[+] index 11649922 -> "but again the nature of the addiction is to deny the problem"
!! No any match in top 100 similarities


.....get random document, tag: 8686132
[+] index 8686132 -> "while sifting through the wreckage investigators reported finding a serrated belt-clip knife as well a a cigarette lighter with a concealed blade"
!! No any match in top 100 similarities


.....get random document, tag: 11976719
[+] index 11976719 -> "cut to neo wet poised beckoning toward smith offscreen to bring it on"
!! No any match in top 100 similarities


.....get random document, tag: 9444833
[+] index 9444833 -> "within organisms genetic information generally is carried in chromosomes where it is represented in the chemical structure of particular dna molecules"
!! No any match in top 100 similarities


.....get random document, tag: 10704704
[+] index 10704704 -> "my feet are covered in chigger bites and it took two showers to wash all the sand out of the concave parts of my body"
!! No any match in top 100 similarities




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (7645262): on june 7 1977 in preparation for a hearing in his murder trial bundy was transported to the pitkin county colorado courthouse

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n30,w3,mc60,s0.0001,t10):

MOST (9444931, 0.9536131024360657): «their most proximal parts emerging from the spinal cord are called nerve roots and the inflammation in most but not all typical guillain-barré syndrome cases starts in these roots»

MEDIAN (8004012, 0.005893263965845108): «further in kelly 's kids mention was made of the brady adoptions when their neighbours the kellys adopted three boys themselves»

LEAST (1724015, -0.9369182586669922): «rising quickly he hurried down with his studious comrades to see what it could be all about»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'zero' model: Doc2Vec(dm/c,d15,n30,w3,mc60,s0.0001,t10):
2020-09-19 10:39:30,742 : INFO : precomputing L2-norms of word weight vectors
     1. 0.94 'nonzero'
     2. 0.90 'gaussian'
     3. 0.90 'maximum'
     4. 0.90 'non-zero'
     5. 0.90 'scalar'
     6. 0.89 'exponential'
     7. 0.89 'dimensionless'


[+] target_word: 'compartment' model: Doc2Vec(dm/c,d15,n30,w3,mc60,s0.0001,t10):
     1. 0.93 'doors'
     2. 0.93 'deck'
     3. 0.92 'flooring'
     4. 0.92 'window-shutters'
     5. 0.91 'folding-doors'
     6. 0.91 'packing-case'
     7. 0.91 'shutters'


[+] target_word: 'gaming' model: Doc2Vec(dm/c,d15,n30,w3,mc60,s0.0001,t10):
     1. 0.97 'entertainment'
     2. 0.96 'warez'
     3. 0.94 'kickboxing'
     4. 0.92 'sports'
     5. 0.92 'merchandising'
     6. 0.92 'host'
     7. 0.92 'motorsport'


[+] target_word: 'nationality' model: Doc2Vec(dm/c,d15,n30,w3,mc60,s0.0001,t10):
     1. 0.90 'citizenship'
     2. 0.89 'polity'
     3. 0.89 'constitutions'
     4. 0.89 'theocracy'
     5. 0.89 'sharia'
     6. 0.89 'ethnicity'
     7. 0.88 'moneylender'


[+] target_word: 'sites' model: Doc2Vec(dm/c,d15,n30,w3,mc60,s0.0001,t10):
     1. 0.93 'weeklies'
     2. 0.93 'bookshops'
     3. 0.92 'networks'
     4. 0.92 'projects'
     5. 0.92 'bookstores'
     6. 0.91 'hotspots'
     7. 0.91 'locations'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-19 10:39:31,789 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-19 10:39:32,224 : INFO : capital-common-countries: 8.7% (44/506)
2020-09-19 10:39:34,223 : INFO : capital-world: 3.9% (87/2245)
2020-09-19 10:39:34,438 : INFO : currency: 2.1% (5/236)
2020-09-19 10:39:36,180 : INFO : city-in-state: 2.1% (51/2394)
2020-09-19 10:39:36,566 : INFO : family: 37.6% (158/420)
2020-09-19 10:39:37,277 : INFO : gram1-adjective-to-adverb: 4.6% (46/992)
2020-09-19 10:39:37,978 : INFO : gram2-opposite: 3.4% (26/756)
2020-09-19 10:39:39,111 : INFO : gram3-comparative: 25.6% (341/1332)
2020-09-19 10:39:40,047 : INFO : gram4-superlative: 11.4% (120/1056)
2020-09-19 10:39:40,904 : INFO : gram5-present-participle: 18.7% (197/1056)
2020-09-19 10:39:42,194 : INFO : gram6-nationality-adjective: 8.6% (118/1371)
2020-09-19 10:39:43,564 : INFO : gram7-past-tense: 20.2% (315/1560)
2020-09-19 10:39:44,806 : INFO : gram8-plural: 12.8% (171/1332)
2020-09-19 10:39:45,599 : INFO : gram9-plural-verbs: 10.1% (88/870)
2020-09-19 10:39:45,600 : INFO : Quadruplets with out-of-vocabulary words: 17.5%
2020-09-19 10:39:45,600 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-19 10:39:45,600 : INFO : Total accuracy: 11.0% (1767/16126)
Doc2Vec(dm/c,d15,n30,w3,mc60,s0.0001,t10): 10.96% correct (1767 of 16126)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-19 10:39:45,887 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5264
2020-09-19 10:39:45,887 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5222
2020-09-19 10:39:45,887 : INFO : Pairs with unknown words ratio: 0.6%
((0.5264197667618534, 2.0558961585512177e-26), SpearmanrResult(correlation=0.5222206559331962, pvalue=5.979181050307758e-26), 0.56657223796034)


02 - simlex999
2020-09-19 10:39:46,164 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3109
2020-09-19 10:39:46,164 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2707
2020-09-19 10:39:46,164 : INFO : Pairs with unknown words ratio: 0.3%
((0.31093590987885417, 9.109605321465402e-24), SpearmanrResult(correlation=0.2706874062541505, pvalue=3.472812316682019e-18), 0.3003003003003003)


03 - simverb3500
2020-09-19 10:39:46,467 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1863
2020-09-19 10:39:46,467 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1747
2020-09-19 10:39:46,467 : INFO : Pairs with unknown words ratio: 0.7%
((0.1862683444162126, 1.6287303492995339e-28), SpearmanrResult(correlation=0.17471436937125673, pvalue=3.1081619628102737e-25), 0.6571428571428571)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
