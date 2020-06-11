a = int(input())
b = int(input())
if 100 <= a < 1000 and 100 <= b < 1000:
    c = b % 10
    print(a * c)
    d = int((b % 100) / 10)
    print(a * d)
    e = int(b / 100)
    print(a * e)
    print(a * b)