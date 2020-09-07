# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=10, negative=5, window=5, min_count=5, sample=0.001,
    dm=1, dm_concat=1, hs=0, epochs=20
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'imdb'

base.train(corpus, common_kwargs, saved_fname)

"""

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS - N.01


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
++ For document 504802..."for the imaginative the third act is a treat a world with underground cities massive deco bombers space cannons gyro copters and secret organizations of scientist saviors"
2020-09-05 23:16:12,544 : INFO : precomputing L2-norms of doc weight vectors
[(334763, 0.9569252133369446), (552527, 0.9560791254043579), (35986, 0.9524310231208801), (824323, 0.9523998498916626)]


++ For document 938581..."god help me  definately one of the most annoying characters i have seen in a long time   i thought this movie was almost a waste of my time and give it a 15/5 mainly because i am usually a fan of susan sarandon she was the only reason i was interested in seeing this movie in the first place  but in this one she is really wasted"
[(938581, 0.9733458757400513), (561351, 0.9654052257537842), (877648, 0.9566806554794312), (75860, 0.9541237950325012)]


++ For document 200664..."but kudos too for the inclusion of lesser-sung but equally relevant films like panic in needle park and joe"
[(1035908, 0.9582715034484863), (246266, 0.9574276208877563), (329752, 0.9570436477661133), (881797, 0.9554643034934998)]


++ For document 981326..."so i am left wondering why this movie was made"
[(430994, 0.9571561217308044), (377933, 0.9523026943206787), (544604, 0.9517704248428345), (445115, 0.9499716758728027)]


++ For document 142004..."my initial feelings towards the film is that it 's not particularly gripping at times especially early on but at least a good dose of comedy is put in in the form of surfing fanatic col"
[(1047047, 0.9690576195716858), (338587, 0.9679978489875793), (286475, 0.9618028402328491), (898303, 0.9495406746864319)]


++ For document 827036..."the journey begins and the copy of immw begins"
[(422308, 0.9791416525840759), (768619, 0.9702602028846741), (362346, 0.9690055847167969), (827036, 0.9688000679016113)]


++ For document 523454..."the third story also has a fine turn from veteran mathieu carrière as a faith healer"
[(881076, 0.9571200609207153), (74518, 0.9521522521972656), (319210, 0.9519453644752502), (1077518, 0.9460244178771973)]




Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (572437): stephanie tries to dissuade her from buying it but sophie is adamant

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d10,n5,w5,mc5,s0.001,t12):

MOST (419802, 0.9601123332977295): «what makes these relationships special however is the attention redford gives to the language as spoken in dialogue»

MEDIAN (701297, 0.002410944551229477): «it 's funny sharp very interesting and easy to watch»

LEAST (376315, -0.9807989597320557): «pirates of the caribbean is more scary than the skeletal bad guys in this film»



Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'ritchie' model: Doc2Vec(dm/c,d10,n5,w5,mc5,s0.001,t12) similar words:
2020-09-05 23:16:14,898 : INFO : precomputing L2-norms of word weight vectors
     1. 0.99 'averill'
     2. 0.98 'rayner'
     3. 0.98 'quinlan'
     4. 0.98 'kringelein'
     5. 0.98 'schipper'
     6. 0.97 'lederer'
     7. 0.97 'stein'
     8. 0.97 'nader'
     9. 0.97 'quinlin'
     10. 0.97 'caldwell'
     11. 0.96 'negulesco'
     12. 0.96 'murphey'
     13. 0.96 'elem'
     14. 0.96 'mclish'
     15. 0.96 'kensit'
     16. 0.96 'carle'
     17. 0.96 'askin'
     18. 0.96 'evigan'
     19. 0.96 'maitland'
     20. 0.96 'warriner'


Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-05 23:16:15,017 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-05 23:16:15,327 : INFO : capital-common-countries: 0.7% (3/420)
2020-09-05 23:16:15,923 : INFO : capital-world: 0.1% (1/780)
2020-09-05 23:16:15,960 : INFO : currency: 0.0% (0/40)
2020-09-05 23:16:17,075 : INFO : city-in-state: 0.0% (0/1445)
2020-09-05 23:16:17,427 : INFO : family: 11.5% (53/462)
2020-09-05 23:16:17,979 : INFO : gram1-adjective-to-adverb: 0.2% (2/992)
2020-09-05 23:16:18,539 : INFO : gram2-opposite: 0.8% (6/756)
2020-09-05 23:16:19,526 : INFO : gram3-comparative: 2.9% (38/1332)
2020-09-05 23:16:20,267 : INFO : gram4-superlative: 1.6% (17/1056)
2020-09-05 23:16:20,928 : INFO : gram5-present-participle: 0.2% (2/930)
2020-09-05 23:16:21,949 : INFO : gram6-nationality-adjective: 0.7% (10/1371)
2020-09-05 23:16:22,977 : INFO : gram7-past-tense: 0.5% (7/1482)
2020-09-05 23:16:23,881 : INFO : gram8-plural: 0.3% (3/1190)
2020-09-05 23:16:24,436 : INFO : gram9-plural-verbs: 1.5% (12/812)
2020-09-05 23:16:24,437 : INFO : Quadruplets with out-of-vocabulary words: 33.1%
2020-09-05 23:16:24,438 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-05 23:16:24,439 : INFO : Total accuracy: 1.2% (154/13068)
Doc2Vec(dm/c,d10,n5,w5,mc5,s0.001,t12): 1.18% correct (154 of 13068)


Benchmark against analogies metric baseline - wordsim353
-----------------------------------------------------
2020-09-05 23:16:24,550 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3275
2020-09-05 23:16:24,551 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.3097
2020-09-05 23:16:24,551 : INFO : Pairs with unknown words ratio: 4.2%
((0.3275266486447517, 6.81982192989976e-10), SpearmanrResult(correlation=0.3096787371817901, pvalue=6.031953146340709e-09), 4.2492917847025495)


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS - N.02


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
++ For document 523351..."i really did enjoy this film much more than somersault and three dollars"
2020-09-06 07:08:55,222 : INFO : precomputing L2-norms of doc weight vectors
[(927021, 0.9738013744354248), (293, 0.9692506194114685), (412201, 0.9634215235710144), (1055669, 0.9606112241744995)]


++ For document 829515..."this is not to be missed by anyone who appreciates uncommonly gifted acting"
[(106095, 0.9746843576431274), (156083, 0.958402156829834), (835032, 0.9508171081542969), (416982, 0.9503941535949707)]


++ For document 362366..."gore for the sake of gore is pointless"
[(278756, 0.9674042463302612), (974055, 0.9654675126075745), (28750, 0.9565852284431458), (808741, 0.955366849899292)]


++ For document 84697..."the film consists of the audition tapes of the surrender girls and some footage from previous films"
[(397631, 0.9748255014419556), (84697, 0.9683823585510254), (807207, 0.9602625370025635), (458294, 0.9583032131195068)]


++ For document 1040237..."thinking this was a horror movie billed as such and starring guys like bela lugosi and lionel atwill i wound up disappointedeven more so because this movie started off pretty well and had promise"
[(1040237, 0.9736462831497192), (583872, 0.9680641889572144), (243593, 0.9548386335372925), (953077, 0.950523853302002)]


++ For document 314914..."well howzbout the rugs of his 33 plural wives no mention whatsoever is made of polygamy"
[(85363, 0.9736698269844055), (314914, 0.9691084623336792), (46151, 0.9651700854301453), (741675, 0.9624115824699402)]


++ For document 757081..."i can not really say what that is about"
[(525807, 0.9659580588340759), (728814, 0.9586215019226074), (380035, 0.9561416506767273), (123942, 0.9531437158584595)]




Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (1005195): king 's quest i was a revolution in adventure games for the computer

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d10,n5,w5,mc5,s0.001,t12):

MOST (967047, 0.967276930809021): «google a synopsis of the book no more bashing to find out more about anti japanese sentiments during the 80 's»

MEDIAN (200482, 0.005653515458106995): «from birth to his first big break and every life altering moment in between a viewer sees our host and other characters in their most private moments all the while experiencing the pain hope and humor that comes with»

LEAST (771251, -0.9905585050582886): «certain fury is grade-z stuff in most departments the low production values and the often very bad dialogue stand out but tatum o'neal is engagingly tough and she makes the film worth watching all by herself»



Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'defines' model: Doc2Vec(dm/c,d10,n5,w5,mc5,s0.001,t12) similar words:
2020-09-06 07:08:57,567 : INFO : precomputing L2-norms of word weight vectors
     1. 0.98 'omits'
     2. 0.97 'lends'
     3. 0.97 'earns'
     4. 0.96 'makes'
     5. 0.96 'contradicts'
     6. 0.96 'invokes'
     7. 0.95 'jettisons'
     8. 0.95 'satirizes'
     9. 0.95 'surpasses'
     10. 0.95 'diminishes'
     11. 0.95 'reinforces'
     12. 0.95 'maintains'
     13. 0.95 'provides'
     14. 0.95 'reminds'
     15. 0.95 'gives'
     16. 0.95 'deconstructs'
     17. 0.95 'squanders'
     18. 0.95 'elevates'
     19. 0.95 'resembles'
     20. 0.95 'reduces'


Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-06 07:08:57,665 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-06 07:08:57,977 : INFO : capital-common-countries: 0.2% (1/420)
2020-09-06 07:08:58,572 : INFO : capital-world: 0.1% (1/780)
2020-09-06 07:08:58,606 : INFO : currency: 0.0% (0/40)
2020-09-06 07:08:59,715 : INFO : city-in-state: 0.1% (2/1445)
2020-09-06 07:09:00,069 : INFO : family: 10.4% (48/462)
2020-09-06 07:09:00,621 : INFO : gram1-adjective-to-adverb: 0.3% (3/992)
2020-09-06 07:09:01,186 : INFO : gram2-opposite: 0.7% (5/756)
2020-09-06 07:09:02,153 : INFO : gram3-comparative: 2.6% (34/1332)
2020-09-06 07:09:02,920 : INFO : gram4-superlative: 1.8% (19/1056)
2020-09-06 07:09:03,593 : INFO : gram5-present-participle: 0.1% (1/930)
2020-09-06 07:09:04,625 : INFO : gram6-nationality-adjective: 0.4% (5/1371)
2020-09-06 07:09:05,671 : INFO : gram7-past-tense: 0.7% (10/1482)
2020-09-06 07:09:06,565 : INFO : gram8-plural: 0.9% (11/1190)
2020-09-06 07:09:07,109 : INFO : gram9-plural-verbs: 0.7% (6/812)
2020-09-06 07:09:07,109 : INFO : Quadruplets with out-of-vocabulary words: 33.1%
2020-09-06 07:09:07,109 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-06 07:09:07,110 : INFO : Total accuracy: 1.1% (146/13068)
Doc2Vec(dm/c,d10,n5,w5,mc5,s0.001,t12): 1.12% correct (146 of 13068)


Benchmark against analogies metric baseline - wordsim353
-----------------------------------------------------
2020-09-06 07:09:07,218 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3080
2020-09-06 07:09:07,218 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.2852
2020-09-06 07:09:07,218 : INFO : Pairs with unknown words ratio: 4.2%

"""
