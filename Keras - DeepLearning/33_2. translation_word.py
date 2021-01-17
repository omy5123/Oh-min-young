import tensorflow as tf
import numpy as np

# 33. translation_char 복사해서 사용

# 문제
# char 버전의 모델을 word 버전으로 수정하세요.
def make_vocab_and_index(data):
    vocab = sorted({c for e, k in data for c in e.split() + k.split()})
    print(vocab)

    vocab = vocab + ['_SOS_', '_EOS_', '_PAD_']

    token2idx = {c: i for i, c in enumerate(vocab)}
    print(token2idx)

    return token2idx, vocab

def make_xy(data, token2idx):
    onehot = np.eye(len(token2idx), dtype=np.float32)

    enc_inputs, dec_inputs, dec_output = [], [], []
    for eng, kor in data:
        encoder_in = [token2idx[c] for c in eng.split()]
        decoder_in = [token2idx[c] for c in ['_SOS_']+kor.split()]
        target = [token2idx[c] for c in kor.split()+['_EOS_']]
        # print(eng_incoder)

        enc_inputs.append(onehot[encoder_in])
        dec_inputs.append(onehot[decoder_in])
        # dec_output.append(onehot[target])
        dec_output.append(target)       # 바로 위에 코드보다 y는 원핫으로 안바꾼게 더 좋음


    return np.float32(enc_inputs), np.float32(dec_inputs), np.float32(dec_output)


def show_translation_word(enc_inputs, dec_inputs, dec_output, token2idx, vocab):
    n_classes, n_hiddens = len(vocab), 128

    # 인코더
    enc_layer = tf.keras.layers.Input(shape=enc_inputs.shape[1:])
    _enc_output, enc_state = tf.keras.layers.SimpleRNN(n_hiddens, return_state=True)(enc_layer)

    # 디코더
    dec_layer = tf.keras.layers.Input(shape=dec_inputs.shape[1:])
    output = tf.keras.layers.SimpleRNN(n_hiddens, return_sequences=True)(dec_layer, initial_state=enc_state)    # state 사용하지 않음, initial_state로 state를 연결받음

    output = tf.keras.layers.Dense(n_classes, activation='softmax')(output)

    model = tf.keras.Model([enc_layer, dec_layer], output)

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.sparse_categorical_crossentropy)

    model.fit([enc_inputs, dec_inputs], dec_output, epochs=100, verbose=2)

    # 문제
    # wood, hero에 대해서 번역 결과를 예측하세요 (predict 호출)
    new_data = [('how many trees are there', '_PAD_ _PAD_ _PAD_ _PAD_'),
                ('we dont need the hero', '_PAD_ _PAD_ _PAD_ _PAD_')] # 패딩으로 채움

    enc_inputs, dec_inputs, _ = make_xy(new_data, token2idx)

    preds = model.predict([enc_inputs, dec_inputs])
    print(preds.shape)      # (2, 5, 57)

    preds_arg = np.argmax(preds, axis=2)
    print(preds_arg.shape)  # (2, 5)

    for tokens in preds_arg:
        # print([vocab[t] for t in tokens])
        print(' '.join([vocab[t] for t in tokens[:-1]]))


# 문제
# 단어 기반의 번역을 위한 데이터를 구축하세요.
data = [('did you have some food', '너는 음식 좀 먹었니'),
        ('how many trees are there', '거기에는 나무가 얼마나 있니'),
        ('i really like blue color', '나는 파랑색을 진짜 좋아해'),
        ('christmas lamp is so pretty', '크리스마스 전구가 너무 이쁘다'),
        ('where do wind come from', '바람은 어디에서 오는 것일까'),
        ('we dont need the hero', '우리에게 영웅은 필요하지 않아')]

token2idx, vocab = make_vocab_and_index(data)

enc_inputs, dec_inputs, dec_output = make_xy(data, token2idx)
print(enc_inputs.shape, dec_inputs.shape, dec_output.shape)     # (6, 5, 57) (6, 5, 57) (6, 5)


show_translation_word(enc_inputs, dec_inputs, dec_output, token2idx, vocab)