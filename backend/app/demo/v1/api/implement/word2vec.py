from __future__ import absolute_import

import json
import os

import gensim

# initialise word2vec model for forum and lecuture content

from os.path import dirname

from app.demo.v1.api.implement import kb_originals, kb_answers, kb_questions

_root = dirname(__file__)


def init_dict(course_code, doc_type, save=False):
    if doc_type == "forum" and save:
        kb_originals[course_code] = dict()
        kb_originals[course_code][doc_type] = list()
        with open('{}/data/{}_original.json'.format(_root, course_code))as file:
            lines = file.readlines()
            for line in lines:
                # from pprint import pprint
                # pprint(line)
                data = json.loads(line)
                # print(type(data))
                orig = data['question']
                kb_originals[course_code][doc_type].append(orig)

    with open('{}/data/{}_{}.json'.format(_root, course_code, doc_type))as f:
        print('[DEBUG word2vec] Initialising in memory dict')
        lines = f.readlines()
        # TODO: save original questions
        kb_questions[course_code] = dict()
        kb_questions[course_code][doc_type] = list()
        kb_answers[course_code] = dict()
        kb_answers[course_code][doc_type] = list()

        for line in lines:
            # from pprint import pprint
            # pprint(line)
            data = json.loads(line)
            # print(type(data))
            _kws = data['question'].split(" ")
            kws = [word.lower() for word in _kws]
            if doc_type == "forum":
                ans = data['answer']
            else:
                # doc_type == "resource":
                ans = data['description']
            kb_questions[course_code][doc_type].append(kws)
            kb_answers[course_code][doc_type].append(ans)

        save_path = "{}/model/W2V_{}_{}.model".format(_root, course_code, doc_type)

        model = gensim.models.Word2Vec(kb_questions[course_code][doc_type], min_count=1)

        if save:
            model.save(save_path)


def init_W2Vmodel(course_code, doc_type):
    #
    global keywords_forum, keywords_content, answers_forum, answers_content
    exists = os.path.isfile('{}/model/W2V_{}_{}.model'.format(_root, course_code, doc_type))
    if not exists:
        init_dict(course_code, doc_type, save=True)
    else:
        init_dict(course_code, doc_type)
    model = gensim.models.Word2Vec.load('{}/model/W2V_{}_{}.model'.format(_root, course_code, doc_type))
    return model


def most_similarity(query, model, question, answer):
    largest = 0
    index = 0
    q = list(filter(lambda x: x in model.wv.vocab, query))
    if not q:
        print("nothing")
        return None,None,None
    for i in range(len(question)):
        try:
            current = model.n_similarity(q, question[i])
        except ValueError:
            continue
        if current > largest:
            index = i
            largest = current
    return question[index], answer[index], largest
