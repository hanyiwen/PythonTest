import tensorflow as tf

#
# w1 = tf.Variable(2.0)
# w2 = tf.Variable(2.0)
#
# a = tf.multiply(w1, 3.0)
# a_stoped = tf.stop_gradient(a)
#
# # b=w1*3.0*w2
# b = tf.multiply(a_stoped, w2)
# gradients = tf.gradients(b, xs=[w1, w2])
#
# print(gradients)


a = tf.Variable(1.0)
b = tf.Variable(1.0)

c = tf.add(a, b)

c_stoped = tf.stop_gradient(c)

d = tf.add(a, b)

e = tf.add(c_stoped, d)

gradients = tf.gradients(e, xs=[a, b])

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    print(sess.run(gradients))
