import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn import preprocessing, model_selection


def get_abalone():
    names = ['Sex', 'Length', 'Diameter','Height','Whole','Shucked','Viscera','Shell','Rings']
    abalone = pd.read_csv('data/abalone.data',header=None, names=names)
    # print(abalone)

    y = []
    for r in abalone.Rings:
        if r <= 8:
            y.append(0)
        elif r <= 10:
            y.append(1)
        else:
            y.append(2)
    #                  1             8   10                                    29
    # categories = [-1,0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    categories = [-1]+[0]*8+[1]*2+[2]*19
    categories = np.int32(categories)

    y = categories[abalone.Rings]
    # y = categories[[3, 12, 21, 8, 10]]

    # 1번
    # x = abalone.values[:, 1:-1]
    # print(x.shape, x.dtype)     # (4177, 7) object
    # x = np.float32(x)           # object를 계속사용할수 없어서 float해줌

    # 2번
    x = abalone.drop(['Sex', 'Rings'],axis=1).values   # axis=0은 죽음
    # print(x.shape, x.dtype)     # (4177, 7) float64

    sex = preprocessing.LabelBinarizer().fit_transform(abalone.Sex) # 원핫 벡터로 하는것이 잴 좋음
    # print(sex[:3])    # [[0 0 1] [0 0 1] [1 0 0]]

    x = np.concatenate([sex, x], axis=1)
    x = np.hstack([sex, x]) # (4177, 10) 밑에랑 똑같음
    # print(x.shape)        # (4177, 10) 컬럼의 갯수 3개 추가되서 10개
    x = preprocessing.scale(x)

    return model_selection.train_test_split(x,y,train_size=0.8)

def build_model(n_classes):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(60, activation='relu'))
    model.add(tf.keras.layers.Dense(n_classes, activation='softmax'))

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['acc'])
    return model

def model_abalone():
    x_train, x_test, y_train, y_test = get_abalone()
    n_classes = len(set(y_train))
    model = build_model(n_classes)

    # 문제
    # x, y로 나누어진 데이터를 tf.data.Datasets 클래스로 변환하세요
    # 변환 데이터를 fit 함수에 넣어서 결과가 나오게 해주세요.
    # (20. chosun.py 파일에 있는 model_chosyn_2 함수참고)

    # 입력        출력
    # (4177,)    -> () scalar
    # (4177, 10) -> (10,)
    # (3, 4, 12) -> (4, 12)
    ds_train = tf.data.Dataset.from_tensor_slices((x_train, y_train))

    # for take in ds_train.take(2):
    #     print(type(take), len(take))

    # for xx, yy in zip(x_train, y_train):
    # for xx, yy in ds_train.take(2):
    #     print(xx, yy)
    #     print(xx.numpy(), yy.numpy())

    ds_train = ds_train.batch(32)

    model.fit(ds_train, epochs=10, verbose=2)
    # model.fit(ds_train.repeat(5), epochs=10, verbose=2)  repeat를 쓰는것이 나쁜건아니지만 지금상황은 안맞음
    print('acc :', model.evaluate(x_test, y_test))


model_abalone()