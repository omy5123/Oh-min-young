# tuner 중요!!
import tensorflow as tf
import numpy as np
import kerastuner as kt         # keras-tuner

# 4.KerasMultiLayers.py(exam 2번) 파일 복사해서 함수로 사용

# 데이터셋 가져와서 return
def get_mnist():
    data = tf.keras.datasets.mnist.load_data()
    (x_train, y_train), (x_test,y_test) = data

    x_train = x_train.reshape(-1, 784)
    x_test = x_test.reshape(-1, 784)

    # 올바른 스케일링
    x_train = x_train / 255
    x_test = x_test / 255
    return x_train, x_test, y_train, y_test

# 모델 구축하는 부분
def model_builder(hp):
    # 지금 조합의 경우의 수는 9가지
    hp_units_1 = hp.Int('units_1', min_value=256, max_value=512, step=128)
    hp_lr = hp.Choice('lr',values=[0.1, 0.01, 0.001])
    # 가장 최선의 것을 찾을수 있음(시간 소모 줄어듬) 튜너를 쓰는이유
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(hp_units_1, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(256, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))

    model.compile(optimizer=tf.keras.optimizers.Adam(hp_lr),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['acc'])
    return model

# 결과를 만들어내는 부분
def optimize_hyper_parameter(tuner):
    x_train, x_test, y_train, y_test = get_mnist()

    # model.fit(x_train, y_train, epochs=10, batch_size=100, verbose=2, validation_data=(x_test, y_test))

    # search 매개변수는 fit함수의 것을 그대로 사용한다.
    tuner.search(x_train, y_train, epochs=10, batch_size=100, verbose=2, validation_split=0.2)

    # tuner.summary_space_summary()     # 중요 x
    tuner.results_summary()     # 이게 중요

    # 가장 좋은결과를 찾자 (최적의 파라미터를 찾는다)
    best_hps = tuner.get_best_hyperparameters(num_trials=3)
    print(type(best_hps))   # <class 'list'>
    print(best_hps[0])

    print(best_hps[0].get('units_1'))       # 512
    print(best_hps[0].get('lr'))            # 0.001

    # ---------------------------------- #

    # 우리 만의 베스트 모델을 만들자
    best_model = tuner.hypermodel.build(best_hps[0])
    best_model.fit(x_train, y_train, epochs=10, batch_size=100, verbose=2, validation_split=0.2)
    print('acc :', best_model.evaluate(x_test, y_test, verbose=0))


tuner_bayesian = kt.BayesianOptimization(
    model_builder,
    objective='val_acc',
    max_trials=5,
    directory='keras_tuner/bayesian',   # 따로 만들어주지 않아도 알아서 만들어줌
    project_name='mnist'
)

tuner_random_search = kt.RandomSearch(
    model_builder,
    objective='val_acc',
    max_trials=5,
    directory='keras_tuner/random_search',   # 따로 만들어주지 않아도 알아서 만들어줌
    project_name='mnist'
)

# 세가지중 hyperband 가 가장 잘찾는다 이거로 쓰면됨
tuner_hyperband = kt.Hyperband(
    model_builder,
    objective='val_loss',
    max_trials=5,
    directory='keras_tuner/hyperband',   # 따로 만들어주지 않아도 알아서 만들어줌
    project_name='mnist'
)


# optimize_hyper_parameter(tuner_bayesian)
# optimize_hyper_parameter(tuner_random_search)
optimize_hyper_parameter(tuner_hyperband)