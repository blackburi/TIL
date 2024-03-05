# 연구소

import sys
input = sys.stdin.readline
from itertools import combinations


def virus() :
    


n, m = map(int, input().rstrip().split())
mat = [list(map(str, input().rstrip().split())) for _ in range(n)]

# 전체 지역에서 1과 2가 아닌 곳(0인 곳)에서 3곳을 뽑아 벽을 세운후 count
# 벽을 세울수 있는 통로 list
lst = []
for i in range(n) :
    for j in range(n) :
        if mat[i][j] == '0' :
            lst.append([i, j])


# 벽을 세울 3곳을 정하기
for a, b, c in combinations(lst, 3) :
    mat[a[0]][a[1]] = '1'
    mat[b[0]][b[1]] = '1'
    mat[c[0]][c[1]] = '1'

# 안전 구역의 넓이
ans = 0

# 안전구역은 바이러스가 퍼진 이후 '0'의 영역
for i in range(n) :
    ans += mat[i].count('0')

print(ans)