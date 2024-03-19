# 업무 처리

import sys
input = sys.stdin.readline

# 조직도의 높이 h, 말단에 대기하는 업무의 개수 k, 업무가 진행되는 날짜 R
# 조직도의 높이가 h라면 h+1번째 날부터 완료된 업무가 나온다.
# 말단 조직원의 수가 정해진다면 -> 업무가 처리되는 순서도 정해진다.
h, k, r = map(int, input().split())

# 업무 번호
tasks = []
for _ in range(2**h) :
    tasks.append(list(map(int, input().rstrip().split())))

# 홀수번째 날엔 왼쪽 부하직원, 짝수번째 날엔 오른쪽 부하직원

# 말단직원에게 number를 부여했을때 업무가 처리되는 순서를 결정
number = [i for i in range(2**h)]
tmp = 1

while 