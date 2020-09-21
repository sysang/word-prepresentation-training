# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=15, negative=3, window=3, min_count=6, sample=0.0008,
    dm=1, dm_concat=1, hs=0, epochs=12
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'imdb'

base.train(corpus, common_kwargs, saved_fname)

"""
 EXAMINING RESULTS
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
++ For document 11772..."the movie is also often way too dark no doubt as an attempt to hide its fairly low budget and it shows very little gore as well mostly due to the fact that you simply can not always see things so very well"
2020-09-05 22:36:17,430 : INFO : precomputing L2-norms of doc weight vectors
[(328364, 0.9454115629196167), (11772, 0.9111897349357605), (829245, 0.880254864692688), (755501, 0.875535786151886)]


++ For document 684643..."i also though the two less hollywood actors edgar ramirez and said taghmaoui did great job in portraying their characters and were stern on screen"
[(358269, 0.9546269178390503), (844727, 0.9359133839607239), (105289, 0.9017440676689148), (560950, 0.8943788409233093)]


++ For document 798040..."a firefighter a cop father and son a little realm of the outer edge with suspense building throughout how could it not be a hit this movie kept me on the edge of my seat and requires you to pay attention to the details so you can grasp the concept"
[(537331, 0.8781260848045349), (767225, 0.877262532711029), (362109, 0.8766690492630005), (734472, 0.8741428852081299)]


++ For document 530774..."i have given the film an 8 out of 10 instead of a 10 out of ten which is where a good portion of this film dwells because in the final 15 minutes the film falls apart in the pacing"
[(682605, 0.8864473104476929), (441931, 0.8834659457206726), (240531, 0.8711609840393066), (503460, 0.8675931692123413)]


++ For document 395995..."beaver 's incessant oh just one more thing dearies and then we will be ready to go punctuated by the children 's simultaneous cries and sighs and moans of no mrs"
[(435037, 0.9058821797370911), (598829, 0.8847544193267822), (818649, 0.8765182495117188), (16741, 0.8711417317390442)]


++ For document 541862..."and at a time when the stereotype about artists is that they are mostly bitter pretentious often mentally unstable people who live in decrepit urban settings goldsworthy seems to be the opposite a stable unpretentious family oriented person who loves nature and lives in a small village in scotland of course i am sure those are the same reasons why he 's shunned by some people on the art world who found his works fluffy or superficial"
[(547078, 0.8753129243850708), (805749, 0.8725252747535706), (583681, 0.866910994052887), (460539, 0.8629534840583801)]


++ For document 158337..."bruce gets bad things happen to him on way to see doctor"
[(1075967, 0.9181204438209534), (1020744, 0.8740605115890503), (119479, 0.8647939562797546), (405771, 0.8624798059463501)]




Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (877296): long time dead a good british horror/thriller movie with some creepy moments in it like the flashback scenes

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n3,w3,mc6,s0.0008,t12):

MOST (164988, 0.8874272704124451): «what 's all the more harrowing is stories like this really did happen in brazil in 1981and are still happening today»

MEDIAN (727006, -0.012337944470345974): «it often offers delicate and classy humour in the juxtapositions of the seedy drafty castle life with the glossy upper-class dinners at the american brothers' estates and indeed the whole film is peppered with light-hearted comedic situations and crafted with humorous charming strokes»

LEAST (832662, -0.9226852059364319): «apart from being one of the goriest films ever to garner an r rating reazione a catena is also something of a record holder when it comes to alternate titles»



Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'half-hour' model: Doc2Vec(dm/c,d15,n3,w3,mc6,s0.0008,t12) similar words:
2020-09-05 22:36:19,693 : INFO : precomputing L2-norms of word weight vectors
     1. 0.94 'reel'
     2. 0.92 'decade'
     3. 0.92 'hour'
     4. 0.91 '2/3rds'
     5. 0.91 'minute'
     6. 0.91 'paragraph'
     7. 0.91 '1/3'
     8. 0.90 'week'
     9. 0.90 'half'
     10. 0.90 'duration'
     11. 0.90 'quarter'
     12. 0.90 'wrinkle'
     13. 0.89 'previews'
     14. 0.89 '30mins'
     15. 0.89 '90mins'
     16. 0.89 'hurrah'
     17. 0.89 'runtime'
     18. 0.88 'ppv'
     19. 0.88 '02'
     20. 0.88 'three-quarters'


Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-05 22:36:19,810 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-05 22:36:20,049 : INFO : capital-common-countries: 1.2% (5/420)
2020-09-05 22:36:20,487 : INFO : capital-world: 0.0% (0/744)
2020-09-05 22:36:20,519 : INFO : currency: 0.0% (0/40)
2020-09-05 22:36:21,416 : INFO : city-in-state: 0.1% (1/1445)
2020-09-05 22:36:21,741 : INFO : family: 23.4% (108/462)
2020-09-05 22:36:22,316 : INFO : gram1-adjective-to-adverb: 0.7% (7/992)
2020-09-05 22:36:22,818 : INFO : gram2-opposite: 1.9% (14/756)
2020-09-05 22:36:23,747 : INFO : gram3-comparative: 12.7% (169/1332)
2020-09-05 22:36:24,461 : INFO : gram4-superlative: 4.0% (42/1056)
2020-09-05 22:36:25,047 : INFO : gram5-present-participle: 1.1% (10/930)
2020-09-05 22:36:25,909 : INFO : gram6-nationality-adjective: 2.2% (29/1299)
2020-09-05 22:36:26,882 : INFO : gram7-past-tense: 3.5% (52/1482)
2020-09-05 22:36:27,635 : INFO : gram8-plural: 1.2% (14/1122)
2020-09-05 22:36:28,172 : INFO : gram9-plural-verbs: 9.0% (73/812)
2020-09-05 22:36:28,172 : INFO : Quadruplets with out-of-vocabulary words: 34.0%
2020-09-05 22:36:28,173 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-05 22:36:28,173 : INFO : Total accuracy: 4.1% (524/12892)
Doc2Vec(dm/c,d15,n3,w3,mc6,s0.0008,t12): 4.06% correct (524 of 12892)


Benchmark against analogies metric baseline - wordsim353
-----------------------------------------------------
2020-09-05 22:36:28,219 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3223
2020-09-05 22:36:28,219 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.2995
2020-09-05 22:36:28,220 : INFO : Pairs with unknown words ratio: 4.5%
((0.32230973029007315, 1.384774715314612e-09), SpearmanrResult(correlation=0.29948219196005876, pvalue=2.0641657699282496e-08), 4.53257790368272)


"""

