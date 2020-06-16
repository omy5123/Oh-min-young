"""
문제
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?



입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 몇 번만에 이동할 수 있는지 출력한다.

예제 입력 1
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
예제 출력 1
5
28
0
"""
import sys

def bfs(n,m,n1,m2):
    queue = [[n,m]]
    dx = [-1,-2,-2,-1,1,2,2,1]
    dy = [-2,-1,1,2,2,1,-1,-2]

    while queue:
        a, b = queue[0][0],queue[0][1]
        if a == n1 and b == m2:
            print(arr[n1][m2])
            return
        del queue[0]
        for i in range(8):
            x = a+dx[i]
            y = b+dy[i]
            if 0 <= x < l and 0 <= y < l and arr[x][y] == 0:
                queue.append([x,y])
                arr[x][y] = arr[a][b] + 1

t = int(input())

for tr in range(t):
    l = int(input())
    arr = [[0]*l for _ in range(l)]
    n, m = map(int, input().split())
    n1,m2 = map(int, input().split())
    bfs(n,m,n1,m2)
