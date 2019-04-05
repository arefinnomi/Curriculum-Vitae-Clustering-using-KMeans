from sklearn.feature_extraction.text import CountVectorizer


def get_top_n_words(corpus, n=None):
	"""
	List the top n words in a vocabulary according to occurrence in a text corpus.
	
	get_top_n_words(["I love Python", "Python is a language programming", "Hello world", "I love the world"]) -> 
	[('python', 2),
	 ('world', 2),
	 ('love', 2),
	 ('hello', 1),
	 ('is', 1),
	 ('programming', 1),
	 ('the', 1),
	 ('language', 1)]
	"""
	vec = CountVectorizer().fit(corpus)
	bag_of_words = vec.transform(corpus)
	sum_words = bag_of_words.sum(axis=0)
	words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
	words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
	return words_freq[:n]
