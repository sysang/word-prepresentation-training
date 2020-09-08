import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=10, negative=4, window=2, min_count=15, sample=0.0001,
    dm=1, dm_concat=1, hs=0, epochs=10
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'mycorus'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d10,n4,w2,mc15,s0.0001,t12)
Save model to: models/dmc_d10_n4_w2_mc15_s0001_ech10_mycorus.bin
2020-09-08 13:10:34,008 : INFO : saving Doc2Vec object under models/dmc_d10_n4_w2_mc15_s0001_ech10_mycorus.bin, separately None
2020-09-08 13:10:34,008 : INFO : storing np array 'vectors_docs' to models/dmc_d10_n4_w2_mc15_s0001_ech10_mycorus.bin.docvecs.vectors_docs.npy
2020-09-08 13:10:34,334 : INFO : saved models/dmc_d10_n4_w2_mc15_s0001_ech10_mycorus.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 4620612
[+] ... "in the uk the mnemonic dr abc is commonly used "
2020-09-08 13:10:34,347 : INFO : precomputing L2-norms of doc weight vectors
[(924308, 0.9766184091567993), (460851, 0.9680538773536682), (1934097, 0.9678187370300293), (2234711, 0.9629461169242859), (755022, 0.9622186422348022)]


.....get random document, tag: 3054582
[+] ... "of course if anyone who ever worked in korea read that it would certainly be a lot more understandable"
[(2804300, 0.9841890931129456), (4035579, 0.9691250324249268), (1473263, 0.9688710570335388), (4694788, 0.9602877497673035), (2711541, 0.9598082304000854)]


.....get random document, tag: 4019096
[+] ... "what right do we then have to expect that those same people should give us the benefit of the doubt or put any effort into finding our positive traits i believe that you should strive to give as much or more as your expect from others"
[(1475938, 0.9791799187660217), (3175968, 0.9757035970687866), (1372914, 0.9687117338180542), (4730560, 0.9667137861251831), (3979398, 0.9666146039962769)]


.....get random document, tag: 1332261
[+] ... "they will get used to everything though"
[(1887739, 0.9713970422744751), (1881558, 0.9686745405197144), (704795, 0.9663367867469788), (2489716, 0.9655454158782959), (3412667, 0.9620736241340637)]


.....get random document, tag: 757549
[+] ... "although i did not identify myself on this movie i have identified some friends in trouble and why not some issues that happens to my marriage"
[(2365239, 0.9688475728034973), (4117999, 0.9623947143554688), (1319412, 0.9612398743629456), (4271475, 0.9573900699615479), (3417789, 0.9572978019714355)]


.....get random document, tag: 2644181
[+] ... "the daily flights are limited as they need to see the mountains in order to land"
[(3067265, 0.9791036248207092), (434924, 0.9760769009590149), (1343943, 0.9757484197616577), (3449879, 0.973920464515686), (199300, 0.9734392166137695)]


.....get random document, tag: 1499303
[+] ... "“between now and november you the american people you can reject the tired old hateful negative politics of the past internal dialogue – woo-hoo they’re finally putting ted kennedy out to pasture rock on shiny hair rock on i take another hit off the bottle and lose my pen"
[(4376229, 0.980786144733429), (2017619, 0.9737756252288818), (3107432, 0.9737040400505066), (1316243, 0.971422553062439), (4009796, 0.9627509117126465)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (306316): for example when she leaves his place after having the beer and he finds the pics and she runs out and he catches her and they end up having sex in that car

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d10,n4,w2,mc15,s0.0001,t12):

MOST (1283090, 0.9718314409255981): «it was indeed a crazy day»

MEDIAN (342088, -0.001316465437412262): «although i do have problems fully understanding the stories  the visual style is unique with all its dirt dust and decay»

LEAST (4372614, -0.9896165728569031): «nobody is breaking my heart and it totally sucks»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'interaction' model: Doc2Vec(dm/c,d10,n4,w2,mc15,s0.0001,t12) similar words:
2020-09-08 13:10:43,993 : INFO : precomputing L2-norms of word weight vectors
     1. 0.98 'emphasis'
     2. 0.98 'self-belief'
     3. 0.97 'hypnosis'
     4. 0.97 'responsiveness'
     5. 0.97 'knowledge'
     6. 0.97 'technicalities'
     7. 0.97 'experimentation'
     8. 0.97 'evidence'
     9. 0.96 'limitation'
     10. 0.96 'mismatch'
     11. 0.96 'aspiration'
     12. 0.96 'restraint'
     13. 0.96 'coherence'
     14. 0.96 'incompatibility'
     15. 0.96 'biases'
     16. 0.96 'insights'
     17. 0.96 'coordination'
     18. 0.96 'stimulus'
     19. 0.95 'rigidity'
     20. 0.95 'diagnoses'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-08 13:10:44,242 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-08 13:10:44,556 : INFO : capital-common-countries: 2.8% (14/506)
2020-09-08 13:10:45,783 : INFO : capital-world: 0.9% (18/1929)
2020-09-08 13:10:45,977 : INFO : currency: 0.0% (0/236)
2020-09-08 13:10:47,837 : INFO : city-in-state: 0.6% (13/2330)
2020-09-08 13:10:48,326 : INFO : family: 16.2% (82/506)
2020-09-08 13:10:49,268 : INFO : gram1-adjective-to-adverb: 0.6% (6/992)
2020-09-08 13:10:50,060 : INFO : gram2-opposite: 1.2% (10/812)
2020-09-08 13:10:51,368 : INFO : gram3-comparative: 8.6% (115/1332)
2020-09-08 13:10:52,465 : INFO : gram4-superlative: 2.4% (27/1122)
2020-09-08 13:10:53,385 : INFO : gram5-present-participle: 5.8% (61/1056)
2020-09-08 13:10:54,412 : INFO : gram6-nationality-adjective: 1.9% (27/1445)
2020-09-08 13:10:55,777 : INFO : gram7-past-tense: 6.7% (104/1560)
2020-09-08 13:10:57,059 : INFO : gram8-plural: 7.0% (93/1332)
2020-09-08 13:10:57,801 : INFO : gram9-plural-verbs: 2.8% (24/870)
2020-09-08 13:10:57,802 : INFO : Quadruplets with out-of-vocabulary words: 18.0%
2020-09-08 13:10:57,802 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-08 13:10:57,802 : INFO : Total accuracy: 3.7% (594/16028)
Doc2Vec(dm/c,d10,n4,w2,mc15,s0.0001,t12): 3.71% correct (594 of 16028)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-08 13:10:57,984 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4359
2020-09-08 13:10:57,985 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4125
2020-09-08 13:10:57,985 : INFO : Pairs with unknown words ratio: 0.6%
((0.4359177934211893, 1.032875819933962e-17), SpearmanrResult(correlation=0.4124542568308612, pvalue=7.538852257549513e-16), 0.56657223796034)


02 - simlex999
2020-09-08 13:10:58,156 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2370
2020-09-08 13:10:58,157 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1902
2020-09-08 13:10:58,157 : INFO : Pairs with unknown words ratio: 0.3%
((0.23699903024166746, 3.498570898571704e-14), SpearmanrResult(correlation=0.19022604989893327, pvalue=1.4374374137763897e-09), 0.3003003003003003)


03 - simverb3500
2020-09-08 13:10:58,358 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1270
2020-09-08 13:10:58,358 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1129
2020-09-08 13:10:58,358 : INFO : Pairs with unknown words ratio: 0.5%
((0.12695238205352524, 5.5647617471501855e-14), SpearmanrResult(correlation=0.11289185205252879, pvalue=2.3961265218281846e-11), 0.5428571428571428)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
