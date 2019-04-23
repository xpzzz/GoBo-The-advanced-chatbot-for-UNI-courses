from os.path import dirname

from .test_query import testQuery


def cnn(query):
    vocab_path = dirname(__file__) + '/model/vocab'
    checkpoint_file = dirname(__file__) + '/model/model-600'
    print(checkpoint_file)
    data_path = dirname(__file__) + '/data/'
    with open(data_path + 'testF.txt', 'w') as f:
        f.write(query)
    testQuery(vocab_path, checkpoint_file, data_path)
    with open(data_path + 'prediction.csv', 'r') as r:
        predict = r.readline()
        result = predict.split(',')
        print(predict)
        print(result)
    _res = result[1].replace('\n', '')
    if _res == '0.0':
        res = 'resource'
    elif _res == '1.0':
        res = 'forum'
    else:
        print('[CNN DEBUG] Something went wrong, falling back')
        res = 'resource'
    # query, 0/1
    return res


print(cnn('i love you xwx'))
