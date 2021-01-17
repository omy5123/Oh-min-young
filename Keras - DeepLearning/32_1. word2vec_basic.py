# https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/03/30/word2vec/
# word2vec - 말 그대로 단어를 벡터로 바꿔주는 알고리즘
# 2가지 방식
# skip_Gram - 중심단어로 주변단어 예측
# 주변단어로 중심단어 예측)


# 문제
# 1. cbow 방식으로 x, y 데이터를 만드세요 (윈도우 크기 1)
# 1. skip-gram 방식으로 x, y 데이터를 만드세요 (윈도우 크기 1)
# ['The', 'quick', 'brown', 'fox', 'jumps']

# cbow
# ('quick'), 'The'
# ('The', 'brown'), 'quick'
# ('quick', 'fox'), 'brown'
# ('brown', 'jumps'), 'fox'
# ('fox'), 'jumps'

# skip-gram
# (The, quick)
# (quick, The) (quick, brown)
# (brown, quick) ( brown, fox)
# (fox, brown) (fox, jumps)
# (jumps, fox)

def extract(token_count, center, window_size):
    start = max(center - window_size, 0)
    end = min(center + window_size+1, token_count)
    return [i for i in range(start, end) if i != center]

def show_dataset(tokens, window_size, is_skipgram):
    token_count = len(tokens)
    for center in range(token_count):
        surround = extract(token_count, center, window_size)

        # 문제
        # skip-gram 방식으로 데이터를 출력하세요
        if is_skipgram:
            for t in surround:
                print('{}, {}'.format(tokens[center], tokens[t]), end=' ')
        else:
            print([tokens[t] for t in surround], tokens[center])

tokens = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# for i in range(len(tokens)):
#     print(i, extract(len(tokens),i,2))

show_dataset(tokens, window_size=1, is_skipgram=False)
