import sys
sys.stdin = open('input.txt')

"""t = int(input())

for tr in range(t):
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a,b):
        i = str(i)
        if '4' not in i:
            cnt += 1

    print('#%d'%(tr+1),cnt-1)
"""


def find_num(a):
    n = len(str(a))
    c = list(str(a))
    num = 0
    for i in range(n):
        if int(c[i]) > 4:
            num += (int(c[i]) - 1) * 9 ** (n - i - 1)
        else:
            num += int(c[i]) * 9 ** (n - i - 1)
    return num


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    if a * b > 0:
        ans = abs(find_num(abs(b)) - find_num(abs(a)))
    else:
        ans = abs(find_num(abs(b)) + find_num(abs(a)) - 1)
    print('#%d' % test_case, ans)