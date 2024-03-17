# 업무 처리

import sys
input = sys.stdin.readline

# 조직의 높이, 업무의 개수, 진행되는 날짜
h, k, r = map(int, input().split())

# 말단 직원들의 업무 번호
task = [list(map(int, input().rstrip().split())) for _ in range(2**h)]

