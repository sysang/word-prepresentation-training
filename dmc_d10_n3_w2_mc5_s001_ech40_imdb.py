import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=10, negative=3, window=2, min_count=5, sample=0.001,
    dm=1, dm_concat=1, hs=0, epochs=40
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'imdb'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d10,n3,w2,mc5,s0.001,t12)
Save model to: models/dmc_d10_n3_w2_mc5_s001_ech40_imdb.bin
2020-09-06 12:47:09,425 : INFO : saving Doc2Vec object under models/dmc_d10_n3_w2_mc5_s001_ech40_imdb.bin, separately None
2020-09-06 12:47:09,426 : INFO : storing np array 'vectors_docs' to models/dmc_d10_n3_w2_mc5_s001_ech40_imdb.bin.docvecs.vectors_docs.npy
2020-09-06 12:47:09,617 : INFO : saved models/dmc_d10_n3_w2_mc5_s001_ech40_imdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
++ For document 364060..."then it just abruptly ends"
2020-09-06 12:47:09,626 : INFO : precomputing L2-norms of doc weight vectors
[(489766, 0.9573098421096802), (480419, 0.9491420388221741), (1037240, 0.945884644985199), (95180, 0.9440039396286011)]


++ For document 959079..."three after all the trouble poor aladdin goes through to get his dad the hand his father hurls it out to the sea"
[(959079, 0.9727059006690979), (1010713, 0.9673176407814026), (322746, 0.9629042148590088), (900666, 0.9618858695030212)]


++ For document 51129..."we have over 100 million budget we have a romance between hollywood stars ben affleck and liv tyler and many other famous actors who are popular with the fact that they rarely agree on becoming a part of the cast of a commercial movie if their names are not written with big letters on the screen"
[(851810, 0.9796070456504822), (645252, 0.9564140439033508), (51129, 0.955711841583252), (1001696, 0.9543179273605347)]


++ For document 990362..."interminably slow pretentious and ultimately not really about anything"
[(345626, 0.9836153984069824), (777689, 0.9779617786407471), (653216, 0.9663646817207336), (6817, 0.9652338027954102)]


++ For document 138421..."it 's beautifully shot has wonderful costumes and interiors and exciting aerial dogfights"
[(195170, 0.9466251730918884), (77567, 0.9455799460411072), (101217, 0.9424891471862793), (552179, 0.9413305521011353)]


++ For document 762505..."it never siezes to amaze me how horrible some people are at making movies"
[(762505, 0.9790705442428589), (14336, 0.9592694044113159), (774821, 0.9540879130363464), (364058, 0.9487994909286499)]


++ For document 206374..."a real sudsy soap opera here as spencer tracy tackles the role of an illiterate until the age of 20"
[(344158, 0.9753437042236328), (222279, 0.9749140739440918), (741712, 0.9687502384185791), (206374, 0.9687367081642151)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (741021): imagine that this is a very revealing portrait that shows just how screwed up the military can be in times of war and in general

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d10,n3,w2,mc5,s0.001,t12):

MOST (960899, 0.9626805186271667): «leila is set in conservative iran»

MEDIAN (206072, -0.0014986582100391388): «many people have called this the killer mannequin movie»

LEAST (1030870, -0.9710886478424072): «this earthquake flick is really no great shakes»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'smash' model: Doc2Vec(dm/c,d10,n3,w2,mc5,s0.001,t12) similar words:
2020-09-06 12:47:11,962 : INFO : precomputing L2-norms of word weight vectors
     1. 0.99 'rush'
     2. 0.98 'eke'
     3. 0.97 'sneak'
     4. 0.97 'graverobbers'
     5. 0.96 'rip'
     6. 0.96 'checking'
     7. 0.96 'hook'
     8. 0.96 'live'
     9. 0.96 'play'
     10. 0.95 'knock'
     11. 0.95 'meeting'
     12. 0.95 'drive'
     13. 0.95 'mow'
     14. 0.95 'hunting'
     15. 0.95 'cashing'
     16. 0.95 'snatch'
     17. 0.95 'curl'
     18. 0.94 'blow'
     19. 0.94 'retrace'
     20. 0.94 'crank'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-06 12:47:12,060 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-06 12:47:12,367 : INFO : capital-common-countries: 0.0% (0/420)
2020-09-06 12:47:12,946 : INFO : capital-world: 0.3% (2/780)
2020-09-06 12:47:12,980 : INFO : currency: 0.0% (0/40)
2020-09-06 12:47:14,077 : INFO : city-in-state: 0.1% (1/1445)
2020-09-06 12:47:14,416 : INFO : family: 9.1% (42/462)
2020-09-06 12:47:14,977 : INFO : gram1-adjective-to-adverb: 0.5% (5/992)
2020-09-06 12:47:15,516 : INFO : gram2-opposite: 0.5% (4/756)
2020-09-06 12:47:16,492 : INFO : gram3-comparative: 2.6% (35/1332)
2020-09-06 12:47:17,200 : INFO : gram4-superlative: 2.2% (23/1056)
2020-09-06 12:47:17,885 : INFO : gram5-present-participle: 0.5% (5/930)
2020-09-06 12:47:18,921 : INFO : gram6-nationality-adjective: 0.6% (8/1371)
2020-09-06 12:47:19,966 : INFO : gram7-past-tense: 0.3% (5/1482)
2020-09-06 12:47:20,871 : INFO : gram8-plural: 0.7% (8/1190)
2020-09-06 12:47:21,442 : INFO : gram9-plural-verbs: 3.1% (25/812)
2020-09-06 12:47:21,443 : INFO : Quadruplets with out-of-vocabulary words: 33.1%
2020-09-06 12:47:21,443 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-06 12:47:21,444 : INFO : Total accuracy: 1.2% (163/13068)
Doc2Vec(dm/c,d10,n3,w2,mc5,s0.001,t12): 1.25% correct (163 of 13068)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------
01 - wordsim353
2020-09-06 12:47:21,550 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.2634
2020-09-06 12:47:21,550 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.2408
2020-09-06 12:47:21,551 : INFO : Pairs with unknown words ratio: 4.2%
((0.2633753711971416, 9.054908905389793e-07), SpearmanrResult(correlation=0.24079487278622774, pvalue=7.584115764907313e-06), 4.2492917847025495)
02 - simlex999
2020-09-06 12:47:21,595 : INFO : Pearson correlation coefficient against simlex999.txt: 0.1538
2020-09-06 12:47:21,595 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1278
2020-09-06 12:47:21,595 : INFO : Pairs with unknown words ratio: 0.8%
((0.15379231215570444, 1.1488520350100794e-06), SpearmanrResult(correlation=0.12777653478111176, pvalue=5.486011066261312e-05), 0.8008008008008007)

"""
