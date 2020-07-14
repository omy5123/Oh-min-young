import sys
sys.stdin = open('input.txt')

def match(nth, plus, minus, Vector_y, Vector_x):
    global Min
    if Min == 0:
        return
    if plus == minus == n // 2:
        temp = (Vector_y) ** 2 + (Vector_x) ** 2
        if temp < Min:
            Min = temp
    else:
        if plus < n // 2:
            match(nth + 1, plus + 1, minus, Vector_y + worm[nth][0], Vector_x + worm[nth][1])
        if minus < n // 2:
            match(nth + 1, plus, minus + 1, Vector_y - worm[nth][0], Vector_x - worm[nth][1])


for num in range(int(input())):
    n = int(input())
    worm = []
    for i in range(n):
        y, x = map(int, input().split())
        worm += [(y, x)]
    Min = 0xfffffffffff
    match(1, 1, 0, worm[0][0], worm[0][1])
    print('#{} {}'.format(num + 1, Min))