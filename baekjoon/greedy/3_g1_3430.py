# 용이 산다

import sys
input = sys.stdin.readline
import heapq


tc = int(input())
for _ in range(tc) :
    # 호수, 호수에 비가 내리는 날의 수
    n, m = map(int, input().rstrip().split())
    rain = list(map(int, input().rstrip().split()))

    # 현재 호수가 비었는지 확인하는 list
    check = [False] * (n+1)
    # 재앙을 피할수 있는지 확인하는 변수
    flag = True
    # 현재 호수 번호가 i일 때, 비가 오는 시간을 역순으로 저장
    rev = [[] for _ in range(n+1)]
    # 현재 시간 t에서 비가 올 때 해당하는 호수의 번호
    time = [-1] * m

    # 거꾸로 저장하여 먼저 마셔야 하는 호수의 번호를 우선순위로 마시도록 하기 위해서
    for i in range(m-1, -1, -1) :
        if rain[i] :
            time[i] = rain[i]
            rev[rain[i]].append(i)

    # 우선순위 큐에 삽입
    pq = []
    for i in range(1, n+1) :
        if rev[i] :
            heapq.heappush(pq, rev[i].pop())

    # 용이 마시는 호수 번호를 저장하는 리스트
    ans = []
    for i in range(m) :
        # 현재 비가 온다면
        if rain[i] :
            # 비가 오는데 호수가 비지 않았다면 -> 재앙이 일어남
            if not check[rain[i]] :
                flag = False
                break
            # 비가 오는데 호수가 비었다면
            # 그 다음 비오는 시간을 우선순위 큐에 저장
            check[rain[i]] = False
            if rev[rain[i]] :
                heapq.heappush(pq, rev[rain[i]].pop())
        # 현재 비가 오지 않는다면
        else :
            # 마실수 있는 호수가 있다면 greedy로 마신다
            if pq :
                now = pq[0]
                heapq.heappop(pq)
                ans.append(time[now])
                check[time[now]] = True
            # 마실수 있는 호수가 없는 경우
            else :
                ans.append(0)

    # 정답 출력
    if not flag :
        print("NO")
    else :
        print("YES")
        print(' '.join(map(str, ans)))