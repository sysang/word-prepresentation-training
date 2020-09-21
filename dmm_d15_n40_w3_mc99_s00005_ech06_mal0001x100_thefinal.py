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
        epochs=6,
        min_alpha=0.0001,
        alpha=0.0001*100*6,
        comment='ech06,mal0001x100',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
2020-09-21 15:28:26,400 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-21 15:28:26,400 : INFO : Loading a fresh vocabulary
2020-09-21 15:28:26,846 : INFO : effective_min_count=99 retains 61077 unique words (3% of original 1784839, drops 1723762)
2020-09-21 15:28:26,846 : INFO : effective_min_count=99 leaves 328657804 word corpus (97% of original 336075146, drops 7417342)
2020-09-21 15:28:26,992 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-21 15:28:27,029 : INFO : sample=5e-05 downsamples 733 most-common words
2020-09-21 15:28:27,029 : INFO : downsampling leaves estimated 147142569 word corpus (44.8% of prior 328657804)
2020-09-21 15:28:27,177 : INFO : estimated required memory for 61077 words and 15 dimensions: 835267740 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech06,mal0001x100",dm/m,d15,n40,w3,mc99,s5e-05,t8)
Save model to: models/dmm_d15_n40_w3_mc99_s00005_ech06_mal0001x100_thefinal.bin
2020-09-21 17:50:17,084 : INFO : saving Doc2Vec object under models/dmm_d15_n40_w3_mc99_s00005_ech06_mal0001x100_thefinal.bin, separately None
2020-09-21 17:50:17,085 : INFO : storing np array 'vectors_docs_lockf' to models/dmm_d15_n40_w3_mc99_s00005_ech06_mal0001x100_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-21 17:50:17,116 : INFO : storing np array 'vectors_docs' to models/dmm_d15_n40_w3_mc99_s00005_ech06_mal0001x100_thefinal.bin.docvecs.vectors_docs.npy
2020-09-21 17:50:17,539 : INFO : saved models/dmm_d15_n40_w3_mc99_s00005_ech06_mal0001x100_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 8765270
[+] index 8765270 -> "western armenian is conservative retaining three conjugations a e and i"
2020-09-21 17:50:17,553 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 100 similarities.


.....get random document, tag: 12507195
[+] index 12507195 -> "she is expecting a detailed letter with photographs decribing the concert"
    No any match in top 100 similarities.


.....get random document, tag: 11673285
[+] index 11673285 -> "plus it was not sunday most of the times these random visits occured"
    No any match in top 100 similarities.


.....get random document, tag: 3800498
[+] index 3800498 -> "perros perros ingleses lepero lepero she cried in exultation as they thrust her over into the boat"
    No any match in top 100 similarities.


.....get random document, tag: 1702061
[+] index 1702061 -> "my labors in regard to vines bushes and all that sort of thing were generally carried on under direction of mrs"
    No any match in top 100 similarities.


.....get random document, tag: 5609343
[+] index 5609343 -> "we may know it in short either by specific experience or on the evidence of our general knowledge of nature"
    No any match in top 100 similarities.


.....get random document, tag: 1554666
[+] index 1554666 -> "the smoke of my own breath echoes ripples buzz 'd whispers love-root silk-thread crotch and vine my respiration and inspiration the beating of my heart the passing of blood and air through my lungs the sniff of green leaves and dry leaves and of the shore and dark-color'd sea-rocks and of hay in the barn the sound of the belch 'd words of my voice loos 'd to the eddies of the wind a few light kisses a few embraces a reaching around of arms the play of shine and shade on the trees as the supple boughs wag the delight alone or in the rush of the streets or along the fields and hill-sides the feeling of health the full-noon trill the song of me rising from bed and meeting the sun"
    No any match in top 100 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (621140): and now my friends i should like to think that there is some piece of advice i might give you some thought some noble saying over which you might ponder in my absence

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x40",dm/m,d15,n40,w3,mc99,s5e-05,t8):

MOST (10415234, 0.9788477420806885): «this requires a program called hello which you can download for free»

MEDIAN (5151544, 0.6692428588867188): «it 's a beautiful day there will be a great crowd»

LEAST (7759103, -0.8524259924888611): «pittsburg is located at 34°42'46 north 95°51'4 west 34 712769 -95 850993»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'begged' model: Doc2Vec("ech06,mal0001x100",dm/m,d15,n40,w3,mc99,s5e-05,t8):
2020-09-21 17:50:43,293 : INFO : precomputing L2-norms of word weight vector
     1. 0.89 'implored'
     2. 0.86 'besought'
     3. 0.85 'entreated'
     4. 0.85 'begging'
     5. 0.84 'beg'
     6. 0.84 'bidden'
     7. 0.81 "'pray"


[+] target_word: 'hunger' model: Doc2Vec("ech06,mal0001x100",dm/m,d15,n40,w3,mc99,s5e-05,t8):
     1. 0.94 'thirst'
     2. 0.90 'famine'
     3. 0.89 'starvation'
     4. 0.89 'fevers'
     5. 0.86 'penury'
     6. 0.86 'pestilence'
     7. 0.86 'bloodshed'


[+] target_word: 'stance' model: Doc2Vec("ech06,mal0001x100",dm/m,d15,n40,w3,mc99,s5e-05,t8):
     1. 0.94 'opposition'
     2. 0.92 'opponents'
     3. 0.92 'leadership'
     4. 0.91 'ideologically'
     5. 0.91 'leanings'
     6. 0.91 'ideology'
     7. 0.91 'stances'


[+] target_word: 'police' model: Doc2Vec("ech05,mal0002x40",dm/m,d15,n40,w3,mc99,s5e-05,t8):
     1. 0.93 'stasi'
     2. 0.92 'gestapo'
     3. 0.91 'lapd'
     4. 0.91 'detectives'
     5. 0.90 'japson'
     6. 0.90 'kgb'
     7. 0.88 'fbi'


[+] target_word: 'converse' model: Doc2Vec("ech05,mal0002x40",dm/m,d15,n40,w3,mc99,s5e-05,t8):
     1. 0.85 'denominational'
     2. 0.81 'deviate'
     3. 0.79 'intelligible'
     4. 0.79 'viewpoints'
     5. 0.79 'minded'
     6. 0.79 'open-minded'
     7. 0.78 'genders'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-21 17:50:43,902 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-21 17:50:44,196 : INFO : capital-common-countries: 9.9% (50/506)
2020-09-21 17:50:45,429 : INFO : capital-world: 5.6% (99/1779)
2020-09-21 17:50:45,549 : INFO : currency: 1.1% (2/178)
2020-09-21 17:50:47,264 : INFO : city-in-state: 1.7% (39/2267)
2020-09-21 17:50:47,564 : INFO : family: 36.4% (153/420)
2020-09-21 17:50:48,113 : INFO : gram1-adjective-to-adverb: 1.1% (11/992)
2020-09-21 17:50:48,472 : INFO : gram2-opposite: 2.7% (19/702)
2020-09-21 17:50:49,362 : INFO : gram3-comparative: 20.0% (267/1332)
2020-09-21 17:50:49,941 : INFO : gram4-superlative: 4.5% (48/1056)
2020-09-21 17:50:50,582 : INFO : gram5-present-participle: 21.2% (224/1056)
2020-09-21 17:50:51,579 : INFO : gram6-nationality-adjective: 8.9% (122/1371)
2020-09-21 17:50:52,514 : INFO : gram7-past-tense: 20.3% (316/1560)
2020-09-21 17:50:53,474 : INFO : gram8-plural: 15.6% (208/1332)
2020-09-21 17:50:53,970 : INFO : gram9-plural-verbs: 7.1% (62/870)
2020-09-21 17:50:53,970 : INFO : Quadruplets with out-of-vocabulary words: 21.1%
2020-09-21 17:50:53,971 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-21 17:50:53,971 : INFO : Total accuracy: 10.5% (1620/15421)
Doc2Vec("ech06,mal0001x100",dm/m,d15,n40,w3,mc99,s5e-05,t8): 10.51% correct (1620 of 15421)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-21 17:50:54,248 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.5873
2020-09-21 17:50:54,248 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.5911
2020-09-21 17:50:54,248 : INFO : Pairs with unknown words ratio: 0.6%
((0.5873001392077322, 6.3420731660211515e-34), SpearmanrResult(correlation=0.5911474803783956, pvalue=1.875439250828364e-34), 0.56657223796034)


02 - simlex999
2020-09-21 17:50:54,299 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3037
2020-09-21 17:50:54,299 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2679
2020-09-21 17:50:54,299 : INFO : Pairs with unknown words ratio: 0.3%
((0.30370748314797535, 1.0678720704373015e-22), SpearmanrResult(correlation=0.26788973621613005, pvalue=7.865575819958256e-18), 0.3003003003003003)


03 - simverb3500
2020-09-21 17:50:54,581 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1782
2020-09-21 17:50:54,581 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1637
2020-09-21 17:50:54,581 : INFO : Pairs with unknown words ratio: 1.4%
((0.17817758970820138, 5.116376037634959e-26), SpearmanrResult(correlation=0.16367409937735114, pvalue=3.7281319338320747e-22), 1.3714285714285714)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
