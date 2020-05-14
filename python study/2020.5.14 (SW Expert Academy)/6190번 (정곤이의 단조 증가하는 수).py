"""
정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했다.

그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.

어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.

예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.

양의 정수 N 개 A1, …, AN이 주어진다.

 1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤N ≤ 1,000) 이 주어진다.

두 번째 줄에는 N개의 정수 A1, …, AN(1 ≤ Ai ≤ 30,000) 이 공백 하나로 구분되어 주어진다.


[출력]

각 테스트 케이스마다 단조 증가하는 수인 Ai x Aj중에서 그 최댓값을 출력한다.

만약 Ai x Aj중에서 단조 증가하는 수가 없다면 -1을 출력한다.

입력
1          // 테스트케이스 개수, T=1
4          // N=4
2 4 7 10	// A1=2, A2=4, A3=7, A4=10

출력
#1 28
"""
import sys
sys.stdin = open('input.txt')
"""def danzo (arr,tr,s):
    s = str(s)
    b = []
    global cnt
    maxlen = 0
    maxi = 0
    for j in s:
        b.append(j)
    c = sorted(b)
    for j in range(len(c)):
        c[j] = int(c[j])
    for j in range(len(b)):
        b[j] = int(b[j])
    if b == c:
        cnt += 1
        d = []
        for j in range(len(b)):
            b[j] = str(b[j])
        maxlen = len(b)
        maxi = int(b[0])
        print(b)
        print('#%d'%(tr+1),end=' ')
        for j in range(len(b)):
            print(b[j],end='')
        print()"""

"""t = int(input())

for tr in range(t):
    a = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    num = arr[0]
    num_1 = 0
    result = []
    if a == 1:
        pass
    else:
        for i in range(0,a):
            for q in range(i+1,a):
                s = 0
                num = arr[i]
                num_1 = arr[q]
                s = num * num_1

                str_s = str(s)
                b = []
                for j in str_s:
                    b.append(j)
                c = sorted(b)
                if (b == c):
                    if s not in result:
                        result.append(s)
    if result:
        ma_x = max(result)
        print('#%d'%(tr+1),ma_x)
    else:
        print('#%d'%(tr+1),-1)
"""

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    ans = -1
    for i in range(N - 1):  # i: 0 ~ N-2
        for j in range(i + 1, N):
            num = arr[i] * arr[j]
            if ans >= num:
                break
            temp = num
            b = temp % 10
            temp //= 10
            while temp:
                a = temp % 10
                if a > b:
                    break
                temp //= 10
                b = a
            else:
                ans = max(ans, num)
    print('#{} {}'.format(t, ans))