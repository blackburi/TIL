# 전광판

import sys
input = sys.stdin.readline

# [최상단, 상단좌측, 상단우측, 중간, 하단좌측, 하단우측, 최하단]
dic = {0 : [1, 1, 1, 0, 1, 1, 1],
       1 : [0, 0, 1, 0, 0, 1, 0],
       2 : [1, 0, 1, 1, 1, 0, 1],
       3 : [1, 0, 1, 1, 0, 1, 1],
       4 : [0, 1, 1, 1, 0, 1, 0],
       5 : [1, 1, 0, 1, 0, 1, 1],
       6 : [1, 1, 0, 1, 1, 1, 1],
       7 : [1, 1, 1, 0, 0, 1, 0],
       8 : [1, 1, 1, 1, 1, 1, 1],
       9 : [1, 1, 1, 1, 0, 1, 1]
       }

T = int(input())
for _ in range(T) :
    a, b = map(int, input().rstrip().split())
    a, b = max(a, b), min(a, b)

    a_lst = []
    b_lst = []

    while a :
        a_lst.append(a%10)
        a //= 10
    
    while b :
        b_lst.append(b%10)
        b //= 10

    # 앞에서 a > b를 정렬했기 때문에 p > q
    p = len(a_lst)
    q = len(b_lst)

    p, q = max(p, q), min(p, q)

    # 눌러야 하는 버튼 수
    cnt = 0

    # 일의 자리부터 비교
    for i in range(q) :
        for j in range(7) :
            if dic[a_lst[i]][j] != dic[b_lst[i]][j] :
                cnt += 1

    # 자릿수가 차이가 난다면 나는만큼 차이나는 라이트 개수를 더함
    for k in range(q, p) :
        cnt += dic[a_lst[k]].count(1)
    
    print(cnt)