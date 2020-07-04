import sys
sys.stdin = open('input.txt')

def main():
    t = int(input())
    for tr in range(t):
        a = list(input())
        a.sort()

        arr = []

        for i in range(1,len(a)+1):
            for j in range(len(a)):
                s = a[j:j+i]
                if len(s) == i:
                    arr.append(s)

        cnt = 0
        for i in arr:
            if i == i[::-1]:
                cnt += 1

        print('#%d'%(tr+1),cnt)

if __name__ == '__main__':
    main()
