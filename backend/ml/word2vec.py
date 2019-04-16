from __future__ import absolute_import
import json
from gensim.models import Phrases
from gensim.models import Word2Vec

# initialise word2vec model for forum and lecuture content
import gensim


def init_W2Vmodel(file_path):
    # keywords
    keywords = []
    # answers
    answers = []

    with open(file_path)as f:
        lines = f.readlines()
        for line in lines:
            # print(line)
            data=json.loads(line)
            # print(type(data))
            _kws=data['word'].split(" ")
            kws = [word.lower() for word in _kws]
            ans=data['description']
            keywords.append(kws)
            answers.append(ans)
        # print(keywords)
    #         question = line
    #         sentense = line.split()
    #         # print(sentense)
    #         training_data.append(sentense)
    # # print(len(training_data))
    # # # train word2vec on the sentences
    model = Word2Vec(keywords, min_count=1)
    return model, keywords, answers

def load_W2Vmodel(model_path):
    pass


def most_similarity(query, model, question, answer):
    largest = 0
    index = 0
    q = list(filter(lambda x: x in model.wv.vocab, query))
    for i in range(len(question)):
        try:
            current = model.n_similarity(q, question[i])
        except ValueError:
            current = 0
        if current > largest:
            index = i
            largest = current
    return question[index],answer[index]


model, questions, answers = init_W2Vmodel("./9311_refin")
query = ['what', 'is', 'the', 'difference', 'between', 'er','model','and','relational','model']
question, answer = most_similarity(query, model, questions, answers)
print("question is:",question)
print("answer is:" ,answer)

