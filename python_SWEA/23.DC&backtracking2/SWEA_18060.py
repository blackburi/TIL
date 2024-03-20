# 부분집합의 합

lst = [i+1 for i in range(12)]

T = int(input())
for tc in range(1, T+1) :
    # 부분집합 원소의 개수, 합
    n, k = map(int, input().split())

    # 정답을 count하는 변수
    cnt = 0

    for i in range(1<<12) :
        sub = []
        for j in range(12) :
            if i & (1<<j) :
                sub.append(lst[j])
            if len(sub) > n or sum(sub) > k :
                break
        if len(sub) == n and sum(sub) == k :
            cnt += 1
    
    print(f'#{tc} {cnt}')