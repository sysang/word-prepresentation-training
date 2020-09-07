dump_blog:
	python dump_blogcorpus_to_mongodb.py

dump_imdb:
	python dump_imdbreviews_to_mongodb.py

dump_enwik8:
	python dump_enwik8_to_mongodb.py

dump_all: dump_blog dump_imdb dump_enwik
