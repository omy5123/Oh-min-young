# https://archive.ics.uci.edu/ml/index.php
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn import preprocessing, model_selection
import collections

# 문제
# wdbc 데이터에 대해 70%로 학습하고 30%에 대해 정확도를 구하세요

def get_data():
    #    1. Sample code number            id number
    #    2. Clump Thickness               1 - 10
    #    3. Uniformity of Cell Size       1 - 10
    #    4. Uniformity of Cell Shape      1 - 10
    #    5. Marginal Adhesion             1 - 10
    #    6. Single Epithelial Cell Size   1 - 10
    #    7. Bare Nuclei                   1 - 10
    #    8. Bland Chromatin               1 - 10
    #    9. Normal Nucleoli               1 - 10
    #   10. Mitoses                       1 - 10
    #   11. Class:                        (2 for benign, 4 for malignant)

    names = ['Clump', 'Size', 'Shape', 'Adhesion',
             'Epithelial', 'Nuclei', 'Chromatin', 'Nucleoli', 'Mitoses', 'Class']

    wdbc = pd.read_csv('../data/breast-cancer-wisconsin.data',
                       header=None,
                       index_col=0,names=names)
    print(wdbc)
    wdbc.info()
    print('-'*50)
    for col in wdbc.columns:
        # print(col,set(wdbc[col]))
        print(col, wdbc[col].unique()) # pd 사용
    # Clump {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # Size {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # Shape {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # Adhesion {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # Epithelial {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # Nuclei {'1', '4', '3', '7', '2', '5', '6', '10', '9', '8', '?'}
    # Chromatin {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # Nucleoli {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # Mitoses {1, 2, 3, 4, 5, 6, 7, 8, 10}
    # Class {2, 4}

    # 1번
    freq = wdbc['Nuclei'].value_counts()
    print(freq)
    print(freq[0], freq[-1])     # 402 4
    print(freq.index[0])         # 1

    # 2번
    # freq = collections.Counter(wdbc['Nuclei'])
    # print(freq)
    print('-' * 50)
    missing_values = (wdbc.Nuclei == '?')
    # missing_values = (wdbc.Nuclei == '?').values
    print(missing_values)

    nuclei = wdbc.Nuclei.values
    nuclei[missing_values] = freq.index[0]  # 가장많은 값 (최빈값)
    print(nuclei.dtype)                     # object

    nuclei = nuclei[:, np.newaxis]          # hstack에 사용하기 위해 2차원으로 변환
    print(nuclei.shape)     # (699, 1)

    # ---------------------------------------- #

    x = wdbc.values[:, :-1]
    x = np.hstack([x[:, :6], nuclei, x[:,7:]])
    print(x.shape, x.dtype)

    x = np.float32(x)
    y = preprocessing.LabelEncoder().fit_transform(wdbc['Class'])
    y = y[:,np.newaxis] # y의 shape이 안맞을거 같으면 evaluate에 넣어본다.
    print(x.shape, y.shape, x.dtype)        # (699, 9) (699, 1) float32

    return model_selection.train_test_split(x, y, train_size=0.7)

def model_breast_cancer():
    x_train, x_test, y_train, y_test = get_data()

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[x_train.shape[1]]))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))  # 로지스틱 리그레션은 시그모이드
    model.summary()

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])

    model.fit(x_train, y_train, epochs=100,batch_size=32, verbose=2)
    print('loss, acc :', model.evaluate(x_test, y_test, verbose=0))


# 문제
# 앞에서 풀었던 코드를 소프트맥스 sparse 버전으로 수정하세요
def model_breast_cancer_softmax_sparse():
    x_train, x_test, y_train, y_test = get_data()

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[x_train.shape[1]]))
    model.add(tf.keras.layers.Dense(2, activation='softmax'))
    model.summary()

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['acc'])

    model.fit(x_train, y_train, epochs=100,batch_size=32, verbose=2)
    print('loss, acc :', model.evaluate(x_test, y_test, verbose=0))

# 문제
# 앞에서 풀었던 코드를 소프트맥스 dense 버전으로 수정하세요. (원핫 벡터 사용)
def model_breast_cancer_softmax_dense():
    x_train, x_test, y_train, y_test = get_data()
    # print(y_train[:10])
    # 1번
    #     y_train = [(1, 0) if i == 0 else (0, 1) for i in y_train.reshape(-1)]
    #     y_test = [(1, 0) if i == 0 else (0, 1) for i in y_test.reshape(-1)]
    #     # print(y_train[:10])
    #
    #     y_train = np.float32(y_train)
    #     y_test = np.float32(y_test)

    # 2번
    onehot = np.eye(2)
    print(onehot)

    y_train = onehot[y_train.reshape(-1)]
    y_test = onehot[y_test.reshape(-1)]
    print(y_train[:10])

    # --------------------------- #
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[x_train.shape[1]]))
    model.add(tf.keras.layers.Dense(2, activation='softmax'))
    model.summary()

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
                  loss=tf.keras.losses.categorical_crossentropy,  # categorical을 하려면 y data가 원핫으로 되있어야함
                  metrics=['acc'])

    model.fit(x_train, y_train, epochs=100,batch_size=32, verbose=2)
    print('loss, acc :', model.evaluate(x_test, y_test, verbose=0))


# model_breast_cancer()
# model_breast_cancer_softmax_sparse()
model_breast_cancer_softmax_dense()

# 결과는 차이 없음
# loss, acc : [0.11780621111392975, 0.976190447807312]      binary
# loss, acc : [0.08119744062423706, 0.9666666388511658]     softmax
# loss, acc : [0.11960536241531372, 0.9428571462631226]     softmax

# sparse: [0 0 1 1 2 2]
# dense: [[1 0 0] [1 0 0] [0 1 0] [0 1 0] [0 0 1] [0 0 1]]