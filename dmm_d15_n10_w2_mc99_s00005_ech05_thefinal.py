import doc2vec_training_script_multiprocessing as base

print("# CODE:")
print(open(__file__, "r").read())
print("# END #")

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=10,
        window=2,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=0,
        hs=0,
        epochs=5,
        comment='ech05',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech05",dm/m,d15,n10,w2,mc99,s5e-05,t6)
Save model to: models/dmm_d15_n10_w2_mc99_s00005_ech05_thefinal.bin
2020-09-22 16:03:27,883 : INFO : saving Doc2Vec object under models/dmm_d15_n10_w2_mc99_s00005_ech05_thefinal.bin, separately None
2020-09-22 16:03:27,884 : INFO : storing np array 'vectors_docs_lockf' to models/dmm_d15_n10_w2_mc99_s00005_ech05_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-22 16:03:27,912 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n10_w2_mc99_s00005_ech05_thefinal.bin.docvecs.vectors_docs.npy
2020-09-22 16:03:28,340 : INFO : saved models/dmm_d15_n10_w2_mc99_s00005_ech05_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 5568938
[+] index 5568938 -> "it is not of long standing i only noticed it a little while ago"
2020-09-22 16:03:28,349 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 100 similarities.


.....get random document, tag: 839193
[+] index 839193 -> "and there exist in writing at this hour various flattering little notes from imperial majesty to that address which begin say many witnesses nay says one good witness hormayr cited in preuss i"
    No any match in top 100 similarities.


.....get random document, tag: 427244
[+] index 427244 -> "that it would redound to any satisfaction of the fool she did not stop to doubt"
    No any match in top 100 similarities.


.....get random document, tag: 5711330
[+] index 5711330 -> "and like i said earlier the idea of an insidious force from the past turning the members of an isolated community against each other is a good one and can sustain interest far above the actual merit of a bad performance"
    No any match in top 100 similarities.


.....get random document, tag: 3567244
[+] index 3567244 -> "the villain repeated rose with a flushed face and flashing eye"
    No any match in top 100 similarities.


.....get random document, tag: 4590918
[+] index 4590918 -> "the case is evidently laid down to every common understanding in the example of spain till now the spaniards for many ages have been overrun and impoverished by their continued wars with the french and it was not doubted but one time or other they would have been entirely conquered by the king of france and have become a mere province of france whereas now having but consented to receive a king from the hands of the invincible monarch they are made easy as to the former danger they were always in axe now most safe under the protection of france and he who before was their terror is now their safety and being safe from him it appears they are so from all the world"
    No any match in top 100 similarities.


.....get random document, tag: 438975
[+] index 438975 -> "in great haste your affectionate son as the spring approached the vision of her independent visit to london which had sustained her throughout the winter having performed its annual function grew mistier and mistier and at last faded away"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (12701085): i ended up having a pretty full day of boat rides bus rides temples floating villages and all that jazz

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05",dm/m,d15,n10,w2,mc99,s5e-05,t6):

MOST (783945, 0.9714916348457336): «one or two dusky shapes seen dimly in the recesses of a large cage built round a hollow tree would be lively owls when evening came on»

MEDIAN (10739512, 0.5774792432785034): «each time i did that i begin to set a higher standard and poured in my willpower to resist the next urge to masturbate to relieve myself from the pressure and temptation»

LEAST (10214648, -0.9233734607696533): «there are 175 households out of which 45 1% have children under the age of 18 living with them 53 7% are married couples living together 13 1% have a female householder with no husband present and 25 1% are non-families»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'can�t' model: Doc2Vec("ech05",dm/m,d15,n10,w2,mc99,s5e-05,t6):
2020-09-22 16:03:53,202 : INFO : precomputing L2-norms of word weight vectors
     1. 0.99 'can’t'
     2. 0.96 'didn�t'
     3. 0.96 'if'
     4. 0.96 'can'
     5. 0.96 'couldn’t'
     6. 0.96 "'d"
     7. 0.95 'could'


[+] target_word: 'contrive' model: Doc2Vec("ech05",dm/m,d15,n10,w2,mc99,s5e-05,t6):
     1. 0.93 'manage'
     2. 0.93 'try'
     3. 0.92 'permit'
     4. 0.92 'help'
     5. 0.91 'want'
     6. 0.91 'able'
     7. 0.91 'wanting'


[+] target_word: 'originating' model: Doc2Vec("ech05",dm/m,d15,n10,w2,mc99,s5e-05,t6):
     1. 0.87 'predate'
     2. 0.85 'originated'
     3. 0.85 'originates'
     4. 0.84 'emergent'
     5. 0.84 'nascent'
     6. 0.83 'predates'
     7. 0.83 'centuries-old'


[+] target_word: 'tries' model: Doc2Vec("ech05",dm/m,d15,n10,w2,mc99,s5e-05,t6):
     1. 0.96 'manages'
     2. 0.89 'decides'
     3. 0.87 'refuses'
     4. 0.87 'balk'
     5. 0.87 'mallika'
     6. 0.86 'arman'
     7. 0.85 'wants'


[+] target_word: 'variant' model: Doc2Vec("ech05",dm/m,d15,n10,w2,mc99,s5e-05,t6):
     1. 0.85 'mirabilis'
     2. 0.84 'triplet'
     3. 0.84 'radiocarbon'
     4. 0.83 'oed'
     5. 0.83 'asterisk'
     6. 0.82 'kalevala'
     7. 0.82 'codex'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-22 16:03:53,787 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-22 16:03:54,104 : INFO : capital-common-countries: 11.3% (57/506)
2020-09-22 16:03:55,274 : INFO : capital-world: 5.3% (94/1779)
2020-09-22 16:03:55,392 : INFO : currency: 1.7% (3/178)
2020-09-22 16:03:56,977 : INFO : city-in-state: 2.0% (45/2267)
2020-09-22 16:03:57,261 : INFO : family: 47.4% (199/420)
2020-09-22 16:03:57,797 : INFO : gram1-adjective-to-adverb: 6.1% (61/992)
2020-09-22 16:03:58,174 : INFO : gram2-opposite: 6.1% (43/702)
2020-09-22 16:03:58,937 : INFO : gram3-comparative: 30.1% (401/1332)
2020-09-22 16:03:59,594 : INFO : gram4-superlative: 16.3% (172/1056)
2020-09-22 16:04:00,314 : INFO : gram5-present-participle: 18.7% (197/1056)
2020-09-22 16:04:01,335 : INFO : gram6-nationality-adjective: 14.2% (194/1371)
2020-09-22 16:04:02,336 : INFO : gram7-past-tense: 39.1% (610/1560)
2020-09-22 16:04:03,276 : INFO : gram8-plural: 21.8% (291/1332)
2020-09-22 16:04:03,876 : INFO : gram9-plural-verbs: 11.1% (97/870)
2020-09-22 16:04:03,877 : INFO : Quadruplets with out-of-vocabulary words: 21.1%
2020-09-22 16:04:03,877 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-22 16:04:03,877 : INFO : Total accuracy: 16.0% (2464/15421)
Doc2Vec("ech05",dm/m,d15,n10,w2,mc99,s5e-05,t6): 15.98% correct (2464 of 15421)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-22 16:04:04,149 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5170
2020-09-22 16:04:04,149 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5079
2020-09-22 16:04:04,149 : INFO : Pairs with unknown words ratio: 0.6%
((0.5169606111449885, 2.2304891837611116e-25), SpearmanrResult(correlation=0.5079320635224752, pvalue=2.0272896745581428e-24), 0.56657223796034)


02 - simlex999
2020-09-22 16:04:04,198 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3161
2020-09-22 16:04:04,198 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2673
2020-09-22 16:04:04,198 : INFO : Pairs with unknown words ratio: 0.3%
((0.31609912627764136, 1.504893463188641e-24), SpearmanrResult(correlation=0.26729970758871524, pvalue=9.334233148462288e-18), 0.3003003003003003)


03 - simverb3500
2020-09-22 16:04:04,476 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1683
2020-09-22 16:04:04,476 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1497
2020-09-22 16:04:04,476 : INFO : Pairs with unknown words ratio: 1.4%
((0.1682506499068574, 2.451835201483257e-23), SpearmanrResult(correlation=0.14966182910827264, pvalue=9.586117346715404e-19), 1.3714285714285714)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
