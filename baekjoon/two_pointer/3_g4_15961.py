# 회전 초밥

import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())

# 회전 초밥 list
sushi = []
for _ in range(n) :
    sushi.append(int(input().rstrip()))

# d종류의 스시에 대해서 선택한 연속된 k개 접시에 포함된 갯수
check = [0 for _ in range(d+1)]

cnt = 0
for i in range(k) :
    # 이번에 추가된 접시가 이전에 고른 스시가 아닌 경우
    if check[sushi[i]] == 0 :
        cnt += 1
    check[sushi[i]] += 1

    # cnt의 최대값이 저장될 변수
    # 쿠폰 스시 포함 여부에 따라 개수를 추가하며 초기화
    if check[c] == 0 :
        answer = cnt + 1
    else : # check[c] != 0
        answer = cnt

# 초기 상태(0 ~ k-1)에서 다음 접시 추가 + 처음 접시 제거
# 0 ~ k-1 번까지 k개 고른뒤 k번째 접시를 넣고, 0번째 접시를 제거
for i in range(k, n+k-1) :
    # 만약 이번에 추가된 접시가 이전에 고른 스시가 아닌경우
    if check[sushi[i%n]] == 0 :
        cnt += 1
    check[sushi[i%n]] += 1

    # 만약 이번에 빠진 스시가 1개만 있었으면 개수 빼기
    if check[sushi[i-k]] == 1 :
        cnt -= 1
    check[sushi[i-k]] -= 1

    # 쿠폰으로 받는 스시가 지금 고른 접시 중에 포함안되어 있으면 추가
    if check[c] == 0 :
        answer = max(answer, cnt+1)
    # 아니라면 그냥 계산
    else : # check[c] != 0
        answer = max(answer, cnt)

print(answer)

### 쿠폰과 관련된 코드를 최적화할 필요가 있음