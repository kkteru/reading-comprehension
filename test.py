import tensorflow as tf

a = tf.Variable(tf.random_normal([100, 30, 600, 400]))

with tf.Session() as sess:
    tf.global_variables_initializer()
    b = sess.run([a])
