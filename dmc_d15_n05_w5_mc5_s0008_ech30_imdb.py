import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=15, negative=5, window=5, min_count=5, sample=0.0008,
    dm=1, dm_concat=1, hs=0, epochs=30
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'imdb'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n5,w5,mc5,s0.0008,t12)
Save model to: models/dmc_d15_n5_w5_mc5_s0008_ech30_imdb.bin
2020-09-06 20:06:15,379 : INFO : saving Doc2Vec object under models/dmc_d15_n5_w5_mc5_s0008_ech30_imdb.bin, separately None
2020-09-06 20:06:15,379 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n5_w5_mc5_s0008_ech30_imdb.bin.docvecs.vectors_docs.npy
2020-09-06 20:06:15,747 : INFO : saved models/dmc_d15_n5_w5_mc5_s0008_ech30_imdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
++ For document 445726..."brady tries to convince him to forget about her brady just wants to get back to lola"
2020-09-06 20:06:15,758 : INFO : precomputing L2-norms of doc weight vectors
[(985915, 0.9138498306274414), (167098, 0.907008707523346), (142087, 0.895677924156189), (896638, 0.8947263956069946)]


++ For document 559700..."evil alien conquerors and horror movies but this movie was however bad in a really bad way"
[(559700, 0.9722360372543335), (609236, 0.9260333180427551), (541113, 0.8942325115203857), (620550, 0.8906360268592834)]


++ For document 477493..."whoopi was the only reason i watched the oscars that year"
[(764401, 0.8931542038917542), (867078, 0.886838972568512), (42081, 0.8719451427459717), (471939, 0.8652311563491821)]


++ For document 614050..."watch out for a cameo by gary oldman as pop he was married to uma thurman at the time"
[(287341, 0.8964206576347351), (374769, 0.8768472075462341), (568994, 0.8715987205505371), (1016750, 0.8709814548492432)]


++ For document 11566..."this is blunt and highly sloppy storytelling"
[(11566, 0.9457056522369385), (984463, 0.9182924032211304), (770442, 0.9056599140167236), (159461, 0.9050650000572205)]


++ For document 397028..."to make matters worse the movie is either silly or stupid when it tries to be funny sexy or dramatic"
[(397028, 0.934363603591919), (542452, 0.9057600498199463), (443535, 0.8949261903762817), (881532, 0.8773809671401978)]


++ For document 894090..."the jokes are painful almost all of them involve farting which usually stops being funny after 6 years old"
[(894090, 0.9344448447227478), (223206, 0.8908135294914246), (629815, 0.8746007680892944), (263976, 0.8687188029289246)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (921492): the story centres around rachael newman who would have been about four years old during the events of the first film

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n5,w5,mc5,s0.0008,t12):

MOST (314759, 0.9226275682449341): «i was first exposed to madtv about a year and a half ago and i think i must have passed out from shock»

MEDIAN (850290, -0.0007936432957649231): «the plot is genuinely intriguing and lieberman plays with the conventions of this type of film by having his protagonist not be terribly likable and by having the supposed villain a politician running for congress 'lost in space 's' mark goddard not being really evil at all but just a guy whose bad decisions in the past are now coming back to haunt him»

LEAST (767081, -0.9067229628562927): «the humor is of course quite dry and draws the occasional laugh»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'brooklyn' model: Doc2Vec(dm/c,d15,n5,w5,mc5,s0.0008,t12) similar words:
2020-09-06 20:06:17,955 : INFO : precomputing L2-norms of word weight vectors
     1. 0.95 'sea-side'
     2. 0.94 'nyc'
     3. 0.93 'coastal'
     4. 0.93 'cayman'
     5. 0.93 'street'
     6. 0.92 'manhattan'
     7. 0.92 'chicago'
     8. 0.92 'parisian'
     9. 0.92 'seaside'
     10. 0.92 'plantation'
     11. 0.92 'saloon'
     12. 0.92 "ants'"
     13. 0.92 'jalopy'
     14. 0.91 'dublin'
     15. 0.91 'winter'
     16. 0.91 'vermont'
     17. 0.91 'arizona'
     18. 0.91 'louisiana'
     19. 0.91 'westchester'
     20. 0.91 'mediterranean'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-06 20:06:18,078 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-06 20:06:18,382 : INFO : capital-common-countries: 1.0% (4/420)
2020-09-06 20:06:18,977 : INFO : capital-world: 0.7% (6/815)
2020-09-06 20:06:19,010 : INFO : currency: 0.0% (0/40)
2020-09-06 20:06:20,117 : INFO : city-in-state: 0.1% (1/1500)
2020-09-06 20:06:20,468 : INFO : family: 19.5% (90/462)
2020-09-06 20:06:21,042 : INFO : gram1-adjective-to-adverb: 0.5% (5/992)
2020-09-06 20:06:21,538 : INFO : gram2-opposite: 1.2% (9/756)
2020-09-06 20:06:22,417 : INFO : gram3-comparative: 7.8% (104/1332)
2020-09-06 20:06:23,191 : INFO : gram4-superlative: 5.0% (53/1056)
2020-09-06 20:06:23,841 : INFO : gram5-present-participle: 0.8% (7/930)
2020-09-06 20:06:24,881 : INFO : gram6-nationality-adjective: 2.2% (30/1371)
2020-09-06 20:06:25,960 : INFO : gram7-past-tense: 4.0% (59/1482)
2020-09-06 20:06:26,807 : INFO : gram8-plural: 2.3% (27/1190)
2020-09-06 20:06:27,392 : INFO : gram9-plural-verbs: 8.6% (70/812)
2020-09-06 20:06:27,393 : INFO : Quadruplets with out-of-vocabulary words: 32.7%
2020-09-06 20:06:27,393 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-06 20:06:27,394 : INFO : Total accuracy: 3.5% (465/13158)
Doc2Vec(dm/c,d15,n5,w5,mc5,s0.0008,t12): 3.53% correct (465 of 13158)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-06 20:06:27,498 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3862
2020-09-06 20:06:27,499 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.3648
2020-09-06 20:06:27,499 : INFO : Pairs with unknown words ratio: 4.2%
((0.38624925121586584, 1.8052637870875868e-13), SpearmanrResult(correlation=0.36478884319376864, pvalue=4.463173802810152e-12), 4.2492917847025495)


02 - simlex999
2020-09-06 20:06:27,542 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2154
2020-09-06 20:06:27,542 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1825
2020-09-06 20:06:27,542 : INFO : Pairs with unknown words ratio: 0.8%
((0.21540141630720483, 7.236189641794486e-12), SpearmanrResult(correlation=0.18253127541313802, pvalue=7.142115190084131e-09), 0.8008008008008007)


03 - simverb3500
2020-09-06 20:06:27,660 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1280
2020-09-06 20:06:27,661 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1313
2020-09-06 20:06:27,661 : INFO : Pairs with unknown words ratio: 2.6%
((0.12804230206219777, 6.236251018492013e-14), SpearmanrResult(correlation=0.1312545383387907, pvalue=1.4386125327512568e-14), 2.6285714285714286)

"""
