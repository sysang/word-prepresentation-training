import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=12, negative=5, window=3, min_count=17, sample=0.0001,
    dm=1, dm_concat=1, hs=0, epochs=25
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'mycorus'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d12,n5,w3,mc17,s0.0001,t6)
Save model to: models/dmc_d12_n5_w3_mc17_s0001_ech25_mycorus.bin
2020-09-08 17:12:22,195 : INFO : saving Doc2Vec object under models/dmc_d12_n5_w3_mc17_s0001_ech25_mycorus.bin, separately None
2020-09-08 17:12:22,195 : INFO : storing np array 'vectors_docs' to models/dmc_d12_n5_w3_mc17_s0001_ech25_mycorus.bin.docvecs.vectors_docs.npy
2020-09-08 17:12:22,598 : INFO : saved models/dmc_d12_n5_w3_mc17_s0001_ech25_mycorus.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 1684841
[+] ... "6000 there are not any my education level could be higher i only have a 2 year degree but i have a lot of professional experience and have run my own businesses in the past"
2020-09-08 17:12:22,607 : INFO : precomputing L2-norms of doc weight vectors
[(2931246, 0.9619573950767517), (1685352, 0.9573418498039246), (1665883, 0.9522591233253479), (1684841, 0.9489223957061768), (3325947, 0.9400041103363037)]


.....get random document, tag: 4164466
[+] ... "i got whiskey you are welcome to some"
[(4332934, 0.9653862714767456), (4073937, 0.9646047949790955), (4034101, 0.9609596729278564), (4225775, 0.9541954398155212), (4571831, 0.9480277299880981)]


.....get random document, tag: 738185
[+] ... "i find it hard to believe that this ill conceived script ever made it past treatment stage particularly when so many established uk film companies like ch4 were involved in its development and finance"
[(738185, 0.9729195833206177), (208979, 0.9575275182723999), (3524265, 0.9476573467254639), (2249698, 0.9468446969985962), (1622867, 0.9462916254997253)]


.....get random document, tag: 2427759
[+] ... "ahhh start the movie already the movie was great but now i am so tired now"
[(2380126, 0.9706314206123352), (689237, 0.957539439201355), (1711636, 0.9509302973747253), (578133, 0.9426259398460388), (3367948, 0.9419698715209961)]


.....get random document, tag: 3665963
[+] ... "i can not decide if that small dark cloud is getting bigger and darker"
[(327008, 0.9597631692886353), (3665963, 0.9589977264404297), (3137226, 0.9511886835098267), (717773, 0.9494911432266235), (3810457, 0.9492546319961548)]


.....get random document, tag: 402493
[+] ... "dramatic license some hate it though it is necessary in retelling any life story"
[(207762, 0.9481591582298279), (4712176, 0.942111611366272), (2250426, 0.939670979976654), (160941, 0.9371615648269653), (239215, 0.9369633793830872)]


.....get random document, tag: 3188260
[+] ... "a member of the administration also made a memory book and a video and guess who was the only person in the entire program not shown or mentioned in either one of them yep you guessed it me and it bothers me as well that people always say the academic classes and the wellness class excuse me i have a bachelor of science in health as far as i am concerned it is an academic area as well"
[(3188260, 0.9767674207687378), (3285985, 0.9463480710983276), (715659, 0.9463310241699219), (4786263, 0.9437332153320312), (2081671, 0.9431408643722534)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (2438554): it was a little undercooked but the sauce made up for it

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d12,n5,w3,mc17,s0.0001,t6):

MOST (2402701, 0.9880416393280029): «made it to coimbatore in no time»

MEDIAN (190379, -0.0012194886803627014): «the daughter molly was exceptionally acted by young india i was able to understand the dialog which is tough in many current films due to rapid speech»

LEAST (3403485, -0.9493077993392944): «the way it works is when grampa starts nodding off behind the wheel of his cadillac of death the strips create a noise and reverberation loud and obnoxious enough to wake him up to enjoy a few more days of adult depends and shuffleboard»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'secure' model: Doc2Vec(dm/c,d12,n5,w3,mc17,s0.0001,t6) similar words:
2020-09-08 17:12:32,119 : INFO : precomputing L2-norms of word weight vectors
     1. 0.95 'destabilize'
     2. 0.94 'overestimate'
     3. 0.94 'hindering'
     4. 0.93 'deterring'
     5. 0.93 'relegate'
     6. 0.93 'gauging'
     7. 0.93 'subsidize'
     8. 0.93 'segregate'
     9. 0.92 'squander'
     10. 0.92 'maximise'
     11. 0.92 'endanger'
     12. 0.92 'equalize'
     13. 0.92 'gain'
     14. 0.92 'limiting'
     15. 0.92 'sidestepping'
     16. 0.91 'partake'
     17. 0.91 'unrestricted'
     18. 0.91 'clamour'
     19. 0.91 'inflame'
     20. 0.91 'investing'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-08 17:12:32,371 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-08 17:12:32,611 : INFO : capital-common-countries: 1.4% (7/506)
2020-09-08 17:12:33,580 : INFO : capital-world: 0.7% (13/1929)
2020-09-08 17:12:33,758 : INFO : currency: 0.0% (0/206)
2020-09-08 17:12:35,039 : INFO : city-in-state: 0.4% (10/2330)
2020-09-08 17:12:35,495 : INFO : family: 20.0% (101/506)
2020-09-08 17:12:36,321 : INFO : gram1-adjective-to-adverb: 1.1% (11/992)
2020-09-08 17:12:37,063 : INFO : gram2-opposite: 0.5% (4/812)
2020-09-08 17:12:38,255 : INFO : gram3-comparative: 15.2% (203/1332)
2020-09-08 17:12:39,252 : INFO : gram4-superlative: 5.3% (60/1122)
2020-09-08 17:12:40,061 : INFO : gram5-present-participle: 7.9% (83/1056)
2020-09-08 17:12:41,170 : INFO : gram6-nationality-adjective: 3.4% (49/1445)
2020-09-08 17:12:42,474 : INFO : gram7-past-tense: 9.2% (143/1560)
2020-09-08 17:12:43,677 : INFO : gram8-plural: 11.0% (147/1332)
2020-09-08 17:12:44,413 : INFO : gram9-plural-verbs: 4.4% (38/870)
2020-09-08 17:12:44,414 : INFO : Quadruplets with out-of-vocabulary words: 18.1%
2020-09-08 17:12:44,414 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-08 17:12:44,415 : INFO : Total accuracy: 5.4% (869/15998)
Doc2Vec(dm/c,d12,n5,w3,mc17,s0.0001,t6): 5.43% correct (869 of 15998)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-08 17:12:44,592 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4650
2020-09-08 17:12:44,592 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4630
2020-09-08 17:12:44,592 : INFO : Pairs with unknown words ratio: 0.6%
((0.4650172085467967, 3.11333038124236e-20), SpearmanrResult(correlation=0.46304605007224725, pvalue=4.695746317411898e-20), 0.56657223796034)


02 - simlex999
2020-09-08 17:12:44,762 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2707
2020-09-08 17:12:44,762 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2241
2020-09-08 17:12:44,762 : INFO : Pairs with unknown words ratio: 0.3%
((0.27065244940307354, 3.508677008799897e-18), SpearmanrResult(correlation=0.224078320705223, pvalue=8.423899710981098e-13), 0.3003003003003003)


03 - simverb3500
2020-09-08 17:12:44,851 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1444
2020-09-08 17:12:44,851 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1357
2020-09-08 17:12:44,851 : INFO : Pairs with unknown words ratio: 0.6%
((0.1443607670857156, 1.1745791169048895e-17), SpearmanrResult(correlation=0.1357425917993565, pvalue=9.00436454843368e-16), 0.6285714285714286)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
