# 연구소

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
mat = [list(map(str, input().rstrip().split())) for _ in range(n)]



# 안전 구역의 넓이
ans = 0

# 안전구역은 바이러스가 퍼진 이후 '0'의 영역
for i in range(n) :
    ans += mat[i].count('0')

print(ans)