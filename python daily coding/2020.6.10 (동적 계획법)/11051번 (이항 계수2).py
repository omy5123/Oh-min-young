"""
문제
자연수 과 정수 가 주어졌을 때 이항 계수 n, k를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 1,000, 0 ≤  ≤ )

출력
 n,k를 10,007로 나눈 나머지를 출력한다.

예제 입력 1
5 2
예제 출력 1
10
"""
n, k = map(int, input().split())
dp = [[0]*1 for _ in range(n+2)]
dp[1].append(1)
for i in range(2,n+2):
    for j in range(1,i+1):
        if j == 1:
            dp[i].append(1)
        elif j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i-1][j-1] + dp[i-1][j])
print(dp[n+1][k+1] % 10007)
