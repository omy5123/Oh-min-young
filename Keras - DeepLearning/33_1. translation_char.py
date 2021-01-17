import tensorflow as tf
import numpy as np

def make_vocab_and_index(data):
    # 문제
    # 영어 단어끼리, 한글 단어 끼리 모아주세요 (eng, kor)
    eng, kor = [], []
    for e, k in data:
        for c in e:
            eng.append(c)
        for c in k:
            kor.append(c)
    eng = sorted(set(eng))
    kor = sorted(set(kor))

    # vocab = eng + kor +['S','E','P']  # 리스트버전, start, end, pad
    vocab = ''.join(eng + kor)+'SEP'    # 문자열버전
    print(vocab)

    # 문제
    # 한글과 영어를 분리하지 말고 단어장을 만드세요
    vocab = sorted({c for e, k in data for c in e + k})
    vocab = ''.join(vocab) + 'SEP'
    print(vocab)        # {'a': 0, 'b': 1, 'd': 2, 'e': 3, 'f': 4, 'h': 5, 'i': 6, 'l': 7, 'm': 8, 'n': 9, 'o': 10, 'p': 11, 'r': 12, 'u': 13, 'w': 14, '구': 15, '나': 16, '람': 17, '랑': 18, '무': 19, '바': 20, '식': 21, '영': 22, '웅': 23, '음': 24, '전': 25, '파': 26, 'S': 27, 'E': 28, 'P': 29}

    token2idx = {c: i for i, c in enumerate(vocab)}
    print(token2idx)

    return token2idx, vocab

def make_xy(data, token2idx):
    onehot = np.eye(len(token2idx), dtype=np.float32)

    enc_inputs, dec_inputs, dec_output = [], [], []
    for eng, kor in data:
        # print(eng, kor)

        # 문제(seq2seq)
        # 나머지 두 개의 코드를 추가하세요.(decoder_incoder, target)
        encoder_in = [token2idx[c] for c in eng]  # 한글자씩 가져와서 숫자로 바꿔줌
        decoder_in = [token2idx[c] for c in 'S'+kor]
        target = [token2idx[c] for c in kor+'E']
        # print(eng_incoder)

        enc_inputs.append(onehot[encoder_in])
        dec_inputs.append(onehot[decoder_in])
        # dec_output.append(onehot[target])
        dec_output.append(target)       # 바로 위에 코드보다 y는 원핫으로 안바꾼게 더 좋음


    return np.float32(enc_inputs), np.float32(dec_inputs), np.float32(dec_output)


def show_translation_char(enc_inputs, dec_inputs, dec_output, token2idx, vocab):
    n_classes, n_hiddens = len(vocab), 128

    # 인코더
    enc_layer = tf.keras.layers.Input(shape=enc_inputs.shape[1:])   # (4, 30)
    _enc_output, enc_state = tf.keras.layers.SimpleRNN(n_hiddens, return_state=True)(enc_layer)

    # 디코더
    dec_layer = tf.keras.layers.Input(shape=dec_inputs.shape[1:])   # (3, 30)
    output = tf.keras.layers.SimpleRNN(n_hiddens, return_sequences=True)(dec_layer, initial_state=enc_state)    # state 사용하지 않음, initial_state로 state를 연결받음

    output = tf.keras.layers.Dense(n_classes, activation='softmax')(output)

    # 문제
    # 모델 객체를 만들고 compile과 fit함수를 호출하세요.
    model = tf.keras.Model([enc_layer, dec_layer], output)

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.sparse_categorical_crossentropy)

    model.fit([enc_inputs, dec_inputs], dec_output, epochs=100, verbose=2)

    # 문제
    # wood, hero에 대해서 번역 결과를 예측하세요 (predict 호출)
    new_data = [('wood', 'PP'), ('hero', 'PP')] # 패딩으로 채움

    enc_inputs, dec_inputs, _ = make_xy(new_data, token2idx)

    preds = model.predict([enc_inputs, dec_inputs])
    print(preds.shape)      # (2, 3, 30)

    preds_arg = np.argmax(preds, axis=2)
    print(preds_arg.shape)  # (2, 3)

    for tokens in preds_arg:
        # print([vocab[t] for t in tokens])
        print(''.join([vocab[t] for t in tokens[:-1]]))



data = [('food', '음식'), ('wood', '나무'), ('blue', '파랑'),
        ('lamp', '전구'), ('wind', '바람'), ('hero', '영웅')]

token2idx, vocab = make_vocab_and_index(data)

enc_inputs, dec_inputs, dec_output = make_xy(data, token2idx)
print(enc_inputs.shape, dec_inputs.shape, dec_output.shape)     # (6, 4, 30) (6, 3, 30) (6, 3)


show_translation_char(enc_inputs, dec_inputs, dec_output, token2idx, vocab)