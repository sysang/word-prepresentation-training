# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=10, negative=2, window=2, min_count=7, sample=0.0005,
    dm=1, dm_concat=1, hs=0, epochs=20
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'mycorus'

base.train(corpus, common_kwargs, saved_fname)


"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d10,n2,w2,mc7,s0.0005,t12)
Save model to: models/dmc_d10_n2_w2_mc7_s0005_ech20_mycorus.bin
2020-09-07 20:56:55,648 : INFO : saving Doc2Vec object under models/dmc_d10_n2_w2_mc7_s0005_ech20_mycorus.bin, separately None
2020-09-07 20:56:55,648 : INFO : storing np array 'vectors_docs' to models/dmc_d10_n2_w2_mc7_s0005_ech20_mycorus.bin.docvecs.vectors_docs.npy
2020-09-07 20:56:56,121 : INFO : saved models/dmc_d10_n2_w2_mc7_s0005_ech20_mycorus.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 422
[+] ... "i realized one of the reasons i was turned off by the show was that they were yanking the lex character around way too much his character was developing into something interesting and they just pulled the rug out from under it so they could do it all over again"
2020-09-07 20:56:56,133 : INFO : precomputing L2-norms of doc weight vectors
[(812586, 0.9737851023674011), (4809022, 0.9700140953063965), (422, 0.9692872166633606), (3246820, 0.9687961339950562), (667497, 0.9680203795433044)]


.....get random document, tag: 243
[+] ... "for anyone who likes guy ritchie movies pre-madonna this is must see tv"
[(3554918, 0.9829355478286743), (2589341, 0.9822196364402771), (3099758, 0.9708715677261353), (1655914, 0.9693818092346191), (4001044, 0.9677633047103882)]


.....get random document, tag: 482
[+] ... "oh and a tv commercial or two would not hurt"
[(3093816, 0.98447585105896), (3550566, 0.9736030697822571), (2962793, 0.9695307016372681), (3451419, 0.9647768139839172), (3007027, 0.9637734293937683)]


.....get random document, tag: 962
[+] ... "feeling unloved by women can make a man feel lonely but i never felt suicidal"
[(28478, 0.9682218432426453), (2683884, 0.9644283056259155), (4671603, 0.9619622230529785), (1700091, 0.9617437124252319), (2912413, 0.9600697755813599)]


.....get random document, tag: 820
[+] ... "a really cool little restaurant in a small private airport with a few ww2 planes on display"
[(3390134, 0.978692352771759), (934457, 0.976942241191864), (2366005, 0.9740731120109558), (561610, 0.9737493991851807), (3087783, 0.9727934002876282)]


.....get random document, tag: 423
[+] ... "i wasnt having any of that so i walked"
[(2955929, 0.9794430732727051), (1723694, 0.9722702503204346), (4165014, 0.9655169248580933), (1853683, 0.9650392532348633), (1043099, 0.9641451239585876)]


.....get random document, tag: 517
[+] ... "what video game character are you eat that bitches"
[(980895, 0.9811477661132812), (2174536, 0.9686651825904846), (511834, 0.9632622003555298), (1856848, 0.962371289730072), (4258664, 0.9614197611808777)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (2580152): to minimalize it to even in some extremes to mock it is to trivialize a great accomplishment and to show a certain flair for the assinine

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d10,n2,w2,mc7,s0.0005,t12):

MOST (3336097, 0.9762976169586182): «there 's a few classic david bowie cuts interpol 's obstacle and loads of other good tunes»

MEDIAN (2192431, 0.008000649511814117): «the train started and we setteled once again»

LEAST (4457757, -0.9823033809661865): «he father says no and that he should not be so interested in science at his young age and adds you will see me in my grave before i let you go gallivanting off to vienna for a couple of years»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'tangled' model: Doc2Vec(dm/c,d10,n2,w2,mc7,s0.0005,t12) similar words:
2020-09-07 20:57:05,910 : INFO : precomputing L2-norms of word weight vectors
     1. 0.98 'deadened'
     2. 0.97 'perforated'
     3. 0.97 'rattling'
     4. 0.96 'broken'
     5. 0.96 'bubbling'
     6. 0.96 'padded'
     7. 0.96 'reeking'
     8. 0.96 'clogged'
     9. 0.96 'shuffling'
     10. 0.96 'chattering'
     11. 0.96 'flaking'
     12. 0.96 'wilting'
     13. 0.96 'melting'
     14. 0.96 'spatter'
     15. 0.96 'rippling'
     16. 0.96 'churning'
     17. 0.96 'trodden'
     18. 0.96 'rotted'
     19. 0.96 'oozing'
     20. 0.96 'fumbling'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-07 20:57:06,221 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-07 20:57:06,898 : INFO : capital-common-countries: 1.6% (8/506)
2020-09-07 20:57:10,686 : INFO : capital-world: 0.3% (8/2970)
2020-09-07 20:57:11,237 : INFO : currency: 0.3% (1/376)
2020-09-07 20:57:14,758 : INFO : city-in-state: 0.3% (6/2394)
2020-09-07 20:57:15,522 : INFO : family: 20.4% (103/506)
2020-09-07 20:57:16,976 : INFO : gram1-adjective-to-adverb: 0.5% (5/992)
2020-09-07 20:57:18,122 : INFO : gram2-opposite: 0.7% (6/812)
2020-09-07 20:57:20,004 : INFO : gram3-comparative: 5.2% (69/1332)
2020-09-07 20:57:21,646 : INFO : gram4-superlative: 0.3% (3/1122)
2020-09-07 20:57:23,102 : INFO : gram5-present-participle: 1.8% (19/1056)
2020-09-07 20:57:25,218 : INFO : gram6-nationality-adjective: 1.2% (17/1445)
2020-09-07 20:57:27,380 : INFO : gram7-past-tense: 1.7% (27/1560)
2020-09-07 20:57:29,396 : INFO : gram8-plural: 2.0% (27/1332)
2020-09-07 20:57:30,476 : INFO : gram9-plural-verbs: 2.5% (22/870)
2020-09-07 20:57:30,478 : INFO : Quadruplets with out-of-vocabulary words: 11.6%
2020-09-07 20:57:30,479 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-07 20:57:30,480 : INFO : Total accuracy: 1.9% (321/17273)
Doc2Vec(dm/c,d10,n2,w2,mc7,s0.0005,t12): 1.86% correct (321 of 17273)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-07 20:57:30,723 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3684
2020-09-07 20:57:30,723 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.3306
2020-09-07 20:57:30,723 : INFO : Pairs with unknown words ratio: 0.3%
((0.36837821905355805, 9.37212336207384e-13), SpearmanrResult(correlation=0.3305788182868429, pvalue=2.0197433495937067e-10), 0.28328611898017)


02 - simlex999
2020-09-07 20:57:30,947 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2279
2020-09-07 20:57:30,947 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1791
2020-09-07 20:57:30,948 : INFO : Pairs with unknown words ratio: 0.3%
((0.22793658690823282, 3.3240746168650093e-13), SpearmanrResult(correlation=0.1791284337202064, pvalue=1.2541346884656244e-08), 0.3003003003003003)


03 - simverb3500
2020-09-07 20:57:31,321 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1206
2020-09-07 20:57:31,321 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1099
2020-09-07 20:57:31,321 : INFO : Pairs with unknown words ratio: 0.1%
((0.1205806511511637, 8.356290342969871e-13), SpearmanrResult(correlation=0.10994344278035127, pvalue=7.03392620239998e-11), 0.05714285714285715)


----------------------- COMPLETED -----------------------
#_________#_______#_______#_______#_______#______#______#

"""
