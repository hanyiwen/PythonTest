import tensorflow as tf
import numpy as np

sess = tf.Session()
a_array = np.array([1,2,3,4,5], dtype=np.float64)
print(sess.run(tf.log(a_array)))