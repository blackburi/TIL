# 텔레포트 3

import sys
input = sys.stdin.readline

start = list(map(int, input().rstrip().split()))
end = list(map(int, input().rstrip().split()))

tel1 = list(map(int, input().rstrip().split()))
tel2 = list(map(int, input().rstrip().split()))
tel3 = list(map(int, input().rstrip().split()))

M = float('inf')

position = [(0, 0), start, end, tel1[:2], tel1[2:], tel2[:2], tel2[2:], tel3[:2], tel3[2:]]

# idx = 0 제외
# 순서대로 start, end, tel1_start, tel1_end, tel2_start, tel2_end, tel3_start, tel3_end
# 걸리는 시간을 담아둔다.
# graph[i][j] : i좌표에서 j좌표까지 가는데 걸리는 시간(position기준)
graph = [[M]*9 for _ in range(9)]
graph[3][4], graph[4][3] = 10, 10
graph[5][6], graph[6][5] = 10, 10
graph[7][8], graph[8][7] = 10, 10

# teleport 이용 X
for i in range(1, 9) :
    for j in range(1, 9) :
        graph[i][j] = min(graph[i][j], abs(position[i][0]-position[j][0])+abs(position[i][1] - position[j][1]))
        graph[j][i] = graph[i][j]

for k in range(1, 9) :
    for a in range(1, 9) :
        for b in range(1, 9) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph[1][2])