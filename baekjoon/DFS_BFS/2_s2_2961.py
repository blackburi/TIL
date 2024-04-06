# 도영이가 만든 맛있는 음식

# 신맛은 곱, 쓴맛은 합

import sys
input = sys.stdin.readline

n = int(input())
lst = [tuple(map(int, input().rstrip().split())) for _ in range(n)]

ans = float('inf')

def dfs(x, s, b) :
    global ans

    if x !=0 and s != 1 and b != 0 :
        ans = min(ans, abs(s-b))

    if x == n :
        return

    dfs(x+1, s*lst[x][0], b+lst[x][1])
    dfs(x+1, s, b)

dfs(0, 1, 0)

print(ans)