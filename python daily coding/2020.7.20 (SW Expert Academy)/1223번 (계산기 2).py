import sys
sys.stdin = open('input.txt')

for tr in range(1, 11):
    n = int(input())
    arr = input()
    num = []
    count = 0
    op = ['+', '*']
    while count < len(arr):
        if arr[count] not in op:
            num.append(int(arr[count]))
        else:
            if arr[count] == '*':
                x = int(num.pop())
                y = int(arr[count + 1])
                num.append(x * y)
                count += 1
        count += 1

    result = sum(num)

    print('#%d'%(tr),result)