import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=15,
        negative=10,
        window=3,
        min_count=99,
        sample=0.001,
        dm=1,
        dm_concat=1,
        hs=0,
        epochs=10,
        min_alpha=0.0002,
        alpha=0.0002*10*10,
        comment='ech10,mal0002x10,refined',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')

    pprint.pprint(common_kwargs)

    base.train(
            common_kwargs=common_kwargs,
            saved_fname=saved_fname,
            evaluate=False,
            database='refined')

"""
2020-10-01 10:31:50,381 : INFO : collected 877734 word types and 46020000 unique tags from a corpus of 46020000 examples and 610836932 words
2020-10-01 10:31:50,381 : INFO : Loading a fresh vocabulary
2020-10-01 10:31:50,636 : INFO : effective_min_count=99 retains 53059 unique words (6% of original 877734, drops 824675)
2020-10-01 10:31:50,637 : INFO : effective_min_count=99 leaves 606131238 word corpus (99% of original 610836932, drops 4705694)
2020-10-01 10:31:50,756 : INFO : deleting the raw counts dictionary of 877734 items
2020-10-01 10:31:50,774 : INFO : sample=0.001 downsamples 47 most-common words
2020-10-01 10:31:50,774 : INFO : downsampling leaves estimated 459319807 word corpus (75.8% of prior 606131238)
2020-10-01 10:31:50,885 : INFO : estimated required memory for 53059 words and 15 dimensions: 2813197820 bytes
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


INFO: Training parameters: {'vector_size': 15, 'negative': 10, 'window': 3, 'min_count': 99, 'sample': 0.001, 'dm': 1, 'dm_concat': 1, 'hs': 0, 'epochs': 10, 'min_alpha': 0.0002, 'alpha': 0.02, 'comment': 'ech10,mal0002x10,refined'}
INFO: Model details: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n10,w3,mc99,s0.001,t6)
INFO: Save model to: models/dmc_d15_n10_w3_mc99_s001_ech10_mal0002x10_refined.bin
2020-10-01 16:22:45,186 : INFO : saving Doc2Vec object under models/dmc_d15_n10_w3_mc99_s001_ech10_mal0002x10_refined.bin, separately None
2020-10-01 16:22:45,186 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n10_w3_mc99_s001_ech10_mal0002x10_refined.bin.trainables.vectors_docs_lockf.npy
2020-10-01 16:22:45,271 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n10_w3_mc99_s001_ech10_mal0002x10_refined.bin.docvecs.vectors_docs.npy
2020-10-01 16:22:46,555 : INFO : saved models/dmc_d15_n10_w3_mc99_s001_ech10_mal0002x10_refined.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 6454755
-> index 6454755 --> "the walnut beside the weird ocean is the printer that behaves globally"
2020-10-01 16:22:46,666 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 22201123
-> index 22201123 --> "he will be opening between thin alice until his cobbler orders actually"
    No any match in top 200 similarities.


.....get random document, tag: 33498546
-> index 33498546 --> "you used the semantical argument that since the have no direct contact info they can not exist"
    No any match in top 200 similarities.


.....get random document, tag: 7761832
-> index 7761832 --> "he will be hating beneath poor chester until his orange shouts totally"
    No any match in top 200 similarities.


.....get random document, tag: 35291634
-> index 35291634 --> "matt has already admitted that he does not know what quotation marks are or how they are used"
    No any match in top 200 similarities.


.....get random document, tag: 22222820
-> index 22222820 --> "i 'd feel the same even if she was not a nurse who actually worked with the guy"
    No any match in top 200 similarities.


.....get random document, tag: 19858071
-> index 19858071 --> "are you man enough to try and back it up"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (23162588): you will not fear me filling for your brave stable

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n10,w3,mc99,s0.001,t6):

MOST (24284250, 0.946395754814148): «the link is gone about godless zionists murdering jews in israel for money»

MEDIAN (7100787, -0.0005648806691169739): «just loving through a raindrop inside the swamp is too difficult for cyrus to attack it»

LEAST (43001098, -0.9437460899353027): «the kidnapping of four american security contractors earlier this month in iraq revived allegations that»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'charity' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n10,w3,mc99,s0.001,t6):
2020-10-01 16:24:16,701 : INFO : precomputing L2-norms of word weight vectors
     1. 0.93 'creditor'
     2. 0.92 'shareholder'
     3. 0.92 'labor'
     4. 0.92 'workforce'
     5. 0.92 'gubmint'
     6. 0.92 'royalty'
     7. 0.91 'coalition'


[+] target_word: 'marked' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n10,w3,mc99,s0.001,t6):
     1. 0.94 'mirrored'
     2. 0.94 'magnified'
     3. 0.94 'shaped'
     4. 0.94 'bridged'
     5. 0.94 'constructed'
     6. 0.93 'graded'
     7. 0.93 'bungled'


[+] target_word: 'crappy' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n10,w3,mc99,s0.001,t6):
     1. 0.97 'crummy'
     2. 0.97 'shitty'
     3. 0.97 'neat'
     4. 0.97 'sucky'
     5. 0.96 'kickass'
     6. 0.96 'wonderful'
     7. 0.96 'fabulous'


[+] target_word: 'shepherd' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n10,w3,mc99,s0.001,t6):
     1. 0.94 'adventurer'
     2. 0.93 'seaman'
     3. 0.92 'lamb'
     4. 0.92 'housewife'
     5. 0.92 'franciscan'
     6. 0.92 'prince'
     7. 0.91 'bandit'


[+] target_word: 'among' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n10,w3,mc99,s0.001,t6):
     1. 0.95 'amoungst'
     2. 0.94 'amoung'
     3. 0.94 'between'
     4. 0.93 'amongst'
     5. 0.92 'including'
     6. 0.91 'involving'
     7. 0.90 'within'


[+] target_word: 'indonesia' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n10,w3,mc99,s0.001,t6):
     1. 0.99 'laos'
     2. 0.99 'malaysia'
     3. 0.98 'liberia'
     4. 0.98 'thailand'
     5. 0.98 'taiwan'
     6. 0.98 'myanmar'
     7. 0.98 'nepal'


[+] target_word: 'notebook' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n10,w3,mc99,s0.001,t6):
     1. 0.97 'toolbox'
     2. 0.97 'camera'
     3. 0.96 'cv'
     4. 0.96 'playlist'
     5. 0.95 'cd'
     6. 0.95 'slideshow'
     7. 0.95 'screensaver'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words.txt
2020-10-01 16:24:18,073 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words.txt
2020-10-01 16:24:18,326 : INFO : capital-common-countries: 4.8% (22/462)
2020-10-01 16:24:18,985 : INFO : capital-world: 1.9% (22/1157)
2020-10-01 16:24:19,092 : INFO : currency: 0.0% (0/178)
2020-10-01 16:24:20,443 : INFO : city-in-state: 0.4% (10/2267)
2020-10-01 16:24:20,720 : INFO : family: 28.1% (118/420)
2020-10-01 16:24:21,240 : INFO : gram1-adjective-to-adverb: 2.3% (23/992)
2020-10-01 16:24:21,702 : INFO : gram2-opposite: 2.1% (16/756)
2020-10-01 16:24:22,410 : INFO : gram3-comparative: 12.8% (171/1332)
2020-10-01 16:24:22,997 : INFO : gram4-superlative: 6.7% (71/1056)
2020-10-01 16:24:23,668 : INFO : gram5-present-participle: 5.6% (59/1056)
2020-10-01 16:24:24,478 : INFO : gram6-nationality-adjective: 2.9% (38/1299)
2020-10-01 16:24:25,473 : INFO : gram7-past-tense: 7.0% (109/1560)
2020-10-01 16:24:26,244 : INFO : gram8-plural: 4.4% (52/1190)
2020-10-01 16:24:26,782 : INFO : gram9-plural-verbs: 13.4% (117/870)
2020-10-01 16:24:26,782 : INFO : Quadruplets with out-of-vocabulary words: 25.3%
2020-10-01 16:24:26,783 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-10-01 16:24:26,783 : INFO : Total accuracy: 5.7% (828/14595)
Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n10,w3,mc99,s0.001,t6): 5.67% correct (828 of 14595)


[+] questions-words-narrowed.txt
2020-10-01 16:24:26,824 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-10-01 16:24:27,108 : INFO : family: 28.1% (118/420)
2020-10-01 16:24:27,631 : INFO : gram1-adjective-to-adverb: 2.3% (23/992)
2020-10-01 16:24:28,093 : INFO : gram2-opposite: 2.1% (16/756)
2020-10-01 16:24:28,820 : INFO : gram3-comparative: 12.8% (171/1332)
2020-10-01 16:24:29,410 : INFO : gram4-superlative: 6.7% (71/1056)
2020-10-01 16:24:30,083 : INFO : gram5-present-participle: 5.6% (59/1056)
2020-10-01 16:24:30,895 : INFO : gram6-nationality-adjective: 2.9% (38/1299)
2020-10-01 16:24:31,890 : INFO : gram7-past-tense: 7.0% (109/1560)
2020-10-01 16:24:32,660 : INFO : gram8-plural: 4.4% (52/1190)
2020-10-01 16:24:33,199 : INFO : gram9-plural-verbs: 13.4% (117/870)
2020-10-01 16:24:33,199 : INFO : Quadruplets with out-of-vocabulary words: 5.8%
2020-10-01 16:24:33,200 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-10-01 16:24:33,200 : INFO : Total accuracy: 7.3% (774/10531)
Doc2Vec("ech10,mal0002x10,refined",dm/c,d15,n10,w3,mc99,s0.001,t6): 7.35% correct (774 of 10531)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-10-01 16:24:33,880 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3853
2020-10-01 16:24:33,880 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.3929
2020-10-01 16:24:33,880 : INFO : Pairs with unknown words ratio: 0.6%
((0.385330909667774, 7.1872648932578e-14), SpearmanrResult(correlation=0.3928574377611104, pvalue=2.115355637706265e-14), 0.56657223796034)


02 - simlex999
2020-10-01 16:24:33,924 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2104
2020-10-01 16:24:33,924 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1880
2020-10-01 16:24:33,924 : INFO : Pairs with unknown words ratio: 0.5%
((0.21040729165584476, 2.077479897167473e-11), SpearmanrResult(correlation=0.1880183751849471, pvalue=2.3194109040833426e-09), 0.5005005005005005)


03 - simverb3500
2020-10-01 16:24:34,610 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1221
2020-10-01 16:24:34,610 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1187
2020-10-01 16:24:34,610 : INFO : Pairs with unknown words ratio: 0.5%
((0.12207617133237657, 4.901957214074665e-13), SpearmanrResult(correlation=0.11870748617887178, pvalue=2.1088355792102298e-12), 0.5142857142857142)

"""
