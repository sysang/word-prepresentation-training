import doc2vec_training_script_multiprocessing as base
import pprint

if __name__ == '__main__':
    common_kwargs = dict(
        vector_size=50,
        negative=67,
        window=5,
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
                database='refined'
            )

"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


        EXAMINING THE MODEL


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


INFO: Training parameters: {'vector_size': 50, 'negative': 67, 'window': 5, 'min_count': 99, 'sample': 0.001, 'dm': 1, 'dm_concat': 1, 'hs': 0, 'epochs': 10, 'min_alpha': 0.0002, 'alpha': 0.02, 'comment': 'ech10,mal0002x10,refined'}
INFO: Model details: Doc2Vec("ech10,mal0002x10,refined",dm/c,d50,n67,w5,mc99,s0.001,t6)
INFO: Save model to: models/dmc_d50_n67_w5_mc99_s001_ech10_mal0002x20_refined.bin
2020-10-03 23:53:24,768 : INFO : saving Doc2Vec object under models/dmc_d50_n67_w5_mc99_s001_ech10_mal0002x20_refined.bin, separately None
2020-10-03 23:53:24,768 : INFO : storing np array 'syn1neg' to models/dmc_d50_n67_w5_mc99_s001_ech10_mal0002x20_refined.bin.trainables.syn1neg.npy
2020-10-03 23:53:24,821 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d50_n67_w5_mc99_s001_ech10_mal0002x20_refined.bin.trainables.vectors_docs_lockf.npy
2020-10-03 23:53:24,894 : INFO : storing np array 'vectors_docs' to models/dmc_d50_n67_w5_mc99_s001_ech10_mal0002x20_refined.bin.docvecs.vectors_docs.npy
2020-10-03 23:53:46,619 : INFO : saved models/dmc_d50_n67_w5_mc99_s001_ech10_mal0002x20_refined.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 25661744
-> index 25661744 --> "i am saying english internationals perform at a level similar to most of their foreign team mates"
2020-10-03 23:53:46,634 : INFO : precomputing L2-norms of doc weight vectors
[*] Matched with rank 1, score: 0.7265260815620422!


.....get random document, tag: 10506865
-> index 10506865 --> "this either it does or it does not criterion has nothing to do with any negative statements"
[*] Matched with rank 1, score: 0.8288900256156921!


.....get random document, tag: 29289685
-> index 29289685 --> "and we see that you are the one escalating"
[*] Matched with rank 6, score: 0.6667473912239075!


.....get random document, tag: 26920110
-> index 26920110 --> "they have both tried to learn thai but found it a hard slog and have more or less given up"
[*] Matched with rank 1, score: 0.7357141375541687!


.....get random document, tag: 6646652
-> index 6646652 --> "lots of ugly polite boat attempts lentils for pearl 's quiet cup"
[*] Matched with rank 56, score: 0.6275023818016052!


.....get random document, tag: 16737328
-> index 16737328 --> "the truth remains the truth no matter how often it 's said"
[*] Matched with rank 39, score: 0.6302719116210938!


.....get random document, tag: 31508176
-> index 31508176 --> "mama broke down soon after papa was lost at sea and let go completely within a year"
[*] Matched with rank 1, score: 0.6528560519218445!




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (7177758): please include your resume in an attached word document

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech10,mal0002x10,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):

MOST (8827313, 0.7318605780601501): «please include your resume in an attached word document»

MEDIAN (11154945, 0.0013265088200569153): «my husband has always maintained that pumpkins are inedible and only fit for table decorations»

LEAST (4083828, -0.6997148394584656): «the solution is making patent and copyright like mining law»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'therapist' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):
2020-10-03 23:56:07,595 : INFO : precomputing L2-norms of word weight vectors
     1. 0.92 'psychiatrist'
     2. 0.88 'nurse'
     3. 0.88 'counselor'
     4. 0.87 'neurologist'
     5. 0.86 'cardiologist'
     6. 0.86 'nutritionist'
     7. 0.85 'chiropractor'


[+] target_word: 'handling' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):
     1. 0.76 'administering'
     2. 0.75 'approving'
     3. 0.75 'purchasing'
     4. 0.74 'executing'
     5. 0.74 'releasing'
     6. 0.73 'installing'
     7. 0.73 'updating'


[+] target_word: 'whole' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):
     1. 0.79 'entire'
     2. 0.65 'main'
     3. 0.64 'longest'
     4. 0.62 'looooong'
     5. 0.62 'tremendous'
     6. 0.62 'unipolar'
     7. 0.61 'fledgling'


[+] target_word: 'confirm' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):
     1. 0.86 'verify'
     2. 0.81 'corroborate'
     3. 0.80 'indicate'
     4. 0.79 'clarify'
     5. 0.79 'illustrate'
     6. 0.78 'emphasize'
     7. 0.77 'infer'


[+] target_word: 'slide' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):
     1. 0.89 'bounce'
     2. 0.88 'slip'
     3. 0.84 'sweep'
     4. 0.83 'float'
     5. 0.79 'flush'
     6. 0.79 'snap'
     7. 0.79 'push'


[+] target_word: 'automotive' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):
     1. 0.86 'auto'
     2. 0.86 'aerospace'
     3. 0.82 'semiconductor'
     4. 0.79 'avionics'
     5. 0.79 'automobile'
     6. 0.79 'aeronautical'
     7. 0.78 'pharmaceutical'


[+] target_word: 'airport' model: Doc2Vec("ech10,mal0002x10,refined",dm/c,d50,n67,w5,mc99,s0.001,t6):
     1. 0.80 'pier'
     2. 0.79 'hotel'
     3. 0.79 'ferry'
     4. 0.79 'airfield'
     5. 0.78 'clinic'
     6. 0.78 'heathrow'
     7. 0.76 'inn'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words-narrowed.txt
2020-10-03 23:56:09,574 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-10-03 23:56:09,854 : INFO : family: 40.7% (171/420)
2020-10-03 23:56:10,463 : INFO : gram1-adjective-to-adverb: 6.1% (61/992)
2020-10-03 23:56:10,949 : INFO : gram2-opposite: 12.3% (93/756)
2020-10-03 23:56:11,750 : INFO : gram3-comparative: 28.3% (377/1332)
2020-10-03 23:56:12,275 : INFO : gram4-superlative: 24.0% (253/1056)
2020-10-03 23:56:12,962 : INFO : gram5-present-participle: 47.7% (504/1056)
2020-10-03 23:56:13,596 : INFO : gram6-nationality-adjective: 20.2% (262/1299)
2020-10-03 23:56:14,544 : INFO : gram7-past-tense: 42.2% (658/1560)
2020-10-03 23:56:15,298 : INFO : gram8-plural: 39.2% (467/1190)
2020-10-03 23:56:15,811 : INFO : gram9-plural-verbs: 53.4% (465/870)
2020-10-03 23:56:15,812 : INFO : Quadruplets with out-of-vocabulary words: 5.8%
2020-10-03 23:56:15,812 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-10-03 23:56:15,812 : INFO : Total accuracy: 31.4% (3311/10531)
Doc2Vec("ech10,mal0002x10,refined",dm/c,d50,n67,w5,mc99,s0.001,t6): 31.44% correct (3311 of 10531)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-10-03 23:56:15,875 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.4774
2020-10-03 23:56:15,875 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.4932
2020-10-03 23:56:15,875 : INFO : Pairs with unknown words ratio: 0.6%
((0.47744502280222334, 2.192589160534176e-21), SpearmanrResult(correlation=0.49317979451404675, pvalue=6.501504902920139e-23), 0.56657223796034)


02 - simlex999
2020-10-03 23:56:16,544 : INFO : Pearson correlation coefficient against simlex999.txt: 0.3360
2020-10-03 23:56:16,544 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.3358
2020-10-03 23:56:16,544 : INFO : Pairs with unknown words ratio: 0.5%
((0.33603308993672665, 1.158233794365907e-27), SpearmanrResult(correlation=0.33577038220029104, pvalue=1.2793293765184893e-27), 0.5005005005005005)


03 - simverb3500
2020-10-03 23:56:16,617 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.2721
2020-10-03 23:56:16,617 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.2651
2020-10-03 23:56:16,617 : INFO : Pairs with unknown words ratio: 0.5%
((0.2721249798823769, 3.593202231071627e-60), SpearmanrResult(correlation=0.26512775380674736, pvalue=4.250775297781745e-57), 0.5142857142857142)


-----------------------------------------------------
Assess stability of inferencing vector
-----------------------------------------------------

"""
