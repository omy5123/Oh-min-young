import tensorflow as tf
import numpy as np
import csv


_PAD_, _SOS_, _EOS_, _UNK_ = 0, 1, 2, 3

# 문제
# 단어장 파일을 읽어서 반환하는 함수를 만드세요.
def read_vocab():
    f = open('chat/vocab.txt', 'r', encoding='utf-8')
    vocab = f.readlines()
    # print(len(vocab))       # 164
    f.close()

    return vocab

# 문제
# 대화를 숫자로 변환한 vectors.txt 파일을 읽어서 반환하는 함수를 만드세요.
def read_vectors():
    f = open('chat/vectors.txt', 'r', encoding='utf-8')
    vectors = [[int(col) for col in row] for row in csv.reader(f)]
    # print(vectors[:3])      # [[105], [105], [114, 128, 85, 79]]
    f.close()

    return vectors

def add_pad(seq, max_len):
    seq_len = len(seq)
    if seq_len > max_len:
        return seq[:max_len]

    return seq + [_PAD_] * (max_len - seq_len)

def load_dataset():
    vocab = read_vocab()
    vectors = read_vectors()

    # 문제
    # 질문과 대답 데이터에서 가장 긴 토큰의 길이를 구하세요.
    dialog_questions = vectors[::2]
    dialog_answers = vectors[1::2]

    max_len_q = max([len(q) for q in dialog_questions])
    max_len_a = max([len(a) for a in dialog_answers]) + 1
    print(max_len_q, max_len_a)     # 9 10

    # ------------------------------------------------ #
    # 33_2 translation_word.py 파일에서 make_xy 함수 가져옴

    # 문제
    # 아래 코드에서 발생하는 에러를 올바르게 수정하세요

    onehot = np.eye(len(vocab), dtype=np.float32)

    enc_inputs, dec_inputs, dec_output = [], [], []
    for question, answer in zip(dialog_questions, dialog_answers):
        encoder_in = add_pad(question, max_len_q)  # 길이를 똑같이 맞춰줘야함
        decoder_in = add_pad([_SOS_] + answer, max_len_a)
        target = add_pad(answer + [_EOS_], max_len_a)
        # print(eng_incoder)

        enc_inputs.append(onehot[encoder_in])
        dec_inputs.append(onehot[decoder_in])
        # dec_output.append(onehot[target])
        dec_output.append(target)  # 바로 위에 코드보다 y는 원핫으로 안바꾼게 더 좋음

    return np.float32(enc_inputs), np.float32(dec_inputs), np.float32(dec_output), vocab


# 문제
# 어린왕자 데이터셋으로 챗봇 모델을 구축하세요. (fit 함수로 학습까지)

def train_and_save_chatbot():
    enc_inputs, dec_inputs, dec_output, vocab = load_dataset()
    print(enc_inputs.shape, dec_inputs.shape, dec_output.shape)  # (52, 9, 164) (52, 10, 164) (52, 10)

    # ---------------------------------------------- #
    # show_translation_word 함수를 수정없이 사용함. 에러없이 잘 동작
    n_classes, n_hiddens = len(vocab), 128

    # 인코더
    enc_layer = tf.keras.layers.Input(shape=enc_inputs.shape[1:])
    _enc_output, enc_state = tf.keras.layers.SimpleRNN(n_hiddens, return_state=True)(enc_layer)

    # 디코더
    dec_layer = tf.keras.layers.Input(shape=dec_inputs.shape[1:])
    output = tf.keras.layers.SimpleRNN(n_hiddens, return_sequences=True)(dec_layer,
                                                                         initial_state=enc_state)  # state 사용하지 않음, initial_state로 state를 연결받음

    output = tf.keras.layers.Dense(n_classes, activation='softmax')(output)

    model = tf.keras.Model([enc_layer, dec_layer], output)

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.sparse_categorical_crossentropy)

    model.fit([enc_inputs, dec_inputs], dec_output, epochs=500, verbose=2)

    model.save('chat/little_prince.h5')

train_and_save_chatbot()
