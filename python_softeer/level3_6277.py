# 사물인식 최소 면적 산출 프로그램

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 최소 면적
area = 2000*2000

# 색별로 모아준다 -> 자연수 이기 때문에 순서대로 맞춰준다
colors = [[] for _ in range(k+1)]
for _ in range(n) :
    x, y, color = map(int, input().split())
    colors[color].append((x, y))

# 포함하는 색의 개수, x 큰값, x작은값, y큰값, y작은값
def dfs(cnt, x_big, x_small, y_big, y_small) :
    global area

    if cnt == k+1 :
        area = min(area, (x_big-x_small)*(y_big-y_small))
        return

    # 현재는 cnt-1개만큼 포함시켰음 -> cnt에 해당하는 색을 포함시킬 차례
    for a, b in colors[cnt] :
        sub_x_big = max(a, x_big)
        sub_x_small = min(a, x_small)
        sub_y_big = max(b, y_big)
        sub_y_small = min(b, y_small)

        if area > (sub_x_big - sub_x_small)*(sub_y_big - sub_y_small) :
            dfs(cnt+1, sub_x_big, sub_x_small, sub_y_big, sub_y_small)


# 색의 순서는 상관없음 차례대로 한개씩 포함
for x, y in colors[1] :
    # 2로 시작하는 이유는 1번 색을 넣고 시작하기 때문에
    # dfs에 넣으면 cnt에 해당하는 색을 선택
    dfs(2, x, x, y, y)

print(area)