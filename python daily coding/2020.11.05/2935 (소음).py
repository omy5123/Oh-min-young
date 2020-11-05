import sys
sys.stdin = open('input.txt')

a = int(input())
operate = input()
b = int(input())

if(operate == '+'):
    print(a+b)
elif(operate == '*'):
    print(a*b)