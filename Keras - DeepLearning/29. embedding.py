import tensorflow_hub as hub
import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np

# 문제
# 텐서플로 허브에서 swivel 모델을 찾아보세요.

def embed_basic():
    url = 'https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1'
    sents = ['cat is on the mat', 'dog is in the fog']

    embed = hub.load(url)
    layer = hub.KerasLayer(url)

    print(embed(sents))         # tensor가 나옴
    print(embed(sents).numpy()) # numpy로 바꿔줌
    print(embed(sents).shape)   # (2, 20)

# embed_basic()


# 문제
# imdb 리뷰를 train, validation, test 데이터로 나눠서
# swivel 임베딩을 사용해서 정확도를 구하는 모델을 만드세요


def show_imdb_with_embed():
    train_set, valid_set, test_set = tfds.load(
        'imdb_review',
        split=['train[:60%]', 'train[60%:]', 'test'],
        as_supervised=True)      # 이 옵션을 주지 않으면 딕셔너리기 때문에 잘라낼 수 없다.

    train_set = train_set.suffle(train_set.cardinality()).batch(512)
    valid_set = valid_set.batch(512)
    test_set = test_set.batch(512)

    hub_layer = hub.KerasLayer(
        "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1",
        output_shape=[20],
        input_shape=[],
        dtype=tf.string,
        trainable=True,   # 여기 중요!!  # 이것을 넣으면 fine-tunning
    )

    model = tf.keras.Sequential()
    model.add(hub_layer)
    model.add(tf.keras.layers.Dense(16, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    model.summary()

    model.compile(optimizer=tf.keras.optimizers.RMSprop(0.0001),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])

    model.fit(train_set, epochs=1,verbose=2,validation_data=valid_set)

show_imdb_with_embed()