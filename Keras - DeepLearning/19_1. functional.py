import tensorflow as tf
import numpy as np

# 문제
# AND 데이터셋에 대해 정확도를 계산하는 모델을 만드세요.

def and_sequential():
    data = [[0,0,0],
            [0,1,0],
            [1,0,0],
            [1,1,1]]
    data = np.int32(data)

    x = data[:, :-1]
    y = data[:, -1:]

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[2]))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])

    model.fit(x, y, epochs=100, verbose=2)
    print('acc :', model.evaluate(x, y))

def xor_sequential():
    data = [[0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]]
    data = np.int32(data)

    x = data[:, :-1]
    y = data[:, -1:]

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[2]))
    model.add(tf.keras.layers.Dense(5, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])

    model.fit(x, y, epochs=100, verbose=2)
    print('acc :', model.evaluate(x, y))

def xor_functional_basic():
    data = [[0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]]
    data = np.int32(data)

    x = data[:, :-1]
    y = data[:, -1:]

    # model = tf.keras.Sequential()
    #     model.add(tf.keras.layers.Input(shape=[2]))
    #     model.add(tf.keras.layers.Dense(5, activation='relu'))
    #     model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    input = tf.keras.layers.Input(shape=[2])

    # 1번 함수형으로 바꾼것
    # dense1 = tf.keras.layers.Dense(5, activation='relu')
    #     output1 = dense1.__call__(input)
    #     dense2 = tf.keras.layers.Dense(1, activation='sigmoid')
    #     output2 = dense2.__call__(output1)

    # 2번
    # dense1 = tf.keras.layers.Dense(5, activation='relu')
    #     output1 = dense1(input)
    #     dense2 = tf.keras.layers.Dense(1, activation='sigmoid')
    #     output2 = dense2(output1)

    # 3번
    output1 = tf.keras.layers.Dense(5, activation='relu')(input)
    output2 = tf.keras.layers.Dense(1, activation='sigmoid')(output1)

    model = tf.keras.Model(input, output2)

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])

    model.fit(x, y, epochs=100, verbose=2)
    print('acc :', model.evaluate(x, y))

def xor_functional_multi_input():
    data = [[0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]]
    data = np.int32(data)

    x1 = data[:, 0:1]
    x2 = data[:, 1:2]
    y = data[:, 2:3]

    # 1번
    # input1 = tf.keras.layers.Input(shape=[1])
    #     input2 = tf.keras.layers.Input(shape=[1])
    #
    #     input = tf.keras.layers.concatenate([input1, input2], axis=1)
    #
    #     output1 = tf.keras.layers.Dense(5, activation='relu')(input)
    #     output2 = tf.keras.layers.Dense(1, activation='sigmoid')(output1)
    #
    #     model = tf.keras.Model([input1,input2], output2)

    # 2번
    input1 = tf.keras.layers.Input(shape=[1])
    output1 = tf.keras.layers.Dense(5, activation='relu')(input1)

    input2 = tf.keras.layers.Input(shape=[1])
    output2 = tf.keras.layers.Dense(5, activation='relu')(input2)

    concat = tf.keras.layers.concatenate([output1, output2], axis=1)

    output3 = tf.keras.layers.Dense(1, activation='sigmoid')(concat)

    model = tf.keras.Model([input1, input2], output3)

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])

    # 학습을 할때도 입력 x 두개
    model.fit([x1, x2], y, epochs=100, verbose=2)
    print('acc :', model.evaluate([x1, x2], y))

def xor_functional_multi_inout(): # 입력 2개 , 출력 2개
    data = [[0, 0, 0, 0],
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [1, 1, 0, 1]]
    data = np.int32(data)

    x1 = data[:, 0:1]
    x2 = data[:, 1:2]
    y1 = data[:, 2:3]
    y2 = data[:, 3:4]

    input1 = tf.keras.layers.Input(shape=[1])
    output1 = tf.keras.layers.Dense(5, activation='relu')(input1)

    input2 = tf.keras.layers.Input(shape=[1])
    output2 = tf.keras.layers.Dense(5, activation='relu')(input2)

    concat = tf.keras.layers.concatenate([output1, output2], axis=1)

    output3 = tf.keras.layers.Dense(3, activation='relu', name='output3')(concat)
    output4 = tf.keras.layers.Dense(1, activation='sigmoid', name='output4')(output3)

    output5 = tf.keras.layers.Dense(3, activation='relu', name='output5')(concat)
    output6 = tf.keras.layers.Dense(1, activation='sigmoid', name='output6')(output5)

    model = tf.keras.Model([input1, input2], [output4, output6])

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])

    history = model.fit([x1, x2], [y1, y2], epochs=1000, verbose=2)
    print('acc :', model.evaluate([x1, x2], [y1, y2]))
    # acc : [0.7960159182548523, 0.6931471228599548, 0.10286880284547806, 0.5, 1.0]

    print(history.history.keys())
    # ['loss', 'output4_loss', 'output6_loss', 'output4_acc', 'output6_acc']

    # 에포크 출력 결과
    # loss: 0.0036 -
    # output4_loss: 0.0034 - output6_loss: 1.7471e-04 -
    # output4_acc: 1.0000 - output6_acc: 1.0000


# and_sequential()
# xor_sequential()
# xor_functional_basic()
xor_functional_multi_input()