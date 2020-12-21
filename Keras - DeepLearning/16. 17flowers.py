import tensorflow as tf
import numpy as np
import os
from PIL import Image   # Pillow 설치

from sklearn import model_selection

# 문제
# 17flowers_origin 폴더의 이미지를 (224, 224)로 줄여서 17flowers_224에 복사하세요.

def resize_17flowers(src_folder, dst_folder, new_size):
    if not os.path.exists(dst_folder):      # 224 폴더 없으면 만듬
        os.mkdir(dst_folder)

    for filename in sorted(os.listdir(src_folder)):
        if filename.startswith('.'):
            continue

        # print(filename)

        img_1 = Image.open(os.path.join(src_folder, filename))
        img_2 = img_1.resize([new_size, new_size])
        img_2.save(os.path.join(dst_folder, filename))

# resize_17flowers('17flowers_origin', '17flowers_56', new_size=56)
# resize_17flowers('17flowers_origin', '17flowers_112', new_size=112)
# resize_17flowers('17flowers_origin', '17flowers_224', new_size=224)

# 문제
# 17flowers 폴더를 읽어서 x, y 데이터를 반환하는 함수를 만드세요.
# x: 4차원
# y: 1차원(1~80은 0번, 81~160은 1번, ...)

def get_xy(data_folder):
    x, y = [], []
    for filename in os.listdir(data_folder):
        if filename.startswith('.'):
            continue

        items = filename.split('.')
        # idx = items[0][-4:]
        idx = items[0].split('_')[1] # 두개 같음

        # 1~80 -> 0~79
        y.append((int(idx)-1) // 80)

        # print(items, idx)    # ['image_1360', 'jpg'] 1360

        img_1 = Image.open(os.path.join(data_folder, filename)) # 이미지를 사용하려면 numpy로 바꿔야댐
        img_2 = np.array(img_1)
        # print(img_2.shape)

        x.append(img_2)

    return np.float32(x), np.int32(y)

def model_17flowers_dense():
    # x, y = get_xy('17flowers_56')
    x, y = get_xy('17flowers_112')
    # print(x.shape, y.shape)     # (1360, 56, 56, 3) (1360,)
    # print(y[:5])                # [0 0 0 0 0]

    x = x / 255     # 효과가 좋아짐

    # 17flowers 데이터셋에 대한 모델을 만드세요.
    # (학습은 80%, 검사는 20%로 진행합니다. 정확도를 구하세요)

    x_train, x_test, y_train, y_test = model_selection.train_test_split(x,y,train_size=0.8)

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[x.shape[1], x.shape[2], x.shape[3]]))


    model.add(tf.keras.layers.Conv2D(16, [3, 3], 1, 'same', activation='relu'))
    model.add(tf.keras.layers.MaxPool2D([2, 2], 2, 'same'))

    model.add(tf.keras.layers.Conv2D(32, [3, 3], 1, 'same', activation='relu'))
    model.add(tf.keras.layers.MaxPool2D([2, 2], 2, 'same'))

    model.add(tf.keras.layers.Conv2D(64, [3, 3], 1, 'same', activation='relu'))
    model.add(tf.keras.layers.MaxPool2D([2, 2], 2, 'same'))

    model.add(tf.keras.layers.Flatten())

    model.add(tf.keras.layers.Dense(1024, activation='relu'))
    model.add(tf.keras.layers.Dense(256, activation='relu'))
    model.add(tf.keras.layers.Dense(17, activation='softmax'))

    model.summary()

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),
              loss=tf.keras.losses.sparse_categorical_crossentropy,
              metrics=['acc'])

    model.fit(x_train, y_train, epochs=10, batch_size=32, verbose=2)
    print('acc :', model.evaluate(x_test, y_test, verbose=0))

# model_17flowers_dense()

# 문제
# 모델 마지막에 있는 dense 레이어를 conv2d로 교체하세요
# (원본 크기는 224를 사용합니다.)
def model_17flowers_conv2d():
    x, y = get_xy('17flowers_56')
    # print(x.shape, y.shape)     # (1360, 56, 56, 3) (1360,)
    # print(y[:5], y[-5:])                # [0 0 0 0 0]  [16 16 16 16 16]

    x = x / 255  # 효과가 좋아짐

    # 17flowers 데이터셋에 대한 모델을 만드세요.
    # (학습은 80%, 검사는 20%로 진행합니다. 정확도를 구하세요)

    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, train_size=0.8)

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[x.shape[1], x.shape[2], x.shape[3]]))

    model.add(tf.keras.layers.Conv2D(16, [3, 3], 1, 'same', activation='relu'))
    model.add(tf.keras.layers.MaxPool2D([2, 2], 2, 'same'))

    model.add(tf.keras.layers.Conv2D(32, [3, 3], 1, 'same', activation='relu'))
    model.add(tf.keras.layers.MaxPool2D([2, 2], 2, 'same'))

    model.add(tf.keras.layers.Conv2D(64, [3, 3], 1, 'same', activation='relu'))
    model.add(tf.keras.layers.MaxPool2D([2, 2], 2, 'same'))

    # 224와 112에서만 사용 (추가한다면)
    # model.add(tf.keras.layers.Conv2D(128, [3, 3], 1, 'same', activation='relu'))
    # model.add(tf.keras.layers.MaxPool2D([2, 2], 2, 'same'))

    # 224에서 만 사용 (추가한다면)
    # model.add(tf.keras.layers.Conv2D(128, [3, 3], 1, 'same', activation='relu'))
    # model.add(tf.keras.layers.MaxPool2D([2,ㅎㄴ다 2], 2, 'same'))

    model.add(tf.keras.layers.Conv2D(1024, [7, 7], 1, activation='relu'))
    model.add(tf.keras.layers.Conv2D(256, [1, 1], 1, activation='relu'))
    model.add(tf.keras.layers.Conv2D(17, [1, 1], 1, activation=None))
    model.add(tf.keras.layers.Reshape([17]))
    model.add(tf.keras.layers.Softmax())

    model.summary()

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['acc'])

    model.fit(x_train, y_train, epochs=10, batch_size=32, verbose=2)
    print('acc :', model.evaluate(x_test, y_test, verbose=0))

model_17flowers_conv2d()