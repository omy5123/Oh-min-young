# 자격증 문제 1번
# 아래의 x, y의 데이터로 모델을 구축하세요. (리니어 리그레션, mae 오차 계산)
import tensorflow as tf
import numpy as np

x = [0, 1, 2, 3, 4, 5, 6]
y = [-3, -2, -1, 0, 1, 2, 3]

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1,activation=None))

model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.1),
              loss=tf.keras.losses.mse,
              metrics=['mae'])  # 이 부분을 알면 이거보고 판단하면됨 모르면 아래 코드

model.fit(x, y, epochs=100)

print(model.evaluate(x, y, verbose=0))

preds = model.predict(x)
preds = preds.reshape(-1) # 2차원 -> 1차원
print(preds)

print('mae :', np.mean(np.abs(preds - y)))  # 모르면 이 코드
