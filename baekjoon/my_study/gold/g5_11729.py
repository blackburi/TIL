import sys
input = sys.stdin.readline

n = int(input())
ans = []
cnt = 0

def hanoi(n, start, end) :
    if n == 1 :
        print(start, end)
    else :
        # 1~(n-1)번 원판을 이동
        hanoi(n-1, start, 6-start-end)
        # n번 원판 이동
        print(start, end)
        # 1~(n-1)번 원판을 n번 원판 위로 이동
        hanoi(n-1, 6-start-end, end)

print(2**n-1) # 총 횟수
hanoi(n, 1, 3)