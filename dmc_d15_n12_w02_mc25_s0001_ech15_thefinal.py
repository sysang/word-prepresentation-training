# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=15, negative=12, window=2, min_count=25, sample=0.0001,
    dm=1, dm_concat=1, hs=0, epochs=15
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'thefinal'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS - 01


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5)
Save model to: models/dmc_d15_n12_w2_mc25_s0001_ech15_thefinal.bin
2020-09-11 10:36:46,799 : INFO : saving Doc2Vec object under models/dmc_d15_n12_w2_mc25_s0001_ech15_thefinal.bin, separately None
2020-09-11 10:36:46,800 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n12_w2_mc25_s0001_ech15_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-11 10:36:46,828 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n12_w2_mc25_s0001_ech15_thefinal.bin.docvecs.vectors_docs.npy
2020-09-11 10:36:47,574 : INFO : saved models/dmc_d15_n12_w2_mc25_s0001_ech15_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 2995125
[+] index 2995125 -> "maginnis for one held him in the very highest esteem"
2020-09-11 10:36:47,585 : INFO : precomputing L2-norms of doc weight vectors
** Matched with rank 84, score: 0.854975700378418


.....get random document, tag: 7954118
[+] index 7954118 -> "males have a median income of $66 042 versus $32 361 for females"
!! No any match in top 100 similarities


.....get random document, tag: 11209120
[+] index 11209120 -> "last night was the bachelorette party that sarah designed"
** Matched with rank 3, score: 0.9393359422683716


.....get random document, tag: 915839
[+] index 915839 -> "it 's just that that i want to say to you not come back to the crescent no mrs roper"
!! No any match in top 100 similarities


.....get random document, tag: 1995689
[+] index 1995689 -> "papakena and vanavana are off there to the westward or west-nor'westward a hundred miles and a bit more he said"
!! No any match in top 100 similarities


.....get random document, tag: 7141231
[+] index 7141231 -> "the median income for a household in the town is $30 078 and the median income for a family is $35 351"
!! No any match in top 100 similarities


.....get random document, tag: 11558157
[+] index 11558157 -> "at the end of the day i wonder if i am fucking crazy"
** Matched with rank 19, score: 0.8934910893440247




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (3692918): heaven bless thee child in thy early risings and in thy later sittings at thy festive board overflowing with essig and fett in the mysteries of thy kuchen in the fulness of thy bier and in thy nightly suffocations beneath mountainous and multitudinous feathers good honest simple-minded cheerful duty-loving lenchen have not thy brothers strong and dutiful as thou lent their gravity and earnestness to sweeten and strengthen the fierce youth of the republic beyond the seas and shall not thy children inherit the broad prairies that still wait for them and discover the fatness thereof and send a portion transmuted in glittering shekels back to thee almost as notable are the children whose round faces have as frequently been reflected in my spion

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5):

MOST (5139469, 0.9546419978141785): «forbear your mirth and rude alarm for none shall do them shame or harm hear ye his boast cried john of brent ever to strife and jangling bent 'shall he strike doe beside our lodge and yet the jealous niggard grudge to pay the forester his fee ll have my share howe'er it be despite of moray mar or thee ' bertram his forward step withstood and burning in his vengeful mood old allan though unfit for strife laid hand upon his dagger-knife but ellen boldly stepped between and dropped at once the tartan screen so from his morning cloud appears the sun of may through summer tears»

MEDIAN (8825477, -0.003984764218330383): «the game takes place two years after gruntilda the witch was defeated by banjo and kazooie»

LEAST (2860482, -0.9500117897987366): «the doctor shook him first and then punched him»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'preference' model: Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5):
2020-09-11 10:37:14,552 : INFO : precomputing L2-norms of word weight vectors
     1. 0.96 'fidelity'
     2. 0.95 'knowledge'
     3. 0.95 'pretensions'
     4. 0.95 'merit'
     5. 0.94 'leadings'
     6. 0.94 'proficiency'
     7. 0.94 'esteem'


[+] target_word: 'yea' model: Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5):
     1. 0.93 'nay'
     2. 0.92 "'perhaps"
     3. 0.91 'wherefore'
     4. 0.91 'haverily'
     5. 0.91 'psha'
     6. 0.91 'alas'
     7. 0.90 'calib'


[+] target_word: 'fastest' model: Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5):
     1. 0.93 'mid-size'
     2. 0.89 'slowest'
     3. 0.88 'privately-owned'
     4. 0.88 'acela'
     5. 0.88 'semi'
     6. 0.88 'main-line'
     7. 0.87 'mid-sized'


[+] target_word: '3/mi²' model: Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5):
     1. 1.00 '7/mi²'
     2. 1.00 '4/mi²'
     3. 1.00 '8/mi²'
     4. 1.00 '5/mi²'
     5. 1.00 '0/mi²'
     6. 1.00 '6/mi²'
     7. 1.00 '1/mi²'


[+] target_word: 'questioning' model: Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5):
     1. 0.92 'pontificating'
     2. 0.91 'censuring'
     3. 0.91 'contradicting'
     4. 0.91 'prayerful'
     5. 0.90 'inquiring'
     6. 0.89 'arguing'
     7. 0.89 'pleading'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-11 10:37:16,344 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-11 10:37:17,070 : INFO : capital-common-countries: 8.9% (45/506)
2020-09-11 10:37:22,453 : INFO : capital-world: 2.2% (83/3701)
2020-09-11 10:37:23,085 : INFO : currency: 1.5% (7/458)
2020-09-11 10:37:26,271 : INFO : city-in-state: 1.5% (36/2394)
2020-09-11 10:37:27,017 : INFO : family: 29.8% (151/506)
2020-09-11 10:37:28,189 : INFO : gram1-adjective-to-adverb: 2.9% (29/992)
2020-09-11 10:37:29,341 : INFO : gram2-opposite: 4.8% (39/812)
2020-09-11 10:37:30,468 : INFO : gram3-comparative: 25.4% (338/1332)
2020-09-11 10:37:31,418 : INFO : gram4-superlative: 11.6% (122/1056)
2020-09-11 10:37:32,620 : INFO : gram5-present-participle: 11.9% (126/1056)
2020-09-11 10:37:34,927 : INFO : gram6-nationality-adjective: 8.5% (130/1521)
2020-09-11 10:37:37,071 : INFO : gram7-past-tense: 16.1% (251/1560)
2020-09-11 10:37:38,950 : INFO : gram8-plural: 10.1% (134/1332)
2020-09-11 10:37:40,220 : INFO : gram9-plural-verbs: 7.9% (69/870)
2020-09-11 10:37:40,223 : INFO : Quadruplets with out-of-vocabulary words: 7.4%
2020-09-11 10:37:40,224 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-11 10:37:40,225 : INFO : Total accuracy: 8.6% (1560/18096)
Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5): 8.62% correct (1560 of 18096)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-11 10:37:40,823 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4636
2020-09-11 10:37:40,823 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4537
2020-09-11 10:37:40,823 : INFO : Pairs with unknown words ratio: 0.0%
((0.46363087541422815, 3.255011043250101e-20), SpearmanrResult(correlation=0.4536596309035586, pvalue=2.5388598231299904e-19), 0.0)


02 - simlex999
2020-09-11 10:37:41,171 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3128
2020-09-11 10:37:41,171 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2770
2020-09-11 10:37:41,171 : INFO : Pairs with unknown words ratio: 0.2%
((0.3128303438811894, 4.485306736675294e-24), SpearmanrResult(correlation=0.27703366201237023, pvalue=5.037390470350372e-19), 0.20020020020020018)


03 - simverb3500
2020-09-11 10:37:41,544 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1778
2020-09-11 10:37:41,544 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1623
2020-09-11 10:37:41,544 : INFO : Pairs with unknown words ratio: 0.1%
((0.17775580894683857, 3.1811396431158084e-26), SpearmanrResult(correlation=0.16229929003253205, pvalue=4.472157570735306e-22), 0.05714285714285715)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS - 02


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5)
Save model to: models/dmc_d15_n12_w02_mc25_s0001_ech15_thefinal.bin
2020-09-11 14:16:13,546 : INFO : saving Doc2Vec object under models/dmc_d15_n12_w02_mc25_s0001_ech15_thefinal.bin, separately None
2020-09-11 14:16:13,547 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n12_w02_mc25_s0001_ech15_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-11 14:16:13,577 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n12_w02_mc25_s0001_ech15_thefinal.bin.docvecs.vectors_docs.npy
2020-09-11 14:16:14,320 : INFO : saved models/dmc_d15_n12_w02_mc25_s0001_ech15_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 2922164
[+] index 2922164 -> "a stranger would have noticed nothing remarkable in him"
2020-09-11 14:16:14,334 : INFO : precomputing L2-norms of doc weight vectors
** Matched with rank 1, score: 0.94222092628479


.....get random document, tag: 4887266
[+] index 4887266 -> "salah-ed-din commander of the faithful the king strong to aid sovereign of the east sat at night in his palace at damascus and brooded on the wonderful ways of god by whom he had been lifted to his high estate"
!! No any match in top 100 similarities


.....get random document, tag: 2489654
[+] index 2489654 -> "jocelyn thew has brought it off against us this time but then you see one must lose a trick now and then"
!! No any match in top 100 similarities


.....get random document, tag: 8855023
[+] index 8855023 -> "the old state house was commissioned by territorial governor john pope and was constructed between 1833 and 1842"
!! No any match in top 100 similarities


.....get random document, tag: 6312904
[+] index 6312904 -> "mchugh repeated his own role in the remake of one way passage from 1940 till we meet again"
** Matched with rank 11, score: 0.8903900384902954


.....get random document, tag: 13171051
[+] index 13171051 -> "we should take a few steps at a time"
** Matched with rank 2, score: 0.9365096092224121


.....get random document, tag: 11002260
[+] index 11002260 -> "and i got to be a dick as he was being a little wishy-washy about the whole thing and your last day will be however he resigned because he 's moving to vegas"
!! No any match in top 100 similarities




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (11376449): nah so i will sign off as ellen aka eaj or as eaj

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5):

MOST (10890701, 0.9544616341590881): «nah so i will sign off as ellen aka eaj or as eaj»

MEDIAN (1755258, -0.0020714960992336273): «you will be astonished when you go on board one of the great liners and as they walked along the boulevards he told her of the floating palaces in one of which they were to cross the ocean and forgetting for a time the questions that absorbed her she listened with the interest of a child hearing a fairy-tale»

LEAST (7643313, -0.9381879568099976): «manly and wade wellamn who wrote sherlock holmes' war of the worlds which describes the famous detective 's adventures during the martian occupation of london turned the martians into simple vampires who suck and ingest human blood»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'hast' model: Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5):
2020-09-11 14:16:40,992 : INFO : precomputing L2-norms of word weight vectors
     1. 0.97 'hadst'
     2. 0.96 'hath'
     3. 0.93 'wert'
     4. 0.91 'botting'
     5. 0.90 'wast'
     6. 0.88 'hereunto'
     7. 0.87 "thou'rt"


[+] target_word: 'excitement' model: Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5):
     1. 0.97 'inquietude'
     2. 0.97 'exhilaration'
     3. 0.97 'restlessness'
     4. 0.97 'elation'
     5. 0.96 'sadness'
     6. 0.96 'trepidation'
     7. 0.96 'lassitude'


[+] target_word: 'sonnets' model: Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5):
     1. 0.98 'poems'
     2. 0.96 'eclogues'
     3. 0.96 'oratorios'
     4. 0.96 'pastorals'
     5. 0.96 'odes'
     6. 0.95 'epistles'
     7. 0.95 'hymns'


[+] target_word: 'jewels' model: Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5):
     1. 0.95 'pearls'
     2. 0.95 'wares'
     3. 0.94 'diamonds'
     4. 0.94 'cordials'
     5. 0.94 'silks'
     6. 0.93 'trinkets'
     7. 0.93 'raiment'


[+] target_word: 'player' model: Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5):
     1. 0.93 'limewire'
     2. 0.92 'mmc'
     3. 0.92 'walkman'
     4. 0.92 'exec'
     5. 0.92 'newswire'
     6. 0.92 'tivo'
     7. 0.92 'newsreader'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-11 14:16:42,278 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-11 14:16:42,986 : INFO : capital-common-countries: 7.9% (40/506)
2020-09-11 14:16:48,339 : INFO : capital-world: 2.7% (100/3701)
2020-09-11 14:16:48,969 : INFO : currency: 1.1% (5/458)
2020-09-11 14:16:52,071 : INFO : city-in-state: 1.5% (35/2394)
2020-09-11 14:16:52,803 : INFO : family: 28.5% (144/506)
2020-09-11 14:16:53,964 : INFO : gram1-adjective-to-adverb: 2.1% (21/992)
2020-09-11 14:16:55,132 : INFO : gram2-opposite: 3.9% (32/812)
2020-09-11 14:16:56,362 : INFO : gram3-comparative: 26.6% (354/1332)
2020-09-11 14:16:57,381 : INFO : gram4-superlative: 11.7% (124/1056)
2020-09-11 14:16:58,678 : INFO : gram5-present-participle: 11.3% (119/1056)
2020-09-11 14:17:00,977 : INFO : gram6-nationality-adjective: 9.3% (141/1521)
2020-09-11 14:17:03,150 : INFO : gram7-past-tense: 17.9% (279/1560)
2020-09-11 14:17:05,159 : INFO : gram8-plural: 10.7% (142/1332)
2020-09-11 14:17:06,421 : INFO : gram9-plural-verbs: 7.4% (64/870)
2020-09-11 14:17:06,422 : INFO : Quadruplets with out-of-vocabulary words: 7.4%
2020-09-11 14:17:06,422 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-11 14:17:06,422 : INFO : Total accuracy: 8.8% (1600/18096)
Doc2Vec(dm/c,d15,n12,w2,mc25,s0.0001,t5): 8.84% correct (1600 of 18096)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-11 14:17:07,015 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4723
2020-09-11 14:17:07,015 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4659
2020-09-11 14:17:07,015 : INFO : Pairs with unknown words ratio: 0.0%
((0.4723498084054025, 5.1074197535235565e-21), SpearmanrResult(correlation=0.46593793727327076, pvalue=2.0042557554845413e-20), 0.0)


02 - simlex999
2020-09-11 14:17:07,366 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3212
2020-09-11 14:17:07,366 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2842
2020-09-11 14:17:07,366 : INFO : Pairs with unknown words ratio: 0.2%
((0.3212086695072286, 2.314762107082221e-25), SpearmanrResult(correlation=0.28424905321328375, pvalue=5.51395413203146e-20), 0.20020020020020018)


03 - simverb3500
2020-09-11 14:17:07,988 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1821
2020-09-11 14:17:07,988 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1691
2020-09-11 14:17:07,988 : INFO : Pairs with unknown words ratio: 0.1%
((0.18207903974929657, 1.870011891398116e-27), SpearmanrResult(correlation=0.16905459124940572, pvalue=7.689662031533942e-24), 0.05714285714285715)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""

