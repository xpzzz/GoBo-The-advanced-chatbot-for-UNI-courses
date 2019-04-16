import nltk
from os.path import dirname
import tensorflow as tf

dest = dirname(__file__) + '/nltk_data/'
nltk.download('punkt', download_dir=dest)
nltk.data.path.append(dest)

data_path = dirname(__file__) + '/data/'

# Parameters
# ==================================================
data1 = data_path + 'testF.txt'
data0 = data_path + 'testP.txt'
# Data Parameters
tf.flags.DEFINE_float("dev_sample_percentage", .5, "Percentage of the training data to use for validation")
tf.flags.DEFINE_string("testF_data_file", data1, "Data source for the test forum data. should be 1")
tf.flags.DEFINE_string("testP_data_file", data0, "Data source for the test Pdf data. should be 0")

# Eval Parameters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
tf.flags.DEFINE_string("checkpoint_dir", "", "Checkpoint directory from training run")
tf.flags.DEFINE_boolean("eval_train", True, "Evaluate on all training data")

# Misc Parameters
tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")