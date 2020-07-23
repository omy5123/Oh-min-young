import sys
sys.stdin = open('input.txt')

for tr in range(10):
    t = int(input())
    arr = input()
    dx = ['(','[','<','{']
    dy = [')',']','>','}']
    stack = []
    for i in arr:
        if i == '(' or i == '[' or i == '<' or i == '{':
            stack.append(i)
        else:
            if dx.index(stack[-1]) == dy.index(i):
                stack.pop()
            else:
                break
    if stack:
        print('#%d'%(tr+1),0)
    else:
        print('#%d' % (tr + 1), 1)
