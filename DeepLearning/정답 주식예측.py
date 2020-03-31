import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import datetime


data = pd.read_csv('samsung.csv')
data.head()
high_prices = data['High'].values
low_prices = data['Low'].values
mid_prices = (high_prices + low_prices) / 2

seq_len = 20
sequence_length = seq_len + 1

result = []
for index in range(len(mid_prices) - sequence_length):
    result.append(mid_prices[index: index + sequence_length])

normalized_data = []
for window in result:
    normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
    normalized_data.append(normalized_window)

result = np.array(normalized_data)

row = int(round(result.shape[0] * 0.7))
train = result[:row, :]
np.random.shuffle(train)

x_train = train[:, :-1]
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
y_train = train[:, -1]
y_train = np.reshape(y_train,(y_train.shape[0],1))
x_test = result[row:, :-1]
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
y_test = result[row:, -1]
y_test = np.reshape(y_test,(y_test.shape[0],1))

learning_rate = 0.01
total_epoch = 100
n_input = 1
n_step = seq_len
n_hidden = 64
n_class = 1

X = tf.placeholder(tf.float32, [None, n_step, n_input])
Y = tf.placeholder(tf.float32, [None,1])

cell1 = tf.nn.rnn_cell.LSTMCell(n_hidden)
cell2 = tf.nn.rnn_cell.LSTMCell(n_hidden)
cell=tf.nn.rnn_cell.MultiRNNCell([cell1, cell2],state_is_tuple=True)
outputs, states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)
Y_pred=tf.contrib.layers.fully_connected(outputs[:,-1],n_class,activation_fn=None)
cost = tf.reduce_mean(tf.square(Y_pred-Y))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for epoch in range(total_epoch):       
    _, cost_val= sess.run([optimizer, cost],
                               feed_dict={X: x_train, Y: y_train})
    print('Epoch:', '%04d' % (epoch + 1),
        'cost = %f',cost_val)
print('최적화 완료!')

test_predict=sess.run(Y_pred, feed_dict={X:x_test})

fig = plt.figure(facecolor='white', figsize=(20, 10))
ax = fig.add_subplot(111)
ax.plot(y_test, label='True')
ax.plot(test_predict, label='Prediction')
ax.legend()
plt.show()
    


    
