# 신발끈 정리의 활용
# 절댓값을 제외하고 내가 사용한 풀이 기준으로
# 양수라면 반시계 방향, 음수라면 시계 방향, 0이라면 일직선이다.

import sys
input = sys.stdin.readline

x1, y1 = map(int, input().rstrip().split())
x2, y2 = map(int, input().rstrip().split())
x3, y3 = map(int, input().rstrip().split())

pandan = (x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3)

if pandan == 0 :
    print(0)
elif pandan > 0 :
    print(1)
elif pandan < 0 :
    print(-1)