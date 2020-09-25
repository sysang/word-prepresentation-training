import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=72,
        window=7,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=5,
        min_alpha=0.0005,
        alpha=0.0005*20*5,
        comment='ech05,mal0005x20',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(common_kwargs=common_kwargs, saved_fname=saved_fname, evaluate=False)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech05,mal0005x20",dm/c,d15,n72,w7,mc99,s5e-05,t6)
Save model to: models/dmc_d15_n72_w7_mc99_s00005_ech05_mal0005x20_refined.bin
2020-09-25 10:42:05,022 : INFO : saving Doc2Vec object under models/dmc_d15_n72_w7_mc99_s00005_ech05_mal0005x20_refined.bin, separately None
2020-09-25 10:42:05,022 : INFO : storing np array 'syn1neg' to models/dmc_d15_n72_w7_mc99_s00005_ech05_mal0005x20_refined.bin.trainables.syn1neg.npy
2020-09-25 10:42:05,048 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n72_w7_mc99_s00005_ech05_mal0005x20_refined.bin.trainables.vectors_docs_lockf.npy
2020-09-25 10:42:05,121 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n72_w7_mc99_s00005_ech05_mal0005x20_refined.bin.docvecs.vectors_docs.npy
2020-09-25 10:42:06,252 : INFO : saved models/dmc_d15_n72_w7_mc99_s00005_ech05_mal0005x20_refined.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 28297708
[+] index 28297708 -> "the amazing puppy wizard does not entertrain at his howes"
2020-09-25 10:42:06,269 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 21574799
[+] index 21574799 -> "do make at least desultory efforts to grow up"
    No any match in top 200 similarities.


.....get random document, tag: 29517337
[+] index 29517337 -> "resident or currently able to legally work in the"
    No any match in top 200 similarities.


.....get random document, tag: 14907855
[+] index 14907855 -> "you will end up with a hell of a lot more bullshit if the apes get to vote on their own pay and bonuses"
    No any match in top 200 similarities.


.....get random document, tag: 38393538
[+] index 38393538 -> "i am taking the liberty to send you this one email to give you legal notice to cease and desist"
    No any match in top 200 similarities.


.....get random document, tag: 22256299
[+] index 22256299 -> "low voltage supply due to a charging system problem might also have the same effect"
    No any match in top 200 similarities.


.....get random document, tag: 28737669
[+] index 28737669 -> "experience in analyzing reports to identify gaps in a legacy reporting system"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (37035439): resident or currently able to legally work in the

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0005x20",dm/c,d15,n72,w7,mc99,s5e-05,t6):

MOST (17697196, 0.9330037832260132): «some of us have been studying each other for five to fifteen years»

MEDIAN (13273432, -0.0007438212633132935): «better target soccers now or jimmy will publicly enquire them as to you»

LEAST (18319900, -0.941826343536377): «we can not irritate puddles unless ronald will usably judge afterwards»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'trouble' model: Doc2Vec("ech05,mal0005x20",dm/c,d15,n72,w7,mc99,s5e-05,t6):
2020-09-25 10:43:34,765 : INFO : precomputing L2-norms of word weight vectors
     1. 0.93 'chances'
     2. 0.92 'pleasure'
     3. 0.91 'chance'
     4. 0.91 'difficulty'
     5. 0.90 'leeway'
     6. 0.90 'knack'
     7. 0.89 'habit'


[+] target_word: 'deliver' model: Doc2Vec("ech05,mal0005x20",dm/c,d15,n72,w7,mc99,s5e-05,t6):
     1. 0.96 'renew'
     2. 0.96 'furnish'
     3. 0.96 'introduce'
     4. 0.95 'distribute'
     5. 0.95 'lend'
     6. 0.95 'receive'
     7. 0.94 'offer'


[+] target_word: 'router' model: Doc2Vec("ech05,mal0005x20",dm/c,d15,n72,w7,mc99,s5e-05,t6):
     1. 0.97 'firewall'
     2. 0.96 'modem'
     3. 0.96 'kvm'
     4. 0.95 'vnc'
     5. 0.95 'adaptor'
     6. 0.95 'handset'
     7. 0.94 'hdd'


[+] target_word: 'observing' model: Doc2Vec("ech05,mal0005x20",dm/c,d15,n72,w7,mc99,s5e-05,t6):
     1. 0.92 'revealing'
     2. 0.92 'analysing'
     3. 0.92 'probing'
     4. 0.90 'suggestive'
     5. 0.90 'describing'
     6. 0.89 'contrasting'
     7. 0.89 'troubling'


[+] target_word: 'inflated' model: Doc2Vec("ech05,mal0005x20",dm/c,d15,n72,w7,mc99,s5e-05,t6):
     1. 0.93 'inflating'
     2. 0.92 'humongous'
     3. 0.91 'overvalued'
     4. 0.91 'bloated'
     5. 0.91 'outsized'
     6. 0.90 'diluting'
     7. 0.89 'undervalued'


[+] target_word: 'nadal' model: Doc2Vec("ech05,mal0005x20",dm/c,d15,n72,w7,mc99,s5e-05,t6):
     1. 0.98 'rafa'
     2. 0.97 'federer'
     3. 0.96 'djokovic'
     4. 0.95 'sampras'
     5. 0.94 'shaq'
     6. 0.94 'sehwag'
     7. 0.93 'lendl'


[+] target_word: 'molesters' model: Doc2Vec("ech05,mal0005x20",dm/c,d15,n72,w7,mc99,s5e-05,t6):
     1. 0.98 'molestors'
     2. 0.96 'pornographers'
     3. 0.93 'molester'
     4. 0.91 'deviants'
     5. 0.90 'molestor'
     6. 0.90 'rapists'
     7. 0.88 'killers'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-25 10:43:35,507 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-25 10:43:35,749 : INFO : capital-common-countries: 4.1% (19/462)
2020-09-25 10:43:36,383 : INFO : capital-world: 1.1% (13/1157)
2020-09-25 10:43:36,482 : INFO : currency: 3.4% (6/178)
2020-09-25 10:43:37,579 : INFO : city-in-state: 1.4% (32/2267)
2020-09-25 10:43:37,844 : INFO : family: 34.8% (146/420)
2020-09-25 10:43:38,364 : INFO : gram1-adjective-to-adverb: 2.6% (26/992)
2020-09-25 10:43:38,798 : INFO : gram2-opposite: 2.2% (17/756)
2020-09-25 10:43:39,369 : INFO : gram3-comparative: 16.0% (213/1332)
2020-09-25 10:43:39,840 : INFO : gram4-superlative: 5.6% (59/1056)
2020-09-25 10:43:40,386 : INFO : gram5-present-participle: 17.5% (185/1056)
2020-09-25 10:43:41,072 : INFO : gram6-nationality-adjective: 9.5% (124/1299)
2020-09-25 10:43:41,940 : INFO : gram7-past-tense: 18.0% (281/1560)
2020-09-25 10:43:42,568 : INFO : gram8-plural: 13.5% (161/1190)
2020-09-25 10:43:43,091 : INFO : gram9-plural-verbs: 12.8% (111/870)
2020-09-25 10:43:43,091 : INFO : Quadruplets with out-of-vocabulary words: 25.3%
2020-09-25 10:43:43,091 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-25 10:43:43,091 : INFO : Total accuracy: 9.5% (1393/14595)
Doc2Vec("ech05,mal0005x20",dm/c,d15,n72,w7,mc99,s5e-05,t6): 9.54% correct (1393 of 14595)


[+] questions-words-narrowed.txt
2020-09-25 10:43:43,130 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-25 10:43:43,398 : INFO : family: 34.8% (146/420)
2020-09-25 10:43:43,921 : INFO : gram1-adjective-to-adverb: 2.6% (26/992)
2020-09-25 10:43:44,360 : INFO : gram2-opposite: 2.2% (17/756)
2020-09-25 10:43:44,929 : INFO : gram3-comparative: 16.0% (213/1332)
2020-09-25 10:43:45,410 : INFO : gram4-superlative: 5.6% (59/1056)
2020-09-25 10:43:45,956 : INFO : gram5-present-participle: 17.5% (185/1056)
2020-09-25 10:43:46,647 : INFO : gram6-nationality-adjective: 9.5% (124/1299)
2020-09-25 10:43:47,521 : INFO : gram7-past-tense: 18.0% (281/1560)
2020-09-25 10:43:48,771 : INFO : gram8-plural: 13.5% (161/1190)
2020-09-25 10:43:49,297 : INFO : gram9-plural-verbs: 12.8% (111/870)
2020-09-25 10:43:49,297 : INFO : Quadruplets with out-of-vocabulary words: 5.8%
2020-09-25 10:43:49,297 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-25 10:43:49,297 : INFO : Total accuracy: 12.6% (1323/10531)
Doc2Vec("ech05,mal0005x20",dm/c,d15,n72,w7,mc99,s5e-05,t6): 12.56% correct (1323 of 10531)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-25 10:43:49,344 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4606
2020-09-25 10:43:49,344 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4634
2020-09-25 10:43:49,344 : INFO : Pairs with unknown words ratio: 0.6%
((0.4606255338221055, 7.749912928176236e-20), SpearmanrResult(correlation=0.4634019823523214, pvalue=4.3607579910559954e-20), 0.56657223796034)


02 - simlex999
2020-09-25 10:43:50,000 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2467
2020-09-25 10:43:50,000 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2185
2020-09-25 10:43:50,000 : INFO : Pairs with unknown words ratio: 0.5%
((0.24672043060767512, 2.9964242054441116e-15), SpearmanrResult(correlation=0.21848468012304256, pvalue=3.3081908738318097e-12), 0.5005005005005005)


03 - simverb3500
2020-09-25 10:43:50,062 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1391
2020-09-25 10:43:50,062 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1329
2020-09-25 10:43:50,062 : INFO : Pairs with unknown words ratio: 0.5%
((0.13905835115269674, 1.682956861219681e-16), SpearmanrResult(correlation=0.13291652952843694, pvalue=3.397893981647125e-15), 0.5142857142857142)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
