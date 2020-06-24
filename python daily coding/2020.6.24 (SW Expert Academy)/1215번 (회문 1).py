"""
"기러기" 또는 "level" 과 같이 거꾸로 읽어도 앞에서부터 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

주어진 8x8 평면 글자판에서 가로, 세로를 모두 보아 제시된 길이를 가진 회문의 총 개수를 구하는 문제이다.




위와 같은 글자판이 주어졌을 때, 길이가 5인 회문은 붉은색 테두리로 표시된 4개가 있으며 따라서 4를 반환하면 된다.


[제약 사항]

각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.

글자 판은 무조건 정사각형으로 주어진다.

ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.

가로, 세로 각각에 대해서 직선으로만 판단한다.

즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.






[입력]

각 테스트 케이스의 첫 번째 줄에는 찾아야 하는 회문의 길이가 주어지며, 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.


[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 개수를 출력한다.
입력
4
CBBCBAAB
CCCBABCB
CAAAACAB
BACCCCAC
AABCBBAC
ACAACABC
BCCBAABC
ABBBCCAA
4
BCBBCACA
BCAAACAC
ABACBCCB
AACBCBCA
ACACBAAA
ACCACCCB
AACAAABA
CACCABCB
...
input.txt
출력
#1 12
#2 10
...

"""
import sys
sys.stdin = open('input.txt')
for tr in range(10):
    t = int(input())
    arr = []
    for i in range(8):
        arr.append(input())
    result = 0

    length = t-1

    for i in range(8):
        for j in range(8):
            temp = ''
            for k in range(8-j):
                temp += arr[i][j+k]

            while length < len(temp):
                if temp == temp[::-1]:
                    if len(temp) == t:
                        result += 1
                temp = temp[:-1]

    for i in range(8):
        for j in range(8):
            temp = ''
            for k in range(8-j):
                temp += arr[j+k][i]

            while length < len(temp):
                if temp == temp[::-1]:
                    if len(temp) == t:
                        result += 1
                temp = temp[:-1]

    print('#%d'%(tr+1),result)
