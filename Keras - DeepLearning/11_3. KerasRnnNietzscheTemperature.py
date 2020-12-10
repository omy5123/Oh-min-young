import tensorflow as tf
# import tensorflow.compat.v1 as tf
# tf.disable_eager_execution()
import numpy as np
from sklearn import preprocessing

np.set_printoptions(linewidth=1000)

# 12. 복사해서 사용

def make_data_2(long_text, seq_len):
    lb = preprocessing.LabelBinarizer()
    lb.fit(list(long_text))

    words = [long_text[i:i+seq_len+1] for i in range(len(long_text)-seq_len)]

    x, y = [], []
    for word in words:
        onehot = lb.transform(list(word))

        x.append(np.float32(onehot[:-1]))
        y.append(np.argmax(onehot[-1]))

    return np.float32(x), np.int32(y), lb


def show_sampling_2(long_text, seq_len, temperature):
    x, y, lb = make_data_2(long_text, seq_len)
    vocab = lb.classes_

    # print(x.shape, y.shape)     # (1, 20, 31) (980,)

    _, seq_len, n_classes = x.shape
    hidden_size = 21

    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=[seq_len, n_classes]),
        tf.keras.layers.LSTM(hidden_size, return_sequences=False),
        tf.keras.layers.Dense(n_classes, activation='softmax'),
    ])
    model.summary()

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['acc'])

    model.fit(x, y, epochs=100, batch_size=32, verbose=2)
    # print(model.evaluate(x, y, verbose=0))

    # --------------------------------------- #
    # 1번 케라스 창시자 코드
    # start = np.random.randint(0, len(y) - 1 - seq_len, 1)
    #     # print(start)        # [426]
    #
    #     start = start[0]
    #     yy = y[start:start + seq_len]
    #     # print(indices)      # [16 25 24  1 18  8 24 25  1 14  8 24 22  5  1  9 26 25  1 25]
    #
    #     if(len(temperature) <= 0):                          # weighted_pick
    #         t = temperature[0]
    #         write_novel_y(model, vocab, seq_len, yy, 0.0)
    #     else:                                               # temperature_pick
    #         for t in temperature:
    #             print(t, '-' *30)
    #             write_novel_y(model, vocab, seq_len, yy, t)

    # 문제
    # x 데이터를 이용해서 소설을 쓰는 코드를 구형하세요.
    # 2번 내가 만든 코드

    start = np.random.randint(0, len(y) - 1 - seq_len, 1)
    start = start[0]
    xx = x[start]
    xx = xx[np.newaxis]

    print(x.shape,xx.shape)

    # print(indices)      # [16 25 24  1 18  8 24 25  1 14  8 24 22  5  1  9 26 25  1 25]

    if (len(temperature) <= 0):                  # weighted_pick
        t = temperature[0]
        write_novel_x(model, vocab, xx, 0.0)
    else:                                        # temperature_pick
        for t in temperature:
            print(t, '-' * 30)
            write_novel_x(model, vocab, xx, t)

# 가중치 비율에 맞게 선택
# def weighted_pick(preds):
#     t = np.cumsum(preds)
#     return np.searchsorted((t, np.random.rand(1)[0] * t[-1]))
#     # return np.searchsorted((t,np.random.rand(1)[0]))

def temperature_pick(preds, temperature):
    if (temperature > 0):
        preds = np.log(preds) / temperature
        preds = np.exp(preds)
        preds = preds / np.sum(preds)

    # weighted_pick 함수
    t = np.cumsum(preds)
    return np.searchsorted(t, np.random.rand(1)[0] * t[-1])
    # return np.searchsorted(t,np.random.rand(1)[0])


# 케라스 창시자가 만든 코드
def write_novel_y(model, vocab, seq_len, yy,temperature):

    for i in range(100):
        xx = np.zeros([1, seq_len, len(vocab)], dtype=np.int32)
        for j,pos in enumerate(yy):
            xx[0,j,pos] = 1

        # print(xx) # 20줄 31개
        preds = model.predict(xx)
        # print(preds.shape)          # (1, 31) 31개에대한 확률 계산 (어떤 토큰은 몇 이런식)

        # p = np.argmax(preds, axis=1)  # 이걸로 하면 큰값만 뽑아냄 그래서 창의적인 활동 불가
        # p = p[0]
        p = temperature_pick(preds, temperature)  # 그래서 temperature를 다르게 하며 창의적인 활동을 하게함
        # print(p)      [25] 대괄호가 남아있음

        # p = 71
        # [16 25 24  1 18]
        # [25 24  1 18 71]
        # 이것을 코드로 구현하게 되면
        yy[:-1] = yy[1:]
        yy[-1] = p

        print(vocab[p], end='')
    print()


# 내가 만든 코드
def write_novel_x(model, vocab, xx, temperature):

    for i in range(100):
        preds = model.predict(xx)
        # print(preds.shape)          # (1, 31) 31개에대한 확률 계산 (어떤 토큰은 몇 이런식)

        p = temperature_pick(preds, temperature)
        # print(p)      [25] 대괄호가 남아있음

        # p = 71
        # [16 25 24  1 18]
        # [25 24  1 18 71]
        # 이것을 코드로 구현하게 되면
        # xx[:, :-1,:] = xx[:,1:,:]       # xx[:-1] = xx[1:]
        xx[0,:-1] = xx[0,1:]
        xx[0,-1]=0
        xx[:,-1,p] = 1                  # xx[-1] = p

        print(vocab[p], end='')
    print()

f = open('data/nietzsche.txt', 'r', encoding='utf-8')
nietzsche = f.read().lower()
f.close()

long_text = nietzsche[:1000]

# show_sampling_2(long_text, seq_len=20, temperature=[])     # weigthed_pick 만
show_sampling_2(long_text, seq_len=20, temperature=[0.2,0.5,1.0,1.2])     # 여기부턴 temperature_pick



