import tensorflow as tf
import numpy as np
from sklearn import datasets

# 문제
# linnerud 데이터셋에 대한 모델을 구축하세요 (mae 결과 표시)


# data = datasets.load_linnerud()
# print(data.keys())
# # ['data', 'feature_names', 'target', 'target_names', 'DESCR', 'data_filename', 'target_filename']
#
# print(data['feature_names'])    # ['Chins', 'Situps', 'Jumps']
# print(data['target_names'])     # ['Weight', 'Waist', 'Pulse']
#
# print(data['data'].shape)       # (20, 3)
# print(data['target'].shape)     # (20, 3)

x, y = datasets.load_linnerud(return_X_y=True)

input = tf.keras.layers.Input(shape=[3])    # x 피처가 3이라

# 1번
# output = tf.keras.layers.Dense(5, activation='relu')(input)
#
# weight = tf.keras.layers.Dense(1, activation=None)(output)
# waist = tf.keras.layers.Dense(1, activation=None)(output)
# pulse = tf.keras.layers.Dense(1, activation=None)(output)

# 2번
weight = tf.keras.layers.Dense(5, activation='relu')(input)
weight = tf.keras.layers.Dense(1, activation=None)(weight)

waist = tf.keras.layers.Dense(5, activation='relu')(input)
waist = tf.keras.layers.Dense(1, activation=None)(waist)

pulse = tf.keras.layers.Dense(5, activation='relu')(input)
pulse = tf.keras.layers.Dense(1, activation=None)(pulse)

model = tf.keras.Model(input, [weight, waist, pulse])
model.summary()

model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
              loss=tf.keras.losses.mse,
              metrics=['mae'])

y0, y1, y2 = y[:, :1], y[:, 1:2], y[:, 2:]  # 컬럼으로 나눠줘야댐
model.fit(x, [y0, y1, y2], epochs=10, verbose=2) # 리스트로 합체
print('acc :', model.evaluate(x, [y0, y1, y2]))
# loss - dense_1_loss - dense_2_loss - dense_3_loss -  dense_1_mae - dense_2_mae - dense_3_mae
# acc : [4286.95849609375,
# 3987.53466796875, 100.49102783203125, 198.9329376220703,
# 52.217796325683594, 8.572031021118164, 12.41090202331543]

y_splits = np.hsplit(y, [1, 2]) # [y0, y1, y2]와 y_split이 동일해짐
# print(type(y_splits), len(y_splits))            # <class 'list'> 3
# print(y_splits[0].shape, y_splits[1].shape)     # (20, 1) (20, 1)

print('acc :', model.evaluate(x, y_splits))
# acc : [4286.95849609375,
# 3987.53466796875, 100.49102783203125, 198.9329376220703,
# 52.217796325683594, 8.572031021118164, 12.41090202331543]

# print(y0.reshape(-1))
# print(y1.reshape(-1))
# print(y2.reshape(-1))
# print(y_splits[0].reshape(-1))
# print(y_splits[1].reshape(-1))
# print(y_splits[2].reshape(-1))

# ---------------------------- #
print('-' * 30)


# 문제
# predict 함수를 사용해서 직접 mae를 계산하세요
def show_mae(p, y):
    print('mae :', np.mean(np.abs(p - y), axis=0))


preds = model.predict(x)
print(type(preds), len(preds))

show_mae(preds[0], y0)
show_mae(preds[1], y1)
show_mae(preds[2], y2)

# 문제
# 아래 코드가 정확하게 동작하도록 수정하세요
show_mae(np.hstack(preds), y)
