import os
import re
import shutil

import textract
from nltk import SnowballStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer


def load_word(_file_path=""):
    if _file_path == "":
        return []
    _file = open(_file_path, 'r')
    _text = _file.read()
    _file.close()
    _words = word_tokenize(_text)
    return _words


# setting values

input_dir_path = "curriculum_vitae_data/word/"
output_dir_path = "output/"
names_file_path = 'resource/human_names.txt'
cities_names_file_path = 'resource/common_cities_state_countries_names.txt'
specific_stopwords_file_path = "resource/specific_stopwords.txt"

tokenizer = '[a-zA-Z\']+'
punctuation = ['.', ',', '\"', '\'', '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '%']

# load all files(pdf/word files, names, specific stopwords)

human_names = load_word(names_file_path)
cities_names = load_word(cities_names_file_path)
remove_keywords = load_word(specific_stopwords_file_path)
filenames = os.listdir(input_dir_path)
docs = [textract.process(input_dir_path + filename) for filename in filenames]

# preprocessing

temp = [re.sub(r'\b\w{1,2}\b', '', doc) for doc in docs]
docs = temp
unicode_docs = [unicode(doc, 'utf-8') for doc in docs]
stop_words = text.ENGLISH_STOP_WORDS.union(punctuation)
stop_words = stop_words.union(remove_keywords)
stop_words = stop_words.union(human_names)
stop_words = stop_words.union(cities_names)
stop_words = frozenset([unicode(_word, 'utf-8') for _word in stop_words])
stop_words = stop_words.union(stopwords.words('english'))

stemmer = SnowballStemmer('english', ignore_stopwords=False)


class StemmedTfidfVectorizer(TfidfVectorizer):

    def __init__(self, _stemmer, *args, **kwargs):
        super(StemmedTfidfVectorizer, self).__init__(*args, **kwargs)
        self.stemmer = _stemmer

    def build_analyzer(self):
        analyzer = super(StemmedTfidfVectorizer, self).build_analyzer()
        return lambda _doc: (self.stemmer.stem(word) for word in analyzer(_doc.replace('\n', ' ')))


# TF-IDF, features extraction

vectorizer = StemmedTfidfVectorizer(_stemmer=stemmer, stop_words=stop_words, token_pattern=tokenizer)
X = vectorizer.fit_transform(unicode_docs)
word_features = vectorizer.get_feature_names()

# clustering

km = KMeans(n_clusters=50, init='k-means++', max_iter=1000, n_init=1)
km.fit(X)

# output generation

output_subdir_names = []
common_words = km.cluster_centers_.argsort()[:, -1:-15:-1]
for num, centroid in enumerate(common_words):
    output_subdir_names.append(', '.join(word_features[word] for word in centroid))

output_subdir_paths = [output_dir_path + _output_subdir_name for _output_subdir_name in output_subdir_names]

if os.path.exists(output_dir_path):
    shutil.rmtree(output_dir_path)
os.mkdir(output_dir_path)

for _output_subdir_path in output_subdir_paths:
    if not os.path.exists(_output_subdir_path):
        os.makedirs(_output_subdir_path)

for index, label in enumerate(km.labels_):
    shutil.copy(input_dir_path + filenames[index], output_subdir_paths[label])
