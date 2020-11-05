import sys

sys.stdin = open('input.txt')

while (True):
    st = input()
    s = []
    check = True
    if (st == '.'):
        break
    for i in st:
        if (i == '(' or i == '['):
            s.append(i)
        elif (i == ')'):
            if(s):
                if (s[-1] == '('):
                    s.pop()
                else:
                    check = False
                    break
            else:
                check = False
                break
        elif (i == ']'):
            if (s):
                if (s[-1] == '['):
                    s.pop()
                else:
                    check = False
                    break
            else:
                check = False
                break
        else:
            continue

    if (len(s) == 0 and check):
        print("yes")
    else:
        print("no")
