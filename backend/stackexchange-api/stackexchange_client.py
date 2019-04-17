import json
import os
from collections import defaultdict
from typing import List

from dotenv import load_dotenv
from mongo_driver import *
from stackexchange import Site, StackOverflow

load_dotenv(verbose=True)

so = Site(StackOverflow, os.environ['STACKAPP_KEY'])


def query_stackoverflow(query_term, skip_counter=0, start_page=0):
    so.be_inclusive()
    qs = so.search(intitle=query_term, pagesize=100, sort='votes') \
        .fetch()
    if start_page > 0:
        qs = qs.fetch_page(start_page)
    # if skip_counter:
    #     print(f'Skipping first {skip_counter} queries...')
    #     # for _ in qs:
    #     #     if counter >= skip_counter:
    #     #         break
    #     #     else:
    #     #         counter += 1
    #     #         qs.next()
    #     #         print(f'{counter} skipped')
    #     for _ in range(skip_counter):
    #         print(f'{_} skipped')
    #         qs.next()
    counter = 0
    skipped = 0
    for _q in qs:
        if skip_counter > 0:
            print(f'initial skipping remaining: {skip_counter}')
            skip_counter -= 1
            continue
        json = get_json(_q.id, query_term)
        print(f'=== inserting {_q} to mongodb ===')
        if json:
            # pprint(json)
            # update_document(_q.id, json)
            insert_document(json)
            counter += 1
            print(f'=== {counter} jobs done ===')
        else:
            skipped += 1
            print(f'=== {skipped} jobs skipped ===')


def get_json(q_id, query_term):
    q = so.question(q_id, filter='!-*f(6rktpIY5')
    try:
        json = {
            '_id': q_id,
            'title': q.json['title'],
            'query_term': query_term, 'tags': q.json['tags'],
            'link': q.json['link'],
            'body': {
                'html': q.json['body'],
                'markdown': q.json['body_markdown']
            },
            'owner': q.json['owner']['display_name'],
            'is_answered': q.json['is_answered']}
        answer_id = q.json.get('accepted_answer_id')
        if not json['is_answered'] or not answer_id:
            return None
        _ans = so.answer(answer_id, filter='!-*f(6rktpIY5')
        answer = {
            'owner': _ans.json['owner']['display_name'],
            'is_accepted': _ans.json['is_accepted'],
            'answer_id': _ans.json['answer_id'],
            'question_id': _ans.json['question_id'],
            'body': {
                'html': _ans.json['body'],
                'markdown': _ans.json['body_markdown']
            }
        }
        json['best_answer'] = answer
        # pprint(json)
    except KeyError:
        return None

    return json


def get_tags_with_synonyms(query: str) -> defaultdict(List):
    tags = so.tags(inname=query, order='desc', sort='popular', pagesize=100, filter='!bNKX0p1erRzsGe') \
        .fetch()
    _dict = defaultdict(list)
    for tag in tags:
        tag_name = tag.name
        if tag.json['has_synonyms']:
            tag_syns = tag.json['synonyms']
        else:
            tag_syns = []
        _dict[tag_name] = tag_syns
        # print(f'{tag_name}:\n{tag_syns}')
    result_dict = {}
    for k in sorted(_dict, key=lambda _k: len(_dict[_k]), reverse=True):
        result_dict[k] = _dict[k]
    return result_dict


def export_as_json(d, filename):
    with open(filename, 'w') as f:
        json.dump(d, f, indent=4)


if __name__ == '__main__':
    d1 = get_tags_with_synonyms('python')
    d2 = get_tags_with_synonyms('postgresql')
    export_as_json(d1, 'python_syn.json')
    export_as_json(d2, 'postgresql_syn.json')
    # query_stackoverflow('python', start_page=25)
    # get_question(394809)
    # get_answer(394814)
    # q = so.question(394809, filter='!-*f(6rktpIY5')
    # print('=== title ===\n', q.title)
    # print('=== question ===\n', q.body_markdown.encode('utf-8'))
    # print('=== answer ===\n', q.answers[0].body_markdown.encode('utf-8'))
    # query_stackoverflow('python')
