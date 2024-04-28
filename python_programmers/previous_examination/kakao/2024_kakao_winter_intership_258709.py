# 2024 KAKAO WINTER INTERSHIP
# programmers 258709
# 주사위 고르기

############
# 정석 풀이 #
############

from itertools import combinations, product
from bisect import bisect_left

def solution(dices):
    dic = {}
    L = len(dices)
    for A_index_combi in combinations(range(L), L//2):
        B_index_combi = [i for i in range(L) if i not in A_index_combi]
    
        A, B = [], []
        # itertools product함수
        # product(lst1, lst2) -> 원소 한개씩을 뽑아와 tuple로 만들어줌
        # product(range(n), repeat=length) -> range(n)을 length만큼 반복하여 tuple로 만들어 반환
        for order_product in product(range(6), repeat=L//2):
            A.append(sum(dices[i][j] for i, j in zip(A_index_combi, order_product)))
            B.append(sum(dices[i][j] for i, j in zip(B_index_combi, order_product)))
        B.sort()

        wins = sum(bisect_left(B, num) for num in A)
        dic[wins] = list(A_index_combi)

    max_key = max(dic.keys())

    return [x+1 for x in dic[max_key]]

#################
# 시간 초과 풀이 #
#################

from itertools import combinations

def solution(dice) :
    n = len(dice)

    # A가 이기는 경우의 수
    tmp = 0
    # 이때 A가 가져가는 주사위
    sub = []
    # 정답 (dice number를 가져와야함)
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
        if dice[0] not in a :
            continue

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
            sub = a

        win = 0
        # B가 이기는 경우 -> 주사위를 절반만 체크하고 B가 이기는경우 이 주사위를 A가 가져가면 된다.
        for i in total[0] :
            for j in total[1] :
                if i < j :
                    win += total[0][i] * total[1][j]
        if tmp < win :
            tmp = win
            sub = b

    for number in range(n) :
        if dice[number] in sub :
            answer.append(number+1)

    return answer