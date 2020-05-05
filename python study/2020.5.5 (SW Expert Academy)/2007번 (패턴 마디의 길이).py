"""
패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.


[제약 사항]

각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 길이가 30인 문자열이 주어진다.


[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


입력
3
KOREAKOREAKOREAKOREAKOREAKOREA
SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
GALAXYGALAXYGALAXYGALAXYGALAXY

출력
#1 5
#2 7
#3 6
"""
import sys
sys.stdin = open('input.txt')

"""t = int(input())


for i in range(t):
    strlist = input()
    a = []
    for j in range(10,0,-1):
        a.append(strlist[:j])
    print(a)
"""

T = int(input())
for t in range(1, T + 1):
    M = input()
    for i in range(1, len(M)):
        if M[:i] == M[i:2 * i]:
            res = M[:i]
            break
    print('#%d'%t, len(res))



