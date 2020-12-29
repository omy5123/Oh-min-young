import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn import preprocessing, model_selection

# 문제
# 전복 데이터를 80%로 학습하고 20%에 대해 정확도를 구하세요
# (3개의 클래스로 재구성: ring classes 1-8, 9 and 10, and 11 on)


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

def save_model_1():
    x_train, x_test, y_train, y_test = get_abalone()
    n_classes = len(set(y_train))
    model = build_model(n_classes)

    model.fit(x_train, y_train, epochs=10, verbose=0)
    print('acc :', model.evaluate(x_test, y_test))

    # acc : [0.7871922850608826, 0.6375598311424255] - non-scaling

    # model.save('model_abalone/keras.h5')  # keras방식 (저장되지 않는부분이 있음) - 수업시간에만 사용
    # model.save('model_abalone')     # tensorflow방식 실전에선 무조건 이것을 써야함!!!

    json = model.to_json()
    print(json)

    model_json = tf.keras.models.model_from_json(json)
    print(model.to_yaml())  # PyYAML 좋음 이것으로 많이 사용
    # model.save_weights()  # 로 가중치


def save_model_2_bug():
    x_train, x_test, y_train, y_test = get_abalone()
    n_classes = len(set(y_train))
    model = build_model(n_classes)

    model.fit(x_train, y_train, epochs=10, verbose=0)
    print('acc 1:', model.evaluate(x_test, y_test, verbose=0))

    model_path = 'model_abalone/bug.h5'
    model.save(model_path)

    saved_model = tf.keras.models.load_model(model_path)
    print('acc 2:', saved_model.evaluate(x_test, y_test, verbose=0))
    # acc 1: [0.7909393906593323, 0.6255980730056763]
    # acc 2: [0.7909393906593323, 0.309808611869812]

    preds = saved_model.predict(x_test)
    preds_arg = np.argmax(preds, axis=1)
    print(preds_arg[:10])
    print('acc 3:', np.mean(preds_arg == y_test))
    # acc 3: 0.6255980730056763

    # acc 2 는 버그..? 하여튼 이러한 일이 벌어짐
    saved_model.compile(optimizer='adam',
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['acc'])
    print('acc 4:', saved_model.evaluate(x_test, y_test, verbose=0))
    # acc 4: 0.6255980730056763
    
# save_model_1()
save_model_2_bug()