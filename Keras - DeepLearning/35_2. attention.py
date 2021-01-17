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

def build_model_attention_1(n_features):
    inputs = tf.keras.layers.Input([n_features])
    att_probs = tf.keras.layers.Dense(n_features, activation='softmax')(inputs)

    # dot product
    output = tf.keras.layers.multiply([inputs, att_probs])

    output = tf.keras.layers.Dense(n_features, activation='relu')(inputs)
    output = tf.keras.layers.Dense(1, activation='sigmoid')(output)

    return tf.keras.Model(inputs, output)

def build_model_attention_2(n_features):
    inputs = tf.keras.layers.Input([n_features])
    att_probs = tf.keras.layers.Dense(n_features, activation='softmax')(inputs)

    # dot product
    output = tf.keras.layers.multiply([inputs, att_probs])

    output = tf.keras.layers.Dense(n_features, activation='relu')(inputs)
    output = tf.keras.layers.Dense(1, activation='sigmoid')(output)

    return tf.keras.Model(inputs, [output, att_probs])

def show_model_1(model_builder):
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

    return model, x_test

def show_model_2(model_builder):
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
    # ----------------------------- #

    preds = model.predict(x_test, verbose=0)
    print(type(preds), len(preds))  # <class 'list'> 2

    att_preds = preds[1]  # 어텐션 레이어의 출력
    print(att_preds.shape)  # (10000, 32)

    activations = np.mean(att_preds, axis=0)

    plt.bar(range(len(activations)), activations)
    plt.show()


def show_activation(model, x_test):
    layer_outputs = [layer.output for layer in model.layers]
    act_model = tf.keras.Model(model.inputs, layer_outputs)

    preds = act_model.predict(x_test, verbose=0)
    print(type(preds), len(preds))      # <class 'list'> 5

    att_preds = preds[1]                # 어텐션 레이어의 출력
    print(att_preds.shape)              # (10000, 32)

    activations = np.mean(att_preds, axis=0)

    plt.bar(range(len(activations)), activations)
    plt.show()

# model, x_test = show_model_1(build_model_attention_1)
# show_activation(model, x_test)

show_model_2(build_model_attention_2)