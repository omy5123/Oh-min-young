import tensorflow as tf
import pandas as pd
import numpy as np
# 1.14버전 -> 2.3.x 버전

#문제
# jean 파일에 있는 온도 데이터를 리니어 리그레션을 사용해서 평균오차를 계산하세요.

def linear_regression_jena():
    jena = pd.read_csv('../data/jena_climate_2009_2016.csv', index_col=0)
    degc = jena['T (degC)'].values
    degc = degc[:1000]

    x, y = degc[:-144], degc[144:]


    # keras 시퀀셜 , 펑션얼 사용

    model = tf.keras.Sequential() # 차례대로 시퀀셜을 지나간다.
    model.add(tf.keras.layers.Dense(1)) # 이제 레이어를 추가한다. 방법 - tf.keras.layers.원하는거    모든 레이어는 대문자 ()안에는 y값 지금은 하나 만들거임

    model.compile(optimizer=tf.keras.optimizers.Adam(), #SGD,Adam는 객체처럼 사용
                  loss=tf.keras.losses.mse) #SGD가 그래디언트 디센트 임  여기서는 소문자.

    model.fit(x, y)
    model.fit(x,y,epochs=100,verbose=0) #verbose=0,1,2 0 : 하면 계산하는 값이 안나옴 (계산은함), 1 : 하면 많이나옴 , 2 : 적게나옴
    print('----------------')
    print(model.evaluate(x,y,verbose=0))

    preds = model.predict(x)
    print(preds.shape) #(856, 1)  잘못구동하다가 컴퓨터 나감 막 5만개 짜리하면 5만*5만하면 메모리 나감
    print(y.shape)  #(856,)
    print('mae :', np.mean(np.abs(preds.reshape(-1) - y)))

# linear_regression_jena()


#문제
# trees.csv 파일로 학습을 해서
# Girth가 10, Height가 75일 때와
# Girth가 15, Height가 80일 때의 Volume을 예측하세요.

def multiple_regression_trees():
    trees = pd.read_csv('../data/trees.csv', index_col=0) # index_col 첫번째줄이 내용들이라
    x = np.transpose([trees["Girth"], trees["Height"]])
    y = np.reshape(trees["Volume"].values, newshape=[-1,1])

    print(x.shape, y.shape)

    # -------------------------------------------------- #

    model = tf.keras.Sequential()  # 차례대로 시퀀셜을 지나간다.
    model.add(tf.keras.layers.Dense(1))  # 이제 레이어를 추가한다. 방법 - tf.keras.layers.원하는거    모든 레이어는 대문자 ()안에는 y값 지금은 하나 만들거임

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.1),  # SGD,Adam는 객체처럼 사용
                  loss=tf.keras.losses.mse,
                  metrics=['mae'])  # SGD가 그래디언트 디센트 임  여기서는 소문자.

    model.fit(x, y)
    model.fit(x, y, epochs=100, verbose=2)  # verbose=0,1,2 하면 계산하는 값이 안나옴 (계산은함)
    print('----------------')
    print(model.evaluate(x, y, verbose=0))

    # print(x[:2])
    xx = [[10,75],
          [15,80]]

    preds = model.predict(xx)
    print(preds)                # [[24.39051 ] [34.575256]]
    print(preds.reshape(-1))    # [21.423847 35.473557]


multiple_regression_trees()

# a = np.arange(6)
# b = a.reshape(-1,1)
# print(a.shape, b.shape)
# print(b-a)