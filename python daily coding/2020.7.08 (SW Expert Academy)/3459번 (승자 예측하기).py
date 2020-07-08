import sys
sys.stdin = open('input.txt')

T = int(input())
res = []
for tc in range(1, T + 1):
    N = int(input())
    winner = True
    num = 1
    while N > 0:
        N -= num
        if winner:
            num *= 4
        winner = not winner

    win = 'Alice' if winner else 'Bob'
    res.append('#{} {}'.format(tc, win))
print('\n'.join(res))