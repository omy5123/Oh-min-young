# 데이터셋에 시계열 특성이 잘드러나 lstm하면 좋다를 보여줌

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection

# 문제
# 예측한 결과에 대해 0.04보다 작다면 정답으로 인정해서
# 정확도가 얼마인지 알려주세요.

def get_data(seq_len=100, size=3000):
    np.random.seed(23)
    x, y = [], []
    for _ in range(size):
        values = np.random.rand(seq_len)
        i0, i1 = np.random.choice(seq_len, 2,replace=False) # 똑같은 수 2개를 가져올수도 있다. 그래서 replace = False한다
        # print(values)
        # print(np.min(values), np.max(values))

        # print(i0,i1)
        assert i0 != i1 # 똑같은거 나오면 경고 주려고 하지만 replace해서 안나옴

        two_hots = np.zeros(seq_len)
        two_hots[[i0, i1]] = 1   # 100개에서 2개를 넣기위해 투핫

        xx = np.transpose([values, two_hots])  # values가 첫번째 feature, two_hot이 두번째
        yy = values[i0] * values[i1]
        # print(xx.shape)
        x.append(xx)
        y.append(yy)

    x = np.float32(x)
    y = np.float32(y)

    return model_selection.train_test_split(x,y, train_size=0.8)


def simple_rnn(): # 매개변수로 쓸 함수
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[100, 2]))
    model.add(tf.keras.layers.SimpleRNN(30, return_sequences=True))
    model.add(tf.keras.layers.SimpleRNN(30, return_sequences=False))
    model.add(tf.keras.layers.Dense(1))

    return model

def lstm(): # 매개변수로 쓸 함수
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[100, 2]))
    model.add(tf.keras.layers.LSTM(30, return_sequences=True))  # lstm이 가장 많이 씀
    model.add(tf.keras.layers.LSTM(30, return_sequences=False))
    model.add(tf.keras.layers.Dense(1))

    return model

def gru(): # 매개변수로 쓸 함수
    model = tf.keras.Sequential()
    # model.add(tf.keras.layers.GRU(30, return_sequences=True, input_shape=[100,2]))  # lstm과 GRU섞어서 씀
    model.add(tf.keras.layers.Input(shape=[100,2]))  # summary 해주기위해 씀
    model.add(tf.keras.layers.GRU(30, return_sequences=True))
    model.add(tf.keras.layers.GRU(30, return_sequences=False))
    model.add(tf.keras.layers.Dense(1))

    return model

def show_history(history):  # 시각적으로 확인하기 위해
    plt.plot(history.history['loss'], 'r--',label='loss')
    plt.plot(history.history['val_loss'], 'g--', label='val_loss')
    plt.legend()
    plt.xlabel('Epochs')
    plt.title('RNN')
    plt.show()

def show_model(model_func):
    x_train, x_test, y_train, y_test = get_data(seq_len=100, size=3000)
    print(x_train.shape, x_test.shape)      # (2400, 100, 2) (600, 100, 2)
    print(y_train.shape, y_test.shape)      # (2400,) (600,)

    model = model_func()
    model.summary()

    model.compile(optimizer=tf.keras.optimizers.Adam(),
                  loss=tf.keras.losses.mse)

    # history 저장할 때는 pickle 사용
    history = model.fit(x_train, y_train, epochs=30, verbose=2,batch_size=32,validation_split=0.2)

    # preds = model.predict(x_test)
    #     print(preds.shape)
    #
    #     preds = preds.reshape(-1)
    #     print('acc :', np.mean(np.abs(preds - y_test <= 0.04)))

    print(history)
    print(history.history)
    # {'loss': [0.11252846568822861, 0.0561690591275692, 0.05428178235888481],
    # 'val_loss': [0.0553494468331337, 0.0533539280295372, 0.05343523249030113]}

    # 문제
    # history 객체에 들어있는 값으로 그래프를 그려주세요.
    show_history(history)

# show_model(simple_rnn)
# show_model(lstm)
show_model(gru)

# simple_rnn
# Epoch 30/30
# 60/60 - 1s - loss: 0.0502 - val_loss: 0.0534
# acc : 0.4816666666666667

# lstm
# Epoch 30/30
# 60/60 - 5s - loss: 0.0075 - val_loss: 0.0095
# acc : 0.925

# gru
# Epoch 30/30
# 60/60 - 3s - loss: 8.0897e-04 - val_loss: 7.0436e-04
# acc : 0.9433333333333334
