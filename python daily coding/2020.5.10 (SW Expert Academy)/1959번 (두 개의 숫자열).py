"""
N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.

아래는 N =3 인 Ai 와 M = 5 인 Bj 의 예이다.


Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.

단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.




서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.

위 예제의 정답은 아래와 같이 30 이 된다.



[제약 사항]

N 과 M은 3 이상 20 이하이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,

두 번째 줄에는 Ai,

세 번째 줄에는 Bj 가 주어진다.

[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
입력
10
3 5
1 5 3
3 6 -7 5 4
7 6
6 0 5 5 -1 1 6
-4 1 8 7 -9 3
...

출력
#1 30
#2 63
...
"""
import sys
sys.stdin = open('input.txt')
t = int(input())

for st in range(t):
    n, m = map(int,input().split())
    n_list = list(map(int,input().split()))
    m_list = list(map(int,input().split()))
    result = 0
    sum = 0
    if(n > m):
        for i in range(n-m+1):
            for j in range(m):
                sum += n_list[i+j] * m_list[j]
            if (result < sum):
                result = sum
            sum = 0
    elif(n<m):
        for i in range(m-n+1):
            for j in range(n):
                sum += n_list[j] * m_list[i+j]
            if (result < sum):
                result = sum
            sum = 0


    print('#%d'%(st+1),result)
