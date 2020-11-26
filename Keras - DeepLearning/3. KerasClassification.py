import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn import preprocessing,model_selection

def logistic_regression():
    # x : 성적
    x = [[1, 2],      # fail
         [2, 1],
         [4, 5],      # pass 4명은 통과
         [5, 4],
         [8, 9],
         [9, 8]]

    y = [[0],[0],[1],[1],[1],[1]]  # 떨어진 : 0 , 붙은 : 1

    model = tf.keras.Sequential() # 모델만들기
    # activaition을 연결하는 방법 3가지 (문자열이 가독성이 좋다)
    # 첫번째 방법 , model.add(tf.keras.layers.Dense(1, activation=tf.keras.activations.sigmoid)) # 레이어추가 , sigmoid 연결
    # 두번째 방법 , model.add(tf.keras.layers.Dense(1, activation=tf.sigmoid))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid')) # 세번째 방법, 가독성이 좋다

    # z = tf.matmul(x, w) + b
    # hz = tf.nn.sigmoid(z)

    model.compile(optimizer=tf.keras.optimizers.SGD(lr= 0.1),
                  loss=tf.keras.losses.binary_crossentropy,   # binary는 0,1중에 선택할때 씀
                  metrics=['acc'])

    model.fit(x,y, epochs=100, verbose=2)
    print(model.evaluate(x,y, verbose=0))

    preds = model.predict(x)
    print(preds)

    preds_bool = (preds > 0.5)
    print(preds_bool)

    equals = (preds_bool == y)  # 최종적인 결과
    print(equals)
    print('acc :', np.mean(equals))

logistic_regression()

# 문제
# 피마 인디언 파일을 읽어서 70%로 학습하고 30%에 대해 정확도를 구하세요.
def logistic_regression_pima_1():
    # 데이터 불러오기
    pima = pd.read_csv('../data/pima-indians.csv')

    x = pima.values[:,:-1]
    # y = pima.values[:,-1:]
    y = pima.Outcome.values
    y = y.reshape(-1,1)

    print(x.shape,y.shape)  # (768, 8) (768, 1)

    x_train, x_test, y_train, y_test = model_selection.train_test_split(x,y,train_size=0.7)
    print(x_train.shape, x_test.shape)  # (537, 8) (231, 8)
    print(y_train.shape, y_test.shape)  # (537, 1) (231, 1)
    # --------------------------------------- #

    model = tf.keras.Sequential()  # 모델만들기
    # activaition을 연결하는 방법 3가지 (문자열이 가독성이 좋다)
    # 첫번째 방법 , model.add(tf.keras.layers.Dense(1, activation=tf.keras.activations.sigmoid)) # 레이어추가 , sigmoid 연결
    # 두번째 방법 , model.add(tf.keras.layers.Dense(1, activation=tf.sigmoid))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))  # 세번째 방법, 가독성이 좋다

    # z = tf.matmul(x, w) + b
    # hz = tf.nn.sigmoid(z)

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),
                  loss=tf.keras.losses.binary_crossentropy,  # binary는 0,1중에 선택할때 씀
                  metrics=['acc'])

    model.fit(x_train, y_train, epochs=100, batch_size=32, verbose=2)
    print(model.evaluate(x_test, y_test, verbose=0))

def logistic_regression_pima_2():
    # 데이터 불러오기
    pima = pd.read_csv('../data/pima-indians.csv')

    x = pima.values[:,:-1]
    # y = pima.values[:,-1:]
    y = pima.Outcome.values
    y = y.reshape(-1,1)

    print(x.shape,y.shape)          # (768, 8) (768, 1)

    x = preprocessing.scale(x)      # 표준화  y는 0,1이라 표준화할 필요 없음

    x_train, x_test, y_train, y_test = model_selection.train_test_split(x,y,train_size=0.7)
    print(x_train.shape, x_test.shape)  # (537, 8) (231, 8)
    print(y_train.shape, y_test.shape)  # (537, 1) (231, 1)
    # --------------------------------------- #

    model = tf.keras.Sequential()  # 모델만들기
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))  # 세번째 방법, 가독성이 좋다

    # z = tf.matmul(x, w) + b
    # hz = tf.nn.sigmoid(z)

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),
                  loss=tf.keras.losses.binary_crossentropy,  # binary는 0,1중에 선택할때 씀
                  metrics=['acc'])

    model.fit(x_train, y_train, epochs=100, batch_size=32, verbose=2,
              validation_data=(x_test, y_test))  # validation <-- 반드시 튜플로 전달, 리스트 안됨
    # print(model.evaluate(x_test, y_test, verbose=0)) <- 경진대회에서 못씀

def logistic_regression_pima_3():
    # 데이터 불러오기
    pima = pd.read_csv('../data/pima-indians.csv')

    x = pima.values[:,:-1]
    # y = pima.values[:,-1:]
    y = pima.Outcome.values
    y = y.reshape(-1,1)

    print(x.shape,y.shape)          # (768, 8) (768, 1)

    x = preprocessing.scale(x)      # 표준화  y는 0,1이라 표준화할 필요 없음

    # x_train, x_test, y_train, y_test = model_selection.train_test_split(x,y,train_size=0.7)
    # print(x_train.shape, x_test.shape)  # (537, 8) (231, 8)
    # print(y_train.shape, y_test.shape)  # (537, 1) (231, 1)
    # --------------------------------------- #

    model = tf.keras.Sequential()  # 모델만들기
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))  # 세번째 방법, 가독성이 좋다

    # z = tf.matmul(x, w) + b
    # hz = tf.nn.sigmoid(z)

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),
                  loss=tf.keras.losses.binary_crossentropy,  # binary는 0,1중에 선택할때 씀
                  metrics=['acc'])

    model.fit(x, y,
              epochs=100, batch_size=32, verbose=2,
              validation_split=(0.3))  # validation <-- 반드시 튜플로 전달, 리스트 안됨 data,split 주로씀 나머지는 잘안씀
                                       # split을 하면 epochs가 한번 끝나면 매번 나눠 학습시킴
    # print(model.evaluate(x, y_test, verbose=0))

def softmax_regression():
    # x : 성적
    x = [[1, 2],      # C학점
         [2, 1],
         [4, 5],      # B학점
         [5, 4],
         [8, 9],      # A학점
         [9, 8]]

    y = [[0,0,1],     # one-hot벡터로~
         [0,0,1],     # softmax는 이 위치가 중요
         [0,1,0],
         [0,1,0],
         [1,0,0],
         [1,0,0]]

    model = tf.keras.Sequential() # 모델만들기
    model.add(tf.keras.layers.Dense(3, activation='softmax')) #결과 3개니깐 3개

    # z = tf.matmul(x, w) + b
    # hz = tf.nn.softmax(z)   <- 여기 바뀜

    model.compile(optimizer=tf.keras.optimizers.SGD(lr= 0.1),
                  loss=tf.keras.losses.categorical_crossentropy,  # <- 여기 바뀜
                  metrics=['acc'])

    model.fit(x,y, epochs=100, verbose=2)
    print(model.evaluate(x,y, verbose=0))  #[0.6383450627326965, 0.8333333134651184]

    preds = model.predict(x)
    print(preds)

    preds_arg = np.argmax(preds, axis=1)
    y_arg = np.argmax(y, axis=1)
    print(preds_arg)
    print(y_arg)

    print('acc :', np.mean(preds_arg == y_arg))

def softmax_regression_iris():
    # 데이터 불러오기
    iris = pd.read_csv('../data/iris(150).csv')

    x = iris.values[:, :-1] # values로 넘파이로 바꿔야 shape 가능
    y = preprocessing.LabelEncoder().fit_transform(iris.Species)
    print(y)
    print(x.shape, y.shape) # (150, 5) (150,)
    print(x.dtype, y.dtype) # object int32

    x = preprocessing.scale(x)  # 이 방법도 됨
    # x = np.float32(x) # 타입 맞춰줘야댐

    model = tf.keras.Sequential() # 모델만들기
    model.add(tf.keras.layers.Dense(3, activation='softmax'))


    model.compile(optimizer=tf.keras.optimizers.SGD(lr= 0.1),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,  # <- 여기 바뀜
                  metrics=['acc'])

    model.fit(x,y, epochs=100, verbose=2)
    print(model.evaluate(x,y, verbose=0))

# logistic_regression_pima_1()
# logistic_regression_pima_2() # validation_data 씀 (0.7,0.3)으로 나눠서 훈련
# logistic_regression_pima_3()  # validation_split 씀 오히려 데이터를 안나눈게 더잘나옴

# softmax_regression()

softmax_regression_iris()