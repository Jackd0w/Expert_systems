import tensorflow as tf
from tf.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
W_relu = tf.Variable(tf.truncated_normal([784, 100], stddev=0.1))
b_relu  = tf.Variable(tf.truncated_normal([100], stddev=0.1))

y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(tf.redice_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init = tf.initialize_global_variables()

train_session = tf.Session()
train_session.run(init)

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    train_session.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print("Accuracy: %s" % train_session.run(accuracy, feed_dict = {x: mnist.test.images, y_: mnist.test.labels}))