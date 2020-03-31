import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot = True)

X = tf.placeholder(tf.float32, [None, 28, 28, 1])
Y = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_normal([3, 3, 1, 32], stddev = 0.01))
L1 = tf.nn.conv2d(X, W1, strides= [1, 1, 1, 1], padding='SAME')
L1 = tf.nn.relu(L1)
L1 = tf.nn.max_pool(L1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
                    padding = 'SAME')

W2 = tf.Variable(tf.random_normal([3, 3, 32, 64], stddev = 0.01))
L2 = tf.nn.conv2d(L1, W2, strides= [1, 1, 1, 1], padding='SAME')
L2 = tf.nn.relu(L2)
L2 = tf.nn.max_pool(L2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
                    padding = 'SAME')

W3 = tf.Variable(tf.random_normal([3, 3, 64, 128], stddev = 0.01))
L3 = tf.nn.conv2d(L2, W3, strides= [1, 1, 1, 1], padding='SAME')
L3 = tf.nn.relu(L3)
L3 = tf.nn.max_pool(L3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
                    padding = 'SAME')

W4 = tf.Variable(tf.random_normal([4 * 4 * 128, 256], stddev = 0.01))
L4 = tf.reshape(L3, [-1, 4 * 4 * 128])
L4 = tf.matmul(L4,W4)
L4 = tf.nn.relu(L4)
L4 = tf.nn.dropout(L4, keep_prob)

W5 = tf.Variable(tf.random_normal([256, 256], stddev = 0.01))
L5 = tf.nn.relu(tf.matmul(L4, W5))
L5 = tf.nn.dropout(L5, keep_prob)

W6 = tf.Variable(tf.random_normal([256, 10], stddev = 0.01))
model = tf.matmul(L5, W6)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
    logits=model, labels=Y))
optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
batch_size = 100
total_batch = int(mnist.train.num_examples / batch_size)

for epoch in range(15):
    total_cost = 0
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs = batch_xs.reshape(-1, 28, 28, 1)

        _, cost_val = sess.run([optimizer, cost],
                               feed_dict = {X: batch_xs, Y: batch_ys, keep_prob: 0.8})
        total_cost += cost_val

    print('Epoch', '%04d' % (epoch + 1),
             'Avg. cost =', '{:3f}'.format(total_cost / total_batch))

print('최적화 완료!')

is_correct = tf.equal(tf.argmax(model,1),tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('정확도:', sess.run(accuracy,
                       feed_dict={X:mnist.test.images.reshape(-1, 28, 28,1),
                                  Y: mnist.test.labels,
                                  keep_prob: 1}))
