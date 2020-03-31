import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

data = pd.read_csv('samsung.csv')
data.head()
 
high_prices = data['High'].values
low_prices = data['Low'].values
mid_prices = (high_prices + low_prices) / 2

seq_len = 50
sequence_length = seq_len + 1

result = []
for index in range(len(mid_prices)-sequence_length):
    result.append(mid_prices[index: index + sequence_length])

normalized_data = []
for window in result:
    normalized_window = [((float(p)/float(window[0]))-1)for p in window]
    normalized_data.append(normalized_window)

result = np.array(normalized_data)

row = int(round(result.shape[0]*0.7))
train = result[:row,:]
np.random.shuffle(train)

x_train = train[:, :-1]
x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
y_train = train[:, -1]
y_train = np.reshape(y_train,(y_train.shape[0],1))

x_test = result[row:, :-1]
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1],1))
y_test = result[row:, -1]
y_test = np.reshape(y_test,(y_test.shape[0],1))

x_train.shape, x_test.shape

X = tf.placeholder(tf.float32, [None, 50 ,1])
Y = tf.placeholder(tf.float32, [None,1])

cell = tf.nn.rnn_cell.BasicLSTMCell(num_units=64,state_is_tuple=True)

outputs, states = tf.nn.dynamic_rnn(cell, X, dtype = tf.float32)
Y_pred = tf.contrib.layers.fully_connected(
    outputs[:,-1], 1, activation_fn=None)

cost = tf.reduce_mean(tf.square(Y_pred-Y))
optimizer = tf.train.AdamOptimizer(0.01).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(100):
    _, l = sess.run([optimizer, cost],
                    feed_dict={X: x_train, Y: y_train})
    print(i,l)

testpredict = sess.run(Y_pred, feed_dict={X: x_test})

plt.plot(y_test)
plt.plot(testpredict)
plt.show()
