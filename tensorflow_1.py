import tensorflow as tf

tf.enable_eager_execution()
x = tf.get_variable('x', shape=[1], initializer=tf.constant_initializer(3.))
with tf.GradientTape() as tape:
    # 在tf.GradientTape() 的上下文内，所有计算步骤都会被记录以用于求导
    y = tf.square(x)
    y_grad = tape.gradient(y, x)  # 计算y 关于x 的导数
print([y.numpy(), y_grad.numpy()])
