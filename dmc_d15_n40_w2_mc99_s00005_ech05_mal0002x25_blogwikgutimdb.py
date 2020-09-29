import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=40,
        window=2,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*25*5,
        comment='ech05,mal0002x25,blogwikgutimdb',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(
            common_kwargs=common_kwargs,
            saved_fname=saved_fname,
            evaluate=False,
            database='blogwikgutimdb')

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6)
Save model to: models/dmc_d15_n40_w2_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin
2020-09-29 17:18:46,511 : INFO : saving Doc2Vec object under models/dmc_d15_n40_w2_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin, separately None
2020-09-29 17:18:46,511 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n40_w2_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin.docvecs.vectors_docs.npy
2020-09-29 17:18:46,877 : INFO : saved models/dmc_d15_n40_w2_mc99_s00005_ech05_mal0002x25_blogwikgutimdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 2741178
[+] index 2741178 -> "they would waste more than they would eat said emmeline"
2020-09-29 17:18:47,792 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 2862421
[+] index 2862421 -> "what was not shown either or not even really hinted was dahmers sexual obsession with the dead"
    No any match in top 200 similarities.


.....get random document, tag: 4824194
[+] index 4824194 -> "the theremin an exceedingly difficult instrument to play was even used in some popular music most notably in good vibrations by the beach boys"
[*] Matched with rank 33, score: 0.8731327056884766!


.....get random document, tag: 1272811
[+] index 1272811 -> "and finally these people inquire whether it is the masses alone who need a reformed and improved education"
    No any match in top 200 similarities.


.....get random document, tag: 87651
[+] index 87651 -> "when they realize what a slippery cunning rascal he is i should gain some credit from the case"
    No any match in top 200 similarities.


.....get random document, tag: 5936434
[+] index 5936434 -> "oswald who i 'd like to do some private target practise myself"
    No any match in top 200 similarities.


.....get random document, tag: 540446
[+] index 540446 -> "so far excellency he continued you can not be in ignorance of the general dissatisfaction prevailing among our most illustrious cousin 's subjects"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (534878): hawley 's office that the article in question emanated from brooke of tipton and that brooke had secretly bought the pioneer some months ago

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):

MOST (4944910, 0.9255120754241943): «it is an important subject because unemployment is a problem that affects the public most directly and severely»

MEDIAN (4164685, 0.002744227647781372): «the transkei has many rivers flowing from the mountains to the oceans so unlike much of south africa it is relatively unscathed by drought»

LEAST (5533390, -0.9297807216644287): «astrology and horoscopes by astrology com free horoscopes and astrology»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'took' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
2020-09-29 17:19:11,720 : INFO : precomputing L2-norms of word weight vectors
     1. 0.94 'fetched'
     2. 0.90 'picked'
     3. 0.89 'ditched'
     4. 0.88 'caught'
     5. 0.88 'gave'
     6. 0.86 'dropped'
     7. 0.86 'got'


[+] target_word: 'frontier' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.93 'seaport'
     2. 0.92 'frontiers'
     3. 0.92 'deccan'
     4. 0.91 'outpost'
     5. 0.90 'asiatic'
     6. 0.89 'capital'
     7. 0.89 'union'


[+] target_word: 'innocence' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.94 'humility'
     2. 0.93 'magnanimity'
     3. 0.92 'meanness'
     4. 0.92 'penitence'
     5. 0.92 'generosity'
     6. 0.91 'vanity'
     7. 0.91 'folly'


[+] target_word: 'invasion' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.93 'conquest'
     2. 0.92 'mutiny'
     3. 0.91 'occupation'
     4. 0.91 'alliance'
     5. 0.91 'reunification'
     6. 0.90 'expedition'
     7. 0.90 'colonisation'


[+] target_word: 'clerk' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.93 'superintendent'
     2. 0.93 'solicitor'
     3. 0.93 'supervisor'
     4. 0.92 'accountant'
     5. 0.92 'warden'
     6. 0.92 'inspector'
     7. 0.91 'broker'


[+] target_word: 'conducted' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.93 'initiated'
     2. 0.92 'overseen'
     3. 0.92 'organized'
     4. 0.92 'funded'
     5. 0.92 'inaugurated'
     6. 0.92 'investigated'
     7. 0.91 'supervised'


[+] target_word: 'odds' model: Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6):
     1. 0.93 'torture'
     2. 0.90 'blunder'
     3. 0.89 'provocation'
     4. 0.89 'threats'
     5. 0.89 'losses'
     6. 0.88 'disadvantage'
     7. 0.87 'offense'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-29 17:19:12,079 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-29 17:19:12,270 : INFO : capital-common-countries: 7.4% (34/462)
2020-09-29 17:19:12,659 : INFO : capital-world: 5.2% (45/862)
2020-09-29 17:19:12,716 : INFO : currency: 0.0% (0/128)
2020-09-29 17:19:13,636 : INFO : city-in-state: 3.4% (69/2009)
2020-09-29 17:19:13,802 : INFO : family: 43.4% (165/380)
2020-09-29 17:19:14,214 : INFO : gram1-adjective-to-adverb: 3.4% (34/992)
2020-09-29 17:19:14,504 : INFO : gram2-opposite: 2.5% (16/650)
2020-09-29 17:19:15,070 : INFO : gram3-comparative: 34.5% (459/1332)
2020-09-29 17:19:15,517 : INFO : gram4-superlative: 10.3% (109/1056)
2020-09-29 17:19:15,907 : INFO : gram5-present-participle: 24.7% (245/992)
2020-09-29 17:19:16,507 : INFO : gram6-nationality-adjective: 12.0% (156/1299)
2020-09-29 17:19:17,290 : INFO : gram7-past-tense: 24.9% (389/1560)
2020-09-29 17:19:17,832 : INFO : gram8-plural: 14.9% (177/1190)
2020-09-29 17:19:18,173 : INFO : gram9-plural-verbs: 15.4% (125/812)
2020-09-29 17:19:18,173 : INFO : Quadruplets with out-of-vocabulary words: 29.8%
2020-09-29 17:19:18,173 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 17:19:18,173 : INFO : Total accuracy: 14.7% (2023/13724)
Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6): 14.74% correct (2023 of 13724)


[+] questions-words-narrowed.txt
2020-09-29 17:19:18,195 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-29 17:19:18,360 : INFO : family: 43.4% (165/380)
2020-09-29 17:19:18,771 : INFO : gram1-adjective-to-adverb: 3.4% (34/992)
2020-09-29 17:19:19,061 : INFO : gram2-opposite: 2.5% (16/650)
2020-09-29 17:19:19,680 : INFO : gram3-comparative: 34.5% (459/1332)
2020-09-29 17:19:20,268 : INFO : gram4-superlative: 10.3% (109/1056)
2020-09-29 17:19:20,657 : INFO : gram5-present-participle: 24.7% (245/992)
2020-09-29 17:19:21,253 : INFO : gram6-nationality-adjective: 12.0% (156/1299)
2020-09-29 17:19:21,965 : INFO : gram7-past-tense: 24.9% (389/1560)
2020-09-29 17:19:22,509 : INFO : gram8-plural: 14.9% (177/1190)
2020-09-29 17:19:22,849 : INFO : gram9-plural-verbs: 15.4% (125/812)
2020-09-29 17:19:22,850 : INFO : Quadruplets with out-of-vocabulary words: 8.2%
2020-09-29 17:19:22,850 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 17:19:22,850 : INFO : Total accuracy: 18.3% (1875/10263)
Doc2Vec("ech05,mal0002x25,blogwikgutimdb",dm/c,d15,n40,w2,mc99,s5e-05,t6): 18.27% correct (1875 of 10263)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-29 17:19:23,006 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5487
2020-09-29 17:19:23,006 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5450
2020-09-29 17:19:23,006 : INFO : Pairs with unknown words ratio: 2.5%
((0.548720008821689, 1.94098711558756e-28), SpearmanrResult(correlation=0.545000631305873, pvalue=5.271337950863538e-28), 2.5495750708215295)


02 - simlex999
2020-09-29 17:19:23,030 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3131
2020-09-29 17:19:23,030 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2678
2020-09-29 17:19:23,030 : INFO : Pairs with unknown words ratio: 0.5%
((0.3131075943121919, 4.761108533117711e-24), SpearmanrResult(correlation=0.2678134951248124, pvalue=8.671560332287864e-18), 0.5005005005005005)


03 - simverb3500
2020-09-29 17:19:23,200 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1742
2020-09-29 17:19:23,200 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1576
2020-09-29 17:19:23,200 : INFO : Pairs with unknown words ratio: 6.0%
((0.17418608842234637, 8.070565853540574e-24), SpearmanrResult(correlation=0.1576250147264676, pvalue=9.614355892373182e-20), 6.0285714285714285)


     ____________     COMPLETED      ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
