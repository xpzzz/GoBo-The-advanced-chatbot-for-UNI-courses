import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import re
from nltk.stem.snowball import SnowballStemmer
from os.path import dirname

_root = dirname(__file__)
def pp():
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

    with open('{}/messages.json'.format(_root), 'r',encoding='utf-8') as f:
        with open ('{}/refine.json'.format(_root), 'w' , encoding='utf-8') as refine:
            for line in f:

                line = line.strip()
                refine.write(line)

                # json分行
                if '},'== line:
                    refine.write('\n')
                # if line == "":
                #     refine.write(' ')


    with open ('{}/refine.json'.format(_root), 'r' , encoding='utf-8') as refine:
        with open ('{}/9311_forum.json'.format(_root), 'w' , encoding='utf-8') as c9311:
            with open('{}/9321_forum.json'.format(_root), 'w', encoding='utf-8') as c9321:
                for line in refine:
                    # print(line)
                    if 'COMP9311 18s2' in line:
                        # print(line)
                        c9311.write(line)
                    if 'COMP9321 18s' in line:
                        c9321.write(line)


    with open('{}/9321_forum.json'.format(_root),'r',encoding='utf-8') as refine:
        with open('{}/reduce_dic.json'.format(_root),'w', encoding='utf-8') as reduce:

            reply_count = {}

            for line in refine:
                # print(line)
                # re.sub('\"', "\'", line)
                line = line.replace('\\','\\\\').replace('\\"',"\\'")
                # print(line)
                line=line[0:-2]
                # print(line)
                d = json.loads(line)
                # print(type(d))

                #课程筛选
                # if d['course'] != 'COMP9321 18s2 Database Systems':
                #     continue

                #数据处理
                del d['posted_by']
                del d['created']

                if 'resource_id' in d.keys():
                    del d['resource_id']
                if 'link_resource' in d.keys():
                    # TODO split 后提取assignment / lecture 范围
                    del d['link_resource']
                if 'html_resource' in d.keys():
                    del d['html_resource']
                reply_count[d['mesg_id']] = 0

                if 'parent_id' in d.keys():
                    reply_count[d['parent_id']] +=1
                    d['host'] = 0
                else:
                    d['host'] = 1
                # print(d)
                reduce.write(json.dumps(d))
                reduce.write('\n')

    print(reply_count)
    fin = {}
    base_url = 'https://webcms3.cse.unsw.edu.au/COMP9321/18s2/forums/'
    # base_url = 'https://webcms3.cse.unsw.edu.au/COMP9321/18s2/forums/'


    with open('{}/reduce_dic.json'.format(_root),'r', encoding='utf-8') as reduce:
        with open('{}/9321_Questions.json'.format(_root), 'w', encoding='utf-8') as final:
            # with open('Q_no_answer.json', 'w', encoding='utf-8') as final_all:
            for line in reduce:
                d = json.loads(line)
                print(line)

                if d['host'] == 1:
                    if reply_count[d['mesg_id']] > 0:
                        fin['question'] = " ".join(preData(d['message_body']))
                        fin['answer'] = (base_url+str(d['mesg_id']), 1)
                        print(11111)

                    if reply_count[d['mesg_id']] == 0:
                        fin['question'] = " ".join(preData(d['message_body']))
                        fin['answer'] = (base_url+str(d['mesg_id']), 0)
                        print(22222222)

                    final.write(json.dumps(fin))
                    final.write('\n')


