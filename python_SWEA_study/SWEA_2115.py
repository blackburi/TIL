# 벌꿀 채취

from itertools import combinations

# 꿀통 list를 가져왔을때 최대 수익을 내는 경우
def comb(lst) :
    re = 0
    for i in range(1, m+1) :
        # lst에서 i개를 선택
        combine = list(combinations(lst, i))
        for j in combine :
            total = 0
            if sum(j) <= c :
                for k in j :
                    total += k**2
            re = max(re, total)
    return re


def find(box, total) :
    global ans

    # 일꾼들이 채집을 완료한 경우
    if box == 2 :
        ans = max(ans, total)
        return

    # 벌꿀 통을 선정



T = int(input())
for tc in range(1, T+1) :
    # 벌통의 크기, 선택할 수 있는 벌통의 수, 채취 가능한 꿀의 최대 양
    n, m, c = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    # 최대 이익
    ans = 0

https://tarra.tistory.com/entry/SW-Expert-Academy-2115-%EB%B2%8C%EA%BF%80%EC%B1%84%EC%B7%A8