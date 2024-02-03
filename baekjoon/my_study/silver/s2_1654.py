import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
short, long = 1, max(lan)

while short <= long:
    mid = (short + long) // 2
    line = 0
    for i in lan:
        line += i//mid

    if line >= n:
        short = mid + 1
    else :
        long = mid - 1

print(long)