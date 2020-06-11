"""
문제
선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 숫자를 버리는 함수이다.

배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.

각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.

다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)

다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 수가 주어진다. (1 ≤ xi ≤ 100)

전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.

출력
각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.

예제 입력 1
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
예제 출력 1
[2,1]
error
[1,2,3,5,8]
error
"""
""" 답은 나오지만 시간복잡도가 효율적이지 않다,,"""

"""import sys
sys.stdin = open('input.txt')
def R (que):
    que = que[::-1]
    return que

def D (que):
    que.pop(0)

    return que

t = int(input())

for i in range(t):
    fun = list(map(str, input()))
    num = int(input())
    if num == 1:
        que = list(input())
        que.pop(0)
        que.pop()
        que = ''.join(que)
        que = list(map(int,que.split(',')))
        cnt = 0
        for j in range(len(fun)):
            if (fun[j] == 'R'):
                que = que
            elif (fun[j] == 'D'):
                if cnt >= 1:
                    print('error')
                    break
                else:
                    que = D(que)
                    cnt += 1
        else:
            print('[', end='')
            for k in range(len(que)):
                print(que[k], end='')
            print(']')
    elif num == 0 :
        que = []
        for j in range(len(fun)):
            if (fun[j] == 'R'):
                que = que
            elif (fun[j] == 'D'):
                print('error')
                break
        else:
            print('[]')

    else:
        que = list(input())
        que.pop(0)
        que.pop()
        que = ''.join(que)
        que = list(que.split(','))
        for j in range(len(fun)):
            if(fun[j] == 'R'):
                que = R(que)
            elif(fun[j] == 'D'):
                que = D(que)
        print('[',end='')
        for k in range(len(que)):
            print(que[k], end=',')
        print('\b]')
"""


import sys
sys.stdin = open('input.txt')

t = int(input())

for i in range(t):
    function = list(input())
    num = int(input())
    que = eval(input())
    R_cnt = 0
    D_cnt = 0
    error = False

    for j in range(len(function)):
        if (function[j] == 'R'):
            R_cnt += 1
        else:
            try:
                if R_cnt % 2 == 0 :
                    D_cnt += 1
                else:
                    que.pop()
            except:
                error = True
                break
    if(error or D_cnt >len(que)):
        print('error')
        continue

    if R_cnt % 2 == 0:
        result = que[D_cnt:]
    else:
        result = list(reversed(que[D_cnt:]))

    print("[", end='')
    for j in range(len(result)):
        if j == len(result) - 1:
            print(result[j], end='')
        else:
            print("%s," % (result[j]), end='')
    print("]")



