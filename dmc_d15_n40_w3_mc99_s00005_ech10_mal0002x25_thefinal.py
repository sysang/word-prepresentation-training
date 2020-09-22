import doc2vec_training_script_multiprocessing as base

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=40,
        window=3,
        min_count=99,
        sample=0.00005,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=10,
        min_alpha=0.0002,
        alpha=0.0002*25*10,
        comment='ech10,mal0002x25',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    base.train(common_kwargs, saved_fname)

"""
2020-09-22 10:22:04,642 : INFO : collected 1784839 word types and 13290000 unique tags from a corpus of 13290000 examples and 336075146 words
2020-09-22 10:22:04,642 : INFO : Loading a fresh vocabulary
2020-09-22 10:22:05,075 : INFO : effective_min_count=99 retains 61077 unique words (3% of original 1784839, drops 1723762)
2020-09-22 10:22:05,075 : INFO : effective_min_count=99 leaves 328657804 word corpus (97% of original 336075146, drops 7417342)
2020-09-22 10:22:05,216 : INFO : deleting the raw counts dictionary of 1784839 items
2020-09-22 10:22:05,253 : INFO : sample=5e-05 downsamples 733 most-common words
2020-09-22 10:22:05,253 : INFO : downsampling leaves estimated 147142569 word corpus (44.8% of prior 328657804)
2020-09-22 10:22:05,363 : INFO : estimated required memory for 61077 words and 15 dimensions: 857255460 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


EXAMINING RESULTS


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


Model details: Doc2Vec("ech10,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6)
Save model to: models/dmc_d15_n40_w3_mc99_s00005_ech10_mal0002x25_thefinal.bin
2020-09-22 12:21:35,584 : INFO : saving Doc2Vec object under models/dmc_d15_n40_w3_mc99_s00005_ech10_mal0002x25_thefinal.bin, separately None
2020-09-22 12:21:35,584 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n40_w3_mc99_s00005_ech10_mal0002x25_thefinal.bin.trainables.vectors_docs_lockf.npy
2020-09-22 12:21:35,612 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n40_w3_mc99_s00005_ech10_mal0002x25_thefinal.bin.docvecs.vectors_docs.npy
2020-09-22 12:21:36,193 : INFO : saved models/dmc_d15_n40_w3_mc99_s00005_ech10_mal0002x25_thefinal.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 6251461
[+] index 6251461 -> "it starts off looking promising with some good death scenes such as a mans head being decapitated with a samurai sword and a woman being stabbed through the neck"
2020-09-22 12:21:36,203 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 100 similarities.


.....get random document, tag: 9132555
[+] index 9132555 -> "these would then be dried in the sun and used for several months"
[*] Matched with rank 1, score: 0.9545280337333679!


.....get random document, tag: 1782165
[+] index 1782165 -> "but again the frost came and made the paths of the sea secure"
[*] Matched with rank 12, score: 0.8879689574241638!


.....get random document, tag: 5695404
[+] index 5695404 -> "one wonders what possessed the people behind the picture to go ahead with rent-a-cop or how they sold it to the studio behind the distribution"
[*] Matched with rank 14, score: 0.9014847278594971!


.....get random document, tag: 9303281
[+] index 9303281 -> "the replacement for microsoft mail starting in the 1997 version of office it includes an e-mail client calendar task manager and address book"
[*] Matched with rank 85, score: 0.8674780130386353!


.....get random document, tag: 7769164
[+] index 7769164 -> "support for conservative causes is often found in the south including resistance to same-sex marriage and abortion while in the past there was major resistance to feminism desegregation the abolition of slavery and interracial marriage"
[*] Matched with rank 1, score: 0.9396144151687622!


.....get random document, tag: 10186307
[+] index 10186307 -> "for example at the tissue level the arterial wall can be modeled as a continuum"
[*] Matched with rank 9, score: 0.9111400842666626!




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (12432583): its almost as though i am standing outside of myself watching the drama

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech10,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6):

MOST (11714189, 0.9339344501495361): «drink from the company toilet eat too many free cookies and vomit on the interviewer 's shoes fart grope the recruiter hire a doppelganger to pretend to be you iron your shirt while you are wearing it jump out the 33rd-floor window kick the interviewer»

MEDIAN (2133854, 0.002334998920559883): «it is this stuff planted in virgin soil and inflated to an immense and buoyant optimism by colossal and unanticipated material prosperity and success»

LEAST (3774105, -0.9341472387313843): «from there a winding path led down to the beach»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'revived' model: Doc2Vec("ech10,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6):
2020-09-22 12:22:01,748 : INFO : precomputing L2-norms of word weight vectors
     1. 0.97 'preceded'
     . 0.94 'resurrected'
     3. 0.94 'rivaled'
     4. 0.94 'encountered'
     5. 0.93 'hailed'
     6. 0.93 'eclipsed'
     7. 0.93 'revealed'


[+] target_word: 'mainly' model: Doc2Vec("ech10,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.94 'mostly'
     2. 0.93 'primarily'
     3. 0.88 'nowadays'
     4. 0.87 'notably'
     5. 0.86 'intensively'
     6. 0.86 'domestically'
     7. 0.85 'especially'


[+] target_word: 'pennsylvania' model: Doc2Vec("ech10,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.98 'maryland'
     2. 0.97 'illinois'
     3. 0.97 'ohio'
     4. 0.97 'ontario'
     5. 0.96 'alabama'
     6. 0.96 'kentucky'
     7. 0.96 'vermont'


[+] target_word: 'mosaic' model: Doc2Vec("ech10,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.96 'mandala'
     2. 0.93 'cuneiform'
     3. 0.92 'mural'
     4. 0.92 'hieroglyphic'
     5. 0.90 'doric'
     6. 0.90 'pottery'
     7. 0.89 'watermark'


[+] target_word: 'menace' model: Doc2Vec("ech10,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6):
     1. 0.91 'mystique'
     2. 0.89 'reaper'
     3. 0.89 'caster'
     4. 0.89 'rage'
     5. 0.88 'fury'
     6. 0.88 'balrog'
     7. 0.88 'frenzy'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------
2020-09-22 12:22:02,296 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-09-22 12:22:02,632 : INFO : capital-common-countries: 7.3% (37/506)
2020-09-22 12:22:03,863 : INFO : capital-world: 4.9% (87/1779)
2020-09-22 12:22:03,982 : INFO : currency: 0.0% (0/178)
2020-09-22 12:22:05,424 : INFO : city-in-state: 2.3% (53/2267)
2020-09-22 12:22:05,725 : INFO : family: 36.2% (152/420)
2020-09-22 12:22:06,333 : INFO : gram1-adjective-to-adverb: 3.6% (36/992)
2020-09-22 12:22:06,700 : INFO : gram2-opposite: 3.7% (26/702)
2020-09-22 12:22:07,377 : INFO : gram3-comparative: 24.3% (324/1332)
2020-09-22 12:22:07,968 : INFO : gram4-superlative: 10.2% (108/1056)
2020-09-22 12:22:08,541 : INFO : gram5-present-participle: 13.8% (146/1056)
2020-09-22 12:22:09,370 : INFO : gram6-nationality-adjective: 9.6% (132/1371)
2020-09-22 12:22:10,344 : INFO : gram7-past-tense: 18.1% (282/1560)
2020-09-22 12:22:11,314 : INFO : gram8-plural: 12.2% (163/1332)
2020-09-22 12:22:11,916 : INFO : gram9-plural-verbs: 9.3% (81/870)
2020-09-22 12:22:11,916 : INFO : Quadruplets with out-of-vocabulary words: 21.1%
2020-09-22 12:22:11,917 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-09-22 12:22:11,917 : INFO : Total accuracy: 10.6% (1627/15421)
Doc2Vec("ech10,mal0002x25",dm/c,d15,n40,w3,mc99,s5e-05,t6): 10.55% correct (1627 of 15421)


-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-09-22 12:22:12,190 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4848
2020-09-22 12:22:12,190 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4762
2020-09-22 12:22:12,191 : INFO : Pairs with unknown words ratio: 0.6%
((0.48480204244230984, 4.328752166457292e-22), SpearmanrResult(correlation=0.4761970108379193, pvalue=2.8760940841244884e-21), 0.56657223796034)


02 - simlex999
2020-09-22 12:22:12,239 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2994
2020-09-22 12:22:12,239 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.2619
2020-09-22 12:22:12,239 : INFO : Pairs with unknown words ratio: 0.3%
((0.2994416992342859, 4.42021846188642e-22), SpearmanrResult(correlation=0.261875641659787, pvalue=4.4148752588693126e-17), 0.3003003003003003)


03 - simverb3500
2020-09-22 12:22:12,518 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1723
2020-09-22 12:22:12,518 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1582
2020-09-22 12:22:12,519 : INFO : Pairs with unknown words ratio: 1.4%
((0.1723124517201282, 2.0514846452748715e-24), SpearmanrResult(correlation=0.15823681941990064, pvalue=8.55071792267485e-21), 1.3714285714285714)


             ____________     COMPLETED          ___________________________
#~~~~~~~~###~~~~~~~~~~~~##~~~~~~~~~~~#~~~~~~~~~~~~~~~##~~~~~~~~~~~~###~~~~~~~~~~~~~#
"""
