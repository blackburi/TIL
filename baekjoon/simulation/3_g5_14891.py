# 톱니바퀴

import sys
input = sys.stdin.readline
from collections import deque

# 톱니 상태 저장
wheels = [deque(list(map(int, input().rstrip()))) for _ in range(4)]

# 톱니 돌리기
k = int(input())

for _ in range(k) :
    # 처음 톱니의 맞닿은 부분을 저장
    first = []
    
    for i in range(4) :
        # 왼쪽과 맞닿는 부분, 오른쪽과 맞닿는 부분
        first.append((wheels[i][6], wheels[i][2]))

    num, dir = map(int, input().split())
    # python은 0까지 계산 -> 미리 1을 빼둔다
    num -= 1

    # 왼쪽 톱니 확인하고 돌리기
    if num != 0 :
        for i in range(num, 0, -1) :
            if first[i][0] != first[i-1][1] :
                if (num-(i-1)) % 2 == 0 :
                    wheels[i-1].rotate(dir)
                else : # (num-(i-1)) % 2 != 0
                    wheels[i-1].rotate(-1*dir)
            else : # first[i][0] == first[i-1][1]
                break

    # 오른쪽 톱니 확인하고 돌리기
    if num != 3 :
        for i in range(num, 3) :
            if first[i][1] != first[i+1][0] :
                if (num-(i+1)) % 2 == 0 :
                    wheels[i+1].rotate(dir)
                else : # (num-(i+1)) % 2 != 0
                    wheels[i+1].rotate(-1*dir)
            else : # first[i][1] == first[i+1][0]
                break

    wheels[num].rotate(dir)

answer = 0
if wheels[0][0] == 1 :
    answer += 1
if wheels[1][0] == 1 :
    answer += 2
if wheels[2][0] == 1 :
    answer += 4
if wheels[3][0] == 1 :
    answer += 8

print(answer)