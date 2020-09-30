import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=67,
        window=5,
        min_count=99,
        sample=0.001,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=20,
        min_alpha=0.0002,
        alpha=0.0002*10*20,
        comment='ech20,mal0002x10,refined',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(
            common_kwargs=common_kwargs,
            saved_fname=saved_fname,
            evaluate=False,
            database='refined')

"""
2020-09-30 13:07:37,723 : INFO : collected 877734 word types and 46020000 unique tags from a corpus of 46020000 examples and 610836932 words
2020-09-30 13:07:37,723 : INFO : Loading a fresh vocabulary
2020-09-30 13:07:37,965 : INFO : effective_min_count=99 retains 53059 unique words (6% of original 877734, drops 824675)
2020-09-30 13:07:37,966 : INFO : effective_min_count=99 leaves 606131238 word corpus (99% of original 610836932, drops 4705694)
2020-09-30 13:07:38,083 : INFO : deleting the raw counts dictionary of 877734 items
2020-09-30 13:07:38,100 : INFO : sample=0.001 downsamples 47 most-common words
2020-09-30 13:07:38,100 : INFO : downsampling leaves estimated 459319807 word corpus (75.8% of prior 606131238)
2020-09-30 13:07:38,185 : INFO : estimated required memory for 53059 words and 15 dimensions: 2825931980 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


INFO: Training parameters: {'vector_size': 15, 'negative': 67, 'window': 5, 'min_count': 99, 'sample': 0.001, 'dm': 1, 'dm_concat': 1, 'hs': 0, 'epochs': 20, 'min_alpha': 0.0002, 'alpha': 0.04, 'comment': 'ech20,mal0002x10,refined'}
INFO: Model details: Doc2Vec("ech20,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6)
INFO: Save model to: models/dmc_d15_n67_w5_mc99_s001_ech20_mal0002x10_refined.bin
2020-09-30 23:29:40,924 : INFO : saving Doc2Vec object under models/dmc_d15_n67_w5_mc99_s001_ech20_mal0002x10_refined.bin, separately None
2020-09-30 23:29:40,925 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n67_w5_mc99_s001_ech20_mal0002x10_refined.bin.trainables.vectors_docs_lockf.npy
2020-09-30 23:29:41,041 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n67_w5_mc99_s001_ech20_mal0002x10_refined.bin.docvecs.vectors_docs.npy
2020-09-30 23:29:42,631 : INFO : saved models/dmc_d15_n67_w5_mc99_s001_ech20_mal0002x10_refined.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 18049879
-> index 18049879 --> "i am clearly not dead and i have no spiritual or psychic source"
2020-09-30 23:29:42,724 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 12071244
-> index 12071244 --> "almost no difficult pens among the sharp bedroom were measuring about the urban stable"
    No any match in top 200 similarities.


.....get random document, tag: 2392402
-> index 2392402 --> "why would they want to follow in your footsteps"
    No any match in top 200 similarities.


.....get random document, tag: 1614679
-> index 1614679 --> "my quiet disk will not answer before i talk it"
    No any match in top 200 similarities.


.....get random document, tag: 24688489
-> index 24688489 --> "and to achieve its goals it must often traverse the same paths in terms of its logic"
    No any match in top 200 similarities.


.....get random document, tag: 6813918
-> index 6813918 --> "please refer to job code tcdba when responding to this ad"
    No any match in top 200 similarities.


.....get random document, tag: 27572234
-> index 27572234 --> "the local taxes collected by hippocrites who condemn smoking while loving it when you pay them"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (40210525): which has a lot to do with the coin hordes found in scandinavia

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech20,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):

MOST (20806261, 0.938428521156311): «how will you waste the angry long books before dickie does»

MEDIAN (17082045, -0.0005177780985832214): «i do not know much about the singer lady gaga»

LEAST (4358247, -0.9449502825737): «currency speculation is a very easy way to lose your shirt»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'management' model: Doc2Vec("ech20,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
2020-09-30 23:31:13,599 : INFO : precomputing L2-norms of word weight vectors
     1. 0.95 'accreditation'
     2. 0.94 'licensing'
     3. 0.94 'recruitment'
     4. 0.94 'managment'
     5. 0.93 'accountancy'
     6. 0.93 'childcare'
     7. 0.93 'enrollment'


[+] target_word: 'estate' model: Doc2Vec("ech20,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.94 'currency'
     2. 0.93 'infrastructure'
     3. 0.93 'securities'
     4. 0.93 'laboratory'
     5. 0.93 'intelligence'
     6. 0.92 'enterprise'
     7. 0.92 'electronics'


[+] target_word: 'wear' model: Doc2Vec("ech20,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.96 'carry'
     2. 0.96 'wash'
     3. 0.95 'drape'
     4. 0.94 'wrap'
     5. 0.94 'climb'
     6. 0.93 'bleed'
     7. 0.93 'suck'


[+] target_word: 'comp' model: Doc2Vec("ech20,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.97 'blitz'
     2. 0.97 'survey'
     3. 0.96 'soundtrack'
     4. 0.96 'pp'
     5. 0.96 'catalog'
     6. 0.95 'package'
     7. 0.95 'workout'


[+] target_word: 'denominations' model: Doc2Vec("ech20,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.97 'sects'
     2. 0.97 'faiths'
     3. 0.96 'professors'
     4. 0.96 'dieties'
     5. 0.95 'partisans'
     6. 0.95 'abductees'
     7. 0.95 'homeschoolers'


[+] target_word: 'cricket' model: Doc2Vec("ech20,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.95 'usaaf'
     2. 0.95 'rugby'
     3. 0.94 'boxing'
     4. 0.94 'gaming'
     5. 0.94 'settlement'
     6. 0.94 'dominion'
     7. 0.94 'football'


[+] target_word: 'compulsive' model: Doc2Vec("ech20,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.98 'sadistic'
     2. 0.97 'pathological'
     3. 0.96 'bloodthirsty'
     4. 0.96 'phobic'
     5. 0.96 'neurotic'
     6. 0.96 'bumbling'
     7. 0.96 'lowlife'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-30 23:31:15,007 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-30 23:31:15,292 : INFO : capital-common-countries: 3.9% (18/462)
2020-09-30 23:31:16,019 : INFO : capital-world: 1.6% (18/1157)
2020-09-30 23:31:16,133 : INFO : currency: 1.7% (3/178)
2020-09-30 23:31:17,569 : INFO : city-in-state: 0.8% (18/2267)
2020-09-30 23:31:17,840 : INFO : family: 16.7% (70/420)
2020-09-30 23:31:18,426 : INFO : gram1-adjective-to-adverb: 2.1% (21/992)
2020-09-30 23:31:18,909 : INFO : gram2-opposite: 2.6% (20/756)
2020-09-30 23:31:19,597 : INFO : gram3-comparative: 9.3% (124/1332)
2020-09-30 23:31:20,210 : INFO : gram4-superlative: 5.6% (59/1056)
2020-09-30 23:31:20,904 : INFO : gram5-present-participle: 5.0% (53/1056)
2020-09-30 23:31:21,720 : INFO : gram6-nationality-adjective: 3.1% (40/1299)
2020-09-30 23:31:22,722 : INFO : gram7-past-tense: 6.0% (94/1560)
2020-09-30 23:31:23,513 : INFO : gram8-plural: 2.5% (30/1190)
2020-09-30 23:31:24,073 : INFO : gram9-plural-verbs: 5.4% (47/870)
2020-09-30 23:31:24,073 : INFO : Quadruplets with out-of-vocabulary words: 25.3%
2020-09-30 23:31:24,074 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-30 23:31:24,074 : INFO : Total accuracy: 4.2% (615/14595)
Doc2Vec("ech20,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6): 4.21% correct (615 of 14595)


[+] questions-words-narrowed.txt
2020-09-30 23:31:24,112 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-30 23:31:24,386 : INFO : family: 16.7% (70/420)
2020-09-30 23:31:24,977 : INFO : gram1-adjective-to-adverb: 2.1% (21/992)
2020-09-30 23:31:25,462 : INFO : gram2-opposite: 2.6% (20/756)
2020-09-30 23:31:26,155 : INFO : gram3-comparative: 9.3% (124/1332)
2020-09-30 23:31:26,769 : INFO : gram4-superlative: 5.6% (59/1056)
2020-09-30 23:31:27,465 : INFO : gram5-present-participle: 5.0% (53/1056)
2020-09-30 23:31:28,286 : INFO : gram6-nationality-adjective: 3.1% (40/1299)
2020-09-30 23:31:29,296 : INFO : gram7-past-tense: 6.0% (94/1560)
2020-09-30 23:31:30,715 : INFO : gram8-plural: 2.5% (30/1190)
2020-09-30 23:31:31,275 : INFO : gram9-plural-verbs: 5.4% (47/870)
2020-09-30 23:31:31,275 : INFO : Quadruplets with out-of-vocabulary words: 5.8%
2020-09-30 23:31:31,275 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-30 23:31:31,275 : INFO : Total accuracy: 5.3% (558/10531)
Doc2Vec("ech20,mal0002x10,refined",dm/c,d15,n67,w5,mc99,s0.001,t6): 5.30% correct (558 of 10531)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-30 23:31:31,327 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3578
2020-09-30 23:31:31,327 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.3981
2020-09-30 23:31:31,327 : INFO : Pairs with unknown words ratio: 0.6%
((0.3578047691419501, 4.858852856354878e-12), SpearmanrResult(correlation=0.39812698009714165, pvalue=8.81741862133913e-15), 0.56657223796034)


02 - simlex999
2020-09-30 23:31:31,989 : INFO : Pearson correlation coefficient against simlex999.txt: 0.1973
2020-09-30 23:31:31,989 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2008
2020-09-30 23:31:31,989 : INFO : Pairs with unknown words ratio: 0.5%
((0.19734501297955195, 3.477609912934156e-10), SpearmanrResult(correlation=0.20081310890313864, pvalue=1.6762314853868335e-10), 0.5005005005005005)


03 - simverb3500
2020-09-30 23:31:32,052 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1316
2020-09-30 23:31:32,052 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1383
2020-09-30 23:31:32,052 : INFO : Pairs with unknown words ratio: 0.5%
((0.1316159468506768, 6.309078775443396e-15), SpearmanrResult(correlation=0.13825077932364727, pvalue=2.5181394561914663e-16), 0.5142857142857142)


-----------------------------------------------------
Benchmark similarity score with respect to theme word
-----------------------------------------------------


 ~  a beautiful girl - a pretty girl, distance score: 1.869662, with respect to theme: beautiful
 ~  a beautiful girl - a pretty woman, distance score: 2.831595, with respect to theme: female
[*] a beautiful girl - a ugly girl, distance score: 0.385104, with respect to theme: beautiful
 ~  a new car - an old car, distance score: 2.715984, with respect to theme: car
[*] a new car - an old car, distance score: 1.194620, with respect to theme: new
 ~  a new car - an huge car, distance score: 2.132449, with respect to theme: car
[*] girl - boy, distance score: 7.758666, with respect to theme: gender
 ~  girl - boy, distance score: 0.936747, with respect to theme: young
[*] girl - woman, distance score: 0.218001, with respect to theme: gender
[*] man - woman, distance score: 0.411710, with respect to theme: gender
 ~  boy - man, distance score: 7.258321, with respect to theme: gender
 ~  girl - man, distance score: 0.313753, with respect to theme: gender
[*] boy - woman, distance score: 7.437166, with respect to theme: gender
 ~  son - daughter, distance score: 0.004308, with respect to theme: boy
[*] son - daughter, distance score: 0.122232, with respect to theme: children
 ~  sea - mountain, distance score: 2.212876, with respect to theme: nature
 ~  forest - mountain, distance score: 2.244954, with respect to theme: nature
 ~  sea - house, distance score: 0.175440, with respect to theme: nature
[*] sea - software, distance score: 0.366089, with respect to theme: nature
[*] house - software, distance score: 0.195492, with respect to theme: nature
[*] sea - mountain, distance score: 0.353894, with respect to theme: climbing
 ~  sea - river, distance score: 1.150359, with respect to theme: climbing
[*] human - dog, distance score: 0.223977, with respect to theme: mammal
[*] human - fish, distance score: 0.815036, with respect to theme: mammal
 ~  dog - fish, distance score: 0.333444, with respect to theme: mammal
[*] bird - fish, distance score: 0.246466, with respect to theme: mammal
[*] man - woman, distance score: 0.067146, with respect to theme: human
 ~  man - elephant, distance score: 0.000013, with respect to theme: human
[*] woman - elephant, distance score: 0.568043, with respect to theme: human
 ~  dog - elephant, distance score: 0.379738, with respect to theme: human
 ~  dog - lion, distance score: 0.235380, with respect to theme: pet
[*] cat - lion, distance score: 1.145791, with respect to theme: pet
 ~  cat - dot, distance score: 0.483226, with respect to theme: pet
 ~  car - orange, distance score: 0.202152, with respect to theme: food
[*] car - apple, distance score: 0.555313, with respect to theme: food
 ~  orange - apple, distance score: 0.599387, with respect to theme: food
[*] car - book, distance score: 0.339339, with respect to theme: food
 ~  car - orange, distance score: 0.041332, with respect to theme: vehicle
 ~  car - grapes, distance score: 0.251038, with respect to theme: vehicle
 ~  car - motorbike, distance score: 0.467719, with respect to theme: vehicle
[*] orange - apple, distance score: 0.109096, with respect to theme: vehicle
<EPOCHS>: 10 - <SCORE>: 46.34


 ~  a beautiful girl - a pretty girl, distance score: 2.051676, with respect to theme: beautiful
 ~  a beautiful girl - a pretty woman, distance score: 3.116945, with respect to theme: female
[*] a beautiful girl - a ugly girl, distance score: 0.995538, with respect to theme: beautiful
 ~  a new car - an old car, distance score: 1.996992, with respect to theme: car
[*] a new car - an old car, distance score: 0.570485, with respect to theme: new
 ~  a new car - an huge car, distance score: 3.837784, with respect to theme: car
[*] girl - boy, distance score: 3.967935, with respect to theme: gender
 ~  girl - boy, distance score: 0.810980, with respect to theme: young
[*] girl - woman, distance score: 0.260881, with respect to theme: gender
 ~  man - woman, distance score: 0.013541, with respect to theme: gender
 ~  boy - man, distance score: 2.505999, with respect to theme: gender
[*] girl - man, distance score: 0.623976, with respect to theme: gender
[*] boy - woman, distance score: 8.210074, with respect to theme: gender
 ~  son - daughter, distance score: 0.001563, with respect to theme: boy
[*] son - daughter, distance score: 0.160791, with respect to theme: children
 ~  sea - mountain, distance score: 3.319176, with respect to theme: nature
 ~  forest - mountain, distance score: 3.505174, with respect to theme: nature
 ~  sea - house, distance score: 0.065849, with respect to theme: nature
 ~  sea - software, distance score: 0.070704, with respect to theme: nature
 ~  house - software, distance score: 0.490822, with respect to theme: nature
[*] sea - mountain, distance score: 0.679504, with respect to theme: climbing
 ~  sea - river, distance score: 2.683488, with respect to theme: climbing
[*] human - dog, distance score: 0.033396, with respect to theme: mammal
 ~  human - fish, distance score: 0.185082, with respect to theme: mammal
 ~  dog - fish, distance score: 0.198144, with respect to theme: mammal
[*] bird - fish, distance score: 0.151936, with respect to theme: mammal
[*] man - woman, distance score: 0.272998, with respect to theme: human
 ~  man - elephant, distance score: 0.191133, with respect to theme: human
[*] woman - elephant, distance score: 0.562110, with respect to theme: human
[*] dog - elephant, distance score: 0.342914, with respect to theme: human
 ~  dog - lion, distance score: 0.091947, with respect to theme: pet
 ~  cat - lion, distance score: 0.247837, with respect to theme: pet
 ~  cat - dot, distance score: 0.377758, with respect to theme: pet
 ~  car - orange, distance score: 0.230149, with respect to theme: food
[*] car - apple, distance score: 0.485012, with respect to theme: food
 ~  orange - apple, distance score: 0.557883, with respect to theme: food
[*] car - book, distance score: 0.045676, with respect to theme: food
 ~  car - orange, distance score: 0.011834, with respect to theme: vehicle
 ~  car - grapes, distance score: 0.217829, with respect to theme: vehicle
 ~  car - motorbike, distance score: 0.659307, with respect to theme: vehicle
[*] orange - apple, distance score: 0.258304, with respect to theme: vehicle
<EPOCHS>: 20 - <SCORE>: 39.02


[*] a beautiful girl - a pretty girl, distance score: 0.168517, with respect to theme: beautiful
 ~  a beautiful girl - a pretty woman, distance score: 6.480746, with respect to theme: female
[*] a beautiful girl - a ugly girl, distance score: 1.099661, with respect to theme: beautiful
 ~  a new car - an old car, distance score: 3.625210, with respect to theme: car
[*] a new car - an old car, distance score: 3.820726, with respect to theme: new
 ~  a new car - an huge car, distance score: 0.367429, with respect to theme: car
[*] girl - boy, distance score: 2.770032, with respect to theme: gender
 ~  girl - boy, distance score: 1.668231, with respect to theme: young
[*] girl - woman, distance score: 0.202659, with respect to theme: gender
 ~  man - woman, distance score: 0.252084, with respect to theme: gender
 ~  boy - man, distance score: 2.876567, with respect to theme: gender
 ~  girl - man, distance score: 0.116143, with respect to theme: gender
[*] boy - woman, distance score: 4.024480, with respect to theme: gender
 ~  son - daughter, distance score: 0.021852, with respect to theme: boy
[*] son - daughter, distance score: 0.001640, with respect to theme: children
 ~  sea - mountain, distance score: 4.518376, with respect to theme: nature
 ~  forest - mountain, distance score: 4.464913, with respect to theme: nature
 ~  sea - house, distance score: 0.149832, with respect to theme: nature
 ~  sea - software, distance score: 0.053357, with respect to theme: nature
[*] house - software, distance score: 0.011021, with respect to theme: nature
[*] sea - mountain, distance score: 2.903982, with respect to theme: climbing
 ~  sea - river, distance score: 5.574004, with respect to theme: climbing
 ~  human - dog, distance score: 0.443277, with respect to theme: mammal
 ~  human - fish, distance score: 0.235418, with respect to theme: mammal
 ~  dog - fish, distance score: 0.187838, with respect to theme: mammal
[*] bird - fish, distance score: 0.263655, with respect to theme: mammal
[*] man - woman, distance score: 0.200586, with respect to theme: human
 ~  man - elephant, distance score: 0.273396, with respect to theme: human
 ~  woman - elephant, distance score: 0.179256, with respect to theme: human
[*] dog - elephant, distance score: 0.182267, with respect to theme: human
 ~  dog - lion, distance score: 0.236343, with respect to theme: pet
 ~  cat - lion, distance score: 0.246304, with respect to theme: pet
[*] cat - dot, distance score: 0.292669, with respect to theme: pet
[*] car - orange, distance score: 0.419361, with respect to theme: food
 ~  car - apple, distance score: 0.186855, with respect to theme: food
[*] orange - apple, distance score: 0.023941, with respect to theme: food
[*] car - book, distance score: 0.152975, with respect to theme: food
 ~  car - orange, distance score: 0.123485, with respect to theme: vehicle
 ~  car - grapes, distance score: 0.208610, with respect to theme: vehicle
 ~  car - motorbike, distance score: 0.462267, with respect to theme: vehicle
[*] orange - apple, distance score: 0.070014, with respect to theme: vehicle
<EPOCHS>: 50 - <SCORE>: 41.46


 ~  a beautiful girl - a pretty girl, distance score: 0.922654, with respect to theme: beautiful
 ~  a beautiful girl - a pretty woman, distance score: 1.272094, with respect to theme: female
[*] a beautiful girl - a ugly girl, distance score: 0.447384, with respect to theme: beautiful
 ~  a new car - an old car, distance score: 1.246170, with respect to theme: car
[*] a new car - an old car, distance score: 1.540527, with respect to theme: new
 ~  a new car - an huge car, distance score: 0.719876, with respect to theme: car
 ~  girl - boy, distance score: 0.253899, with respect to theme: gender
 ~  girl - boy, distance score: 1.890623, with respect to theme: young
[*] girl - woman, distance score: 0.140667, with respect to theme: gender
 ~  man - woman, distance score: 0.097338, with respect to theme: gender
 ~  boy - man, distance score: 0.395498, with respect to theme: gender
 ~  girl - man, distance score: 0.187048, with respect to theme: gender
[*] boy - woman, distance score: 0.674289, with respect to theme: gender
 ~  son - daughter, distance score: 0.003645, with respect to theme: boy
[*] son - daughter, distance score: 0.147474, with respect to theme: children
 ~  sea - mountain, distance score: 0.526942, with respect to theme: nature
 ~  forest - mountain, distance score: 2.884585, with respect to theme: nature
 ~  sea - house, distance score: 0.109952, with respect to theme: nature
 ~  sea - software, distance score: 0.133266, with respect to theme: nature
[*] house - software, distance score: 0.093058, with respect to theme: nature
[*] sea - mountain, distance score: 0.818123, with respect to theme: climbing
 ~  sea - river, distance score: 5.321771, with respect to theme: climbing
[*] human - dog, distance score: 0.112490, with respect to theme: mammal
 ~  human - fish, distance score: 0.092065, with respect to theme: mammal
 ~  dog - fish, distance score: 0.158985, with respect to theme: mammal
[*] bird - fish, distance score: 0.101380, with respect to theme: mammal
[*] man - woman, distance score: 0.076469, with respect to theme: human
 ~  man - elephant, distance score: 0.109979, with respect to theme: human
 ~  woman - elephant, distance score: 0.048544, with respect to theme: human
[*] dog - elephant, distance score: 0.224422, with respect to theme: human
 ~  dog - lion, distance score: 0.280599, with respect to theme: pet
 ~  cat - lion, distance score: 0.118325, with respect to theme: pet
[*] cat - dot, distance score: 0.286487, with respect to theme: pet
 ~  car - orange, distance score: 0.335921, with respect to theme: food
 ~  car - apple, distance score: 0.160411, with respect to theme: food
[*] orange - apple, distance score: 0.219167, with respect to theme: food
[*] car - book, distance score: 0.257769, with respect to theme: food
[*] car - orange, distance score: 0.501491, with respect to theme: vehicle
 ~  car - grapes, distance score: 0.215744, with respect to theme: vehicle
[*] car - motorbike, distance score: 0.143026, with respect to theme: vehicle
[*] orange - apple, distance score: 0.103996, with respect to theme: vehicle
<EPOCHS>: 100 - <SCORE>: 41.46


[*] a beautiful girl - a pretty girl, distance score: 0.218613, with respect to theme: beautiful
 ~  a beautiful girl - a pretty woman, distance score: 0.529284, with respect to theme: female
 ~  a beautiful girl - a ugly girl, distance score: 0.153231, with respect to theme: beautiful
 ~  a new car - an old car, distance score: 0.511106, with respect to theme: car
[*] a new car - an old car, distance score: 0.704522, with respect to theme: new
[*] a new car - an huge car, distance score: 0.007923, with respect to theme: car
 ~  girl - boy, distance score: 0.107657, with respect to theme: gender
 ~  girl - boy, distance score: 0.525131, with respect to theme: young
[*] girl - woman, distance score: 0.103271, with respect to theme: gender
 ~  man - woman, distance score: 0.140435, with respect to theme: gender
 ~  boy - man, distance score: 0.375100, with respect to theme: gender
 ~  girl - man, distance score: 0.026711, with respect to theme: gender
[*] boy - woman, distance score: 0.712447, with respect to theme: gender
 ~  son - daughter, distance score: 0.012617, with respect to theme: boy
[*] son - daughter, distance score: 0.074019, with respect to theme: children
 ~  sea - mountain, distance score: 1.533285, with respect to theme: nature
 ~  forest - mountain, distance score: 0.849726, with respect to theme: nature
 ~  sea - house, distance score: 0.030157, with respect to theme: nature
 ~  sea - software, distance score: 0.049825, with respect to theme: nature
[*] house - software, distance score: 0.073369, with respect to theme: nature
 ~  sea - mountain, distance score: 0.247549, with respect to theme: climbing
 ~  sea - river, distance score: 2.410728, with respect to theme: climbing
[*] human - dog, distance score: 0.024027, with respect to theme: mammal
 ~  human - fish, distance score: 0.007870, with respect to theme: mammal
 ~  dog - fish, distance score: 0.079788, with respect to theme: mammal
[*] bird - fish, distance score: 0.052052, with respect to theme: mammal
[*] man - woman, distance score: 0.088591, with respect to theme: human
 ~  man - elephant, distance score: 0.059145, with respect to theme: human
 ~  woman - elephant, distance score: 0.001209, with respect to theme: human
[*] dog - elephant, distance score: 0.155376, with respect to theme: human
 ~  dog - lion, distance score: 0.017292, with respect to theme: pet
 ~  cat - lion, distance score: 0.040928, with respect to theme: pet
[*] cat - dot, distance score: 0.097729, with respect to theme: pet
 ~  car - orange, distance score: 0.053236, with respect to theme: food
 ~  car - apple, distance score: 0.158413, with respect to theme: food
[*] orange - apple, distance score: 0.088395, with respect to theme: food
[*] car - book, distance score: 0.297767, with respect to theme: food
 ~  car - orange, distance score: 0.072421, with respect to theme: vehicle
 ~  car - grapes, distance score: 0.002626, with respect to theme: vehicle
[*] car - motorbike, distance score: 0.035953, with respect to theme: vehicle
[*] orange - apple, distance score: 0.165913, with respect to theme: vehicle
<EPOCHS>: 200 - <SCORE>: 39.02




_____  COMPLETED  _________________________________
###~~~~~~~~#~~~~~~~#~~~~~~~#~~~~~~~~~~#~~~~~~~~~###


"""
