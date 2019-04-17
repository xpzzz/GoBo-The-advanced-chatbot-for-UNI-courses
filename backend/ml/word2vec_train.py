from __future__ import absolute_import
import os
import gensim
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import nltk
import re

def preprocess():
    fp = open('python.json','rb')
    content = fp.read().decode('utf-8')
    with  open(r'python.json', 'r',encoding='utf-8',) as f:
        lines = f.readlines()

    with open('synopses.txt','w') as f_titile:
        for line in lines:
            text = json.loads(line)
            # print(text)
            title=text['title']
            # print(title)
            f_titile.write(str(title).lower()+'\n')

    stop_words = set(stopwords.words('english'))
    stop_words.add('python')
    stop_words.add('i')
    print(stop_words)

    with  open(r'synopses.txt', 'r', encoding='utf-8', ) as f:
        lines = f.readlines()
    f = open('stopword.txt', 'w')
    for line in lines:
        word_tokens = word_tokenize(line)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = []

        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)

    # print(word_tokens)
    # print(filtered_sentence)
    for i in filtered_sentence:
        # print(i)
        f.write(i + ' ')
    f.write('\n')
    # f_id.write(filtered_sentence+'\n')
    #将stopword的数据进行stem化

    synopses = []
    with  open(r'stopword.txt', 'r') as f:
        lines1 = f.readlines()
    for line1 in lines1:
        synopses.append(line1.replace('\n', ''))
    # print(title)


    # load nltk's SnowballStemmer as variabled 'stemmer'
    from nltk.stem.snowball import SnowballStemmer

    stemmer = SnowballStemmer("english")
    stemmer.stem("and")
    # print(stemmer)

    # here I define a tokenizer and stemmer which returns the set of stems in the text that it is passed
    f=open('result.txt','w')
    def tokenize_and_stem(text):
        # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
        tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        filtered_tokens = []
        # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
        for token in tokens:
            if re.search('[a-zA-Z]', token):
                filtered_tokens.append(token)
        stems = [stemmer.stem(t) for t in filtered_tokens]
        # print(stems)
        # print(type(stems))
        for i in stems:
            # print(i)
            f.write(i + ' ')
        f.write('\n')
        return stems


    def tokenize_only(text):
        # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
        tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        filtered_tokens = []
        # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
        for token in tokens:
            if re.search('[a-zA-Z]', token):
                filtered_tokens.append(token)
        return filtered_tokens


    # not super pythonic, no, not at all.
    # use extend so it's a big flat list of vocab
    totalvocab_stemmed = []
    totalvocab_tokenized = []
    for i in synopses:
        allwords_stemmed = tokenize_and_stem(i)  # for each item in 'synopses', tokenize/stem
        totalvocab_stemmed.extend(allwords_stemmed)  # extend the 'totalvocab_stemmed' list

        allwords_tokenized = tokenize_only(i)
        totalvocab_tokenized.extend(allwords_tokenized)



# preprocess()


def train(file_path):
    # class MySentences(object):
    #     def __init__(self, fname):
    #         self.fname = fname
    #
    #     def __iter__(self):
    #         for line in open(self.fname):
    #             yield line.split()
    #
    # sentences = MySentences("./result.txt")
    questions = []
    training_data = []
    with open(file_path,"r")as f:
            for line in f:
                questions.append(line)
                sentense = line.split()
                # print(sentense)
                training_data.append(sentense)
    # print(len(training_data))
    # # train word2vec on the sentences
    model = gensim.models.Word2Vec(training_data,min_count=1)
    return training_data, questions, model


def similarity(query, model, training_data, data):
    largest = 0
    index = 0
    for i in range(len(training_data)):
        current = model.n_similarity(query, training_data[i])
        print(current)
        if current > largest:
            index = i
            largest = current
        else:
            continue
    return data[index]


if __name__ == "__main__":
    train_data, text, model = train("./result.txt")
    vacablary = model.wv.index2word
    # train,text,model=train("data")
    # t = preprocess("what is your time?")
    # f = preprocess("what is lecture name?")
    # print(model.n_similarity(t, f))
    print("---------------")
    train, text, model = train("./result.txt")
    vacablary = model.wv.index2word
    print(model.most_similar("append",topn=5))
