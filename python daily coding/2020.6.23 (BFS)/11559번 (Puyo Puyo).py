"""
문제
뿌요뿌요의 룰은 다음과 같다.

필드에 여러 가지 색깔의 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다.

뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다.

뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.

아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.

터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.

남규는 최근 뿌요뿌요 게임에 푹 빠졌다. 이 게임은 1:1로 붙는 대전게임이라 잘 쌓는 것도 중요하지만, 상대방이 터뜨린다면 연쇄가 몇 번이 될지 바로 파악할 수 있는 능력도 필요하다. 하지만 아직 실력이 부족하여 남규는 자기 필드에만 신경 쓰기 바쁘다. 상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산하여 남규를 도와주자!

입력
12*6의 문자가 주어진다.

이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.

R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.(모두 대문자로 주어진다.)

입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태(즉 뿌요 아래에 빈 칸이 있는 경우는 없음) 이다.

출력
현재 주어진 상황에서 몇연쇄가 되는지 출력하라. (하나도 터지지 않는다면 0을 출력하면 된다.)

예제 입력 1
......
......
......
......
......
......
......
......
.Y....
.YG...
RRYG..
RRYGG.
예제 출력 1
3
"""
from collections import deque
import sys
sys.stdin = open('input.txt')
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j,char,arr):
    queue = deque()
    queue.append([i,j])
    chain.append([i,j])
    visit[i][j] = 1
    while queue:
        a, b = queue.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < 12 and 0 <= y < 6 and visit[x][y] == 0 and arr[x][y] == char:
                visit[x][y] = 1
                queue.append([x,y])
                chain.append([x,y])

def down(arr):
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if arr[j][i] != "." and arr[k][i] == ".":
                    arr[k][i] = arr[j][i]
                    arr[j][i] = "."
                    break

arr = [list(input()) for _ in range(12)]
count = 0

while 1:
    flag = False
    visit = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.':
                chain = []
                bfs(i,j,arr[i][j],arr)
                if len(chain) >= 4:
                    for p,q in chain:
                        arr[p][q] = '.'
                    flag = True

    if not flag:
        break
    down(arr)
    count += 1

print(count)