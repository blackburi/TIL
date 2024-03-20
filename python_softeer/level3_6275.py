# 로봇이 지나간 경로

# 출력형식
# 처음 로봇을 두어야 하는 위치 (a, b)
# 처음 로봇이 바라보는 방향 (>는 동쪽, <는 서쪽, v는 남쪽, ^는 북쪽)
# 명령어출력 (단 명령어의 개수는 최소여야 한다.)


import sys
input = sys.stdin.readline

h, w = map(int, input().split())
mat = [list(input()) for _ in range(h)]