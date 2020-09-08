import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=10, negative=4, window=2, min_count=15, sample=0.0001,
    dm=1, dm_concat=1, hs=0, epochs=20
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'mycorus'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d10,n4,w2,mc15,s0.0001,t24)
Save model to: models/dmc_d10_n4_w2_mc15_s0001_ech20_mycorus.bin
2020-09-08 15:19:01,474 : INFO : saving Doc2Vec object under models/dmc_d10_n4_w2_mc15_s0001_ech20_mycorus.bin, separately None
2020-09-08 15:19:01,474 : INFO : storing np array 'vectors_docs' to models/dmc_d10_n4_w2_mc15_s0001_ech20_mycorus.bin.docvecs.vectors_docs.npy
2020-09-08 15:19:01,810 : INFO : saved models/dmc_d10_n4_w2_mc15_s0001_ech20_mycorus.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 4260471
[+] ... "i like having 4 friends in nyc"
2020-09-08 15:19:01,818 : INFO : precomputing L2-norms of doc weight vectors
[(2074805, 0.9817140698432922), (1099344, 0.973467230796814), (2627512, 0.9711224436759949), (2573526, 0.9690694808959961), (3740187, 0.9673570394515991)]


.....get random document, tag: 3608932
[+] ... "about two weeks ago i weighed around 165"
[(1073474, 0.9790376424789429), (2140357, 0.9708013534545898), (3339745, 0.9651678800582886), (2466274, 0.9646884202957153), (2027322, 0.9598497152328491)]


.....get random document, tag: 3996294
[+] ... "but this one is less daunting i also picked up two cd�s john mayer�s room for squares and angie aparo�s the american"
[(3996294, 0.9866167306900024), (1047954, 0.976254940032959), (1316435, 0.9761562943458557), (1758431, 0.9704985022544861), (2770613, 0.9648193717002869)]


.....get random document, tag: 4426102
[+] ... "the air is thin the roads are curvy"
[(410266, 0.9783536791801453), (4598436, 0.9764955639839172), (2013642, 0.9688836932182312), (1600224, 0.9665447473526001), (4200005, 0.9634998440742493)]


.....get random document, tag: 1926393
[+] ... "all ready for school -christa"
[(2947283, 0.9697936773300171), (1619372, 0.9649617671966553), (3613343, 0.9645590782165527), (509758, 0.9634242057800293), (4152153, 0.9633229374885559)]


.....get random document, tag: 3602762
[+] ... "why should i compromise myself i should not i can not divorce physical intimacy from emotional intimacy so i end up turning off my phone and doing the deed with myself"
[(3289993, 0.978392481803894), (2305843, 0.9714874029159546), (2324118, 0.9641358852386475), (2796325, 0.9640077352523804), (3028813, 0.9596858024597168)]


.....get random document, tag: 1186657
[+] ... " hamilton of the walkmen gets grumpier during a mess of a show"
[(522839, 0.9815146327018738), (556498, 0.9762671589851379), (2042947, 0.9683527946472168), (962010, 0.9659589529037476), (3376525, 0.9647440910339355)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (2118489): he stated the converging of millions of iranian youth imbued with the spirit of shehada martyrdom in the basij forces

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d10,n4,w2,mc15,s0.0001,t24):

MOST (1981801, 0.9794538021087646): «later cougar rolled solo to the sunset»

MEDIAN (3463794, -0.0010634809732437134): «i do not know why but everytime i sleep in so like every day almost my inner clock or something says ok katelyn its ten o'clock you can not sleep any more»

LEAST (3843892, -0.9859995245933533): «yes i am wearing jeans but i also have on my nice black buttondown so i am dress cas and that 's as good as it 's getting today»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'sow' model: Doc2Vec(dm/c,d10,n4,w2,mc15,s0.0001,t24) similar words:
2020-09-08 15:19:11,311 : INFO : precomputing L2-norms of word weight vectors
     1. 0.96 'lashing'
     2. 0.95 'entangle'
     3. 0.94 'repel'
     4. 0.94 'quench'
     5. 0.94 'oscillate'
     6. 0.94 'bubbled'
     7. 0.94 'cleanse'
     8. 0.94 'infest'
     9. 0.93 'extinguish'
     10. 0.93 'resound'
     11. 0.93 'suckle'
     12. 0.93 'thrusting'
     13. 0.93 'shielding'
     14. 0.93 'secrete'
     15. 0.93 'purify'
     16. 0.93 'threateningly'
     17. 0.93 'cling'
     18. 0.93 'breathes'
     19. 0.92 'coursing'
     20. 0.92 'unlocks'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-08 15:19:11,487 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-08 15:19:11,788 : INFO : capital-common-countries: 0.8% (4/506)
2020-09-08 15:19:12,976 : INFO : capital-world: 0.5% (9/1929)
2020-09-08 15:19:13,186 : INFO : currency: 0.4% (1/236)
2020-09-08 15:19:15,013 : INFO : city-in-state: 0.4% (9/2330)
2020-09-08 15:19:15,512 : INFO : family: 17.6% (89/506)
2020-09-08 15:19:16,441 : INFO : gram1-adjective-to-adverb: 0.3% (3/992)
2020-09-08 15:19:17,247 : INFO : gram2-opposite: 0.6% (5/812)
2020-09-08 15:19:18,526 : INFO : gram3-comparative: 8.6% (114/1332)
2020-09-08 15:19:19,600 : INFO : gram4-superlative: 2.8% (31/1122)
2020-09-08 15:19:20,535 : INFO : gram5-present-participle: 5.1% (54/1056)
2020-09-08 15:19:21,398 : INFO : gram6-nationality-adjective: 2.8% (40/1445)
2020-09-08 15:19:22,740 : INFO : gram7-past-tense: 5.0% (78/1560)
2020-09-08 15:19:24,008 : INFO : gram8-plural: 4.7% (62/1332)
2020-09-08 15:19:24,730 : INFO : gram9-plural-verbs: 2.6% (23/870)
2020-09-08 15:19:24,732 : INFO : Quadruplets with out-of-vocabulary words: 18.0%
2020-09-08 15:19:24,733 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-08 15:19:24,734 : INFO : Total accuracy: 3.3% (522/16028)
Doc2Vec(dm/c,d10,n4,w2,mc15,s0.0001,t24): 3.26% correct (522 of 16028)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-08 15:19:24,922 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4100
2020-09-08 15:19:24,922 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.3884
2020-09-08 15:19:24,922 : INFO : Pairs with unknown words ratio: 0.6%
((0.4100091461680409, 1.1567211506305355e-15), SpearmanrResult(correlation=0.38839693428987665, pvalue=4.383482356379088e-14), 0.56657223796034)


02 - simlex999
2020-09-08 15:19:25,095 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2437
2020-09-08 15:19:25,095 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1964
2020-09-08 15:19:25,095 : INFO : Pairs with unknown words ratio: 0.3%
((0.2437223325423957, 6.190595995924164e-15), SpearmanrResult(correlation=0.19644945185949306, pvalue=4.024264142159157e-10), 0.3003003003003003)


03 - simverb3500
2020-09-08 15:19:25,298 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1258
2020-09-08 15:19:25,298 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1131
2020-09-08 15:19:25,298 : INFO : Pairs with unknown words ratio: 0.5%
((0.1258483759699958, 9.191369410102386e-14), SpearmanrResult(correlation=0.11305890767342844, pvalue=2.2387693758286147e-11), 0.5428571428571428)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
