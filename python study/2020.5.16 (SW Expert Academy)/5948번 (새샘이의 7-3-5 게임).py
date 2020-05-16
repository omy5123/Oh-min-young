"""
숫자게임을 좋아하는 새샘이는 서로 다른 7개의 정수 중에서 3개의 정수를 골라 합을 구해서 수를 만들려고 한다.

이렇게 만들 수 있는 수 중에서 5번째로 큰 수를 출력하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 7개의 서로 다른 정수가 공백으로 구분되어 주어진다. 각 정수는 1이상 100이하이다.


[출력]

각 테스트 케이스마다 첫 번째 줄에는 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 답을 출력한다.



입력
2      //Test Case 갯수
1 2 3 4 5 6 7   //Test Case #1의 입력
5 24 99 76 1 77 6

출력
#1 14
#2 181
"""
import sys
sys.stdin = open('input.txt')

t = int(input())
result = []
for tr in range(t):
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    arr = []
    for i in range(7):
        for j in range(i+1,7):
            for k in range(j+1,7):
                num_sum = a[i]+a[j]+a[k]
                arr.append(num_sum)

    result.append(sorted(set(arr))[-5])
for i in range(len(result)):
    print('#%d'%(i+1),result[i])




