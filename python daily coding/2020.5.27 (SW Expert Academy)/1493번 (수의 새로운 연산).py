"""
2차원 평면 제 1사분면 위의 격자점 (x,y)에 위 그림과 같이 대각선 순서로 점에 수를 붙인다.

점 (x,y)에 할당된 수는 #(x,y)로 나타낸다.

예를 들어 #(1,1) = 1, #(2,1)=3, #(2,2) = 5, #(4,4) = 25이다.

반대로 수 p가 할당된 점을 &(p)로 나타낸다.

예를 들어 &(1) = (1,1), &(3) = (2,1), &(5) = (2,2), &(25) = (4,4)이다.

두 점에 대해서 덧셈을 정의한다. 점 (x,y)와 점 (z,w)를 더하면 점 (x+z, y+w)가 된다.

즉, (x,y) + (z,w) = (x+z, y+w)로 정의한다.

우리가 해야 할 일은 수와 수에 대한 새로운 연산 ★를 구현하는 것으로, p★q는 #(&(p)+&(q))으로 나타난다.

예를 들어, &(1)=(1,1), &(5) = (2,2)이므로, 1★5 = #(&(1)+&(5)) = #((1,1)+(2,2)) = #(3,3) = 13이 된다.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 두 정수 p,q(1 ≤ p, q ≤ 10,000)가 주어진다.


[출력]

각 테스트 케이스마다 ‘#t’(t는 테스트 케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 각 테스트 케이스마다 p★q의 값을 출력한다.
입력
2
1 5
3 9

input.txt
출력
#1 13
#2 26
"""
import sys
sys.stdin = open('input.txt')

result = []
number =  [0]
max, cnt = 50000, 0
distance = 0

while cnt < max:
    for i in range(0, distance+1):
        j = distance - i
        number.append((i+1,j+1))
        cnt += 1
    distance += 1
t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    (x1, x2) = number[x]
    (y1, y2) = number[y]

    x, y = x1+y1, x2+y2
    result.append(number.index((x, y)))
for i in range(len(result)):
    print('#%d'%(i+1),result[i])















