import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=15, negative=5, window=5, min_count=5, sample=0.0008,
    dm=1, dm_concat=1, hs=0, epochs=20
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'blog'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n5,w5,mc5,s0.0008,t12)
Save model to: models/dmc_d15_n5_w5_mc5_s0008_ech20_blog.bin
2020-09-06 21:50:42,698 : INFO : saving Doc2Vec object under models/dmc_d15_n5_w5_mc5_s0008_ech20_blog.bin, separately None
2020-09-06 21:50:42,698 : INFO : storing np array 'syn1neg' to models/dmc_d15_n5_w5_mc5_s0008_ech20_blog.bin.trainables.syn1neg.npy
2020-09-06 21:50:42,736 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n5_w5_mc5_s0008_ech20_blog.bin.docvecs.vectors_docs.npy
2020-09-06 21:50:43,034 : INFO : saved models/dmc_d15_n5_w5_mc5_s0008_ech20_blog.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
++ For document 608802..."he placed a rainbow in the sky as a visible sign of this promise he made"
2020-09-06 21:50:43,244 : INFO : precomputing L2-norms of doc weight vectors
[(608802, 0.9469003081321716), (3180328, 0.9358028173446655), (2392209, 0.9242509007453918), (564704, 0.9201347231864929)]


++ For document 999288..."we have had some really great times"
[(41142, 0.944887101650238), (999288, 0.9275373816490173), (667187, 0.9130600690841675), (1620125, 0.9126618504524231)]


++ For document 3120299..."good on the door staff for keeping the line moving"
[(3120299, 0.9619579315185547), (235233, 0.9090828895568848), (584023, 0.9075973033905029), (1055362, 0.9043583869934082)]


++ For document 1643996..."the difference between margarine and butter"
[(2356950, 0.9101229906082153), (1941912, 0.9077026844024658), (2742777, 0.9046909809112549), (1412694, 0.903786838054657)]


++ For document 3438280..."as tired as i was it was so refreshing to be in contact with all those enthusiastic people the hall is much larger than the milwaukee venue and well laid out"
[(3438280, 0.952491283416748), (2747172, 0.9222274422645569), (1698231, 0.9161701798439026), (3417393, 0.9040316343307495)]


++ For document 2239190..."silence jef well t i think so"
[(1689480, 0.9451541304588318), (2239190, 0.916193962097168), (945897, 0.907479465007782), (1051596, 0.9029110670089722)]


++ For document 291303..."mind your p 's and q 's from the learn something new every day department to mind your p 's and q 's refers to english drinks being served in pints and quarts"
[(2211495, 0.9197996854782104), (3242661, 0.9184167981147766), (2787299, 0.9030596017837524), (768936, 0.9022441506385803)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (2053813): i only hope that i maintain the strength that i have found

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n5,w5,mc5,s0.0008,t12):

MOST (3196330, 0.9451351165771484): «i love my families dearly the biological one and the one that i made for myself»

MEDIAN (958508, 0.001818416640162468): «i would like to think that i would have given young meursault the benefit of the doubt if i had known him in real life»

LEAST (148434, -0.9443349838256836): «maybe retarded people have a hierarchy i mean when a retard calls you a retard then you know you are retarded»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'searching' model: Doc2Vec(dm/c,d15,n5,w5,mc5,s0.0008,t12) similar words:
2020-09-06 21:50:56,187 : INFO : precomputing L2-norms of word weight vectors
     1. 0.93 'applying'
     2. 0.93 'trashes'
     3. 0.92 'bombarding'
     4. 0.91 'steeling'
     5. 0.91 'crucifying'
     6. 0.89 'overstepping'
     7. 0.89 'pushing'
     8. 0.89 'eyeballing'
     9. 0.89 'goading'
     10. 0.88 'shunning'
     11. 0.88 'readying'
     12. 0.88 'nuking'
     13. 0.88 'foisted'
     14. 0.88 'spying'
     15. 0.88 'waitingandnbsp'
     16. 0.88 'trumped'
     17. 0.88 'conning'
     18. 0.87 'borrowing'
     19. 0.87 'tweeking'
     20. 0.87 'suing'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-06 21:50:56,443 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-06 21:50:57,195 : INFO : capital-common-countries: 1.0% (5/506)
2020-09-06 21:51:00,185 : INFO : capital-world: 0.5% (11/2048)
2020-09-06 21:51:00,749 : INFO : currency: 0.5% (2/376)
2020-09-06 21:51:04,380 : INFO : city-in-state: 0.5% (13/2394)
2020-09-06 21:51:05,148 : INFO : family: 25.9% (131/506)
2020-09-06 21:51:06,516 : INFO : gram1-adjective-to-adverb: 0.7% (7/992)
2020-09-06 21:51:07,603 : INFO : gram2-opposite: 2.3% (19/812)
2020-09-06 21:51:09,591 : INFO : gram3-comparative: 13.1% (175/1332)
2020-09-06 21:51:11,100 : INFO : gram4-superlative: 4.0% (45/1122)
2020-09-06 21:51:12,287 : INFO : gram5-present-participle: 8.3% (88/1056)
2020-09-06 21:51:14,406 : INFO : gram6-nationality-adjective: 1.8% (26/1445)
2020-09-06 21:51:16,442 : INFO : gram7-past-tense: 8.8% (138/1560)
2020-09-06 21:51:18,460 : INFO : gram8-plural: 6.2% (82/1332)
2020-09-06 21:51:19,547 : INFO : gram9-plural-verbs: 8.9% (77/870)
2020-09-06 21:51:19,548 : INFO : Quadruplets with out-of-vocabulary words: 16.3%
2020-09-06 21:51:19,549 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-06 21:51:19,549 : INFO : Total accuracy: 5.0% (819/16351)
Doc2Vec(dm/c,d15,n5,w5,mc5,s0.0008,t12): 5.01% correct (819 of 16351)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-06 21:51:19,855 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4360
2020-09-06 21:51:19,855 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4218
2020-09-06 21:51:19,855 : INFO : Pairs with unknown words ratio: 0.3%
((0.4360399094332247, 9.069174354349266e-18), SpearmanrResult(correlation=0.4218496081151371, pvalue=1.2748201819210582e-16), 0.28328611898017)


02 - simlex999
2020-09-06 21:51:20,054 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2693
2020-09-06 21:51:20,054 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2340
2020-09-06 21:51:20,054 : INFO : Pairs with unknown words ratio: 0.3%
((0.2692856107377301, 5.23724377551569e-18), SpearmanrResult(correlation=0.2339752628467686, pvalue=7.494036621391967e-14), 0.3003003003003003)


03 - simverb3500
2020-09-06 21:51:20,279 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1674
2020-09-06 21:51:20,279 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1558
2020-09-06 21:51:20,279 : INFO : Pairs with unknown words ratio: 0.1%
((0.16740391435033827, 2.1085540347596325e-23), SpearmanrResult(correlation=0.15578441930745981, pvalue=1.913951176151988e-20), 0.05714285714285715)

"""

