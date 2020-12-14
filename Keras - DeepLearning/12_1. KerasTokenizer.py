import tensorflow as tf

long_text = ("if you want to build a ship,"
             " don't drum up people to collect wood and"
             " don't assign them tasks and work,"
             " but rather teach them to long"
             " for the endless immensity of the sea.")

# 1. tokenizer를 만든다.
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=10) # 패딩을 제외한 최빈값 9개만 사용한다. 0번쨰는 항상 비워둠

# 2. 데이터셋에 대해 공부한다.
# tokenizer.fit_on_texts(long_text)
# print(tokenizer.index_word)     # {1: 't', 2: 'o', 3: 'e', ...}
# print(tokenizer.word_index)     # {'t': 1, 'o': 2, 'e': 3, ...}

tokenizer.fit_on_texts(long_text.split())
print(tokenizer.index_word)     # {1: 'to', 2: "don't", 3: 'and', ...}
print(tokenizer.word_index)     # {'to': 1, "don't": 2, 'and': 3, ...}
print()

# print(tokenizer.index_word[0])    # 에러. 1번 부터해야됨
print(tokenizer.oov_token)          # None. oov(out of vocabulary)
tokenizer.oov_token = '*'
print(tokenizer.oov_token)          # * 보통은 쓸일이 없음
print()

print(tokenizer.index_word[9])      # build
print(tokenizer.index_word[10])     # a
print(tokenizer.index_word[11])     # ship
print()

print(tokenizer.texts_to_sequences(['build','a','ship']))     # [[9], [], []]
print(tokenizer.texts_to_sequences([['build','a','ship']]))   # [[9]]  document를 여러개 전달할거라 2차원이 맞다.
print()

# 문제
# sequences_to_texts 함수에 전달할 배열을 만드세요.
sequences = [[3,9,2,4,7],[1,4,13,8],[10,15]]
print(tokenizer.sequences_to_texts(sequences))
# ["and build don't them you", 'to them want', ''] 10과 15는 변환할수 없음
print()

print(tf.keras.preprocessing.sequence.pad_sequences(sequences))
# [[ 3  9  2  4  7]    길이를 똑같이 만들어줌
#  [ 0  1  4 13  8]
#  [ 0  0  0 10 15]]
print()

print(tf.keras.preprocessing.sequence.pad_sequences(sequences, padding='pre')) # 패딩이 앞쪽  pre가 더좋아서 기본값
print(tf.keras.preprocessing.sequence.pad_sequences(sequences, padding='post')) # 패딩이 뒷쪽
print()

print(tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=4))
# [[ 9  2  4  7]   긴건 짤라지고 짧은건 패딩
#  [ 1  4 13  8]
#  [ 0  0 10 15]]
print(tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=4,truncating='pre')) # 뒷쪽 짜름
print(tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=4,truncating='post')) # 앞쪽 짜름
