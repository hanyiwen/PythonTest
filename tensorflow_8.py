import tensorflow as tf

sess = tf.Session()
# indices = [[0, 2], [1, -1]]
indices = [0, 1, 2, 3]
depth = 3
# one_hot_indices = tf.one_hot(indices, depth,
#            on_value=1.0, off_value=0.0,
#            axis=1)  # output: [4 x 3]
one_hot_indices = tf.one_hot(indices, depth,
           on_value=1.0, off_value=0.0, )  # output: [4 x 3]

print(sess.run(one_hot_indices))