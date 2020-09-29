import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=30,
        window=3,
        min_count=75,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*20*5,
        comment='ech05,mal0002x20,blogwikgutimdb',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(
            common_kwargs=common_kwargs,
            saved_fname=saved_fname,
            evaluate=False,
            database='blogwikgutimdb')

"""
2020-09-29 15:54:45,449 : INFO : collected 605528 word types and 7410000 unique tags from a corpus of 7410000 examples and 121440062 words
2020-09-29 15:54:45,449 : INFO : Loading a fresh vocabulary
2020-09-29 15:54:45,621 : INFO : effective_min_count=75 retains 40444 unique words (6% of original 605528, drops 565084)
2020-09-29 15:54:45,622 : INFO : effective_min_count=75 leaves 118479531 word corpus (97% of original 121440062, drops 2960531)
2020-09-29 15:54:45,711 : INFO : deleting the raw counts dictionary of 605528 items
2020-09-29 15:54:45,723 : INFO : sample=5e-05 downsamples 735 most-common words
2020-09-29 15:54:45,723 : INFO : downsampling leaves estimated 51884236 word corpus (43.8% of prior 118479531)
2020-09-29 15:54:45,785 : INFO : estimated required memory for 40444 words and 15 dimensions: 484235120 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/c,d15,n30,w3,mc75,s5e-05,t6)
Save model to: models/dmc_d15_n30_w3_mc75_s00005_ech05_mal0002x20_blogwikgutimdb.bin
2020-09-29 16:32:40,374 : INFO : saving Doc2Vec object under models/dmc_d15_n30_w3_mc75_s00005_ech05_mal0002x20_blogwikgutimdb.bin, separately None
2020-09-29 16:32:40,374 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n30_w3_mc75_s00005_ech05_mal0002x20_blogwikgutimdb.bin.docvecs.vectors_docs.npy
2020-09-29 16:32:40,792 : INFO : saved models/dmc_d15_n30_w3_mc75_s00005_ech05_mal0002x20_blogwikgutimdb.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 4760834
[+] index 4760834 -> "the hostility commonly faced by jews in the diaspora has been extensively described by john m"
2020-09-29 16:32:42,386 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 1639229
[+] index 1639229 -> "on the flank of the armed men sentot was performing a slow dance but he too seemed to have gone dumb"
    No any match in top 200 similarities.


.....get random document, tag: 2392573
[+] index 2392573 -> "you need not fear militza said the beautiful girl looking at the prince with friendly eyes"
    No any match in top 200 similarities.


.....get random document, tag: 1998920
[+] index 1998920 -> "alas alas i see no more my love who yet my sadness cheers"
    No any match in top 200 similarities.


.....get random document, tag: 7366936
[+] index 7366936 -> "i would like to see the rest of europe australia new zealand and morocco"
    No any match in top 200 similarities.


.....get random document, tag: 47198
[+] index 47198 -> "and he redoubled his efforts to such an extent that the boat scarcely went down stream at all yet edged closer to the right hand shore"
    No any match in top 200 similarities.


.....get random document, tag: 6424902
[+] index 6424902 -> "thank god for email at least we will be able to get in touch easily"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (2609480): i do not know just what we can offer to do but we must find out

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/c,d15,n30,w3,mc75,s5e-05,t6):

MOST (3929005, 0.9329736232757568): «for every 100 females age 18 and over there are 87 0 males»

MEDIAN (1874228, 0.00014301761984825134): «together they walked up the golden arcade to tell the others»

LEAST (4773496, -0.9376237392425537): «machinery and transport equipment manufactured goods chemicals fuels and lubrican nots food»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'cannon' model: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/c,d15,n30,w3,mc75,s5e-05,t6):
2020-09-29 16:33:07,476 : INFO : precomputing L2-norms of word weight vectors
     1. 0.94 'torpedo'
     2. 0.91 'tomahawk'
     3. 0.91 'cannons'
     4. 0.90 'airship'
     5. 0.90 'cruiser'
     6. 0.90 'musket'
     7. 0.90 'sabre'


[+] target_word: 'increasing' model: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/c,d15,n30,w3,mc75,s5e-05,t6):
     1. 0.96 'decreasing'
     2. 0.96 'diminishing'
     3. 0.95 'lessening'
     4. 0.94 'reducing'
     5. 0.93 'considerable'
     6. 0.93 'increased'
     7. 0.92 'sustaining'


[+] target_word: 'slowly' model: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/c,d15,n30,w3,mc75,s5e-05,t6):
     1. 0.94 'steadily'
     2. 0.91 'quickly'
     3. 0.91 'swiftly'
     4. 0.91 'rapidly'
     5. 0.90 'lazily'
     6. 0.90 'uneasily'
     7. 0.89 'warily'


[+] target_word: 'controlled' model: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/c,d15,n30,w3,mc75,s5e-05,t6):
     1. 0.92 'combined'
     2. 0.91 'protected'
     3. 0.91 'exploited'
     4. 0.91 'regulated'
     5. 0.91 'targeted'
     6. 0.90 'marshalled'
     7. 0.90 'concentrated'


[+] target_word: 'carried' model: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/c,d15,n30,w3,mc75,s5e-05,t6):
     1. 0.95 'backed'
     2. 0.93 'ejected'
     3. 0.93 'removed'
     4. 0.92 'retrieved'
     5. 0.92 'thrown'
     6. 0.92 'dropped'
     7. 0.91 'tracked'


[+] target_word: 'franchise' model: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/c,d15,n30,w3,mc75,s5e-05,t6):
     1. 0.95 'tournament'
     2. 0.93 'expos'
     3. 0.93 'airline'
     4. 0.93 'tourney'
     5. 0.93 'league'
     6. 0.93 'viacom'
     7. 0.93 'team'


[+] target_word: 'targets' model: Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/c,d15,n30,w3,mc75,s5e-05,t6):
     1. 0.88 'infiltration'
     2. 0.88 'carriers'
     3. 0.88 'defenses'
     4. 0.87 'weapons'
     5. 0.87 'missiles'
     6. 0.87 'maneuver'
     7. 0.87 'fallout'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-09-29 16:33:07,917 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-29 16:33:08,118 : INFO : capital-common-countries: 9.3% (43/462)
2020-09-29 16:33:08,624 : INFO : capital-world: 6.2% (69/1119)
2020-09-29 16:33:08,684 : INFO : currency: 0.0% (0/128)
2020-09-29 16:33:09,542 : INFO : city-in-state: 2.3% (47/2071)
2020-09-29 16:33:09,743 : INFO : family: 44.2% (168/380)
2020-09-29 16:33:10,157 : INFO : gram1-adjective-to-adverb: 1.7% (17/992)
2020-09-29 16:33:10,480 : INFO : gram2-opposite: 3.8% (25/650)
2020-09-29 16:33:10,985 : INFO : gram3-comparative: 35.4% (471/1332)
2020-09-29 16:33:11,416 : INFO : gram4-superlative: 18.8% (199/1056)
2020-09-29 16:33:11,809 : INFO : gram5-present-participle: 19.0% (188/992)
2020-09-29 16:33:12,476 : INFO : gram6-nationality-adjective: 10.5% (137/1299)
2020-09-29 16:33:13,192 : INFO : gram7-past-tense: 27.8% (433/1560)
2020-09-29 16:33:13,767 : INFO : gram8-plural: 19.2% (228/1190)
2020-09-29 16:33:14,157 : INFO : gram9-plural-verbs: 17.9% (145/812)
2020-09-29 16:33:14,157 : INFO : Quadruplets with out-of-vocabulary words: 28.1%
2020-09-29 16:33:14,158 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 16:33:14,158 : INFO : Total accuracy: 15.5% (2170/14043)
Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/c,d15,n30,w3,mc75,s5e-05,t6): 15.45% correct (2170 of 14043)


[+] questions-words-narrowed.txt
2020-09-29 16:33:14,186 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-09-29 16:33:14,386 : INFO : family: 44.2% (168/380)
2020-09-29 16:33:14,801 : INFO : gram1-adjective-to-adverb: 1.7% (17/992)
2020-09-29 16:33:15,124 : INFO : gram2-opposite: 3.8% (25/650)
2020-09-29 16:33:15,627 : INFO : gram3-comparative: 35.4% (471/1332)
2020-09-29 16:33:16,059 : INFO : gram4-superlative: 18.8% (199/1056)
2020-09-29 16:33:16,451 : INFO : gram5-present-participle: 19.0% (188/992)
2020-09-29 16:33:17,118 : INFO : gram6-nationality-adjective: 10.5% (137/1299)
2020-09-29 16:33:17,835 : INFO : gram7-past-tense: 27.8% (433/1560)
2020-09-29 16:33:18,410 : INFO : gram8-plural: 19.2% (228/1190)
2020-09-29 16:33:18,799 : INFO : gram9-plural-verbs: 17.9% (145/812)
2020-09-29 16:33:18,799 : INFO : Quadruplets with out-of-vocabulary words: 8.2%
2020-09-29 16:33:18,799 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-29 16:33:18,800 : INFO : Total accuracy: 19.6% (2011/10263)
Doc2Vec("ech05,mal0002x20,blogwikgutimdb",dm/c,d15,n30,w3,mc75,s5e-05,t6): 19.59% correct (2011 of 10263)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-29 16:33:18,966 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5594
2020-09-29 16:33:18,966 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5480
2020-09-29 16:33:18,966 : INFO : Pairs with unknown words ratio: 2.0%
((0.5594005657145331, 7.033761543819887e-30), SpearmanrResult(correlation=0.5479517577809883, pvalue=1.6664202496818561e-28), 1.9830028328611897)


02 - simlex999
2020-09-29 16:33:18,995 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3271
2020-09-29 16:33:18,995 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2754
2020-09-29 16:33:18,995 : INFO : Pairs with unknown words ratio: 0.4%
((0.32710414344629485, 3.0447036767736996e-26), SpearmanrResult(correlation=0.2754232515737719, pvalue=8.860693970110708e-19), 0.40040040040040037)


03 - simverb3500
2020-09-29 16:33:19,048 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1697
2020-09-29 16:33:19,048 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1561
2020-09-29 16:33:19,048 : INFO : Pairs with unknown words ratio: 3.8%
((0.16967534428419367, 3.623473963821668e-23), SpearmanrResult(correlation=0.15606615639340018, pvalue=8.362679946626142e-20), 3.8)


     ____________     COMPLETED      ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#

"""
