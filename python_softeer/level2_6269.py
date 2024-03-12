# 비밀 메뉴

import sys
input = sys.stdin.readline

# 비밀메뉴 길이, 사용자 입력 길이, 숫자
m, n, k = map(int, input().split())
secret = list(map(int, input().split()))

number = list(map(int, input().split()))

if m > n :
    print('normal')
    exit()

# 비밀 메뉴가 있는지 체크하는 변수
# cnt = m 이 되면 비밀메뉴를 받을수 있다.
for i in range(n-m+1) :
    cnt = 0
    for j in range(m) :
        if secret[j] == number[i+j] :
            cnt += 1
        else :
            break

    if cnt == m :
        break

if cnt == m :
    print('secret')
else :
    print('normal')