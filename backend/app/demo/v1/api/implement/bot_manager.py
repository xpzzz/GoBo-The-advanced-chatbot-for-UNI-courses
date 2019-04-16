# this is the workflow for the case that DF can not recognize
from __future__ import absolute_import, print_function

from pprint import pprint

from . import detect_intent_via_text as di
# from .preprocess import preData
from .cnn import cnn
from .word2vec import init_W2Vmodel, most_similarity, kb_questions, kb_answers, kb_originals
from .preprocess import preData
# config threshold here
THRESHOLD = 0.7


def match_question(query, course_context):
    # return (forum,0, original question, link): forum but no reply
    # return (forum,1, original question, link): forum and replied
    # (resource,course code, keywords, answer) : content
    # (not found,0,None,None): no matching
    # query = preData(query)
    doc_type = cnn(query)
    print("cnn successfully", doc_type)
    model = init_W2Vmodel(course_context, doc_type)
    questions = kb_questions[course_context][doc_type]
    answers = kb_answers[course_context][doc_type]
    query = preData(query)
    if not query:
        return 0, 0, None, None
    print("preprocess successfully", query)
    qes, ans, score = most_similarity(query, model, questions, answers)
    if not qes:
        return 0,0,None,None
    print('question is: ', qes)
    index = questions.index(qes)
    print('answer is: ', ans)
    if score > THRESHOLD:
        if doc_type == "forum":
            qes_str = " ".join(qes)
            return doc_type, ans[1], kb_originals[course_context][doc_type][index], ans[0]
        elif doc_type == "resource":
            qes_str = " ".join(qes)
            return doc_type, course_context, qes_str, ans
    # score < threshold, return default
    return 0, 0, None, None


def self_refine(query_text, course_context):
    location, flag, matched_text, answer = match_question(query_text, course_context)
    if location == "forum":
        # match the forum
        first_chunk = "Your question might be asked by someone already " \
                      "on forum in the past, the original one is: {}".format(matched_text)
        if flag:
            # be replied
            second_chunk = "and it has been replied, you can find it through {} before you post again.".format(answer)
            # not replied
        else:
            second_chunk = "and it has not been replied, you can post again under this link to refresh: {}".format(
                answer)

    elif location == "resource":
        # match the resource
        first_chunk = "It is declared in text book of {} about {},".format(flag, matched_text)
        second_chunk = "the explanation is {}".format(answer)
    else:
        # no matched answer
        # temporary return default answer from dialogflow
        first_chunk = ""
        second_chunk = ""
    return (first_chunk + second_chunk, location)


def manage(pid, sid, text, context):
    resp_dict = di.detect_intent_texts(pid, sid, text, context)
    # pprint('=======================')
    # pprint((pid, sid, text, context))
    # pprint('=======================')
    confidence = resp_dict["confidence"]
    text = resp_dict["text"]
    query_text = resp_dict["query_text"]
    detected_intent = resp_dict["detected_intent"][0]  # return a tuple here
    # default response
    text_dict = {"text": text, "flag":"dialogflow"}
    # still won't show default fallback
    if confidence < 0.7 or detected_intent == "Default Fallback Intent":
        print("get default fallback")
        madeup_resp = self_refine(query_text, context)
        if madeup_resp[0]:
            text_dict['text'] = madeup_resp[0]
            text_dict["flag"] = madeup_resp[1]

    return text_dict
