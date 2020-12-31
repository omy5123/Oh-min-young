import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn import preprocessing, model_selection

# 문제
# 자동차 데이터에 대해 80%로 학습하고 20%에 대해 정확도를 구하세요


# sparse : LabelEncoder
def get_cars_sparse():
    names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'acc']
    cars = pd.read_csv('data/car.data', header=None, names=names)
    # print(cars)

    enc = preprocessing.LabelEncoder()

    buying = enc.fit_transform(cars.buying)
    maint = enc.fit_transform(cars.maint)
    doors = enc.fit_transform(cars.doors)
    persons = enc.fit_transform(cars.persons)
    lug_boot = enc.fit_transform(cars.lug_boot)
    safety = enc.fit_transform(cars.safety)
    acc = enc.fit_transform(cars.acc)
    # print(buying.shape, maint.shape)    # (1728,) (1728,)

    data = np.transpose([buying, maint, doors, persons, lug_boot, safety, acc])
    print(data.shape)                     # (1728, 7)

    # ---------------------------------------------- #
    train_size = int(len(data) * 0.8)

    ds_train = tf.data.Dataset.from_tensor_slices(data[train_size:])
    ds_train = ds_train.map(lambda chunk: (chunk[:-1], chunk[-1]))
    ds_train = ds_train.batch(32, drop_remainder=True)

    ds_test = tf.data.Dataset.from_tensor_slices(data[train_size:])
    ds_test = ds_test.map(lambda chunk: (chunk[:-1], chunk[-1]))
    ds_test = ds_test.batch(32, drop_remainder=True)

    return ds_train, ds_test

# 문제
# 데이터를 원핫 벡터로 만들어서 반환하는 get_cats_dense 함수를 만들고
# 그에 따라 발생하는 에러도 수정하세요.

# dense : LabelBinarizer
def get_cars_dense():
    names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'acc']
    cars = pd.read_csv('data/car.data', header=None, names=names)
    # print(cars)

    enc = preprocessing.LabelBinarizer()

    buying = enc.fit_transform(cars.buying)
    maint = enc.fit_transform(cars.maint)
    doors = enc.fit_transform(cars.doors)
    persons = enc.fit_transform(cars.persons)
    lug_boot = enc.fit_transform(cars.lug_boot)
    safety = enc.fit_transform(cars.safety)
    # print(buying.shape, maint.shape)      # (1728, 4) (1728, 4)
    # print(buying[:3])                     # [[0 0 0 1] [0 0 0 1] [0 0 0 1]]

    # acc = enc.fit_transform(cars.acc)
    # acc = np.argmax(acc, axis=1).reshape(-1, 1)
    acc = preprocessing.LabelEncoder().fit_transform(cars.acc)
    acc = acc.reshape(-1, 1)
    # print(acc.shape)        # (1728, 1)
    # print(acc[:3])          # [[2] [2] [2]]

    data = np.hstack([buying, maint, doors, persons, lug_boot, safety, acc])
    # print(data.shape)                     # (1728, 25)

    # ----------------------------------------------- #

    train_size = int(len(data) * 0.8)

    ds_train = tf.data.Dataset.from_tensor_slices(data[:train_size])
    ds_train = ds_train.map(lambda chunk: (chunk[:-1], chunk[-1]))
    ds_train = ds_train.batch(32, drop_remainder=True)

    ds_test = tf.data.Dataset.from_tensor_slices(data[train_size:])
    ds_test = ds_test.map(lambda chunk: (chunk[:-1], chunk[-1]))
    ds_test = ds_test.batch(32, drop_remainder=True)

    return ds_train, ds_test


# 이전 파일에서 가져온 함수
def build_model(n_classes):
    model = tf.keras.Sequential()
    # model.add(tf.keras.layers.Dense(60, activation='relu'))
    model.add(tf.keras.layers.Dense(n_classes, activation='softmax'))

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['acc'])
    return model


class EveryBatch(tf.keras.callbacks.Callback):
    def __init__(self):
        self.batch_loss = []
        self.batch_acc = []
    def on_batch_begin(self, batch, logs=None):
        print('on_batch_begin :', batch, logs)

    def on_batch_end(self, batch, logs=None):
        print('on_batch_end :', batch, logs)

        self.batch_loss.append(logs['loss'])
        self.batch_acc.append(logs['acc'])

# ds_train, ds_test = get_cars_sparse()
ds_train, ds_test = get_cars_dense()
model = build_model(4)

# checkpoint = tf.keras.callbacks.ModelCheckpoint('model_callback/first.h5')
# checkpoint = tf.keras.callbacks.ModelCheckpoint(
#     'model_callback/keras_{epoch:03d}_val_loss_{val_loss:.4f}.h5')
checkpoint = tf.keras.callbacks.ModelCheckpoint(
    'model_callback/keras_val_acc_{epoch:03d}_{val_acc:.4f}.h5',
    monitor='val_acc',
    save_best_only=True,    # 점점 좋아지는 상태로 저장이됨 안좋은것이 나오면 스킵
)

early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_acc', patience=10,
)

model.fit(ds_train, epochs=30, verbose=2,
          validation_data=ds_test,
          callbacks=[checkpoint, early_stopping])
# print('acc :', model.evaluate(ds_test))
