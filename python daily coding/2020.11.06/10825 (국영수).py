
"""import functools

n = int(input())
def comparator(a,b):
    if(int(a[1]) < int(b[1])):
        return 1
    elif(int(a[1]) > int(b[1])):
        return -1
    else:
        if(int(a[2]) < int(b[2])):
            return -1
        elif(int(a[2]) > int(b[2])):
            return 1
        else:
            if(int(a[3]) < int(b[3])):
                return 1
            elif(int(a[3])>int(b[3])):
                return -1
            else:
                if(a[0] < b[0]):
                    return -1
                elif(a[0] > b[0]):
                    return 1
                else:
                    return 0

arr = []
for line in range(n):
    arr.append(list(map(str, input().split())))
arr = sorted(arr, key=functools.cmp_to_key(comparator))

for i in range(len(arr)):
    print(arr[i][0])"""
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    name,a,b,c = map(str,input().split())
    arr.append([name,int(a),int(b),int(c)])
arr.sort(key=lambda x : (x[0]))
arr.sort(key=lambda x : (x[3]),reverse = True)
arr.sort(key=lambda x : (x[2]))
arr.sort(key=lambda x : (x[1]),reverse = True)
for i in range(len(arr)):
    print(arr[i][0])
