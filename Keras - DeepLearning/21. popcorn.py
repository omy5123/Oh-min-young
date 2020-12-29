# Day_29_01_popcorn.py
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gensim
import nltk
from sklearn import model_selection, feature_extraction, linear_model
import re


def tokenizing_and_padding(x, vocab_size, seq_len):
    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=vocab_size)
    tokenizer.fit_on_texts(x)

    # print(tokenizer.num_words)            # 2000
    # print(len(tokenizer.index_word))      # 88582
    # print(x[1])
    # \The Classic War of the ...

    x = tokenizer.texts_to_sequences(x)
    # print(x[1])
    # [1, 372, 276, 4, 1, ...]

    # 250개는 80%, 500개는 90%의 리뷰를 포함
    # freqs = sorted([len(t) for t in x])
    # plt.plot(freqs)
    # plt.show()

    x = tf.keras.preprocessing.sequence.pad_sequences(x, maxlen=seq_len)

    return x, tokenizer


# 문제
# 서브미션 파일을 만드세요
def make_submission(ids, preds, file_path):
    f = open(file_path, 'w', encoding='utf-8')

    f.write('"id","sentiment"\n')
    for i, p in zip(ids, preds):
        f.write('"{}",{}\n'.format(i, p))

    f.close()


# 사용 모델: baseline, rnn, cnn, cnn-tf.data
def make_submission_for_deep(ids, x_test, model, tokenizer, seq_len, file_path):
    x_test = tokenizer.texts_to_sequences(x_test)
    x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, maxlen=seq_len)

    preds = model.predict(x_test)
    preds_arg = preds.reshape(-1)
    preds_bool = np.int32(preds_arg > 0.5)
    # print(preds_bool[:10])            # [1 0 0 1 0 1 0 0 0 0]

    make_submission(ids, preds_bool, file_path)


def make_submission_for_word2vec(ids, x_test, model, word2vec, n_features, idx2word, file_path):
    x_test = [s.lower().split() for s in x_test]
    features = [make_features_for_word2vec(tokens, word2vec, n_features, idx2word) for tokens in x_test]
    x_test = np.vstack(features)

    preds = model.predict(x_test)
    make_submission(ids, preds, file_path)


# 사용 모델: word2vec, word2vec_nltk
# tokens: [the, in, happy, in, disney]
def make_features_for_word2vec(tokens, word2vec, n_features, idx2word):
    binds, n_words = np.zeros(n_features), 0

    for w in tokens:
        if w in idx2word:
            binds += word2vec.wv[w]
            n_words += 1

    return binds if n_words == 0 else binds / n_words


def model_baseline(x, y, ids, x_test):
    vocab_size, seq_len = 2000, 200
    x, tokenizer = tokenizing_and_padding(x, vocab_size, seq_len)

    # 문제
    # x, y 데이터를 80%로 학습하고 20%로 예측하는 모델을 구축하세요
    data = model_selection.train_test_split(x, y, train_size=0.8, shuffle=False)
    x_train, x_valid, y_train, y_valid = data

    # ------------------------------------- #

    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=[seq_len]),
        tf.keras.layers.Embedding(vocab_size, 100),         # 입력(2차원), 출력(3차원)
        tf.keras.layers.LSTM(128, return_sequences=False),
        tf.keras.layers.Dense(1, activation='sigmoid'),
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])

    model.fit(x_train, y_train, epochs=10, batch_size=128, verbose=2,
              validation_data=(x_valid, y_valid))

    # -----------------------------------------#

    make_submission_for_deep(ids, x_test, model, tokenizer, seq_len, 'popcorn_models/baseline.csv')


# tf-idf: Term Frequency-Inverse Document Frequency
def model_tfidf(x, y, ids, x_test):
    vocab_size, seq_len = 2000, 200
    x, tokenizer = tokenizing_and_padding(x, vocab_size, seq_len)
    # print(x.shape)              # (1000, 200)

    x = tokenizer.sequences_to_texts(x)

    tfidf = feature_extraction.text.TfidfVectorizer(
        min_df=0.0, analyzer='word', sublinear_tf=True,
        ngram_range=(1, 3), max_features=5000
    )
    x = tfidf.fit_transform(x)
    # print(x.shape)              # (1000, 5000)

    data = model_selection.train_test_split(x, y, train_size=0.8, shuffle=False)
    x_train, x_valid, y_train, y_valid = data

    # ------------------------------------- #

    linear_regression = linear_model.LogisticRegression(class_weight='balanced')
    linear_regression.fit(x_train, y_train)
    print('acc :', linear_regression.score(x_valid, y_valid))

    # -----------------------------------------#

    # 문제
    # tf-idf 알고리즘을 적용한 모델에 대해 서브미션 파일을 만드세요
    # (예측할 때는 predict 함수를 사용합니다)
    x_test = tokenizer.texts_to_sequences(x_test)
    x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, maxlen=seq_len)

    x_test = tokenizer.sequences_to_texts(x_test)
    x_test = tfidf.fit_transform(x_test)

    preds = linear_regression.predict(x_test)
    # print(preds)          # [1 1 1 ... 0 1 0]

    make_submission(ids, preds, 'popcorn_models/tfidf.csv')


def model_word2vec(x, y, ids, x_test):
    x = [s.lower().split() for s in x]

    n_features = 100
    word2vec = gensim.models.Word2Vec(x, workers=4, size=n_features, min_count=40, window=10, sample=0.001)

    idx2word = set(word2vec.wv.index2word)
    features = [make_features_for_word2vec(tokens, word2vec, n_features, idx2word) for tokens in x]

    # x = np.reshape(features, newshape=[-1, n_features])   # (1000, 100)
    x = np.vstack(features)                                 # (1000, 100)
    # print(x.shape)

    # 리뷰: [the, in, happy, in, disney]
    # the   : 1 0 0 0 0 0
    # in    : 0 0 1 0 0 0
    # happy : 0 0 0 0 0 1
    # in    : 0 0 1 0 0 0
    # disney: 0 0 0 0 0 0
    #       + -----------
    #         1 0 2 0 0 1 / 4

    data = model_selection.train_test_split(x, y, train_size=0.8, shuffle=False)
    x_train, x_valid, y_train, y_valid = data

    # ------------------------------------- #

    linear_regression = linear_model.LogisticRegression(class_weight='balanced')
    linear_regression.fit(x_train, y_train)
    print('acc :', linear_regression.score(x_valid, y_valid))

    # -----------------------------------------#

    # 문제
    # 앞의 코드를 사용해서 서브미션 파일을 만드세요
    make_submission_for_word2vec(
        ids, x_test, linear_regression, word2vec, n_features, idx2word,
        'popcorn_models/word2vec.csv'
    )


def model_word2vec_nltk(x, y, ids, x_test):
    # x = [s.lower().split() for s in x]

    tokenizer = nltk.RegexpTokenizer(r'\w+')
    sent_tokens = [tokenizer.tokenize(s.lower()) for s in x]
    # print(sent_tokens[0])   # ['with', 'all', 'this', 'stuff', ...]

    # 문제
    # stem 함수를 사용하면 어간을 추출할 수 있습니다
    # stem 함수를 사용해서 sent_stems 변수를 완성하세요
    st = nltk.stem.PorterStemmer()
    sent_stems = [[st.stem(w) for w in s] for s in sent_tokens]
    # print(sent_stems[0])    # ['with', 'all', 'thi', 'stuff', ...]

    # 문제
    # sent_stems로부터 불용어를 제거하세요
    stop_words = nltk.corpus.stopwords.words('english')
    # print(stop_words)       # ['i', 'me', 'my', 'myself', ...]
    sent_stops = [[w for w in s if w not in stop_words] for s in sent_stems]
    x = sent_stops

    # ------------------------------------- #
    # 아래 코드는 앞에 나온 model_word2vec 함수와 완벽하게 동일함

    n_features = 100
    word2vec = gensim.models.Word2Vec(x, workers=4, size=n_features, min_count=40, window=10, sample=0.001)

    idx2word = set(word2vec.wv.index2word)
    features = [make_features_for_word2vec(tokens, word2vec, n_features, idx2word) for tokens in x]
    x = np.vstack(features)                                 # (1000, 100)

    data = model_selection.train_test_split(x, y, train_size=0.8, shuffle=False)
    x_train, x_valid, y_train, y_valid = data

    # ------------------------------------- #

    linear_regression = linear_model.LogisticRegression(class_weight='balanced')
    linear_regression.fit(x_train, y_train)
    print('acc :', linear_regression.score(x_valid, y_valid))

    # -----------------------------------------#

    make_submission_for_word2vec(
        ids, x_test, linear_regression, word2vec, n_features, idx2word,
        'popcorn_models/word2vec_nltk.csv'
    )


# baseline 모델 확장
def model_rnn(x, y, ids, x_test):
    vocab_size, seq_len = 2000, 200
    x, tokenizer = tokenizing_and_padding(x, vocab_size, seq_len)

    data = model_selection.train_test_split(x, y, train_size=0.8, shuffle=False)
    x_train, x_valid, y_train, y_valid = data

    # ------------------------------------- #

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[seq_len]))
    model.add(tf.keras.layers.Embedding(vocab_size, 100))
    # model.add(tf.keras.layers.LSTM(64, return_sequences=True))
    # model.add(tf.keras.layers.LSTM(64, return_sequences=False))
    cells = [tf.keras.layers.LSTMCell(64) for _ in range(2)]
    multi = tf.keras.layers.StackedRNNCells(cells)
    model.add(tf.keras.layers.RNN(multi))
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])

    model.fit(x_train, y_train, epochs=10, batch_size=128, verbose=1,
              validation_data=(x_valid, y_valid))

    # -----------------------------------------#

    make_submission_for_deep(ids, x_test, model, tokenizer, seq_len, 'popcorn_models/rnn.csv')


# conv1d 사용
def model_cnn(x, y, ids, x_test):
    vocab_size, seq_len = 2000, 200
    x, tokenizer = tokenizing_and_padding(x, vocab_size, seq_len)

    data = model_selection.train_test_split(x, y, train_size=0.8, shuffle=False)
    x_train, x_valid, y_train, y_valid = data

    # ------------------------------------- #

    input = tf.keras.layers.Input(shape=[seq_len])

    embed = tf.keras.layers.Embedding(vocab_size, 100)(input)
    embed = tf.keras.layers.Dropout(0.5)(embed)

    conv1 = tf.keras.layers.Conv1D(128, 3, activation='relu')(embed)
    conv1 = tf.keras.layers.GlobalAvgPool1D()(conv1)

    model = tf.keras.Model(input, conv1)
    model.summary()
    return

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
                  loss=tf.keras.losses.binary_crossentropy,
                  metrics=['acc'])

    model.fit(x_train, y_train, epochs=10, batch_size=128, verbose=1,
              validation_data=(x_valid, y_valid))

    # -----------------------------------------#

    make_submission_for_deep(ids, x_test, model, tokenizer, seq_len, 'popcorn_models/rnn.csv')


# ------------------------------------------------------------------------------ #

popcorn = pd.read_csv('popcorn/labeledTrainData.tsv', delimiter='\t', index_col=0)
# print(popcorn)

x = popcorn.review.values
y = popcorn.sentiment.values.reshape(-1, 1)
# print(x.dtype, y.dtype)       # object int64

n_samples = 1000
# x, y = x[:n_samples], y[:n_samples]

test_set = pd.read_csv('popcorn/testData.tsv', delimiter='\t', index_col=0)
ids = test_set.index.values
x_test = test_set.review.values

# model_baseline(x, y, ids, x_test)
# model_tfidf(x, y, ids, x_test)
# model_word2vec(x, y, ids, x_test)
# model_word2vec_nltk(x, y, ids, x_test)
model_rnn(x, y, ids, x_test)
# model_cnn(x, y, ids, x_test)


# baseline: 0.8634
# tf-idf  : 0.8742
# word2vec: 0.8244
# nltk    : 0.8562
# rnn     : 0.8794
