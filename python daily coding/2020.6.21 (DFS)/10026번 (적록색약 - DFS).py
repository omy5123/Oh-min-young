"""
적록색약 성공출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	13114	7505	5952	58.170%
문제
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

예제 입력 1
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
예제 출력 1
4 3
"""
import sys

sys.setrecursionlimit(10000)
def arr_dfs(v,i,j):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    arr[i][j] = 0
    for k in range(4):
        x = i+dx[k]
        y = j+dy[k]
        if 0 <= x < n and 0 <= y < n and arr[x][y] == v:
            arr[x][y] = 0
            arr_dfs(v,x,y)

def brr_dfs(v,i,j):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    brr[i][j] = 0
    for k in range(4):
        x = i+dx[k]
        y = j+dy[k]
        if 0 <= x < n and 0 <= y < n and brr[x][y] == v:
            brr[x][y] = 0
            brr_dfs(v,x,y)


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))
brr = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            brr[i][j] = 'R'
        else:
            brr[i][j] = arr[i][j]

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr_dfs('R',i,j)
            cnt += 1
        if arr[i][j] == 'G':
            arr_dfs('G',i,j)
            cnt += 1
        if arr[i][j] == 'B':
            arr_dfs('B',i,j)
            cnt += 1
print(cnt,end=' ')
cnt = 0
for i in range(n):
    for j in range(n):
        if brr[i][j] == 'R':
            brr_dfs('R',i,j)
            cnt += 1
        if brr[i][j] == 'B':
            brr_dfs('B',i,j)
            cnt += 1
print(cnt)