"""
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.


[예제]

N이 3일 경우,




N이 4일 경우,



[제약사항]

달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 N이 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
입력
2
3
4

출력
#1
1 2 3
8 9 4
7 6 5
#2
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
"""
import sys
sys.stdin = open('input.txt')
t = int(input())

for sd in range(t):
    a = int(input())
    arr = []
    for i in range(a):
        arr.append([0]*a)
    x=y=s=0
    for i in range(a**2):
        arr[x][y] = i+1
        if s == 0:
            if y+1 >= a or arr[x][y+1] > 0:
                s += 1
                x += 1
            else:
                y+=1
        elif s==1:
            if x+1 >= a or arr[x+1][y] > 0:
                s += 1
                y -= 1
            else:
                x += 1
        elif s == 2:
            if y-1 < 0 or arr[x][y-1] > 0:
                s += 1
                x -= 1
            else:
                y -= 1
        elif s == 3:
            if x-1 < 0 or arr[x-1][y] > 0:
                s = 0
                y += 1
            else:
                x -= 1
    print('#%d'%(sd+1))
    for i in range(a):
        for j in range(a):
            print(arr[i][j],end=' ')
        print()








"""
for a in range(int(input())):
    n=int(input())
    m=[]
    for i in range(n):
        m.append([0 for i in range(n)])
    x=y=s=0
    for j in range(n*n):
        m[x][y]=j+1
        if s==0:
            if y+1>=n or m[x][y+1]>0:
                s=1
                x+=1
            else:
                y+=1
        elif s==1:
            if x+1>=n or m[x+1][y]>0:
                s=2
                y-=1
            else:
                x+=1
        elif s==2:
            if y-1<0 or m[x][y-1]>0:
                s=3
                x-=1
            else:
                y-=1
        elif s==3:
            if x-1<0 or m[x-1][y]>0:
                s=0
                y+=1
            else:
                x-=1
    print(f'#{a+1}')
    for j in m:
        print(' '.join(map(str,j)))
"""