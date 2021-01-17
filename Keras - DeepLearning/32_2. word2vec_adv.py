import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import gensim

# tokens추가
def extract(token_count, center, window_size, tokens):
    start = max(center - window_size, 0)
    end = min(center + window_size + 1, token_count)
    return [tokens[i] for i in range(start, end) if i != center]


def make_vocab_and_index(corpus, stop_words):
    # 문제
    # 코퍼스에서 불용어를 제외한 토큰 목록으로 변환하세요
    # 'king is a strong man' -> ['king', 'strong', 'man']
    def remove_stop_words(corpus, stop_words):
        # print([s for s in corpus])
        # ['king is a strong man', 'queen is a wise woman', ...]

        # print([s.split() for s in corpus])
        # [['king', 'is', 'a', 'strong', 'man'], ['queen', 'is', 'a', 'wise', 'woman'], ...]

        # print([[t for t in s.split() if t not in stop_words] for s in corpus])
        # [['king', 'strong', 'man'], ['queen', 'wise', 'woman'], ...]

        return [[t for t in s.split() if t not in stop_words] for s in corpus]

    # 문제
    # 단어장을 구하는 함수를 만드세요 (1차원 반환)
    def make_vocab(corpus):
        # return [t for tokens in corpus for t in tokens]
        # return {t for tokens in corpus for t in tokens}
        return sorted({t for tokens in corpus for t in tokens})

    corpus_by_word = remove_stop_words(corpus, stop_words)
    print(corpus_by_word)
    # [['king', 'strong', 'man'], ['queen', 'wise', 'woman'], ...]

    vocab = make_vocab(corpus_by_word)
    print(vocab)
    # ['boy', 'girl', 'king', 'man', 'pretty', 'prince', 'princess', 'queen', 'strong', 'wise', 'woman', 'young']

    corpus_idx = [[vocab.index(t) for t in tokens] for tokens in corpus_by_word]
    print(corpus_idx)
    # king - 2, strong - 8, man - 3
    # [[2, 8, 3], [7, 9, 10], [0, 11, 3], [1, 11, 10], [5, 11, 2], [6, 11, 7], [3, 8], [10, 4], [5, 0, 2], [6, 1, 7]]

    return corpus_idx, vocab


def build_dataset(corpus_idx, n_classes, window_size, is_skipgram):
    xx, yy = [], []
    for tokens in corpus_idx:       # [[2, 8, 3], [7, 9, 10], ...]
        for center_idx, center_token in enumerate(tokens):
            # print(center_idx, center_token, tokens)

            surround = extract(len(tokens), center_idx, window_size, tokens)
            # print(surround)

            if is_skipgram:
                for neighbor in surround:
                    xx.append(center_token)
                    yy.append(neighbor)
            # cbow
            else:
                xx.append(surround)
                yy.append(center_token)

    print(xx[:5])  # skip-gram [2, 8, 8, 3, 7] cbow [[8], [2, 3], [8], [9], [7, 10]]
    print(yy[:5])  # [8, 2, 3, 8, 9] y값은 동일

    # 더좋은 결과를 위해 원핫벡터를 만든다.
    return make_onehot(xx,n_classes,is_skipgram), np.int32(yy)

def make_onehot(xx, n_classes, is_skipgram):
    x = np.zeros([len(xx), n_classes], dtype=np.float32)

    for i, input in enumerate(xx):
        if is_skipgram:     # input : 한 자리 숫자
            x[i, input] = 1 # 특정한 행의 위치만 덮어씀

        else:               # input : 인덱스 리스트
            # for pos in input: # 중복처리를 하지 못함
            #     x[i, pos] = 1
            z = [[int(j == pos) for j in range(n_classes)] for pos in input]
            # print(z,end='\n\n')
            # cbow방식
            # [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            #  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]

            x[i] = np.mean(z, axis=0)   # 압축, 전체 행 덮어쓰기
            # print(x[i])
            # [0.  0.  0.5 0.5 0.  0.  0.  0.  0.  0.  0.  0. ]

    print(x[:3])
    # skip-gram방식 (원핫을 이용하면 성능좋아짐)
    # [[0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]]
    return x

def show_word2vec(corpus_idx, vocab, window_size, is_skipgram):
    n_classes = len(vocab)
    x, y = build_dataset(corpus_idx, n_classes, window_size, is_skipgram)

    n_embed = 2

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=n_classes))                   # x.shape[1:]
    model.add(tf.keras.layers.Dense(n_embed,activation='relu'))         # (12, 2)
    model.add(tf.keras.layers.Dense(n_classes, activation='softmax'))   # (2, 12)
    model.summary()
    # dense - 12*2+2
    # dense_1 - 2*12+12
    
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.sparse_categorical_crossentropy)
    # 문제
    # 100번의 에포크마다 중간 결과를 출력할 수 있도록 callback을 추가하세요.
    model.fit(x, y, epochs=20000, verbose=0, callbacks=[EveryEpoch()])

    dense_1 = model.get_layer(index=0)
    lookup_1 = dense_1.weights[0].numpy()
    print(dense_1)
    print(lookup_1)

    # 문제
    # 두 번째 dense 레이어의 가중치를 그래프에 그려보세요
    dense_2 = model.get_layer(index=1)
    lookup_2 = dense_2.weights[0].numpy().transpose()

    plt.subplot(1, 2, 1)
    show_similarity(lookup_1, vocab, 'skip-gram' if is_skipgram else 'cbow')

    plt.subplot(1, 2, 2)
    show_similarity(lookup_2, vocab, 'skip-gram' if is_skipgram else 'cbow')
    plt.show()


def show_similarity(vectors, vocab, title):
    for (x1, x2), w in zip(vectors, vocab):
        plt.text(x1, x2, w)

    x_min, y_min = np.min(vectors, axis=0) - 1
    x_max, y_max = np.max(vectors, axis=0) + 1

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    plt.title(title)

# callback클래스를 하나 만든 것
class EveryEpoch(tf.keras.callbacks.Callback):
    def __init__(self, epoch_steps=100):
        self.epoch_steps = epoch_steps

    def on_epoch_end(self, epoch, logs=None):   # epoch가 끝날때 마다 라는 함수
        if epoch % self.epoch_steps == self.epoch_steps-1:
            print(epoch+1,logs['loss'])


def show_word2vec_by_gensim(corpus, vocab, stop_words,window_size, is_skipgram):
    def remove_stop_words(corpus, stop_words):
        return [[t for t in s.split() if t not in stop_words] for s in corpus]

    corpus_by_word = remove_stop_words(corpus, stop_words)

    result = gensim.models.Word2Vec(corpus_by_word, size=2, window=1, min_count=1, sg=is_skipgram)
    print(result.wv)                # <gensim.models.keyedvectors.Word2VecKeyedVectors object at 0x00000208FD858BE0>
    print(result.wv.vectors.shape)  # (12, 2)

    show_similarity(result.wv.vectors, vocab, 'skip-gram' if is_skipgram else 'cbow')
    plt.show()

# 10개의 문장
corpus = [
    'king is a strong man',
    'queen is a wise woman',
    'boy is a young man',
    'girl is a young woman',
    'prince is a young king',
    'princess is a young queen',
    'man is strong',
    'woman is pretty',
    'prince is a boy will be king',
    'princess is a girl will be queen',
]

stop_words = ['is', 'a', 'will', 'be']

corpus_idx , vocab= make_vocab_and_index(corpus, stop_words)

# skipgram 방식
show_word2vec(corpus_idx, vocab, window_size=1, is_skipgram=True)

# cbow방식
# show_word2vec(corpus_idx, vocab, window_size=1, is_skipgram=False)

# --------------------------- #
# gensim- skipgram
# show_word2vec_by_gensim(corpus, vocab, stop_words, window_size=1, is_skipgram=True)



