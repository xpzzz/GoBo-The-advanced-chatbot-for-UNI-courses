import nltk
from os.path import dirname
import tensorflow as tf

kb_questions = dict()
kb_answers = dict()
kb_originals = dict()


def init_ml():
    global kb_questions, kb_answers, kb_originals
    if not (kb_questions and kb_answers and kb_originals):
        kb_questions = dict()
        kb_answers = dict()
        kb_originals = dict()
    app = tf.app
    print('initialising ml module...')
    dest = dirname(__file__) + '/nltk_data/'
    nltk.download('punkt', download_dir=dest)
    nltk.download('stopwords', download_dir=dest)
    nltk.data.path.append(dest)

    data_path = dirname(__file__) + '/data/'

    # Parameters
    # ==================================================
    data1 = data_path + 'testF.txt'
    data0 = data_path + 'testP.txt'
    # Data Parameters
    app.flags.DEFINE_float("dev_sample_percentage", .5, "Percentage of the training data to use for validation")
    app.flags.DEFINE_string("testF_data_file", data1, "Data source for the test forum data. should be 1")
    app.flags.DEFINE_string("testP_data_file", data0, "Data source for the test Pdf data. should be 0")

    # Eval Parameters
    app.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
    app.flags.DEFINE_string("checkpoint_dir", "./ckpt", "Checkpoint directory from training run")
    app.flags.DEFINE_boolean("eval_train", True, "Evaluate on all training data")

    # Misc Parameters
    app.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
    app.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")

    # gunicorn parameters
    app.flags.DEFINE_integer("w", 4, 'Server Workers')
    app.flags.DEFINE_integer("b", 4, 'Server Address')
    app.flags.DEFINE_integer("t", 4, 'Server Timeout')

    print(tf.flags.FLAGS)
    return app


if __name__ == '__main__':
    app = init_ml()
    # print(app)
    pass
