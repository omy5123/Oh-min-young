import sys
sys.stdin = open('input.txt')

for tr in range(1):
    n = int(input())
    arr = input()
    num = []
    stack = []
    for i in arr:
        if i == '+':
            if not stack or stack[-1] != '+':
                stack.append(i)
            else:
                a = num.pop()
                b = num.pop()
                c = stack.pop()
                if c == '+':
                    num.append(a+b)
                    stack.append(i)
        else:
            num.append(int(i))
    a = num.pop()
    b = num.pop()
    c = stack.pop()
    if c == '+':
        num.append(a+b)
    print('#%d'%(tr+1),num.pop())

