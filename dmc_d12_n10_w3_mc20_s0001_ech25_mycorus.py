import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=12, negative=10, window=3, min_count=20, sample=0.0001,
    dm=1, dm_concat=1, hs=0, epochs=25
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'mycorus'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d12,n10,w3,mc20,s0.0001,t10)
Save model to: models/dmc_d12_n10_w3_mc20_s0001_ech25_mycorus.bin
2020-09-09 19:19:55,042 : INFO : saving Doc2Vec object under models/dmc_d12_n10_w3_mc20_s0001_ech25_mycorus.bin, separately None
2020-09-09 19:19:55,042 : INFO : storing np array 'vectors_docs' to models/dmc_d12_n10_w3_mc20_s0001_ech25_mycorus.bin.docvecs.vectors_docs.npy
2020-09-09 19:19:55,696 : INFO : saved models/dmc_d12_n10_w3_mc20_s0001_ech25_mycorus.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 4619922
[+] ... "when i think of it i want to shake you to squeeze you until you scream then please do not think of it she said"
2020-09-09 19:19:55,704 : INFO : precomputing L2-norms of doc weight vectors
[(9269614, 0.9674045443534851), (6720503, 0.9552537798881531), (6083960, 0.9530664682388306), (684435, 0.9511041045188904), (4159115, 0.9494420289993286)]


.....get random document, tag: 9197876
[+] ... "i do not stalk for real but if i want something hells if i am not going to go for it"
[(5330392, 0.961092472076416), (9741064, 0.9504188299179077), (6226498, 0.9504178762435913), (7344584, 0.9488785266876221), (9664139, 0.9465285539627075)]


.....get random document, tag: 7825365
[+] ... "i feel as if i am either going to have to find the path by touch or by hacking one out of the clutter that i have amassed of life"
[(7825365, 0.9688466787338257), (1900348, 0.9496582746505737), (7764897, 0.9449467658996582), (216715, 0.9423065781593323), (9426874, 0.9413809776306152)]


.....get random document, tag: 986833
[+] ... "the militia was raised to prevent it and now i suppose all will be quiet"
[(2270072, 0.9606310129165649), (2671065, 0.9484516978263855), (2709412, 0.9480851292610168), (6285186, 0.9429194927215576), (1172226, 0.9427967071533203)]


.....get random document, tag: 9050472
[+] ... "i can respect that but looking back i have my fears that is more like looking for other pussy"
[(8139142, 0.9761379361152649), (5556693, 0.9610348343849182), (6382459, 0.955551266670227), (47259, 0.9446572065353394), (7471587, 0.9440778493881226)]


.....get random document, tag: 1577236
[+] ... "i was only colouring the canaletto engravings that hung in my old bedroom at home the picture was a shifting one my mind wandering uncertainly in search of more vivid images i could see no accident of form or shadow without conscious labour after the necessary conditions"
[(485567, 0.9674605131149292), (1577236, 0.951709508895874), (4098711, 0.9516301155090332), (3936312, 0.9504102468490601), (5446624, 0.9481081366539001)]


.....get random document, tag: 8563433
[+] ... "so far melanie beah and karen have sent in pictures so i am calling out to all you other friends"
[(4944436, 0.9732697606086731), (3175497, 0.9491265416145325), (8152085, 0.9480865001678467), (8250971, 0.9480841755867004), (7039052, 0.9470381140708923)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (2192698): once we turned a corner suddenly and surprised a slender girl of twelve years or upward just stepping into the water

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d12,n10,w3,mc20,s0.0001,t10):

MOST (6916470, 0.9653477668762207): «flickr-photo border solid 1px 000000 flickr-yourcomment flickr-frame float left width 150px text-align center padding 3px margin-right 10px flickr-caption font 75% / color 666666 /       margin-top 0px flickr-buddyicon margin-right 5px vertical-align middle border solid 1px flickr-postedby font 75% week 3 front view originally uploaded by bigbelly»

MEDIAN (1317148, -0.0017068535089492798): «'tis wonderful one said not so much that our new comrade should have killed the leopard though that was a great feat but that armed only with a knife he should attack a beast like this to save the life of a stranger»

LEAST (7707292, -0.9612028002738953): «mas indi and i along with dimas adi jay broke the fast in geylang night market at s-11 food court»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'aright' model: Doc2Vec(dm/c,d12,n10,w3,mc20,s0.0001,t10) similar words:
2020-09-09 19:20:13,900 : INFO : precomputing L2-norms of word weight vectors
     1. 0.91 'wherefore'
     2. 0.91 'beforehand'
     3. 0.89 'arga'
     4. 0.89 'lyndar'
     5. 0.88 'nilang'
     6. 0.88 'kayang'
     7. 0.87 'her/him'
     8. 0.87 'alm'
     9. 0.87 'n-no'
     10. 0.87 'buhay'
     11. 0.87 'bigamy'
     12. 0.87 'mahirap'
     13. 0.86 'whensoever'
     14. 0.86 'galit'
     15. 0.85 'boab'
     16. 0.85 'maaga'
     17. 0.85 'bukas'
     18. 0.85 'fisc'
     19. 0.85 'emp'
     20. 0.85 'whosoever'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-09 19:20:14,314 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-09 19:20:14,667 : INFO : capital-common-countries: 2.8% (14/506)
2020-09-09 19:20:15,987 : INFO : capital-world: 1.2% (21/1775)
2020-09-09 19:20:16,284 : INFO : currency: 0.0% (0/236)
2020-09-09 19:20:18,367 : INFO : city-in-state: 0.4% (10/2330)
2020-09-09 19:20:18,996 : INFO : family: 27.1% (137/506)
2020-09-09 19:20:20,090 : INFO : gram1-adjective-to-adverb: 1.1% (11/992)
2020-09-09 19:20:20,893 : INFO : gram2-opposite: 2.0% (14/702)
2020-09-09 19:20:22,231 : INFO : gram3-comparative: 24.2% (323/1332)
2020-09-09 19:20:23,315 : INFO : gram4-superlative: 6.3% (71/1122)
2020-09-09 19:20:24,423 : INFO : gram5-present-participle: 5.7% (60/1056)
2020-09-09 19:20:25,820 : INFO : gram6-nationality-adjective: 2.2% (30/1371)
2020-09-09 19:20:27,580 : INFO : gram7-past-tense: 14.2% (222/1560)
2020-09-09 19:20:29,158 : INFO : gram8-plural: 7.1% (95/1332)
2020-09-09 19:20:30,161 : INFO : gram9-plural-verbs: 6.8% (59/870)
2020-09-09 19:20:30,162 : INFO : Quadruplets with out-of-vocabulary words: 19.7%
2020-09-09 19:20:30,162 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-09 19:20:30,162 : INFO : Total accuracy: 6.8% (1067/15690)
Doc2Vec(dm/c,d12,n10,w3,mc20,s0.0001,t10): 6.80% correct (1067 of 15690)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-09 19:20:30,445 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4311
2020-09-09 19:20:30,445 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4221
2020-09-09 19:20:30,445 : INFO : Pairs with unknown words ratio: 0.6%
((0.4311205727715411, 2.5520396249681907e-17), SpearmanrResult(correlation=0.4221225301601715, pvalue=1.3399742167957386e-16), 0.56657223796034)


02 - simlex999
2020-09-09 19:20:30,894 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2812
2020-09-09 19:20:30,894 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2382
2020-09-09 19:20:30,894 : INFO : Pairs with unknown words ratio: 0.2%
((0.2811676867680704, 1.429616605496913e-19), SpearmanrResult(correlation=0.2382386884556537, pvalue=2.4775885888561222e-14), 0.20020020020020018)


03 - simverb3500
2020-09-09 19:20:31,194 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1486
2020-09-09 19:20:31,194 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1290
2020-09-09 19:20:31,194 : INFO : Pairs with unknown words ratio: 0.1%
((0.14860679330788365, 9.997228306498545e-19), SpearmanrResult(correlation=0.12895014053197698, pvalue=1.920084059325663e-14), 0.05714285714285715)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
