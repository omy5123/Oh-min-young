"""
성경이는 대통령 직속 통역관이다.

대통령은 사람 이름을 외우는 것을 굉장히 중요시 한다.

따라서 외국 대사와의 대화에서 나오는 모든 이름을 외워달라고 성경이에게 부탁했다.

외국 대사는 총 N개의 문장을 말했다.

각 문장의 마지막 단어는 세 가지 구두점 ‘.’, ‘?’, ‘!’ 중 하나를 마지막에 포함한다.

문장은 대소문자 알파벳와 숫자로 이루어진 단어들이 공백을 사이에 두고 구성되어 있으며, 예외적으로 마지막 단어는 구두점으로 끝나게 된다.

이름은 대문자 알파벳으로 시작하며 나머지는 소문자 알파벳인 단어들이다.

예외적으로, 단어의 마지막이 구두점일 경우에도 이름이며, 대문자 한글자도 이름이다.

성경이는 대통령을 위해서 외국 대사와의 대화를 문서로 받아서 이름이 몇 번 나오는 지를 알려줘야 한다.

N개의 문장을 받아서 문장 별로 이름의 개수를 구하여라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T(1 ≤ T ≤ 11)가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 문장의 개수 N(1 ≤ N ≤ 5)이 주어진다.

두 번째 줄에는 N개의 문장이 주어지며, 총 문자의 개수는 1,000개 이하이다.


[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

N개의 수를 공백 하나로 구분하여 출력해야 하며, 각수는 각 문장에 속한 이름의 개수여야 한다.

입력
2
2
Annyung Hasae Yo! LoL!
3
my name is Hye Soo. my id is
Rhs0266. what your id Bro?	// 테스트 케이스 개수
// 첫 번째 테스트 케이스, N = 2


// 두 번째 테스트 케이스, N = 3

출력
#1 3 0
#2 2 0 1
"""
import sys
sys.stdin = open('input.txt')
t = int(input())
for tr in range(t):
    a = int(input())
    arr = list(map(str, input().split()))
    upper = []
    check = 1
    nums= '1234567890'
    result = [0]*a
    for i in range(26):
        upper.append(chr(65+i))
    s = 0
    cnt = 0
    for i in arr:
        cnt_1 = 0
        for j in range(len(i)):
            if i[j] in upper:
                cnt_1 += 1
            if i[j] in nums:
                cnt_1 = 0
                break
        if cnt_1 ==1:
            cnt += 1
        if i[-1] == '!' or i[-1] == '.'or i[-1] == '?':
            result[s] = cnt
            s += 1
            cnt = 0
    print('#%d'%(tr+1),end=' ')
    for i in range(a):
        print(result[i], end=' ')
    print()