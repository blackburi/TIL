# '현재 물건을 담으면서 최대가치 vs 현재 물건을 담지 않으면서 최대가치'를 비교
# 현재 물건을 담는 경우 : 현재 물건의 가치 + (현재 가방의 무게 - 현재 물건 무게)의 최대 가치
# 현재 물건을 담지 않는 경우 : 이전 물건까지의 가방에서의 최대 가치
# 두개를 비교하여 계속 maximum값을 찾으면 된다.

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 이중 for문에서 indexerror를 방지하기 위해 [0, 0]을 추가하고 mat을 k+1, n+1까지 만든다.
# [무게-가치] 쌍으로 input을 받는다.
w_v = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
mat = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1) :
    for j in range(1, k+1) :
        if j < w_v[i][0] : # 현재 가방의 무게 < 물건의 무게
            mat[i][j] = mat[i-1][j]
        else : # j >= w_v[i][0]
            mat[i][j] = max(w_v[i][1]+mat[i-1][j-w_v[i][0]], mat[i-1][j])

print(mat[-1][-1])