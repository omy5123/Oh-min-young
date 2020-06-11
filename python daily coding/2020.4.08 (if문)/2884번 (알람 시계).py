a, b = map(int, input().split())
if a == 0:
    if b >= 45:
        print(a, b - 45)
    else:
        print(23, b+15)
else:
    if b >= 45:
        print(a, b-45)
    else:
        print(a-1, b+15)