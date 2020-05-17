"""
양의 정수 N에 대해 N = X3가 되는 양의 정수X 를 구하여라.



[입력]


첫 번째 줄에 테스트 케이스의 수 T가 주어진다.


각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1≤N≤1018) 이 주어진다.

[출력]


각 테스트 케이스마다 첫 번째 줄에는‘#T’(T는 테스트케이스 번호를 의미하며 1부터 시작한다.)를 출력하고, N = X3가 되는 양의 정수 X를 출력한다.

만약 이런 X가 존재하지 않으면 -1을 출력한다.

입력
3     // 총 테스트 케이스 개수 T=1
27    // 첫 번째 테스트케이스, N=27
7777  // 두 번째 테스트케이스
64


출력
#1 3
#2 -1
#3 4
"""
import sys
sys.stdin = open('input.txt')
t = int(input())
result = []
b = []
c = []
for tr in range(t):
    a = int(input())
    c.append(a**(1/3))
    b.append(round(a**(1/3)))
for i in range(t):
    if(abs(b[i] - c[i]) < 0.000000001):
        result.append(b[i])
    else:
        result.append(-1)

for i in range(len(result)):
    print('#%d'%(i+1),result[i])