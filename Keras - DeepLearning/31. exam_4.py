import tensorflow as tf
import numpy as np
from sklearn import model_selection
import urllib.request
import json

# 문제
# 기사 데이터에 대해 80% 이상의 정확도를 갖는 모델을 구축하세요.

# 다운완료 시 주석
# url = 'https://storage.googleapis.com/download.tensorflow.org/data/sarcasm.json'
# urllib.request.urlretrieve(url, 'data/sarcasm.json')

def get_xy():
    f = open('data/sarcasm.json', 'r', encoding='utf-8')
    articles = json.load(f)
    f.close()

    print(type(articles), len(articles), type(articles[0])) # <class 'list'> 26709 <class 'dict'>

    x, y = [], []
    for item in articles:
        # print(item)
        x.append(item['headline'])
        y.append(item['is_sarcastic'])

    return x, np.int32(y)

x, y = get_xy()

vocab_size, max_len = 2000 , 25
# 계속 이 4가지 순서
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(x)

x = tokenizer.texts_to_sequences(x)     # 숫자로 바꿈
x = tf.keras.preprocessing.sequence.pad_sequences(x, maxlen=max_len)

x_train, x_test, y_train, y_test = model_selection.train_test_split(x,y,train_size=0.8)
# -------------------------------------- #

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=[max_len]),
    tf.keras.layers.Embedding(vocab_size, 100),     # 입력(2차원), 출력(3차원)
    # tf.keras.layers.LSTM(21, return_sequences=False),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(21)), # rnn에서는 bidirection을 써보는게 좋음
    tf.keras.layers.Dense(1, activation='sigmoid'),
])
model.summary()

model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
              loss=tf.keras.losses.binary_crossentropy,
              metrics=['acc'])

model.fit(x_train, y_train, epochs=10, batch_size=32, verbose=2,validation_split=0.2)
print(model.evaluate(x_test, y_test, verbose=0))
