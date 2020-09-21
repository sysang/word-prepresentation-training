import doc2vec_training_script_rpc_connect as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=40,
        window=3,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=0,
        hs=0,
        epochs=10,
        min_alpha=0.0002,
        alpha=0.0002*20*10,
        comment='ech10,mal0002x20',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
2020-09-20 21:19:39,951 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-20 21:19:39,951 : INFO : Loading a fresh vocabulary
2020-09-20 21:19:40,421 : INFO : effective_min_count=99 retains 61077 unique words (3% of original 1784839, drops 1723762)
2020-09-20 21:19:40,421 : INFO : effective_min_count=99 leaves 328657804 word corpus (97% of original 336075146, drops 7417342)
2020-09-20 21:19:40,562 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-20 21:19:40,597 : INFO : sample=5e-05 downsamples 733 most-common words
2020-09-20 21:19:40,597 : INFO : downsampling leaves estimated 147142569 word corpus (44.8% of prior 328657804)
2020-09-20 21:19:40,714 : INFO : estimated required memory for 61077 words and 15 dimensions: 835267740 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech10_mal0002x20",dm/m,d15,n40,w3,mc99,s5e-05,t8)
Save model to: models/dmm_d15_n40_w3_mc99_s00005_ech10_mal0002x20_thefinal.bin
2020-09-21 15:12:23,781 : INFO : saving Doc2Vec object under models/dmm_d15_n40_w3_mc99_s00005_ech10_mal0002x20_thefinal.bin, separately None
2020-09-21 15:12:23,782 : INFO : storing np array 'vectors_docs_lockf' to models/dmm_d15_n40_w3_mc99_s00005_ech10_mal0002x20_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-21 15:12:23,810 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n40_w3_mc99_s00005_ech10_mal0002x20_thefinal.bin.docvecs.vectors_docs.npy
2020-09-21 15:12:24,251 : INFO : saved models/dmm_d15_n40_w3_mc99_s00005_ech10_mal0002x20_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 5314828
[+] index 5314828 -> "on this his third birthday a day when we should have been rejoicing at the health the strength and beauty of our child we wept together over the ruin of our happiness"
2020-09-21 15:12:24,262 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 100 similarities.


.....get random document, tag: 8826841
[+] index 8826841 -> "a fishery can consist of one man with a small boat hand-casting nets to a huge fleet of trawlers processing tons of fish per day"
    No any match in top 100 similarities.


.....get random document, tag: 12517505
[+] index 12517505 -> "atlantic city new jersey which was perhaps a page out of my fantasy book"
[*] Matched with rank 19, score: 0.9306212067604065!


.....get random document, tag: 2782738
[+] index 2782738 -> "i hardly know which is the worst class in this country the aristocracy the middle class or what they call the people"
    No any match in top 100 similarities.


.....get random document, tag: 5209568
[+] index 5209568 -> "if you have not got them all the beneficiaries you have got in having me i should suppose about the biggest ah what has he done for you nanda asked"
    No any match in top 100 similarities.


.....get random document, tag: 12084999
[+] index 12084999 -> "azizi later gave the conspirators permission to act in the name of al qaeda although it is unclear whether he authorized money or other assistance — or indeed whether al qaeda had much support to offer"
[*] Matched with rank 66, score: 0.8980430960655212!


.....get random document, tag: 6917465
[+] index 6917465 -> "in a cabinet reshuffle but retained the wales portfolio"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (2372002): why is it not more apt to anticipate and provide for reform why does it not cherish its wise minority why does it cry and resist before it is hurt why does it not encourage its citizens to be on the alert to point out its faults and do better than it would have them why does it always crucify christ and excommunicate copernicus and luther and pronounce washington and franklin rebels one would think that a deliberate and practical denial of its authority was the only offence never contemplated by government else why has it not assigned its definite its suitable and proportionate penalty if a man who has no property refuses but once to earn nine shillings for the state he is put in prison for a period unlimited by any law that i know and determined only by the discretion of those who placed him there but if he should steal ninety times nine shillings from the state he is soon permitted to go at large again

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech10_mal0002x20",dm/m,d15,n40,w3,mc99,s5e-05,t8):

MOST (2551359, 0.9564839601516724): «why is it not more apt to anticipate and provide for reform why does it not cherish its wie minority why does it cry and resist before it is hurt why does it not encourage its citizens to put out its faults and do better than it would have them why does it always crucify christ and excommunicate copernicus and luther and pronounce washington and franklin rebels one would think that a deliberate and practical denial of its authority was the only offense never contemplated by its government else why has it not assigned its definite its suitable and proportionate penalty if a man who has no property refuses but once to earn nine shillings for the state he is put in prison for a period unlimited by any law that i know and determined only by the discretion of those who put him there but if he should steal ninety times nine shillings from the state he is soon permitted to go at large again»

MEDIAN (5870101, 0.2582831382751465): «unfortunately where it 's at does not have much else going for it other than the now-dated ruminations on ethics between adults and their kids some quick tanda shots and amusingly jaded satirical bits on the high-stakes world of gambling most of which has been covered by now ad nauseum»

LEAST (7579460, -0.7173686623573303): «embarrass is located at 44°40'15 north 88°42'12 west 44 670716 -88 703361»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'is' model: Doc2Vec("ech10_mal0002x20",dm/m,d15,n40,w3,mc99,s5e-05,t8):
2020-09-21 15:12:50,535 : INFO : precomputing L2-norms of word weight vectors
     1. 0.90 'real'
     2. 0.89 'kind'
     3. 0.87 'esp'
     4. 0.86 'as'
     5. 0.85 'sort'
     6. 0.85 'part'
     7. 0.83 'freak'


[+] target_word: 'reminiscent' model: Doc2Vec("ech10_mal0002x20",dm/m,d15,n40,w3,mc99,s5e-05,t8):
     1. 0.96 'depicts'
     2. 0.95 'typified'
     3. 0.94 'recreated'
     4. 0.94 'pictured'
     5. 0.93 'captures'
     6. 0.92 'morphed'
     7. 0.91 'emblematic'


[+] target_word: 'adorable' model: Doc2Vec("ech10_mal0002x20",dm/m,d15,n40,w3,mc99,s5e-05,t8):
     1. 0.94 'busty'
     2. 0.92 'blonde'
     3. 0.92 'sexy'
     4. 0.92 'dorky'
     5. 0.91 'vamp'
     6. 0.91 'sassy'
     7. 0.89 'slutty'


[+] target_word: 'distracted' model: Doc2Vec("ech10_mal0002x20",dm/m,d15,n40,w3,mc99,s5e-05,t8):
     1. 0.92 'arousing'
     2. 0.91 'upsetting'
     3. 0.91 'intoxicated'
     4. 0.91 'overwhelmed'
     5. 0.91 'oblivious'
     6. 0.90 'unaccustomed'
     7. 0.90 'aroused'


[+] target_word: 'ascend' model: Doc2Vec("ech10_mal0002x20",dm/m,d15,n40,w3,mc99,s5e-05,t8):
     1. 0.94 'descend'
     2. 0.91 'encircle'
     3. 0.89 'ascending'
     4. 0.86 'splits'
     5. 0.86 'descending'
     6. 0.86 'traverse'
     7. 0.85 'converge'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-21 15:12:51,042 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-21 15:12:51,359 : INFO : capital-common-countries: 10.1% (51/506)
2020-09-21 15:12:52,686 : INFO : capital-world: 4.9% (88/1779)
2020-09-21 15:12:52,815 : INFO : currency: 2.2% (4/178)
2020-09-21 15:12:54,776 : INFO : city-in-state: 2.2% (50/2267)
2020-09-21 15:12:55,060 : INFO : family: 39.3% (165/420)
2020-09-21 15:12:55,903 : INFO : gram1-adjective-to-adverb: 1.8% (18/992)
2020-09-21 15:12:56,266 : INFO : gram2-opposite: 3.1% (22/702)
2020-09-21 15:12:57,110 : INFO : gram3-comparative: 21.8% (291/1332)
2020-09-21 15:12:57,754 : INFO : gram4-superlative: 4.0% (42/1056)
2020-09-21 15:12:58,287 : INFO : gram5-present-participle: 23.4% (247/1056)
2020-09-21 15:12:59,200 : INFO : gram6-nationality-adjective: 8.1% (111/1371)
2020-09-21 15:13:00,052 : INFO : gram7-past-tense: 19.2% (300/1560)
2020-09-21 15:13:01,082 : INFO : gram8-plural: 13.4% (179/1332)
2020-09-21 15:13:01,632 : INFO : gram9-plural-verbs: 7.1% (62/870)
2020-09-21 15:13:01,633 : INFO : Quadruplets with out-of-vocabulary words: 21.1%
2020-09-21 15:13:01,633 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-21 15:13:01,633 : INFO : Total accuracy: 10.6% (1630/15421)
Doc2Vec("ech10_mal0002x20",dm/m,d15,n40,w3,mc99,s5e-05,t8): 10.57% correct (1630 of 15421)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-21 15:13:01,905 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5879
2020-09-21 15:13:01,905 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5853
2020-09-21 15:13:01,905 : INFO : Pairs with unknown words ratio: 0.6%
((0.5878956914059905, 5.2575849917703076e-34), SpearmanrResult(correlation=0.5852781114044698, pvalue=1.1953719775428517e-33), 0.56657223796034)


02 - simlex999
2020-09-21 15:13:01,954 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3031
2020-09-21 15:13:01,954 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2569
2020-09-21 15:13:01,954 : INFO : Pairs with unknown words ratio: 0.3%
((0.30314533035894764, 1.2894599706676251e-22), SpearmanrResult(correlation=0.25693280604527996, pvalue=1.7636313872344457e-16), 0.3003003003003003)


03 - simverb3500
2020-09-21 15:13:02,232 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1784
2020-09-21 15:13:02,232 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1613
2020-09-21 15:13:02,232 : INFO : Pairs with unknown words ratio: 1.4%
((0.17838723301713927, 4.473234526125652e-26), SpearmanrResult(correlation=0.16133440149133876, pvalue=1.4545964636348141e-21), 1.3714285714285714)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
s
"""
