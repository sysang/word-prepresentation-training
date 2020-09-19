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
        epochs=5
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    corpus = 'thefinal'

    base.train(corpus, common_kwargs, saved_fname)

"""
2020-09-19 12:51:51,493 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-19 12:51:51,494 : INFO : Loading a fresh vocabulary
2020-09-19 12:51:51,968 : INFO : effective_min_count=75 retains 70715 unique words (3% of original 1784839, drops 1714124)
2020-09-19 12:51:51,968 : INFO : effective_min_count=75 leaves 329482258 word corpus (98% of original 336075146, drops 6592888)
2020-09-19 12:51:52,130 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-19 12:51:52,166 : INFO : sample=5e-05 downsamples 730 most-common words
2020-09-19 12:51:52,166 : INFO : downsampling leaves estimated 148046269 word corpus (44.9% of prior 329482258)
2020-09-19 12:51:52,304 : INFO : estimated required memory for 70715 words and 15 dimensions: 866700700 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10)
Save model to: models/dmc_d15_n30_w3_mc75_s0001_ech05_thefinal.bin
2020-09-19 12:20:09,285 : INFO : saving Doc2Vec object under models/dmc_d15_n30_w3_mc75_s0001_ech05_thefinal.bin, separately None
2020-09-19 12:20:09,285 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n30_w3_mc75_s0001_ech05_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-19 12:20:09,313 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n30_w3_mc75_s0001_ech05_thefinal.bin.docvecs.vectors_docs.npy
2020-09-19 12:20:09,909 : INFO : saved models/dmc_d15_n30_w3_mc75_s0001_ech05_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 1826183
[+] index 1826183 -> "she must be courteous and she must be compassionate"
2020-09-19 12:20:09,922 : INFO : precomputing L2-norms of doc weight vectors
!! No any match in top 100 similarities


.....get random document, tag: 10235142
[+] index 10235142 -> "a mermaid from mere in the obsolete sense sea maid en is a legendary aquatic creature with the head and torso of human female and the tail of a fish"
!! No any match in top 100 similarities


.....get random document, tag: 5084421
[+] index 5084421 -> "how d'ye think your fathers got your land who has risen not by breaking their word"
!! No any match in top 100 similarities


.....get random document, tag: 8238340
[+] index 8238340 -> "the only one of his works which has been printed besides a few letters in the historical works of gervase of can noterbury ed"
** Matched with rank 12, score: 0.881281852722168


.....get random document, tag: 803734
[+] index 803734 -> "yes sir it was replied slurk and sir if you like that better ha ha mr"
!! No any match in top 100 similarities


.....get random document, tag: 1068033
[+] index 1068033 -> "peter 's aim was to save the life of the girl her gentle attractions and kind attentions to himself having wrought this much in her favor and he believed no means of doing so as certain as forming a close connection for her with the great medicine-bee-hunter"
!! No any match in top 100 similarities


.....get random document, tag: 8434123
[+] index 8434123 -> "the same year he was elected president of the american bar association"
!! No any match in top 100 similarities




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (8592745): the gods were said to have created human beings from clay for the purpose of serving them

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):

MOST (11962791, 0.9372025728225708): «i am sure he could go if he pays his own way»

MEDIAN (5748668, -0.0041187480092048645): «the controls are great some of the best for the wii»

LEAST (3263092, -0.9260739088058472): «the front door however was only separated by a little flight of steps from the pavement upon which the house abutted»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'corresponding' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
2020-09-19 12:20:34,915 : INFO : precomputing L2-norms of word weight vectors
     1. 0.89 'varying'
     2. 0.89 'proportional'
     3. 0.89 'normalized'
     4. 0.88 'discrete'
     5. 0.88 'fourfold'
     6. 0.88 'logarithmic'
     7. 0.88 'fractional'


[+] target_word: 'excursion' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.96 'jaunt'
     2. 0.92 'tour'
     3. 0.91 'trip'
     4. 0.91 'stopover'
     5. 0.89 'tours'
     6. 0.89 'halting-place'
     7. 0.88 'voyage'


[+] target_word: 'cleared' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.93 'swept'
     2. 0.92 'laid'
     3. 0.92 'fended'
     4. 0.91 'ejected'
     5. 0.91 'carried'
     6. 0.91 'transported'
     7. 0.91 'drained'


[+] target_word: 'kick' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.96 'nip'
     2. 0.95 'piss'
     3. 0.94 'whack'
     4. 0.94 'smack'
     5. 0.93 'rip'
     6. 0.93 'shove'
     7. 0.93 'crack'


[+] target_word: 'suburb' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.95 'suburbs'
     2. 0.94 'ardmore'
     3. 0.93 'roxbury'
     4. 0.93 'belgravia'
     5. 0.93 'market-town'
     6. 0.93 'neighborhood'
     7. 0.93 'carbondale'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-19 12:20:35,651 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-19 12:20:36,011 : INFO : capital-common-countries: 9.9% (50/506)
2020-09-19 12:20:37,445 : INFO : capital-world: 4.6% (88/1929)
2020-09-19 12:20:37,637 : INFO : currency: 3.8% (9/236)
2020-09-19 12:20:39,182 : INFO : city-in-state: 2.4% (55/2330)
2020-09-19 12:20:39,528 : INFO : family: 35.7% (150/420)
2020-09-19 12:20:40,206 : INFO : gram1-adjective-to-adverb: 4.1% (41/992)
2020-09-19 12:20:40,736 : INFO : gram2-opposite: 5.4% (38/702)
2020-09-19 12:20:41,645 : INFO : gram3-comparative: 28.8% (384/1332)
2020-09-19 12:20:42,433 : INFO : gram4-superlative: 10.7% (113/1056)
2020-09-19 12:20:43,072 : INFO : gram5-present-participle: 25.4% (268/1056)
2020-09-19 12:20:44,093 : INFO : gram6-nationality-adjective: 13.3% (182/1371)
2020-09-19 12:20:45,228 : INFO : gram7-past-tense: 26.4% (412/1560)
2020-09-19 12:20:46,133 : INFO : gram8-plural: 12.3% (164/1332)
2020-09-19 12:20:46,758 : INFO : gram9-plural-verbs: 10.0% (87/870)
2020-09-19 12:20:46,759 : INFO : Quadruplets with out-of-vocabulary words: 19.7%
2020-09-19 12:20:46,759 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-19 12:20:46,759 : INFO : Total accuracy: 13.0% (2041/15692)
Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10): 13.01% correct (2041 of 15692)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-19 12:20:47,037 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5495
2020-09-19 12:20:47,037 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5449
2020-09-19 12:20:47,037 : INFO : Pairs with unknown words ratio: 0.6%
((0.5495010590964712, 4.420576315823605e-29), SpearmanrResult(correlation=0.5449484521389131, pvalue=1.5418604555778427e-28), 0.56657223796034)


02 - simlex999
2020-09-19 12:20:47,093 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3206
2020-09-19 12:20:47,093 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2741
2020-09-19 12:20:47,093 : INFO : Pairs with unknown words ratio: 0.3%
((0.3206080528402713, 3.0333465915052807e-25), SpearmanrResult(correlation=0.2740928250288352, pvalue=1.2672469775879997e-18), 0.3003003003003003)


03 - simverb3500
2020-09-19 12:20:47,378 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1821
2020-09-19 12:20:47,378 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1664
2020-09-19 12:20:47,379 : INFO : Pairs with unknown words ratio: 0.7%
((0.18213608121230912, 2.7082417071065573e-27), SpearmanrResult(correlation=0.16643481546187022, pvalue=5.332902755950357e-23), 0.7428571428571429)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
