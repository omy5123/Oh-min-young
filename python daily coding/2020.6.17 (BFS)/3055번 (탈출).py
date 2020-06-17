"""
문제
사악한 암흑의 군주 이민혁은 드디어 마법 구슬을 손에 넣었고, 그 능력을 실험해보기 위해 근처의 티떱숲에 홍수를 일으키려고 한다. 이 숲에는 고슴도치가 한 마리 살고 있다. 고슴도치는 제일 친한 친구인 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 한다.

티떱숲의 지도는 R행 C열로 이루어져 있다. 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다. 비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다. (위, 아래, 오른쪽, 왼쪽) 물도 매 분마다 비어있는 칸으로 확장한다. 물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다. 물과 고슴도치는 돌을 통과할 수 없다. 또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.

티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.

고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다. 이동할 수 있으면 고슴도치가 물에 빠지기 때문이다.

입력
첫째 줄에 50보다 작거나 같은 자연수 R과 C가 주어진다.

다음 R개 줄에는 티떱숲의 지도가 주어지며, 문제에서 설명한 문자만 주어진다. 'D'와 'S'는 하나씩만 주어진다.

출력
첫째 줄에 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간을 출력한다. 만약, 안전하게 비버의 굴로 이동할 수 없다면, "KAKTUS"를 출력한다.

예제 입력 1
3 3
D.*
...
.S.
예제 출력 1
3
예제 입력 2
3 3
D.*
...
..S
예제 출력 2
KAKTUS
예제 입력 3
3 6
D...*.
.X.X..
....S.
예제 출력 3
6
예제 입력 4
5 4
.D.*
....
..X.
S.*.
....
예제 출력 4
4
"""
"""from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < r and 0 <= y < c and arr[x][y] == '.':
                queue.append([x,y])
                arr[x][y] = arr[a][b]+1

def bfs_S(i,j):
    queue = deque()
    queue.append([i,j])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < r and 0 <= y < c and arr[x][y] > arr[a][b]:
                queue.append([x,y])
                arr[x][y] = arr[a][b]+1

r, c =map(int, input().split())
q, p =0,0
arr = []
for i in range(r):
    arr.append(list(input()))


for i in range(r):
    for j in range(c):
        if arr[i][j] == '*':
            arr[i][j] = 0
            bfs(i,j)
            break

for i in range(r):
    for j in range(c):
        if arr[i][j] == '.':
            arr[i][j] = 501
        elif arr[i][j] == 'D':
            arr[i][j] = 500
            q = i
            p = j
        elif arr[i][j] == 'X':
            arr[i][j] = -1

check = True

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S':
            arr[i][j] = 1
            bfs_S(i,j)
            if arr[q][p] == 500:
                check = False
                break

if check:
    print(arr[q][p]-1)
else:
    print('KAKTUS')"""


from collections import deque
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def water():
    qlen = len(queue_2)
    while qlen:
        a, b = queue_2.popleft()
        for i in range(4):
            x = dx[i] + a
            y = dy[i] + b
            if 0 <= x < r and 0 <= y < c:
                if arr[x][y] == '.':
                    arr[x][y] = '*'
                    queue_2.append([x,y])
        qlen -= 1


def bfs(a,b):
    queue_1.append([a,b])
    n[a][b] = 1
    while queue_1:
        qlen = len(queue_1)
        while qlen:
            a, b = queue_1.popleft()
            for i in range(4):
                x = dx[i] + a
                y = dy[i] + b
                if 0 <= x < r and 0 <= y < c:
                    if arr[x][y] == '.' and n[x][y] == 0:
                        n[x][y] = n[a][b] + 1
                        queue_1.append([x,y])
                    elif arr[x][y] == 'D':
                        print(n[a][b])
                        return
            qlen -= 1
        water()
    print('KAKTUS')
    return


r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(input()))
n = [[0]*c for _ in range(r)]
queue_1 = deque()
queue_2 = deque()

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S':
            p = i
            q = j
            arr[i][j] = '.'
        elif arr[i][j] == '*':
            queue_2.append([i,j])

water()
bfs(p,q)



