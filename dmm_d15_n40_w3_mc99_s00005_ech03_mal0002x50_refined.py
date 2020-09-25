import doc2vec_training_script_multiprocessing as base
import pprint

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
        epochs=3,
        min_alpha=0.0002,
        alpha=0.0002*50*3,
        comment='ech05,mal0002x20,refined',
    )

    saved_fname = 'models/' + __file__.replace('.py', '.bin')
    pprint.pprint(common_kwargs)

    base.train(
            common_kwargs=common_kwargs,
            saved_fname=saved_fname,
            evaluate=False,
            database='refined')

"""
2020-09-25 19:16:00,801 : INFO : collected 877734 word types and 46020000 unique tags from a corpus of 46020000 examples and 610836932 words
2020-09-25 19:16:00,801 : INFO : Loading a fresh vocabulary
2020-09-25 19:16:01,050 : INFO : effective_min_count=99 retains 53059 unique words (6% of original 877734, drops 824675)
2020-09-25 19:16:01,050 : INFO : effective_min_count=99 leaves 606131238 word corpus (99% of original 610836932, drops 4705694)
2020-09-25 19:16:01,170 : INFO : deleting the raw counts dictionary of 877734 items
2020-09-25 19:16:01,187 : INFO : sample=5e-05 downsamples 822 most-common words
2020-09-25 19:16:01,187 : INFO : downsampling leaves estimated 265856440 word corpus (43.9% of prior 606131238)
2020-09-25 19:16:01,272 : INFO : estimated required memory for 53059 words and 15 dimensions: 2794096580 bytes

"""
