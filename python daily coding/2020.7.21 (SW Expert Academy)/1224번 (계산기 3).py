import sys
sys.stdin = open('input.txt')
for t in range(1):
    N = int(input())
    num = []
    stack = []
    for i in input():
        if i == '(':
            stack.append(i)
        elif i == '*':
            if not stack or stack[-1] != '*':
                stack.append(i)
            else:
                a = num.pop()
                b = num.pop()
                num.append(a*b)
        elif i == '+':
            if not stack or stack[-1] == '(':
                stack.append(i)
            else:
                a = num.pop()
                b = num.pop()
                c = stack.pop()
                if c == '*':
                    num.append(a*b)
                    stack.append(i)
                else:
                    num.append(a+b)
                    stack.append(i)
        elif i == ')':
            c = stack.pop()
            while c != '(':
                a = num.pop()
                b = num.pop()
                if c == '+':
                    num.append(a+b)
                else:
                    num.append(a*b)
                c = stack.pop()
        else:
            num.append(int(i))
    print('#{} {}'.format(t, num.pop()))