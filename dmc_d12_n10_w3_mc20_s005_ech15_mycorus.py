import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=12, negative=10, window=3, min_count=20, sample=0.005,
    dm=1, dm_concat=1, hs=0, epochs=15
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'mycorus'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d12,n10,w3,mc20,s0.005,t10)
Save model to: models/dmc_d12_n10_w3_mc20_s005_ech15_mycorus.bin
2020-09-09 21:57:58,882 : INFO : saving Doc2Vec object under models/dmc_d12_n10_w3_mc20_s005_ech15_mycorus.bin, separately None
2020-09-09 21:57:58,882 : INFO : storing np array 'vectors_docs' to models/dmc_d12_n10_w3_mc20_s005_ech15_mycorus.bin.docvecs.vectors_docs.npy
2020-09-09 21:57:59,537 : INFO : saved models/dmc_d12_n10_w3_mc20_s005_ech15_mycorus.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 2498051
[+] ... "the glory of lodging over this structure would have compensated him i dare say for many inconveniences but as there were really few to bear beyond the compound of flavours i have already mentioned and perhaps the want of a little more elbow-room he was perfectly charmed with his accommodation"
2020-09-09 21:57:59,547 : INFO : precomputing L2-norms of doc weight vectors
[(6747516, 0.9483538269996643), (2510691, 0.9483426809310913), (9355454, 0.948197603225708), (8463650, 0.9358583688735962), (6556306, 0.9333260655403137)]


.....get random document, tag: 2116268
[+] ... "and what we see is constantly changing in shape as we move about the room so that here again the senses seem not to give us the truth about the table itself but only about the appearance of the table"
[(909761, 0.9692115783691406), (9584526, 0.965015709400177), (2325828, 0.9574019312858582), (2601096, 0.9569863677024841), (2494981, 0.9566344022750854)]


.....get random document, tag: 6643268
[+] ... "he and i have remarkably different taste in music for the most part but over the years we have each bent a little and expanded our mutual horizons"
[(812941, 0.9634590148925781), (1164098, 0.9514676332473755), (9003344, 0.9449469447135925), (2323334, 0.9404301643371582), (2963866, 0.9391875267028809)]


.....get random document, tag: 35292
[+] ... "'did not you ever see sir francis drake again 'dan asked"
[(4262148, 0.9604718089103699), (8346222, 0.9592999219894409), (5646766, 0.9585494995117188), (6825947, 0.9541319608688354), (6531171, 0.9537328481674194)]


.....get random document, tag: 7716663
[+] ... "trademark cocktails old-fashioned cap would probably like an old-fashioned just fine or a dry martini or a gin an d tonic or a gimlet or any other no-nonsense quaff"
[(7716663, 0.9679645895957947), (4383883, 0.9653164744377136), (6479152, 0.9513527154922485), (5554387, 0.9498651027679443), (5919540, 0.9493077397346497)]


.....get random document, tag: 1440371
[+] ... "that 's a good deal oh that yes but strether hesitated"
[(6890304, 0.9656898975372314), (6220421, 0.9515254497528076), (6522219, 0.946465253829956), (4599730, 0.9442457556724548), (1383136, 0.9421204328536987)]


.....get random document, tag: 1628885
[+] ... "the nine dogs were also seated round the room watching the process with melancholy interest for their supper was not in that pot and they knew it and wished it was"
[(5386414, 0.9655930399894714), (4883504, 0.9572414755821228), (8775115, 0.953679084777832), (8075451, 0.9509193897247314), (6043833, 0.94951331615448)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (7860869): rather i am referring to people who like i wish to will never give up what they believe in nor what they demand to posess in this life no matter the obstacles such as disease persectution ignorance or stereotypes which may come along in their daily lives

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d12,n10,w3,mc20,s0.005,t10):

MOST (7483832, 0.9648570418357849): «or god forbid created cults as a way to make a family»

MEDIAN (1086279, -0.00479474663734436): «let gian maria come and he will find valentina della rovere none so easy to reduce»

LEAST (4383148, -0.962679922580719): «i drank my first cocktail at eleven-thirty when i took the morning 's mail into the hammock and i drank my second cocktail an hour later just before i ate»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'labored' model: Doc2Vec(dm/c,d12,n10,w3,mc20,s0.005,t10) similar words:
2020-09-09 21:58:17,572 : INFO : precomputing L2-norms of word weight vectors
     1. 0.98 'laboured'
     2. 0.97 'slurred'
     3. 0.96 'focussed'
     4. 0.96 'gelled'
     5. 0.96 'contracted'
     6. 0.95 'staid'
     7. 0.95 'boggled'
     8. 0.95 'grinded'
     9. 0.95 'transposed'
     10. 0.95 'pipped'
     11. 0.94 'sweated'
     12. 0.94 'softened'
     13. 0.94 'chafed'
     14. 0.94 'honed'
     15. 0.94 'relaxed'
     16. 0.94 'cowed'
     17. 0.94 'discriminated'
     18. 0.94 'pinched'
     19. 0.94 'focused'
     20. 0.94 'cribbed'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-09 21:58:18,168 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-09 21:58:18,802 : INFO : capital-common-countries: 2.4% (12/506)
2020-09-09 21:58:21,135 : INFO : capital-world: 0.4% (7/1775)
2020-09-09 21:58:21,386 : INFO : currency: 0.0% (0/236)
2020-09-09 21:58:24,225 : INFO : city-in-state: 0.2% (4/2330)
2020-09-09 21:58:24,836 : INFO : family: 27.5% (139/506)
2020-09-09 21:58:26,088 : INFO : gram1-adjective-to-adverb: 0.3% (3/992)
2020-09-09 21:58:26,902 : INFO : gram2-opposite: 1.1% (8/702)
2020-09-09 21:58:28,373 : INFO : gram3-comparative: 5.4% (72/1332)
2020-09-09 21:58:29,482 : INFO : gram4-superlative: 2.6% (29/1122)
2020-09-09 21:58:30,770 : INFO : gram5-present-participle: 1.3% (14/1056)
2020-09-09 21:58:32,117 : INFO : gram6-nationality-adjective: 1.4% (19/1371)
2020-09-09 21:58:34,051 : INFO : gram7-past-tense: 1.7% (26/1560)
2020-09-09 21:58:35,809 : INFO : gram8-plural: 1.5% (20/1332)
2020-09-09 21:58:36,870 : INFO : gram9-plural-verbs: 4.5% (39/870)
2020-09-09 21:58:36,871 : INFO : Quadruplets with out-of-vocabulary words: 19.7%
2020-09-09 21:58:36,871 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-09 21:58:36,871 : INFO : Total accuracy: 2.5% (392/15690)
Doc2Vec(dm/c,d12,n10,w3,mc20,s0.005,t10): 2.50% correct (392 of 15690)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-09 21:58:37,170 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.2788
2020-09-09 21:58:37,170 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.2894
2020-09-09 21:58:37,170 : INFO : Pairs with unknown words ratio: 0.6%
((0.27883634803008844, 1.0898633243157093e-07), SpearmanrResult(correlation=0.2894343588745883, pvalue=3.3546694441812714e-08), 0.56657223796034)


02 - simlex999
2020-09-09 21:58:37,448 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2269
2020-09-09 21:58:37,448 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2203
2020-09-09 21:58:37,448 : INFO : Pairs with unknown words ratio: 0.2%
((0.22688802172575465, 4.1731851896277867e-13), SpearmanrResult(correlation=0.2203181151895642, pvalue=1.999809476875055e-12), 0.20020020020020018)


03 - simverb3500
2020-09-09 21:58:37,747 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1162
2020-09-09 21:58:37,747 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1179
2020-09-09 21:58:37,747 : INFO : Pairs with unknown words ratio: 0.1%
((0.11617582076258383, 5.502026009556657e-12), SpearmanrResult(correlation=0.11792679121092214, pvalue=2.622831544306418e-12), 0.05714285714285715)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
