tryit:
	python3 trial_scripts/tryit.py

dump_blog:
	python3 dump_blogcorpus_to_mongodb.py

dump_imdb:
	python3 dump_imdbreviews_to_mongodb.py

dump_enwik8:
	python3 dump_enwik8_to_mongodb.py

dump_enwik9:
	python3 dump_enwik9_to_mongodb.py

dump_gutenberg:
	python3 dump_gutenberg_to_mongodb.py

train:
	python3 $(file) --check-dataset=0 --database=thefinal

check_dataset:
	python3 dmc_d15_n18_w2_mc60_s0001_ech05_thefinal.py --check-dataset=1 --database=enwik8
