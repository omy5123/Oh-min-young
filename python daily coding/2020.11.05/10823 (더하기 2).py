import sys
sys.stdin = open('input.txt')

st = ""
while(True):
    try:
        st += input()
    except EOFError:
        break
arr = list(map(int,st.split(',')))
print(sum(arr))