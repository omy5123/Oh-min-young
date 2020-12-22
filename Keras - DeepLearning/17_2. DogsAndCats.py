import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import pickle
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def get_model_name(version):
    filename = 'dogcat_small_{}.h5'.format(version)
    return os.path.join('dogs_and_cats_model', filename)


def get_history_name(version):
    filename = 'dogcat_small_{}.history'.format(version)
    return os.path.join('dogs_and_cats_model', filename)


def show_history_ema(history, version):
    def get_ema(points, factor=0.8):
        smoothed = [points[0]]
        for pt in points[1:]:
            prev = smoothed[-1]
            smoothed.append(prev * factor + pt * (1 - factor))
        return smoothed

    loss1 = get_ema(history['val_loss'])
    loss2 = get_ema(history['loss'])

    acc1 = get_ema(history['val_acc'])
    acc2 = get_ema(history['acc'])

    epochs = np.arange(len(history['loss']))

    plt.subplot(1, 2, 1)
    plt.plot(epochs, loss1, 'r', label='valid')
    plt.plot(epochs, loss2, 'g', label='train')
    plt.title('loss {}'.format(version))
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(epochs, acc1, 'r', label='valid')
    plt.plot(epochs, acc2, 'g', label='train')
    plt.title('accuracy {}'.format(version))
    plt.legend()

    plt.show()


def show_history(history, version):
    plt.subplot(1, 2, 1)
    plt.plot(history['loss'], 'r', label='train')
    plt.plot(history['val_loss'], 'g', label='valid')
    plt.title('loss {}'.format(version))
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history['acc'], 'r', label='train')
    plt.plot(history['val_acc'], 'g', label='valid')
    plt.title('acc {}'.format(version))
    plt.legend()

    plt.show()


def save_history(history, version):
    with open(get_history_name(version), 'wb') as f:
        pickle.dump(history.history, f)     # dump에는 저장할 객체


def load_history(version):
    with open(get_history_name(version), 'rb') as f:
        history = pickle.load(f)            # load에는 파일
        show_history(history, version)
        # show_history_ema(history, version)


def load_model(version):
    model = tf.keras.models.load_model(get_model_name(version))
    # model.summary()

    test_gen = ImageDataGenerator(rescale=1/255)

    test_flow = test_gen.flow_from_directory(
        'dogs_and_cats/small/test',
        batch_size=1000,                # 검사 데이터 전체
        target_size=(150, 150),
        class_mode='binary'
    )

    # print('acc :', model.evaluate_generator(test_flow, steps=1, verbose=0))

    x_test, y_test = test_flow.next()
    print('acc :', model.evaluate(x_test, y_test, verbose=0))

def model_1_baseline():
    data_gen = ImageDataGenerator(rescale=1/255)

    batch_size = 32
    train_flow = data_gen.flow_from_directory(
        'dogs_and_cats/small/train',
        batch_size=batch_size,      # 한번에 가져올 이미지 갯수
        target_size=(150, 150),
        class_mode='binary'
    )
    valid_flow = data_gen.flow_from_directory(
        'dogs_and_cats/small/validation',
        batch_size=batch_size,
        target_size=(150, 150),
        class_mode='binary'
    )

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[150, 150, 3]))

    model.add(tf.keras.layers.Conv2D(32, [3, 3], activation='relu'))
    model.add(tf.keras.layers.MaxPool2D([2, 2]))
    model.add(tf.keras.layers.Conv2D(64, [3, 3], activation='relu'))
    model.add(tf.keras.layers.MaxPool2D([2, 2]))
    model.add(tf.keras.layers.Conv2D(128, [3, 3], activation='relu'))
    model.add(tf.keras.layers.MaxPool2D([2, 2]))
    model.add(tf.keras.layers.Conv2D(128, [3, 3], activation='relu'))
    model.add(tf.keras.layers.MaxPool2D([2, 2]))

    model.add(tf.keras.layers.Flatten())    # 3차원 -> 1차원으로 바꿀 플래튼
    model.add(tf.keras.layers.Dense(512, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))   # 로지스틱이라 1

    model.compile(optimizer=tf.keras.optimizers.RMSprop(0.0001),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])

    history = model.fit_generator(
        train_flow,
        epochs=10,
        steps_per_epoch=2000 // batch_size,
        validation_data=valid_flow,
        # validation_steps=batch_size,
        verbose=2,
    )

    model.save(get_model_name(version=1))
    save_history(history, version=1)


def model_2_augmentation():
    train_gen = ImageDataGenerator(     # train데이터는 증식
        rescale=1/255,
        horizontal_flip=True,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1,
        rotation_range=20,
    )
    valid_gen = ImageDataGenerator(     # valid에서는 이미지 증식 안함
        rescale=1/255,
    )

    batch_size = 32
    train_flow = train_gen.flow_from_directory(
        'dogs_and_cats/small/train',
        batch_size=batch_size,
        target_size=(150, 150),
        class_mode='binary'
    )
    valid_flow = valid_gen.flow_from_directory(
        'dogs_and_cats/small/validation',
        batch_size=batch_size,
        target_size=(150, 150),
        class_mode='binary'
    )

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[150, 150, 3]))

    model.add(tf.keras.layers.Conv2D(32, [3, 3], activation='relu'))
    model.add(tf.keras.layers.MaxPool2D([2, 2]))
    model.add(tf.keras.layers.Conv2D(64, [3, 3], activation='relu'))
    model.add(tf.keras.layers.MaxPool2D([2, 2]))
    model.add(tf.keras.layers.Conv2D(128, [3, 3], activation='relu'))
    model.add(tf.keras.layers.MaxPool2D([2, 2]))
    model.add(tf.keras.layers.Conv2D(128, [3, 3], activation='relu'))
    model.add(tf.keras.layers.MaxPool2D([2, 2]))

    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(512, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer=tf.keras.optimizers.RMSprop(0.0001),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])

    history = model.fit_generator(
        train_flow,
        epochs=10,
        steps_per_epoch=2000 // batch_size,
        validation_data=valid_flow,
        # validation_steps=batch_size,
        verbose=2,
    )

    model.save(get_model_name(version=2))
    save_history(history, version=2)


def model_3_pretrained():
    def extract_features(conv_base, data_gen, directory, sample_count, batch_size): # feature 추출하는 함수
        x = np.zeros([sample_count, 4, 4, 512])
        y = np.zeros([sample_count])

        flow = data_gen.flow_from_directory(
            directory,
            target_size=(150,150),
            batch_size=batch_size,
            class_mode='binary'
        )

        for ii, (xx, yy) in enumerate(flow):
            n1 = ii * batch_size
            n2 = n1 + batch_size

            # 문제
            # 마지막 자투리를 x, y에 추가하는 코드를 구현하세요
            if n2 > sample_count:
                remained = sample_count - n1
                x[n1:] = conv_base.predict(xx[:remained])
                y[n1:] = yy[:remained]
                break

            x[n1:n2] = conv_base.predict(xx)
            y[n1:n2] = yy

        return x.reshape(-1,4*4*512), y

    conv_base = tf.keras.applications.VGG16(
        include_top=False,      # dense layer는 안가져옴
        input_shape=[150, 150, 3],
    )
    conv_base.summary()

    batch_size = 32
    data_gen = ImageDataGenerator(rescale=1/255)

    x_train, y_train = extract_features(conv_base, data_gen, 'dogs_and_cats/small/train', 2000, batch_size)
    x_valid, y_valid = extract_features(conv_base, data_gen, 'dogs_and_cats/small/valid', 1000, batch_size)
    x_test, y_test = extract_features(conv_base, data_gen, 'dogs_and_cats/small/test', 1000, batch_size)

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[4 * 4 * 512]))

    model.add(tf.keras.layers.Dense(512, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer=tf.keras.optimizers.RMSprop(0.0001),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])

    history = model.fit(
        x_train, y_train,
        epochs=10, batch_size=batch_size, verbose=2,
        validation_data=(x_valid, y_valid)
    )

    # 모델을 저장하기는 하지만, 다른 모델과 호환은 되지 않는다. (입력 모양이 다름)
    model.save(get_model_name(version=3))
    save_history(history, version=3)

    print('acc :', model.evaluate(x_test, y_test))


def model_4_pretrained_augmentation():
    train_gen = ImageDataGenerator(     # train데이터는 증식
        rescale=1/255,
        horizontal_flip=True,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1,
        rotation_range=20,
    )
    valid_gen = ImageDataGenerator(     # valid에서는 이미지 증식 안함
        rescale=1/255,
    )

    batch_size = 32
    train_flow = train_gen.flow_from_directory(
        'dogs_and_cats/small/train',
        batch_size=batch_size,
        target_size=(150, 150),
        class_mode='binary'
    )
    valid_flow = valid_gen.flow_from_directory(
        'dogs_and_cats/small/validation',
        batch_size=batch_size,
        target_size=(150, 150),
        class_mode='binary'
    )

    conv_base = tf.keras.applications.VGG16(
        include_top=False,  # dense layer는 안가져옴
        input_shape=[150, 150, 3],
    )
    conv_base.trainable = False     # 학습하지 않겟어 -> 그러면 weight가 바뀌지 않음

    # 위에 처럼 말고 layer개별적으로 선택할수도 있다.
    #     for layer in conv_base.layers:
    #         print(layer.name)
    #         # layer.trainable = True
    #         if 'block5' in layer.name:
    #             layer.trainable = False

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[150, 150, 3]))
    model.add(conv_base)

    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(512, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer=tf.keras.optimizers.RMSprop(0.0001),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])

    history = model.fit_generator(
        train_flow,
        epochs=10,
        steps_per_epoch=2000 // batch_size,
        validation_data=valid_flow,
        # validation_steps=batch_size,
        # verbose=2,
    )

    model.save(get_model_name(version=4))
    save_history(history, version=4)



# model_1_baseline()
# model_2_augmentation()
model_3_pretrained()
# model_4_pretrained_augmentation()

# load_history(version=1)
# load_history(version=2)
# load_history(version=3)

# load_model(version=1)
# load_model(version=2)
# load_model(version=3)     # 입력 모양이 달라서 에러
# load_model(version=4)


# [3, 3] 필터 2개를 보틀넥으로 하는 부분 설명 부탁합니다.
# [1,1] + [3,3] +[1,1] 되는 부분
