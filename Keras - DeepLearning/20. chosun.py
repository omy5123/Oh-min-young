# Day_28_02_chosun.py
import tensorflow as tf
import numpy as np
import re


# 텐서플로 2.0 프로그래밍
# # url = 'http://bit.ly/2Mc3SOV'
# url = 'https://raw.githubusercontent.com/greentec/greentec.github.io/master/public/other/data/chosundynasty/corpus.txt'
# file_path = tf.keras.utils.get_file(
#     'chosun.txt', url, cache_dir='.', cache_subdir='data')
# print(file_path)


def clean_str(string):
    string = re.sub(r"[^가-힣0-9]", " ", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)

    return string.strip()


def get_data():
    f = open('data/chosun.txt', 'r', encoding='utf-8')
    long_text = f.read()
    long_text = clean_str(long_text)
    long_text = long_text[:1000]
    f.close()

    tokens = long_text.split()
    vocab = ['UNK'] + sorted(set(tokens)) # unknown

    return tokens, vocab


def model_chosun_1():
    # 파일 읽기 -> 긴 문장 -> 토큰 분리 -> 인덱스로 변환 -> x, y 생성
    tokens, vocab = get_data()
    # print(len(tokens), len(vocab))        # 338 113

    word2idx = {w: i for i, w in enumerate(vocab)}
    # idx2word = {i: w for i, w in enumerate(vocab)}
    idx2word = np.array(vocab)

    # print(tokens[:5])                   # ['태조', '이성계', '선대의', '가계', '목조']
    # print(list(word2idx.items())[:3])   # [(',', 0), ('001', 1), ('002', 2)]
    # print(idx2word[:3])                 # [',' '001' '002']

    # tokens_idx = [vocab.index(w) for w in tokens] 밑에랑 같은코드 인덱스 위치 알려줌 (list)
    tokens_idx = [word2idx[w] for w in tokens]  # 위에랑 비교해서 훨씬 빠르다 (dict)라서
    # print(tokens_idx[:5])               # [104, 74, 47, 6, 34]

    # 25글자로 그 다음 글자 예측
    seq_len, vocab_size = 25, len(vocab)

    x = [tokens_idx[i:i+seq_len] for i in range(len(tokens) - seq_len)]
    y = [tokens_idx[i+seq_len] for i in range(len(tokens) - seq_len)]
    # print(x[0])     # [104, 74, 47, 6, 34, 79, 92, 45, 68, 8, 59, 93, 104, 7, 94, 12, 48, 56, 28, 4, 5, 67, 49, 77, 4]
    # print(y[:5])    # [5, 64, 0, 111, 4]

    # 모델 구축
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=[seq_len]),
        tf.keras.layers.Embedding(vocab_size, 100),  # 12-2navermovie 참조 임베딩 필수!!(원핫으로 하면 메모리 상상초과) 입력(2차원), 출력(3차원)
        tf.keras.layers.LSTM(128, return_sequences=False),
        tf.keras.layers.Dense(vocab_size, activation='softmax'),
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['acc'])

    model.fit(x, y, epochs=10, batch_size=32, verbose=2)
    model.save('data/chosun_model_1.h5')

    # sent = '동헌에 나가 활을 쏘다'
    # act_like_writer_1(sent, model, word2idx, idx2word, seq_len)

def model_chosun_2():
    # 파일 읽기 -> 긴 문장 -> 토큰 분리 -> 인덱스로 변환 -> x, y 생성
    tokens, vocab = get_data()

    word2idx = {w: i for i, w in enumerate(vocab)}
    idx2word = np.array(vocab)

    tokens_idx = [word2idx[w] for w in tokens]  # 위에랑 비교해서 훨씬 빠르다 (dict)라서

    # 25글자로 그 다음 글자 예측
    seq_len, vocab_size = 25, len(vocab)

    # x = [tokens_idx[i:i+seq_len] for i in range(len(tokens) - seq_len)]
    # y = [tokens_idx[i+seq_len] for i in range(len(tokens) - seq_len)]

    # Dataset 생성 -> (seq_len+1) 분할 -> (x, y) 튜플 변환 -> 셔플 -> 배치 크기 분할 -> 원하는 만큼 무제한 반복
    sent_slices = tf.data.Dataset.from_tensor_slices(tokens_idx)
    # print(type(sent_slices))
    # print(sent_slices.take(2))

    # for takes in sent_slices.take(2):
    #     print(takes.numpy(), takes)
    # 195 tf.Tensor(195, shape=(), dtype=int32)
    # 150 tf.Tensor(150, shape=(), dtype=int32)

    sent_sequences = sent_slices.batch(seq_len+1, drop_remainder=True) # 자투리 버림
    # for takes in sent_sequences.take(2):
    #    print(takes.numpy())
    # [195 150 105  11  75 155 175 100 141 ...  107 153 131 208  47  48]
    # [156 167  47  31 146  35 208  47 150 ...  160 142 115 124  85 196]

    sent_xy = sent_sequences.map(lambda chunk: (chunk[:-1], chunk[-1])) # (x, y)튜플로 변환한 부분

    # for xx, yy in sent_xy.take(2):
    #     print(xx.numpy(), yy.numpy())
    # [195 150 105  11  75 155 175 ... 51 138 107 153 131 208  47] 48
    # [156 167  47  31 146  35 208 ... 91 208 160 142 115 124  85] 196

    steps_per_epoch = len(tokens_idx) // (seq_len+1)
    sent_shuffled = sent_xy.shuffle(buffer_size=steps_per_epoch)
    # for xx, yy in sent_shuffled.take(2):
    #     print(xx.numpy(), yy.numpy())
    # [156 167  47  31 146  35 208  ...  91 208 160 142 115 124  85] 196
    # [137  42 190 208  21 137  42  ...  208 184  73  42 185 208  32] 137

    # 문제
    # sent_batches에 들어있는 값을 출력하세요.
    batch_size = 32
    sent_batches = sent_shuffled.batch(batch_size)
    # for xx, yy in sent_batches.take(2):
    #    print(xx.shape, yy.shape)       # (12, 25) (12,)

    sent_infinite = sent_batches.repeat()

    # 모델 구축
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=[seq_len]),
        tf.keras.layers.Embedding(vocab_size, 100),  # 12-2navermovie 참조 임베딩 필수!!(원핫으로 하면 메모리 상상초과) 입력(2차원), 출력(3차원)
        tf.keras.layers.LSTM(128, return_sequences=False),
        tf.keras.layers.Dense(vocab_size, activation='softmax'),
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['acc'])

    model.fit(sent_infinite, epochs=10, steps_per_epoch=steps_per_epoch, verbose=2)
    model.save('data/chosun_model_2.h5')

    sent = '동헌에 나가 활을 쏘다'
    # act_like_writer_1(sent, model, word2idx, idx2word, seq_len)



def act_like_writer_1(sent, model, word2idx, idx2word, seq_len):
    current = sent.split()

    for i in range(100):
        tokens = current[-seq_len:] # 맨밑 주석부분
        tokens_idx = [word2idx[w] if w in word2idx else word2idx['UNK'] for w in tokens]

        tokens_pad = tf.keras.preprocessing.sequence.pad_sequences( # pad_sequences는 2차원만 받는다
            [tokens_idx], maxlen=seq_len, value=word2idx['UNK']     # 그래서 2차원만들어줌
        )

        preds = model.predict(tokens_pad)
        # print(preds.shape)                # (1, 113)
        # preds_arg = np.argmax(preds, axis=1)
        preds_arg = np.argmax(preds[0])     # argmax를 통해 위치 찾음
        # print(preds_arg)                  # 4

        current.append(idx2word[preds_arg])

    print(current)

def act_like_writer_2(sent, model, word2idx, idx2word, seq_len):
    TOKEN_UNK = word2idx['UNK']
    current = [word2idx[w] if w in word2idx else TOKEN_UNK for w in sent.split()]

    filled = seq_len - len(current)
    if filled <= 0:
        filled = 0
    else:
        # current = current + [TOKEN_UNK] * filled      # difficult
        current = [TOKEN_UNK] * filled + current

    for i in range(100):
        tokens_idx = current[-seq_len:]
        # tokens_pad = [tokens_idx]             # 25번째에서 에러
        tokens_pad = np.array([tokens_idx])

        preds = model.predict(tokens_pad)
        preds_arg = np.argmax(preds[0])

        # print(i, preds_arg, idx2word[preds_arg])
        current.append(preds_arg)

    valid = current[filled + len(sent.split()):]
    print(sent, ' '.join(idx2word[valid]))

# 문제
# 모델을 읽어와서 전달받은 문장으로부터 새로운 문장을 생성하는 함수를 만드세요.
def load_model(sent, model_path):
    tokens, vocab = get_data()

    word2idx = {w: i for i, w in enumerate(vocab)}
    idx2word = np.array(vocab)

    model = tf.keras.models.load_model(model_path)
    # act_like_writer_1(sent, model, word2idx, idx2word, seq_len=25)
    act_like_writer_2(sent, model, word2idx, idx2word, seq_len=25)


# model_chosun_1()
model_chosun_2()

# load_model('동헌에 나가 활을 쏘다', 'data/chosun_model_1.h5')
# load_model('태조 이성계 아들 이방헌', 'data/chosun_model_1.h5')

load_model('태조 이성계 아들 이방헌', 'data/chosun_model_2.h5')

# [h e l l o] k라는 새로운 글자 얻음
# [e l l o k] t
# [l l o k t]
