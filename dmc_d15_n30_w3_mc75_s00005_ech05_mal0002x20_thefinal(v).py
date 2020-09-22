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
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*20*5
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10)
Save model to: models/dmc_d15_n30_w3_mc75_s00005_ech05_mal0002x20_thefinal.bin
2020-09-20 09:28:54,985 : INFO : saving Doc2Vec object under models/dmc_d15_n30_w3_mc75_s00005_ech05_mal0002x20_thefinal.bin, separately None
2020-09-20 09:28:54,985 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n30_w3_mc75_s00005_ech05_mal0002x20_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-20 09:28:55,015 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n30_w3_mc75_s00005_ech05_mal0002x20_thefinal.bin.docvecs.vectors_docs.npy
2020-09-20 09:28:55,620 : INFO : saved models/dmc_d15_n30_w3_mc75_s00005_ech05_mal0002x20_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 4688651
[+] index 4688651 -> "it specially excepted the quakers from service and constrained nobody but declared it lawful for such as chose to form themselves into companies and to elect officers by ballot"
2020-09-20 09:28:55,631 : INFO : precomputing L2-norms of doc weight vectors
[*] Matched with rank 19, score: 0.8899510502815247!


.....get random document, tag: 10716204
[+] index 10716204 -> "i didn’t see any tongues whipping out or anything… if i hadn’t been staring at the cage i would have missed it…i got online and found out that she is a southern wood house toad"
    No any match in top 100 similarities.


.....get random document, tag: 7096203
[+] index 7096203 -> "in tu o nadie her brother played a pshysically challenged person"
    No any match in top 100 similarities.


.....get random document, tag: 5822310
[+] index 5822310 -> "they are larger or smaller filling the screen or hovering meekly in the air depending on what is being said"
    No any match in top 100 similarities.


.....get random document, tag: 315386
[+] index 315386 -> "as we went forth from the doors a small circumstance occurred which came afterwards to look extremely big"
    No any match in top 100 similarities.


.....get random document, tag: 3095743
[+] index 3095743 -> "but tekin alp deals even less tenderly with russia"
    No any match in top 100 similarities.


.....get random document, tag: 4698108
[+] index 4698108 -> "and this keep he added giving her one addressed to his father"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (8935586): the word quarantine originates from a 40 day isolation of ships and people prior to entering the city of dubrovnik aka ragusa

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):

MOST (544901, 0.9334778785705566): «i beg leave to observe that intrigue here is the business of life when a woman marries she throws off all restraint but i believe their conduct is chaste enough before»

MEDIAN (12973647, 0.0016435086727142334): «it 's such a pervasive term some could argue that the term jumping the shark may have just done that that there 's a website that chronicles the climax and inevitable downfall of countless television shows»

LEAST (7374222, -0.9030811786651611): «zuehl is located at 29°29'30 north 98°9'10 west 29 491600 -98 152772»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'defeat' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
2020-09-20 09:29:19,869 : INFO : precomputing L2-norms of word weight vectors
     1. 0.96 'repulse'
     2. 0.92 'downfall'
     3. 0.92 'victory'
     4. 0.91 'mutiny'
     5. 0.90 'overthrow'
     6. 0.89 'retaliation'
     7. 0.89 'truce'


[+] target_word: 'beds' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.94 'basements'
     2. 0.93 'outhouses'
     3. 0.93 'barns'
     4. 0.93 'greenhouses'
     5. 0.93 'mounds'
     6. 0.93 'floors'
     7. 0.92 'nests'


[+] target_word: 'subsequent' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.91 'recent'
     2. 0.90 'eight-year'
     3. 0.89 'seven-year'
     4. 0.89 'simultaneous'
     5. 0.89 'year-long'
     6. 0.89 'well-publicized'
     7. 0.89 'abortive'


[+] target_word: 'solid' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.91 'infinitesimal'
     2. 0.91 'lighter'
     3. 0.90 'miniscule'
     4. 0.90 'lightest'
     5. 0.90 'compact'
     6. 0.89 'ultra'
     7. 0.89 'tiniest'


[+] target_word: 'poison' model: Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10):
     1. 0.93 'gall'
     2. 0.91 'bile'
     3. 0.91 'canker'
     4. 0.90 'blood'
     5. 0.90 'pox'
     6. 0.90 'venom'
     7. 0.89 'eater'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-20 09:29:20,555 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-20 09:29:20,914 : INFO : capital-common-countries: 9.5% (48/506)
2020-09-20 09:29:22,321 : INFO : capital-world: 4.3% (82/1929)
2020-09-20 09:29:22,504 : INFO : currency: 2.5% (6/236)
2020-09-20 09:29:24,080 : INFO : city-in-state: 2.0% (46/2330)
2020-09-20 09:29:24,420 : INFO : family: 37.6% (158/420)
2020-09-20 09:29:25,110 : INFO : gram1-adjective-to-adverb: 4.9% (49/992)
2020-09-20 09:29:25,668 : INFO : gram2-opposite: 4.4% (31/702)
2020-09-20 09:29:26,584 : INFO : gram3-comparative: 32.2% (429/1332)
2020-09-20 09:29:27,380 : INFO : gram4-superlative: 10.7% (113/1056)
2020-09-20 09:29:28,051 : INFO : gram5-present-participle: 22.4% (237/1056)
2020-09-20 09:29:29,055 : INFO : gram6-nationality-adjective: 11.7% (160/1371)
2020-09-20 09:29:30,222 : INFO : gram7-past-tense: 26.7% (416/1560)
2020-09-20 09:29:31,157 : INFO : gram8-plural: 14.3% (190/1332)
2020-09-20 09:29:31,807 : INFO : gram9-plural-verbs: 9.1% (79/870)
2020-09-20 09:29:31,808 : INFO : Quadruplets with out-of-vocabulary words: 19.7%
2020-09-20 09:29:31,808 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-20 09:29:31,809 : INFO : Total accuracy: 13.0% (2044/15692)
Doc2Vec(dm/c,d15,n30,w3,mc75,s5e-05,t10): 13.03% correct (2044 of 15692)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-20 09:29:32,088 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5501
2020-09-20 09:29:32,088 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5477
2020-09-20 09:29:32,088 : INFO : Pairs with unknown words ratio: 0.6%
((0.5501449416419827, 3.6988877449789306e-29), SpearmanrResult(correlation=0.5477203105817895, pvalue=7.222556713039177e-29), 0.56657223796034)


02 - simlex999
2020-09-20 09:29:32,145 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3200
2020-09-20 09:29:32,145 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2745
2020-09-20 09:29:32,145 : INFO : Pairs with unknown words ratio: 0.3%
((0.32002681527460247, 3.734707803754506e-25), SpearmanrResult(correlation=0.2745059258348018, pvalue=1.1202828892027247e-18), 0.3003003003003003)


03 - simverb3500
2020-09-20 09:29:32,429 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1827
2020-09-20 09:29:32,429 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1706
2020-09-20 09:29:32,429 : INFO : Pairs with unknown words ratio: 0.7%
((0.18268649270298404, 1.882763842641288e-27), SpearmanrResult(correlation=0.17062920625826913, pvalue=4.161993920915018e-24), 0.7428571428571429)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
