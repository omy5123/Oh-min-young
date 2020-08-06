"""문제
자연수 과 정수 가 주어졌을 때 이항 계수 를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 4,000,000, 0 ≤  ≤ )

출력
 를 1,000,000,007로 나눈 나머지를 출력한다.

예제 입력 1
5 2
예제 출력 1
10"""

def solve(A, B):
    if (B % 2 > 0):
        return solve(A, B - 1) * A
    elif (B == 0):
        return 1
    elif (B == 1):
        return A
    else:
        result = solve(A, B // 2)
        return result ** 2 % p


n, k = map(int, input().split())

a = 1
b = 1

p = 1000000007

for num in range(1, n + 1):
    a *= num;
    a %= p

for num in range(1, k + 1):
    b *= num;
    b %= p

for num in range(1, n - k + 1):
    b *= num;
    b %= p

b = solve(b, p - 2) % p

result = (a * b) % p
print(result)