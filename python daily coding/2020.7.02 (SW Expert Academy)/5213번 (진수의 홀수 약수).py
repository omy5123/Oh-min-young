import sys
sys.stdin = open('input.txt')
MAX = 10 ** 6 + 1
DP = [0] * MAX
for i in range(1, MAX, 2):
    for j in range(i, MAX, i):
        DP[j] += i
answer = []

for testCase in range(int(input())):
    ans = 0
    S, E = map(int, input().split())
    for i in range(S,E+1):
        ans += DP[i]
    print('#%d'%(testCase+1),ans)