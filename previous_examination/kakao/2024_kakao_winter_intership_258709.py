# 2024 KAKAO WINTER INTERSHIP
# programmers 258709
# 주사위 고르기

from itertools import combinations

def solution(dice) :
    n = len(dice)

    # A가 이기는 경우의 수
    tmp = 0
    # 이떄 A가 가져가는 주사위
    answer = []

    # A or B, dice list, 계산한 주사위 갯수, 계산한 주사위의 합
    def check(k, lst, cnt, hap) :
        if len(lst) == cnt :
            if hap in total[k] :
                total[k][hap] += 1
            else :
                total[k][hap] = 1
            return

        for i in range(n//2) :
            if visited[k][i] is False :
                for j in range(6) :
                    visited[k][i] = True
                    check(k, lst, cnt+1, hap+lst[i][j])
                    visited[k][i] = False

    # A가 가지고 있는 주사위
    for a in combinations(dice, n//2) :
        # B가 가지고 있는 주사위
        b = []
        for i in dice :
            if i not in a :
                b.append(i)

        # A가 가진 주사위의 합:개수 dictionary, B가 가진 주사위의 합
        total = [{}, {}]
        visited = [[False] * (n//2) for _ in range(2)]

        check(0, a, 0, 0)
        check(1, b, 0, 0)

        # A가 이기는 경우
        win = 0
        for i in total[0] :
            for j in total[1] :
                if i > j :
                    win += total[0][i] * total[1][j]
        
        if tmp < win :
            tmp = win
            answer = a

    return answer