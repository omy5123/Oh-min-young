import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import collections

# att: attention의 약자
def get_xy(n, n_features, att_column):
    x = np.random.standard_normal([n, n_features])   # 평균 0, 표준편차 1
    y = np.random.choice([0, 1], size=[n, 1])

    x[:, att_column] = y[:, 0]

    return x, y

def build_model_normal(n_features):
    inputs = tf.keras.layers.Input([n_features])
    output = tf.keras.layers.Dense(n_features, activation='relu')(inputs)
    output = tf.keras.layers.Dense(1, activation='sigmoid')(output)

    return tf.keras.Model(inputs, output)

def show_model(model_builder):
    n_features, att_column = 32, 7

    x_train, y_train = get_xy(10000, n_features, att_column)
    x_test, y_test = get_xy(10000, n_features, att_column)

    model = model_builder(n_features)
    model.summary()

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])
    model.fit(x_train, y_train, epochs=20, batch_size=64, verbose=2,
              validation_data=(x_test, y_test))

show_model(build_model_normal)