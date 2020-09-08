# coding: utf-8
import doc2vec_training_script_enhanced_preprocessing as base

common_kwargs = dict(
    vector_size=10, negative=4, window=3, min_count=10, sample=0.005,
    dm=1, dm_concat=1, hs=0, epochs=5
)

saved_fname = 'models/' + __file__.replace('.py', '.bin')
corpus = 'mycorus'

base.train(corpus, common_kwargs, saved_fname)

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS - 01


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d10,n4,w3,mc10,s0.005,t12)
Save model to: models/dmc_d10_n4_w3_mc10_s005_ech05_mycorus.bin
2020-09-07 22:56:34,195 : INFO : saving Doc2Vec object under models/dmc_d10_n4_w3_mc10_s005_ech05_mycorus.bin, separately None
2020-09-07 22:56:34,196 : INFO : storing np array 'vectors_docs' to models/dmc_d10_n4_w3_mc10_s005_ech05_mycorus.bin.docvecs.vectors_docs.npy
2020-09-07 22:56:34,641 : INFO : saved models/dmc_d10_n4_w3_mc10_s005_ech05_mycorus.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 154343
[+] ... "andnbsp be affectionate andnbsp tell them you love them"
2020-09-07 22:56:34,655 : INFO : precomputing L2-norms of doc weight vectors
[(864177, 0.972165584564209), (1850100, 0.9719691872596741), (2668987, 0.9689594507217407), (619268, 0.9688869118690491), (57906, 0.9682390689849854)]


.....get random document, tag: 2172616
[+] ... "francis with new understanding of genre by tim waldorf staff writer wasteland poet dale ritterbusch a creative writing and literature professor at the university of wisconsin-whitewater stood in an auditorium half-filled with hand-selected st"
[(2199396, 0.9648192524909973), (3036045, 0.9643988013267517), (142792, 0.9643493890762329), (871992, 0.9553544521331787), (3321396, 0.9542526006698608)]


.....get random document, tag: 4596434
[+] ... "on the few occasions that the centipede is seen it looks like one of those chinese dragons from a chinatown new year 's festival parade"
[(2978514, 0.9838422536849976), (3029376, 0.9724769592285156), (1490668, 0.9616516828536987), (137795, 0.9586300849914551), (1974668, 0.9542694687843323)]


.....get random document, tag: 2549907
[+] ... "the old way function getimplementingobject const ainstance iunknown const aguid tguid const aimplclass tclass tobject var linterfaceentry pinterfaceentry begin result nil if aimplclass nil or ainstance nil then begin exit end linterfaceentry aimplclass getinterfaceentry aguid if assigned linterfaceentry then begin if linterfaceentry^ ioffset andgt 0 then begin result tobject integer ainstance linterfaceentry^ ioffset end end end it does seem that my current blogger theme is not quite cut out for posting source code"
[(3218897, 0.9739636182785034), (348016, 0.97231125831604), (4482479, 0.9718945622444153), (784585, 0.9645411968231201), (4232568, 0.9598491787910461)]


.....get random document, tag: 4203212
[+] ... "while monsoon wedding was a great film it was in a format i was comfortable with while asoka gave me something new"
[(97720, 0.9698711633682251), (3215156, 0.9591776132583618), (2692467, 0.95798259973526), (3185815, 0.956365168094635), (3237637, 0.9530988931655884)]


.....get random document, tag: 4808497
[+] ... "those idealized beliefs were only the ghosts of the past haunting the present"
[(913013, 0.9829459190368652), (3877420, 0.9731865525245667), (4239732, 0.9680322408676147), (4507837, 0.9647110104560852), (2831449, 0.9610860347747803)]


.....get random document, tag: 826266
[+] ... "now creeping up on 40 years lehane is starting to show a little silver around the edges of his short auburn hair"
[(2194008, 0.9758858680725098), (835565, 0.9734438061714172), (4623935, 0.9725972414016724), (263908, 0.9709126353263855), (1676740, 0.9649783968925476)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (2799070): start your yah-yah job and get your pay

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d10,n4,w3,mc10,s0.005,t12):

MOST (240329, 0.9821293950080872): «you know i’m warm if i’m wearing shorts it’s always a scary time of year when i have to bring out my big white legs»

MEDIAN (4093759, -0.00251094251871109): «looker is not without weaknesses such as lapses in logic but it possesses the traits of a typical michael crichton story that make for a thoughtful excursion into another person 's world»

LEAST (903903, -0.9722144603729248): «there was the harry green goblin 's son turmoil with spiderman»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'revisions' model: Doc2Vec(dm/c,d10,n4,w3,mc10,s0.005,t12) similar words:
2020-09-07 22:56:44,327 : INFO : precomputing L2-norms of word weight vectors
     1. 0.99 'correlations'
     2. 0.98 'assurances'
     3. 0.98 'screenshots'
     4. 0.98 'collisions'
     5. 0.98 'ordeals'
     6. 0.98 'numbers'
     7. 0.98 'enquiries'
     8. 0.98 'prospects'
     9. 0.98 'discussions'
     10. 0.98 'tests'
     11. 0.98 'delays'
     12. 0.98 'efficiencies'
     13. 0.98 'restrictions'
     14. 0.97 'pressures'
     15. 0.97 'pretenses'
     16. 0.97 'profiles'
     17. 0.97 'positions'
     18. 0.97 'components'
     19. 0.97 'developments'
     20. 0.97 'losses'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-07 22:56:44,609 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-07 22:56:45,256 : INFO : capital-common-countries: 1.8% (9/506)
2020-09-07 22:56:48,155 : INFO : capital-world: 0.5% (11/2306)
2020-09-07 22:56:48,499 : INFO : currency: 0.0% (0/302)
2020-09-07 22:56:51,443 : INFO : city-in-state: 0.5% (11/2330)
2020-09-07 22:56:52,050 : INFO : family: 14.0% (71/506)
2020-09-07 22:56:53,274 : INFO : gram1-adjective-to-adverb: 0.2% (2/992)
2020-09-07 22:56:54,203 : INFO : gram2-opposite: 0.9% (7/812)
2020-09-07 22:56:55,804 : INFO : gram3-comparative: 2.1% (28/1332)
2020-09-07 22:56:56,742 : INFO : gram4-superlative: 0.9% (10/1122)
2020-09-07 22:56:57,965 : INFO : gram5-present-participle: 0.9% (9/1056)
2020-09-07 22:56:59,310 : INFO : gram6-nationality-adjective: 0.9% (13/1445)
2020-09-07 22:57:01,173 : INFO : gram7-past-tense: 0.4% (7/1560)
2020-09-07 22:57:02,847 : INFO : gram8-plural: 0.8% (10/1332)
2020-09-07 22:57:03,841 : INFO : gram9-plural-verbs: 2.1% (18/870)
2020-09-07 22:57:03,841 : INFO : Quadruplets with out-of-vocabulary words: 15.7%
2020-09-07 22:57:03,842 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-07 22:57:03,842 : INFO : Total accuracy: 1.3% (206/16471)
Doc2Vec(dm/c,d10,n4,w3,mc10,s0.005,t12): 1.25% correct (206 of 16471)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-07 22:57:04,049 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3414
2020-09-07 22:57:04,049 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.3188
2020-09-07 22:57:04,049 : INFO : Pairs with unknown words ratio: 0.6%
((0.34136300720170376, 4.996404074933212e-11), SpearmanrResult(correlation=0.31882019319320637, pvalue=9.838077050854932e-10), 0.56657223796034)


02 - simlex999
2020-09-07 22:57:04,241 : INFO : Pearson correlation coefficient against simlex999.txt: 0.1870
2020-09-07 22:57:04,241 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1624
2020-09-07 22:57:04,241 : INFO : Pairs with unknown words ratio: 0.3%
((0.18695380004677523, 2.7604098722072248e-09), SpearmanrResult(correlation=0.16236339463583205, pvalue=2.57875967423722e-07), 0.3003003003003003)


03 - simverb3500
2020-09-07 22:57:04,579 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1072
2020-09-07 22:57:04,579 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1098
2020-09-07 22:57:04,579 : INFO : Pairs with unknown words ratio: 0.1%
((0.10723931964557981, 2.059889454088662e-10), SpearmanrResult(correlation=0.10984297422460172, pvalue=7.412025439640497e-11), 0.1142857142857143)


                ---------------        COMPLETED 01        --------------
#~~~~~~~~###~~~~~~~~~~~~~~##~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS - 02


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec(dm/c,d10,n4,w3,mc10,s0.005,t12)
Save model to: models/dmc_d10_n4_w3_mc10_s005_ech25_mycorus.bin
2020-09-08 10:35:35,556 : INFO : saving Doc2Vec object under models/dmc_d10_n4_w3_mc10_s005_ech25_mycorus.bin, separately None
2020-09-08 10:35:35,556 : INFO : storing np array 'vectors_docs' to models/dmc_d10_n4_w3_mc10_s005_ech25_mycorus.bin.docvecs.vectors_docs.npy
2020-09-08 10:35:35,988 : INFO : saved models/dmc_d10_n4_w3_mc10_s005_ech25_mycorus.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 874716
[+] ... "unfortunately the suicide was just the start of their problems"
2020-09-08 10:35:35,996 : INFO : precomputing L2-norms of doc weight vectors
[(3231257, 0.9771239161491394), (87357, 0.9742224812507629), (2952992, 0.9704503417015076), (3706746, 0.9694812893867493), (2894997, 0.9688774347305298)]


.....get random document, tag: 4020984
[+] ... "i am thinkin 'bout ppl i know and ppl i knew"
[(3192406, 0.9873345494270325), (2279763, 0.9662176370620728), (3897457, 0.9652042984962463), (4789527, 0.9642302989959717), (4168901, 0.9611018896102905)]


.....get random document, tag: 332836
[+] ... "there 's nothing wrong with filming classic novels but why must they all be filmed by talentless nobodies this film rips the guts out of orwell 's tough novel turning it into a harmless fluffy romantic comedy"
[(3898759, 0.9810470938682556), (2238967, 0.97910475730896), (4096340, 0.9697048664093018), (250606, 0.9682275056838989), (3486108, 0.9635429382324219)]


.....get random document, tag: 3296802
[+] ... "i 'd probably be happier doing that kind of work as well but i do not know if i will be able to find a good office job that will hire me with my lousy resume"
[(4726489, 0.9773578643798828), (4366871, 0.9755213260650635), (2604534, 0.9753007888793945), (4660794, 0.9748955965042114), (1904371, 0.9721579551696777)]


.....get random document, tag: 3089722
[+] ... "this year will be my first year away from my mother"
[(4163196, 0.9945762157440186), (3794424, 0.9697399139404297), (2487604, 0.9694765210151672), (2677003, 0.9690213799476624), (3498688, 0.9675275087356567)]


.....get random document, tag: 3375676
[+] ... "the president has no excuses for not adjusting more quickly to this fact he was told beforehand he was told afterward but he and the defense secretary were too pig-headed to change course"
[(1430142, 0.9791989326477051), (2596825, 0.9756781458854675), (3893376, 0.9753589034080505), (4404106, 0.9753298759460449), (3869859, 0.9683084487915039)]


.....get random document, tag: 519516
[+] ... "walker must outwit quaien for survival"
[(951858, 0.973883330821991), (957803, 0.9629162549972534), (3000388, 0.9621170163154602), (144477, 0.96141117811203), (97055, 0.9596017599105835)]




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (1483835): still it has little i had the necessity to be to its side

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec(dm/c,d10,n4,w3,mc10,s0.005,t12):

MOST (4052167, 0.9701100587844849): «i saw the mri film it was undeniably there a smallish white thing in my left occipital lobe»

MEDIAN (3426216, -0.010126039385795593): «this created quite a buzz at the time»

LEAST (2870360, -0.9835653305053711): «adjani in her element the cinema depardieu a powerful political figure the likable fugitives and a friendly shop girl ledoyen lit by sunset a grim discovery the tragic accident remind you of wages of fear france 's finest vino trouble in paradise adjani finds a new audience»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
target_word: 'receptive' model: Doc2Vec(dm/c,d10,n4,w3,mc10,s0.005,t12) similar words:
2020-09-08 10:35:45,388 : INFO : precomputing L2-norms of word weight vectors
     1. 0.99 'permissible'
     2. 0.98 'vulnerable'
     3. 0.98 'harmful'
     4. 0.98 'distorted'
     5. 0.98 'antithetical'
     6. 0.98 'preferable'
     7. 0.97 'skewed'
     8. 0.97 'reactive'
     9. 0.97 'distinguishable'
     10. 0.97 'stunted'
     11. 0.97 'unsuitable'
     12. 0.97 'unfriendly'
     13. 0.97 'diversified'
     14. 0.97 'incompatible'
     15. 0.97 'proactive'
     16. 0.97 'insistent'
     17. 0.97 'amenable'
     18. 0.97 'varied'
     19. 0.97 'responsive'
     20. 0.97 'sensitive'


-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-08 10:35:45,662 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-08 10:35:46,292 : INFO : capital-common-countries: 1.2% (6/506)
2020-09-08 10:35:48,988 : INFO : capital-world: 0.3% (6/2306)
2020-09-08 10:35:49,321 : INFO : currency: 0.0% (0/302)
2020-09-08 10:35:52,003 : INFO : city-in-state: 0.4% (9/2330)
2020-09-08 10:35:52,601 : INFO : family: 10.1% (51/506)
2020-09-08 10:35:53,790 : INFO : gram1-adjective-to-adverb: 0.7% (7/992)
2020-09-08 10:35:54,803 : INFO : gram2-opposite: 0.7% (6/812)
2020-09-08 10:35:56,472 : INFO : gram3-comparative: 5.5% (73/1332)
2020-09-08 10:35:57,840 : INFO : gram4-superlative: 1.2% (13/1122)
2020-09-08 10:35:59,130 : INFO : gram5-present-participle: 1.3% (14/1056)
2020-09-08 10:36:00,932 : INFO : gram6-nationality-adjective: 1.4% (20/1445)
2020-09-08 10:36:02,798 : INFO : gram7-past-tense: 1.0% (15/1560)
2020-09-08 10:36:04,460 : INFO : gram8-plural: 1.3% (17/1332)
2020-09-08 10:36:05,498 : INFO : gram9-plural-verbs: 2.8% (24/870)
2020-09-08 10:36:05,500 : INFO : Quadruplets with out-of-vocabulary words: 15.7%
2020-09-08 10:36:05,501 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-08 10:36:05,502 : INFO : Total accuracy: 1.6% (261/16471)
Doc2Vec(dm/c,d10,n4,w3,mc10,s0.005,t12): 1.58% correct (261 of 16471)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-08 10:36:05,713 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3688
2020-09-08 10:36:05,713 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.3450
2020-09-08 10:36:05,713 : INFO : Pairs with unknown words ratio: 0.6%
((0.3687800447553679, 9.498914238755553e-13), SpearmanrResult(correlation=0.34503081558777243, pvalue=3.005762707002154e-11), 0.56657223796034)


02 - simlex999
2020-09-08 10:36:05,905 : INFO : Pearson correlation coefficient against simlex999.txt: 0.1786
2020-09-08 10:36:05,905 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1457
2020-09-08 10:36:05,905 : INFO : Pairs with unknown words ratio: 0.3%
((0.17864241330536904, 1.3747759582647224e-08), SpearmanrResult(correlation=0.14568342179215946, pvalue=3.901377096787781e-06), 0.3003003003003003)


03 - simverb3500
2020-09-08 10:36:06,123 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1141
2020-09-08 10:36:06,123 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1072
2020-09-08 10:36:06,123 : INFO : Pairs with unknown words ratio: 0.1%
((0.11412894362247603, 1.3074626762691833e-11), SpearmanrResult(correlation=0.10720688779265505, pvalue=2.0859675809584427e-10), 0.1142857142857143)


             ____________     COMPLETED     _________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
