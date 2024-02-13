''' idea
제일 아래 주사위의 바닥면이 정해진다면 최댓값이 정해진다
바닥면이 정해지면 윗면이 정해지고, 옆면의 최댓값을 더한다.
아래 주사위의 윗면이 정해지면 위 주사위의 아랫면이 결정
-> 옆면과 윗면도 결정 -> 옆면의 최댓값을 더하면된다.
즉 제일 아래 주사위의 바닥면(또는 윗면)만 결정되면 최댓값은 하나로 결정된다.
'''

import sys
input = sys.stdin.readline

n = int(input())
dice = [list(map(int, input().rstrip().split())) for _ in range(n)]

connect = {0:5,
           1:3,
           2:4,
           3:1,
           4:2,
           5:0} # 바닥면 index : 윗면 index
# 바닥면 index or 윗면 index : [옆면 index list]
side = {0:[1, 2, 3, 4],
        1:[0, 2, 4, 5],
        2:[0, 1, 3, 5],
        3:[0, 2, 4, 5],
        4:[0, 1, 3, 5],
        5:[1, 2, 3, 4]}

ans = 0 # 결과값(최댓값끼리 비교)

for i in range(6) : # 제일 아래 주사위의 바닥면 'index' = i -> 각면이 바닥면일때의 최댓값을 비교
    # 매 주사위마다 갱신을 해야 하는 목록
    top_idx = connect[i] # 제일 아래 주사위의 윗면 'index' = connect[i] // 1번
    top = dice[0][top_idx] # 제일 아래주사위의 윗면 '숫자' // 2번
    side_index = side[i] # 4개의 옆면의 'index' list // 3번
    
    # 각 주사위 옆면의 최댓값을 더해야 하는 변수
    total = max(dice[0][idx] for idx in side_index) # 제일 아래주사위의 옆면 최댓값을 total값으로 지정(처음이기 때문에)
    
    for j in range(1, len(dice)) : # 나머지 n-1개의 주사위에 대하여 계산, j번째 주사위
        # j번째 주사위의 바닥면 숫자 = (j-1)번째 주사위 윗면의 숫자 = top
        bot_idx = dice[j].index(top) # j번째 주사위의 바닥면 'index'
        top_idx = connect[bot_idx] # j번째 주사위의 윗면 'index'  // 1번 갱신
        top = dice[j][top_idx] # j번째 주사위 윗면 '숫자' // 2번 갱신
        side_index = side[bot_idx] # j번째 주사위 옆면의 'index' list // 3번 갱신
        
        total += max(dice[j][idx] for idx in side_index)
    
    # for 구문이 다 돌면 제일 아래 주사위의 바닥면 'index'= i 일때 옆면의 최댓값이 나온다.
    if ans < total :
        ans = total

print(ans)