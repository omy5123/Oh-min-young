"""
1 이상 100만(106) 이하의 모든 소수를 구하는 프로그램을 작성하시오.

참고로, 10 이하의 소수는 2, 3, 5, 7 이다.

[입력]

이 문제의 입력은 없다.

[출력]

1 이상 100만 이하의 소수를 공백을 사이에 두고 한 줄에 모두 출력한다.

입력

출력
 2 3 5 7 .... (생략) ... 999983
"""
arr = [2]
for i in range(3,10**6,2):
    check = 1
    for j in range(3,i+1,2):
        if i%j == 0 and i != j:
            check = 0
            break
    if check:
        arr.append(i)
print(' '.join(map(str,arr)))