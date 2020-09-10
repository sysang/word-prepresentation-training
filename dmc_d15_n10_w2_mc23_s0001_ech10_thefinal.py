# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=15, negative=10, window=2, min_count=23, sample=0.0001,
    dm=1, dm_concat=1, hs=0, epochs=10
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'thefinal'

base.train(corpus, common_kwargs, saved_fname, True)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d15,n10,w2,mc23,s0.0001,t5)
Save model to: models/dmc_d15_n10_w2_mc23_s0001_ech10_thefinal.bin
2020-09-10 18:09:29,820 : INFO : saving Doc2Vec object under models/dmc_d15_n10_w2_mc23_s0001_ech10_thefinal.bin, separately None
2020-09-10 18:09:29,820 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n10_w2_mc23_s0001_ech10_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-10 18:09:29,848 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n10_w2_mc23_s0001_ech10_thefinal.bin.docvecs.vectors_docs.npy
2020-09-10 18:09:30,611 : INFO : saved models/dmc_d15_n10_w2_mc23_s0001_ech10_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 12914040
[+] ... "is nothing sacred anymore from the ap trouble in doll-ville barbie and ken split in valley of the dolls new york just like j lo and ben the romance is over for barbie and ken"
2020-09-10 18:09:30,624 : INFO : precomputing L2-norms of doc weight vectors
[(12914040, 0.9406051635742188), (5885680, 0.9267581701278687), (80853, 0.9245311617851257), (560463, 0.9159746766090393), (1285091, 0.9112211465835571), (1561323, 0.9049980044364929), (1070143, 0.9040980935096741), (11476426, 0.9024956226348877), (8939223, 0.9018628001213074), (12560265, 0.9017863869667053)]


.....get random document, tag: 6893063
[+] ... "controversy surrounded him when a contractor who remodeled his home in bethesda maryland at a reduced cost sought his help for obtaining a $5 million extra payment for building a garage adjacent to the united states capitol building"
[(1815460, 0.9472692012786865), (5118889, 0.9358959197998047), (8985080, 0.9273601770401001), (5336177, 0.921749472618103), (11625829, 0.9189000725746155), (6893063, 0.9128921627998352), (820402, 0.9122552275657654), (12124958, 0.9093188047409058), (8124610, 0.90805584192276), (4594602, 0.9077768921852112)]


.....get random document, tag: 4202534
[+] ... "he meant after he had seen adrea to consider whether it would not be best to tell his brother everything"
[(10319292, 0.9302782416343689), (12349148, 0.9271630048751831), (9457159, 0.9232257008552551), (5116832, 0.9196593761444092), (10737711, 0.912236750125885), (3528567, 0.9101275205612183), (8609065, 0.9097853899002075), (9969267, 0.907669186592102), (11829269, 0.9069642424583435), (4202534, 0.9053832292556763)]


.....get random document, tag: 11263536
[+] ... "i think i may just still be in shock"
[(9567558, 0.9337486624717712), (12696910, 0.9323983192443848), (13288804, 0.9082909822463989), (9696338, 0.906914234161377), (176692, 0.9059352874755859), (6009840, 0.9057350754737854), (2187840, 0.90207839012146), (13053532, 0.9019303321838379), (7226494, 0.9010910987854004), (2178832, 0.8985204696655273)]


.....get random document, tag: 2316888
[+] ... "some of his highest flights rise from an entirely different inspiration and deal with the public affairs of the nation"
[(9898843, 0.9311657547950745), (9940975, 0.917375922203064), (1544428, 0.9149323105812073), (10008311, 0.9112774133682251), (1657865, 0.909640371799469), (7366511, 0.90941321849823), (10276019, 0.9075901508331299), (4300235, 0.9071061015129089), (12111262, 0.9061633348464966), (12047163, 0.9055266380310059)]


.....get random document, tag: 903184
[+] ... "this notion of the destination of the study of natural laws is to our minds a complete dereliction of the essential principles which form the positive conception of science and contained the germ of the perversion of his own philosophy which marked his later years"
[(8332536, 0.9367437362670898), (5790039, 0.9220239520072937), (1239458, 0.9201388359069824), (12695944, 0.9182050228118896), (9204378, 0.9147617816925049), (7432753, 0.9146018028259277), (4300915, 0.9119065403938293), (3419977, 0.9116635322570801), (5167259, 0.9096354246139526), (7199472, 0.9093706607818604)]


.....get random document, tag: 7860585
[+] ... "as they would not yield the walls were torn down after six of the victims had died and mimi was dragged through the city and slain"
[(3716283, 0.956846296787262), (6335549, 0.9343458414077759), (13099231, 0.9318176507949829), (6405957, 0.9262264966964722), (2018697, 0.9185011386871338), (2143438, 0.9170279502868652), (4129473, 0.9133594632148743), (2930388, 0.9132987856864929), (1937367, 0.9122170209884644), (11231468, 0.9091441631317139)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (1663088): for two days after holstein 's departure daun sat still on his safe northern shore stirring nothing but his own cunctations and investigations leaving the bombardment or cannonade to take its own course

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d15,n10,w2,mc23,s0.0001,t5):

MOST (9534226, 0.9326680898666382): «it is known that further reserves of oil exist within the country in addition to the oilfields that are already being exploited»

MEDIAN (12044682, 0.0032056421041488647): «he is a good man i love him dearly and i know that he loves me»

LEAST (9892881, -0.9255713224411011): «under colorado law timnath is governed in the mayor-council form of government by a board of trustees»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'selfishness' model: Doc2Vec(dm/c,d15,n10,w2,mc23,s0.0001,t5) similar words:
2020-09-10 18:09:57,202 : INFO : precomputing L2-norms of word weight vectors
     1. 0.98 'meanness'
     2. 0.98 'wilfulness'
     3. 0.97 'frailty'
     4. 0.97 'worldliness'
     5. 0.97 'baseness'
     6. 0.96 'self-will'
     7. 0.96 'heartlessness'
     8. 0.96 'hypocrisy'
     9. 0.96 'sinfulness'
     10. 0.96 'ill-nature'
     11. 0.96 'self-love'
     12. 0.96 'self-conceit'
     13. 0.95 'callousness'
     14. 0.95 'submissiveness'
     15. 0.95 'self-hatred'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-10 18:09:57,761 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-10 18:09:58,520 : INFO : capital-common-countries: 7.1% (36/506)
2020-09-10 18:10:04,434 : INFO : capital-world: 2.1% (78/3773)
2020-09-10 18:10:05,140 : INFO : currency: 0.9% (4/458)
2020-09-10 18:10:08,614 : INFO : city-in-state: 1.3% (32/2467)
2020-09-10 18:10:09,417 : INFO : family: 26.7% (135/506)
2020-09-10 18:10:10,708 : INFO : gram1-adjective-to-adverb: 3.2% (32/992)
2020-09-10 18:10:11,811 : INFO : gram2-opposite: 4.6% (37/812)
2020-09-10 18:10:13,406 : INFO : gram3-comparative: 25.6% (341/1332)
2020-09-10 18:10:15,200 : INFO : gram4-superlative: 11.4% (128/1122)
2020-09-10 18:10:16,352 : INFO : gram5-present-participle: 14.0% (148/1056)
2020-09-10 18:10:18,799 : INFO : gram6-nationality-adjective: 9.0% (137/1521)
2020-09-10 18:10:20,916 : INFO : gram7-past-tense: 16.1% (251/1560)
2020-09-10 18:10:22,770 : INFO : gram8-plural: 11.1% (148/1332)
2020-09-10 18:10:23,949 : INFO : gram9-plural-verbs: 9.0% (78/870)
2020-09-10 18:10:23,950 : INFO : Quadruplets with out-of-vocabulary words: 6.3%
2020-09-10 18:10:23,951 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-10 18:10:23,951 : INFO : Total accuracy: 8.7% (1585/18307)
Doc2Vec(dm/c,d15,n10,w2,mc23,s0.0001,t5): 8.66% correct (1585 of 18307)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-10 18:10:24,320 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4885
2020-09-10 18:10:24,320 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4826
2020-09-10 18:10:24,320 : INFO : Pairs with unknown words ratio: 0.0%
((0.48853114937991093, 1.4224226708963302e-22), SpearmanrResult(correlation=0.4826252048757278, pvalue=5.373247746018795e-22), 0.0)


02 - simlex999
2020-09-10 18:10:24,673 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3138
2020-09-10 18:10:24,673 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2710
2020-09-10 18:10:24,673 : INFO : Pairs with unknown words ratio: 0.2%
((0.3137502197247046, 3.254287347803005e-24), SpearmanrResult(correlation=0.27100784016665386, pvalue=3.0406856262829007e-18), 0.20020020020020018)


03 - simverb3500
2020-09-10 18:10:25,293 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1795
2020-09-10 18:10:25,293 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1649
2020-09-10 18:10:25,293 : INFO : Pairs with unknown words ratio: 0.1%
((0.17952556858975496, 1.0058201586047151e-26), SpearmanrResult(correlation=0.16493178023376223, pvalue=9.369761180710706e-23), 0.05714285714285715)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
