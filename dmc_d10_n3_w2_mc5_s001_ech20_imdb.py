# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=10, negative=3, window=2, min_count=5, sample=0.001,
    dm=1, dm_concat=1, hs=0, epochs=20
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'imdb'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
++ For document 620125..."untalented american writer living the ultimate petty-bourgeois life in paris and who thinks he 's hemingway falls in love at first sight with a young french woman while riding on a bushe gives her his ticket and leaves the bus"
2020-09-06 08:37:28,177 : INFO : precomputing L2-norms of doc weight vectors
[(10744, 0.9691877961158752), (620125, 0.9683263301849365), (46128, 0.9650380611419678), (1031651, 0.9597961902618408)]


++ For document 389812..."the scientist and his wife are two of worst heroes or protagonists ever put on screen"
[(162028, 0.9509511590003967), (540450, 0.9442402720451355), (1108358, 0.9431399703025818), (777072, 0.9413890838623047)]


++ For document 442980..."so for them from one side it 's a non challenging job which is also fairly boring sometimes and from another they start to figure out people 's behavior"
[(919440, 0.9709038734436035), (265990, 0.9599562287330627), (762567, 0.9568172693252563), (434860, 0.9545714855194092)]


++ For document 845698..."the chemistry they held was almost so obscure and confusing it was realistic and some how gives the audience a feel of a real-life partnership"
[(672798, 0.9600827693939209), (982858, 0.9566782712936401), (1010207, 0.9564805030822754), (845698, 0.9560452699661255)]


++ For document 377206..."but all of this posturing is merely a lead-in for blood"
[(786002, 0.9654167294502258), (294571, 0.9592487215995789), (163097, 0.9570318460464478), (776732, 0.9558088183403015)]


++ For document 88167..."the film leaves a bad flavor in the mouths of modern movie audiences"
[(750491, 0.9712749719619751), (1022770, 0.9574966430664062), (314078, 0.9508250951766968), (1074742, 0.9497777223587036)]


++ For document 355933..."i could not stop watching"
[(327758, 0.9730660319328308), (102343, 0.9607230424880981), (532434, 0.953145444393158), (779206, 0.9515972137451172)]




Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (875792): if you think japanese animation is all giant robots and superhuman schoolgirls this could be the film which changes your mind

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d10,n3,w2,mc5,s0.001,t12):

MOST (198436, 0.9502442479133606): «celluloid heroes never feel any pain»

MEDIAN (1082155, 0.0014947522431612015): «i will not say it was a bad offering but why does not someone make a vampire film that actually is a vampire film and not another kung fu action movie where the villains just happen to drink blood what we get from dracula 's curse is once again lots of fancy gunplay swordfighting and martial arts involving hot goth chicks which seems to have become the rule for vampire films these days blade underworld van helsing etc»

LEAST (745569, -0.9591847062110901): «al pacino returns to the big screen after a four year hiatus in sea of love»



Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'cassidy' model: Doc2Vec(dm/c,d10,n3,w2,mc5,s0.001,t12) similar words:
2020-09-06 08:37:30,540 : INFO : precomputing L2-norms of word weight vectors
     1. 0.99 'morrison'
     2. 0.98 'osborne'
     3. 0.98 'hurst'
     4. 0.98 'ruiz'
     5. 0.98 'sullivan'
     6. 0.98 'agar'
     7. 0.98 'jeffries'
     8. 0.98 'kruschen'
     9. 0.98 'agee'
     10. 0.98 'cain'
     11. 0.98 'freleng'
     12. 0.98 'larson'
     13. 0.97 'klaw'
     14. 0.97 'kennedy'
     15. 0.97 'thorpe'
     16. 0.97 'jefferies'
     17. 0.97 'pare'
     18. 0.97 'potts'
     19. 0.97 'jolley'
     20. 0.97 'chamberlain'


Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-06 08:37:30,660 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-06 08:37:30,961 : INFO : capital-common-countries: 0.0% (0/420)
2020-09-06 08:37:31,545 : INFO : capital-world: 0.0% (0/780)
2020-09-06 08:37:31,581 : INFO : currency: 0.0% (0/40)
2020-09-06 08:37:32,685 : INFO : city-in-state: 0.1% (1/1445)
2020-09-06 08:37:33,027 : INFO : family: 12.3% (57/462)
2020-09-06 08:37:33,650 : INFO : gram1-adjective-to-adverb: 0.4% (4/992)
2020-09-06 08:37:34,207 : INFO : gram2-opposite: 0.7% (5/756)
2020-09-06 08:37:35,175 : INFO : gram3-comparative: 4.9% (65/1332)
2020-09-06 08:37:35,938 : INFO : gram4-superlative: 1.3% (14/1056)
2020-09-06 08:37:36,608 : INFO : gram5-present-participle: 0.4% (4/930)
2020-09-06 08:37:37,639 : INFO : gram6-nationality-adjective: 0.7% (9/1371)
2020-09-06 08:37:38,668 : INFO : gram7-past-tense: 0.9% (14/1482)
2020-09-06 08:37:39,568 : INFO : gram8-plural: 0.4% (5/1190)
2020-09-06 08:37:40,124 : INFO : gram9-plural-verbs: 1.7% (14/812)
2020-09-06 08:37:40,125 : INFO : Quadruplets with out-of-vocabulary words: 33.1%
2020-09-06 08:37:40,126 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-06 08:37:40,128 : INFO : Total accuracy: 1.5% (192/13068)
Doc2Vec(dm/c,d10,n3,w2,mc5,s0.001,t12): 1.47% correct (192 of 13068)


Benchmark against analogies metric baseline - wordsim353
-----------------------------------------------------
2020-09-06 08:37:40,183 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3003
2020-09-06 08:37:40,184 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.2865
2020-09-06 08:37:40,186 : INFO : Pairs with unknown words ratio: 4.2%
((0.3003247498141753, 1.7867360428928835e-08), SpearmanrResult(correlation=0.28652570227250157, pvalue=8.275685614201312e-08), 4.2492917847025495)

"""

