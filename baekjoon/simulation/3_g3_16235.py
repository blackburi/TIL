# 나무 재테크

import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())

# 양분
mat = [list(map(int, input().rstrip().split())) for _ in range(n)]
# 초기 밭
first = [[5]*n for _ in range(n)]
# 나무 나이를 저장할 배열
trees = [[deque() for _ in range(n)] for _ in range(n)]
# 죽은 나무
dead = [[list() for _ in range(n)] for _ in range(n)]

# 입력받은 나무위치 + 나이
for _ in range(m) :
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

dx = (1, 1, 1, 0, 0, -1, -1, -1)
dy = (1, 0, -1, 1, -1, 1, 0, -1)

# 봄, 여름
def ss() :
    for p in range(n) :
        for q in range(n) :
            for r in range(len(trees[p][q])) :
                # 나무가 죽은 경우
                if first[p][q] < trees[p][q][r] :
                    # 죽은 나무 저장
                    for _ in range(r, len(trees[p][q])) :
                        dead[p][q].append(trees[p][q].pop())
                    break
                # 나무가 성장하는 경우
                else :
                    first[p][q] -= trees[p][q][r]
                    trees[p][q][r] += 1
    # 죽은 나무들 만큼 양분 저장
    for i in range(n) :
        for j in range(n) :
            while dead[p][q] :
                first[p][q] += dead[p][q].pop() // 2

# 가을 겨울
def fw() :
    for p in range(n) :
        for q in range(n) :
            # 현재 위치의 나무들 탐색
            for r in range(len(trees[p][q])) :
                # 나이가 씨를 뿌릴수 있는 나이의 경우
                if trees[p][q][r] % 5 == 0 :
                    for dir in range(8) :
                        mx = p + dx[dir]
                        my = q + dy[dir]
                        if 0 <= mx < n and 0 <= my < n :
                            # 새로 태어난 나무들 앞으로 샆입
                            trees[mx][my].appendleft(1)
            first[p][q] += mat[p][q]


for i in range(k) :
    ss()
    fw()

answer = 0
for i in range(n) :
    for j in range(n) :
        answer += len(trees[i][j])

print(answer)