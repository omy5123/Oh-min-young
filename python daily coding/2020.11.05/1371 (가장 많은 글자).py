import sys

sys.stdin = open('input.txt')

alpha = [0] * 26
while (True):
    try:
        st = input()
        for i in st:
            if(i == ' '):
                continue
            alpha[ord(i)-97] += 1
    except EOFError:
        break
m = max(alpha)
result = []
for i in range(len(alpha)):
    if(alpha[i] == m):
        result.append(i)
for i in result:
    print(chr(i+97), end='')