"""
N을 입력 받아 다음의 세 가지 합을 구하는 프로그램을 작성하라.

S1 = 양의 정수 중에서 작은 순서대로 N개의 합.

S2 = 양의 정수 중 홀수인 것들 중에서 작은 순서대로 N개의 합.

S3= 양의 정수 중 짝수인 것들 중에서 작은 순서대로 N개의 합.

예를 들어 N = 5의 입력이 들어왔을 경우,

S1 = 1 + 2 + 3 + 4 + 5,

S2 = 1 + 3 + 5 + 7 + 9,

S3 = 2 + 4 + 6 + 8 + 10 이다.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 자연수 N(1 ≤ N ≤ 109)가 주어진다.


[출력]

각 테스트 케이스마다 S1, S2, S3을 공백으로 구분하여 출력한다.


입력
3      //testCase의 개수
1      //N = 1
10
1001

출력
#1 1 1 2
#2 55 100 110
#3 501501 1002001 1003002
"""
import sys
sys.stdin = open('input.txt')
"""t = int(input())
s1 = []
s2 = []
s3 = []
for tr in range(t):
    a = int(input())  # 갯수

    s1_sum = 0
    for i in range(1,a+1):
        s1_sum += i
    s1.append(s1_sum)

    s2_sum = 0
    for i in range(1,(a*2+1),2):
        s2_sum += i
    s2.append(s2_sum)

    s3_sum = 0
    for i in range(2, (a * 2 + 1), 2):
        s3_sum += i
    s3.append(s3_sum)
for i in range(t):
    print('#%d'%(i+1),s1[i],s2[i],s3[i])"""

t = int(input())
for tr in range(t):
    a = int(input())

    print('#%d'%(tr+1),a*(a+1)//2,a*(a+1)-a,a*(a+1))



