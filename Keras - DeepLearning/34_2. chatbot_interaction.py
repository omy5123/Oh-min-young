import tensorflow as tf
import numpy as np
import nltk
import sys
# import 34_1. chatbot_model as chatbot

# 문제
# 어린왕자 데이터셋을 읽어서 전체 데이터에 대해 결과를 예측하세요
# 예측한 결과를 출력합니다.


def load_and_predict():
    enc_inputs, dec_inputs, dec_output, vocab = chatbot.load_dataset()
    model = tf.keras.models.load_model('chat/little_prince.h5')

    # ------------------------------------------------ #
    # show_translation_word 함수의 예측하는 코드 사용
    preds = model.predict([enc_inputs, dec_inputs])
    print(preds.shape)  # (52, 10, 164)

    preds_arg = np.argmax(preds, axis=2)
    # print(preds_arg.shape)  # (52, 10)

    #_EOS_ 와 _PAD_ 가 출력되는 코드
    # for tokens in preds_arg:
    #     print(' '.join([vocab[t] for t in tokens[:-1]]))

    # 문제
    # 출력 뒤에 붙어있는 _EOS_와_PAD_ 토큰을 제거하세요.

    # 문제
    # 정답 앞쪽에 질문을 출력하세요.
    len_answers = [list(answer).index(chatbot._EOS_) for answer in dec_output]
    for len_a, question, answer, result in zip(len_answers,enc_inputs, dec_output, preds_arg):
        # 정답
        answer = np.int32(answer)

        # 질문 출력 위치
        question_arg = np.argmax(question, axis=1)
        question_arg = list(question_arg)

        while chatbot._PAD_ in question_arg:
            question_arg.remove(chatbot._PAD_)

        print(' '.join([vocab[t] for t in question_arg]))
        print(' '.join([vocab[t] for t in answer[:len_a]]))
        print(' '.join([vocab[t] for t in result[:len_a]]))
        print()

def talk_to_bot():
    vocab = chatbot.read_vocab()
    vectors = chatbot.read_vectors()

    # 문제
    # 질문과 대답 데이터에서 가장 긴 토큰의 길이를 구하세요.
    dialog_questions = vectors[::2]
    dialog_answers = vectors[1::2]

    max_len_q = max([len(q) for q in dialog_questions])
    max_len_a = max([len(a) for a in dialog_answers]) + 1
    print(max_len_q, max_len_a)  # 9 10

    # ------------------------------------------------ #

    model = tf.keras.
    onehot = np.eye(len(vocab), dtype=np.float32)

    while True:
        sys.stdout.write('왕자: ')
        sys.stdout.flush()

        line = sys.stdin.readline()
        line = line.strip()

        if '끝' == line:
            break

        # 문제
        # 입력 문장을 토큰으로 분리하세요.
        # tokens = line.split()         # 공백이 여러 개 일때(?)
        tokens = nltk.regexp_tokenize(line, r'\w+')
        # print(tokens)                 # ['이리', '와서', '나하고', '놀자']

        # 문제
        # 토큰을 질문으로 변환하세요. (문자열 토큰을 숫자로 변환하세요)
        question = [vocab.index(t) if t in vocab else chatbot._UNK_ for t in tokens]
        # print(question)                 # [125, 118, 37, 49]

        # ---------------------------------------- #

        # 문제
        # 사용자 질문에 대해 답변하세요 (predict)

    # enc_inputs, dec_inputs, dec_output = [], [], []
    # for question, answer in zip(dialog_questions, dialog_answers):
    #     encoder_in = add_pad(question, max_len_q)  # 길이를 똑같이 맞춰줘야함
    #     decoder_in = add_pad([_SOS_] + answer, max_len_a)
    #     target = add_pad(answer + [_EOS_], max_len_a)
    #     # print(eng_incoder)

    #     enc_inputs.append(onehot[encoder_in])
    #     dec_inputs.append(onehot[decoder_in])
    #     # dec_output.append(onehot[target])
    #     dec_output.append(target)  # 바로 위에 코드보다 y는 원핫으로 안바꾼게 더 좋음

    # return np.float32(enc_inputs), np.float32(dec_inputs), np.float32(dec_output), vocab


# load_and_predict()
talk_to_bot()