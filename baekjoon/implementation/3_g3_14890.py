# 경사로

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
mat = [list(map(int, input().rstrip().split())) for _ in range(n)]

visited = [False for _ in range(n)]

answer = 0

# 경사로 설치가 가능한지 확인하는 함수
def check(now) :
    for i in range(1, n) :
        # 높이 차이가 1인 경우에만 가능
        if abs(now[i] - now[i-1]) > 1 :
            return False

        # 현재 높이 < 이전 높이 -> 낮은곳(현재)
        if now[i] < now[i-1] :
            # l만큼 경사로 길이 필요
            for j in range(l) :
                # 범위 초과, 이미 설치된 곳, 낮은 곳의 높이가 다른 경우
                if i + j >= n or visited[i+j] or now[i] != now[i+j] :
                    return False
                # 높이가 같은 경우
                if now[i] == now[i+j] :
                    visited[i+j] = True
        # 현재 높이 > 이전 높이 -> 낮은곳(이전)
        elif now[i] > now[i-1] :
            for k in range(l) :
                if i-k-1 < 0 or now[i-1] != now[i-k-1] or visited[i-k-1] :
                    return False
                if now[i-1] == now[i-k-1] :
                    visited[i-k-1] = True
    return True

# 가로 확인
for i in range(n) :
    visited = [False for _ in range(n)]
    if check(mat[i]) :
        answer += 1

# 세로 확인
for i in range(n) :
    visited = [False for _ in range(n)]
    if check([mat[j][i] for j in range(n)]) :
        answer += 1

print(answer)