a = int(input())
b = 0
for i in range(2*a-1, 0,-2):
    print(" "*b+"*"*i)
    b += 1
b = b-2
for i in range(3, 2*a,2):
    print(" "*b+"*"*i)
    b -= 1

