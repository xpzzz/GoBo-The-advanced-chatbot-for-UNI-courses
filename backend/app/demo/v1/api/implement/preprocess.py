from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import re
from nltk.stem.snowball import SnowballStemmer

def preData(str):
    stop_words = set(stopwords.words('english'))
    # stop_words.add('python')
    # stop_words.add('i')
    word_tokens = word_tokenize(str)
    print(word_tokens)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    stemmer = SnowballStemmer("english")
    stemmer.stem("and")
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(' '.join(filtered_sentence)) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]

    return stems



