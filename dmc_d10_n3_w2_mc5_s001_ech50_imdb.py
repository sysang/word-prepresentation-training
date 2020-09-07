# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=10, negative=3, window=2, min_count=5, sample=0.001,
    dm=1, dm_concat=1, hs=0, epochs=50
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'imdb'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d10,n3,w2,mc5,s0.001,t12)
Save model to: models/dmc_d10_n3_w2_mc5_s001_ech50_imdb.bin
2020-09-06 10:21:17,721 : INFO : saving Doc2Vec object under models/dmc_d10_n3_w2_mc5_s001_ech50_imdb.bin, separately None
2020-09-06 10:21:17,721 : INFO : storing np array 'vectors_docs' to models/dmc_d10_n3_w2_mc5_s001_ech50_imdb.bin.docvecs.vectors_docs.npy
2020-09-06 10:21:17,908 : INFO : saved models/dmc_d10_n3_w2_mc5_s001_ech50_imdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
++ For document 663777..."it is a mistake to make us side and sympathise with them if ultimately they are not important or developed"
2020-09-06 10:21:17,918 : INFO : precomputing L2-norms of doc weight vectors
[(663777, 0.9853774905204773), (208836, 0.965277373790741), (414210, 0.9603495597839355), (915006, 0.9510324001312256)]


++ For document 1057951..."this film heaps annoying precocious display upon annoying precocious display culminating in the stereotypical homosexual fantasy everyone desirable is gay or suppressing their gay tendencies"
[(1057951, 0.9956645965576172), (281373, 0.9650563597679138), (800150, 0.9510282278060913), (114673, 0.9450544714927673)]


++ For document 541528..."and lets just say the end shooting scene is messed up"
[(481724, 0.9633686542510986), (618656, 0.9566845893859863), (295606, 0.9558315873146057), (550912, 0.9523283839225769)]


++ For document 702978..."there 's also a magnificent score by bruce smeaton that deftly blends the romanticism of nino rota with the majestic sweep of morricone 's best work and adds a dash of electronic dissonance for good measure"
[(683059, 0.9734058380126953), (702978, 0.9725067019462585), (395190, 0.9606512784957886), (568918, 0.9568352699279785)]


++ For document 584771..."this is especially important for reviews that will be published on the internet as search engines are always looking for the correct spellings of key words"
[(584771, 0.9864466190338135), (200531, 0.9636088013648987), (753949, 0.9616748094558716), (499131, 0.9604594707489014)]


++ For document 652910..."they are right in tune with the director 's amoral consciousness and act the heck out of their roles"
[(652910, 0.9645562767982483), (705195, 0.9601619243621826), (561753, 0.9573649168014526), (1097848, 0.9523898959159851)]


++ For document 634861..."however it s refreshing to see such commitment to adventure in a kids film and paired with a uniquely winding story of friendship and courage devillier 's rousting thrill ride never falters"
[(634861, 0.9824996590614319), (858250, 0.972762942314148), (825527, 0.9605064988136292), (68355, 0.959394097328186)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (271250): but when i saw this movie i was very happy that there is a cool story and the main characters really fit in it

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d10,n3,w2,mc5,s0.001,t12):

MOST (1093849, 0.975295901298523): «there were just so many things wrong with this movie»

MEDIAN (70465, 0.0021980255842208862): «so a few weeks later i enter my video store and i see david michael latt 's version of war of the worlds on the shelf»

LEAST (672278, -0.9729342460632324): «this is an often overlooked gem in coppola 's filmography»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'waltz' model: Doc2Vec(dm/c,d10,n3,w2,mc5,s0.001,t12) similar words:
2020-09-06 10:21:20,202 : INFO : precomputing L2-norms of word weight vectors
     1. 0.96 'rampages'
     2. 0.95 'duet'
     3. 0.95 'threesomes'
     4. 0.94 'tryst'
     5. 0.94 'crime-solving'
     6. 0.94 'bombardment'
     7. 0.93 'brawl'
     8. 0.92 'canister'
     9. 0.92 'positioning'
     10. 0.92 'subdivision'
     11. 0.92 'dogfights'
     12. 0.92 'face-off'
     13. 0.92 'removals'
     14. 0.92 'nest'
     15. 0.92 'duel'
     16. 0.92 'jaunt'
     17. 0.92 'synthesis'
     18. 0.92 'pile-up'
     19. 0.92 'exposures'
     20. 0.92 'blares'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-06 10:21:20,324 : INFO : Evaluating word analogies for top 300000 words in the model on questions-
words.txt
2020-09-06 10:21:20,628 : INFO : capital-common-countries: 0.0% (0/420)
2020-09-06 10:21:21,219 : INFO : capital-world: 0.4% (3/780)
2020-09-06 10:21:21,252 : INFO : currency: 0.0% (0/40)
2020-09-06 10:21:22,347 : INFO : city-in-state: 0.1% (1/1445)
2020-09-06 10:21:22,691 : INFO : family: 9.5% (44/462)
2020-09-06 10:21:23,276 : INFO : gram1-adjective-to-adverb: 0.3% (3/992)
2020-09-06 10:21:23,810 : INFO : gram2-opposite: 0.3% (2/756)
2020-09-06 10:21:24,770 : INFO : gram3-comparative: 3.2% (43/1332)
2020-09-06 10:21:25,507 : INFO : gram4-superlative: 2.0% (21/1056)
2020-09-06 10:21:26,191 : INFO : gram5-present-participle: 0.8% (7/930)
2020-09-06 10:21:27,229 : INFO : gram6-nationality-adjective: 0.6% (8/1371)
2020-09-06 10:21:28,281 : INFO : gram7-past-tense: 0.7% (11/1482)
2020-09-06 10:21:29,184 : INFO : gram8-plural: 0.3% (3/1190)
2020-09-06 10:21:29,749 : INFO : gram9-plural-verbs: 2.0% (16/812)
2020-09-06 10:21:29,749 : INFO : Quadruplets with out-of-vocabulary words: 33.1%
2020-09-06 10:21:29,750 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-06 10:21:29,750 : INFO : Total accuracy: 1.2% (162/13068)
Doc2Vec(dm/c,d10,n3,w2,mc5,s0.001,t12): 1.24% correct (162 of 13068)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-06 10:21:29,801 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3093
2020-09-06 10:21:29,802 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.2887
2020-09-06 10:21:29,802 : INFO : Pairs with unknown words ratio: 4.2%
((0.3092860455698174, 6.318174254000289e-09), SpearmanrResult(correlation=0.2887418226450865, pvalue=6.505188490699478e-08), 4.2492917847025495)


02 - simlex999
2020-09-06 10:21:29,896 : INFO : Pearson correlation coefficient against simlex999.txt: 0.1324
2020-09-06 10:21:29,896 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1095
2020-09-06 10:21:29,896 : INFO : Pairs with unknown words ratio: 0.8%
((0.13240491623190595, 2.8986221651513895e-05), SpearmanrResult(correlation=0.10945619345328339, pvalue=0.0005570159186683874), 0.8008008008008007)


"""

