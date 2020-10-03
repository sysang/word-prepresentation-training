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
        epochs=5,
        min_alpha=0.0002,
        alpha=0.0002*20*5,
        comment='ech05,mal0002x20,refined',
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


INFO: Training parameters: {'vector_size': 15, 'negative': 67, 'window': 5, 'min_count': 99, 'sample': 0.001, 'dm': 1, 'dm_concat': 1, 'hs': 0, 'epochs': 5, 'min_alpha': 0.0002, 'alpha': 0.02, 'comment': 'ech05,mal0002x20,refined'}
INFO: Model details: Doc2Vec("ech05,mal0002x20,refined",dm/c,d15,n67,w5,mc99,s0.001,t6)
INFO: Save model to: models/dmc_d15_n67_w5_mc99_s001_ech05_mal0002x20_refined.bin
2020-10-02 20:25:32,947 : INFO : saving Doc2Vec object under models/dmc_d15_n67_w5_mc99_s001_ech05_mal0002x20_refined.bin, separately None
2020-10-02 20:25:32,947 : INFO : storing np array 'vectors_docs_lockf' to models/dmc_d15_n67_w5_mc99_s001_ech05_mal0002x20_refined.bin.trainables.vectors_docs_lockf.npy
2020-10-02 20:25:33,026 : INFO : storing np array 'vectors_docs' to models/dmc_d15_n67_w5_mc99_s001_ech05_mal0002x20_refined.bin.docvecs.vectors_docs.npy
2020-10-02 20:25:34,409 : INFO : saved models/dmc_d15_n67_w5_mc99_s001_ech05_mal0002x20_refined.bin


-----------------------------------------------------
Are inferred vectors close to the precalculated ones?
-----------------------------------------------------
.....get random document, tag: 11993573
-> index 11993573 --> "hardly any good lazy exit departs eggs above ken 's rude enigma"
2020-10-02 20:25:34,420 : INFO : precomputing L2-norms of doc weight vectors
    No any match in top 200 similarities.


.....get random document, tag: 18149612
-> index 18149612 --> "does it make sense just to go ahead and declare every field non nullable"
    No any match in top 200 similarities.


.....get random document, tag: 42869474
-> index 42869474 --> "these differences are detectable with fmri and may have clinical utility"
    No any match in top 200 similarities.


.....get random document, tag: 15480520
-> index 15480520 --> "she 'd rather shout neatly than receive with lionel 's shallow dust"
    No any match in top 200 similarities.


.....get random document, tag: 76041
-> index 76041 --> "i just do not think you are a good one"
    No any match in top 200 similarities.


.....get random document, tag: 10704758
-> index 10704758 --> "a scholarship for students from northern virginia is named in his honor"
    No any match in top 200 similarities.


.....get random document, tag: 26142432
-> index 26142432 --> "can you give me a clue as to what i am jealous of"
    No any match in top 200 similarities.




-----------------------------------------------------
Do close documents seem more related than distant ones?
-----------------------------------------------------
TARGET (9402117): but i remember one particular spring day when dh came home from work

SIMILAR/DISSIMILAR DOCS PER MODEL Doc2Vec("ech05,mal0002x20,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):

MOST (18294931, 0.948215901851654): «they globally expect behind eliza when the strange sauces solve beside the thin office»

MEDIAN (3582859, -0.0014746934175491333): «i mould eerily if claude 's film is not polite»

LEAST (26049273, -0.9308178424835205): «the action of satanic bushite bombers targeting samara as war criminals is fully documented»



-----------------------------------------------------
Do the word vectors show useful similarities?
-----------------------------------------------------
[+] target_word: 'mickey' model: Doc2Vec("ech05,mal0002x20,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
2020-10-02 20:27:04,375 : INFO : precomputing L2-norms of word weight vectors
     1. 0.94 'minnie'
     2. 0.94 'fatboy'
     3. 0.93 'micky'
     4. 0.93 'rosemary'
     5. 0.93 'jack'
     6. 0.92 'gerber'
     7. 0.92 'tee'


[+] target_word: 'space' model: Doc2Vec("ech05,mal0002x20,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.96 'generator'
     2. 0.96 'payload'
     3. 0.96 'grid'
     4. 0.95 'hotspot'
     5. 0.95 'chassis'
     6. 0.95 'bracket'
     7. 0.94 'tempo'


[+] target_word: 'solves' model: Doc2Vec("ech05,mal0002x20,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.99 'recommends'
     2. 0.99 'joins'
     3. 0.99 'grasps'
     4. 0.99 'receives'
     5. 0.99 'fills'
     6. 0.99 'pours'
     7. 0.99 'departs'


[+] target_word: 'captives' model: Doc2Vec("ech05,mal0002x20,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.98 'soldiers'
     2. 0.97 'detainees'
     3. 0.97 'prisoners'
     4. 0.97 'pows'
     5. 0.97 'attackers'
     6. 0.97 'kidnappers'
     7. 0.97 'runaways'


[+] target_word: '1990s' model: Doc2Vec("ech05,mal0002x20,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.99 '1960s'
     2. 0.98 '1970s'
     3. 0.98 '1950s'
     4. 0.98 'september'
     5. 0.98 'december'
     6. 0.98 '1800s'
     7. 0.97 '1920s'


[+] target_word: 'disapproval' model: Doc2Vec("ech05,mal0002x20,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.97 'faithfulness'
     2. 0.96 'condemnation'
     3. 0.96 'acquiescence'
     4. 0.96 'acceptance'
     5. 0.94 'loyalty'
     6. 0.94 'trustworthiness'
     7. 0.93 'rejection'


[+] target_word: 'prevents' model: Doc2Vec("ech05,mal0002x20,refined",dm/c,d15,n67,w5,mc99,s0.001,t6):
     1. 0.94 'corrects'
     2. 0.94 'removes'
     3. 0.94 'renders'
     4. 0.93 'corrupts'
     5. 0.93 'disallows'
     6. 0.93 'eliminates'
     7. 0.93 'disables'




-----------------------------------------------------
Are the word vectors from this dataset any good at analogies?
-----------------------------------------------------


[+] questions-words-narrowed.txt
2020-10-02 20:27:05,801 : INFO : Evaluating word analogies for top 300000 words in the model on questions-words-narrowed.txt
2020-10-02 20:27:06,080 : INFO : family: 19.0% (80/420)
2020-10-02 20:27:06,661 : INFO : gram1-adjective-to-adverb: 1.5% (15/992)
2020-10-02 20:27:07,196 : INFO : gram2-opposite: 1.7% (13/756)
2020-10-02 20:27:07,897 : INFO : gram3-comparative: 14.0% (187/1332)
2020-10-02 20:27:08,545 : INFO : gram4-superlative: 4.5% (47/1056)
2020-10-02 20:27:09,260 : INFO : gram5-present-participle: 4.7% (50/1056)
2020-10-02 20:27:10,175 : INFO : gram6-nationality-adjective: 2.6% (34/1299)
2020-10-02 20:27:11,248 : INFO : gram7-past-tense: 4.4% (68/1560)
2020-10-02 20:27:12,244 : INFO : gram8-plural: 4.9% (58/1190)
2020-10-02 20:27:13,103 : INFO : gram9-plural-verbs: 9.7% (84/870)
2020-10-02 20:27:13,103 : INFO : Quadruplets with out-of-vocabulary words: 5.8%
2020-10-02 20:27:13,103 : INFO : NB: analogies containing OOV words were skipped from evaluation! To change this behavior, use "dummy4unknown=True"
2020-10-02 20:27:13,103 : INFO : Total accuracy: 6.0% (636/10531)
Doc2Vec("ech05,mal0002x20,refined",dm/c,d15,n67,w5,mc99,s0.001,t6): 6.04% correct (636 of 10531)




-----------------------------------------------------
Benchmark against analogies metric baseline
-----------------------------------------------------


01 - wordsim353
2020-10-02 20:27:13,150 : INFO : Pearson correlation coefficient against wordsim353.tsv: 0.3916
2020-10-02 20:27:13,150 : INFO : Spearman rank-order correlation coefficient against wordsim353.tsv: 0.3966
2020-10-02 20:27:13,150 : INFO : Pairs with unknown words ratio: 0.6%
((0.39162917432743516, 2.5881936393509143e-14), SpearmanrResult(correlation=0.39655408178966756, pvalue=1.14680364908508e-14), 0.56657223796034)


02 - simlex999
2020-10-02 20:27:13,814 : INFO : Pearson correlation coefficient against simlex999.txt: 0.2059
2020-10-02 20:27:13,814 : INFO : Spearman rank-order correlation coefficient against simlex999.txt: 0.1850
2020-10-02 20:27:13,815 : INFO : Pairs with unknown words ratio: 0.5%
((0.20593789057677536, 5.56503125081292e-11), SpearmanrResult(correlation=0.1849783153727827, pvalue=4.2185018771766224e-09), 0.5005005005005005)


03 - simverb3500
2020-10-02 20:27:13,879 : INFO : Pearson correlation coefficient against simverb3500_DGerz.txt: 0.1334
2020-10-02 20:27:13,879 : INFO : Spearman rank-order correlation coefficient against simverb3500_DGerz.txt: 0.1376
2020-10-02 20:27:13,879 : INFO : Pairs with unknown words ratio: 0.5%
((0.13338669729526192, 2.7126830803554844e-15), SpearmanrResult(correlation=0.13763528325942004, pvalue=3.4179865873642853e-16), 0.5142857142857142)

"""
