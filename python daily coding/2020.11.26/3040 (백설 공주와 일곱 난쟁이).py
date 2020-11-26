import sys
sys.stdin = open('input.txt')

arr = []
check = False
def dfs(cnt, s, idx):
    global check
    if(check):
        return
    if(cnt == 7):
        if (s == 100):
            for i in arr:
                print(i)
            check = True
            return

    else:
        for i in range(idx,9):
            arr.append(a[i])
            dfs(cnt+1, s + a[i],i+1)
            arr.pop()
a = []
for _ in range(9):
    a.append(int(input()))

dfs(0, 0, 0)