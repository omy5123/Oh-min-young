import numpy as np
import collections

np.set_printoptions(precision=2, floatmode='fixed', suppress=True)    # precision=2(소수 2째자리), floatmode='fixed', suppress=True로 지수표기법도 다없애줌

# 확률분포에대해 얘기
def softmax_1(dist):
    return dist / np.sum(dist)

def softmax_2(dist):  # -값이 들어와도 1을 만듬
    dist = np.exp(dist)
    return dist / np.sum(dist)

def temperature_1(dist, t):
    dist = np.log(dist) / t
    dist = np.exp(dist)
    return dist / np.sum(dist)

def temperature_2(dist, t):
    dist = dist / t
    dist = np.exp(dist)
    return dist / np.sum(dist)

dist = [2.0,1.0,0.1]
print(softmax_1(dist))          # [0.64516129 0.32258065 0.03225806]
print(softmax_2(dist))          # [0.65900114 0.24243297 0.09856589]
print()

for t in np.linspace(0.1, 1.0, 10):
    print(temperature_1(dist, t))
print()

for t in np.linspace(0.1, 1.0, 10):
    print(temperature_2(dist, t))
print()
# ----------------------------------------- #

d1 = softmax_1(dist)            # [0.65 0.32 0.03]
d2 = np.cumsum(d1)              # [0.65 0.97 1.00]
print(d1)
print(d2)

# searchsorted - 정렬된데이터에서 인덱스를 찾아준다.
print(np.searchsorted([0.5, 1.0, 2.0], 0.1))        # 0  [0.1, 0.5, 1.0, 2.0]
print(np.searchsorted([0.5, 1.0, 2.0], 0.7))        # 1  [0.5, 0.7, 1.0, 2.0]
print(np.searchsorted([0.5, 1.0, 2.0], 1.5))        # 2
print(np.searchsorted([0.5, 1.0, 2.0], 3.0))        # 3

print(np.random.rand(1))                            # [0.37]
print(np.searchsorted([0.5, 1.0, 2.0],
                      np.random.rand(1)))           # [1]
print()

indices = [np.searchsorted(d2, np.random.rand(1)[0]) for _ in range(100)] # 대괄호 없애기 위해 [0]해준다.
# [0.65 0.97 1.00] 에서 0이 나올 확률 65%, 1 - 32%, 2 - 3%, 3 - 0%
print(indices)
print(collections.Counter(indices))
# Counter({0: 62, 1: 36, 2: 2}) 비슷하게 나옴 확률과
