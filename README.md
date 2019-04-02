# `Curriculum Vitae Clustering using k-means`

A repository of datasets of curriculum vitaes and an example of clustering curriculum Vitae/resume using k-means. If interest is only on datasets, read this [README.md](https://github.com/arefinnomi/Curriculum-Vitae-Clustering-using-KMeans/tree/master/curriculum_vitae_data) file.

**Requirement:**  
* [scikit-learn](https://scikit-learn.org)
* [nltk](http://www.nltk.org/)
* [textract](https://github.com/deanmalmgren/textract)
* [PyPDF2](https://github.com/mstamy2/PyPDF2)

**Description:**
* `data/word` directory contains the word(.docx) files of Curriculum Vitae.
* `resource/common_cities_state_countries_names.txt` files contains the common cities, states, countries names. The main routine includes the contains of this file as stopwords.
* `resource/human_names.txt` contains common human names. The main routine includes the contains of this file as stopwords.
* `resource/specific_stopwords.txt` contains some user defined stopwords. The main routine includes the contains of this file as stopwords.
* The main routine folderize the docx files of same cluster in a new folder with in `output\` directory . The name of new directory is the first 15 most frequent features of that cluster.
  

**Run:**
* `python main.py` for clustering docx file in `data/word`
* `python clean_resources.py` to remove duplicate words in `resource/human_names.txt` & `resource/common_cities_state_countries_names.txt` files
