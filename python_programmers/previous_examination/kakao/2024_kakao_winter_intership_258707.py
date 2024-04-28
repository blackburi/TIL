# 2024 KAKAO WINTER INTERSHIP
# programmers 258707
# n+1 카드게임

from collections import deque

def solution(coin, cards) :
    n = len(cards)
    # 시작 카드 덱
    start = cards[:n//3]
    # 남은 카드 덱
    rest = deque(cards[n//3:])

    # 합이 n+1이 되는 쌍이 존재하는지 check하는 함수
    def check(lst1, lst2) :
        for x in lst1 :
            if (x != n+1-x) and (n+1-x in lst2):
                lst1.remove(x)
                lst2.remove(n+1-x)
                return True
        return False

    answer = 1
    # 버리는 카드를 전부 버리면 안된다 -> 나중에 쓸수 있기 때문에
    get = []

    while rest :
        get.append(rest.popleft())
        get.append(rest.popleft())

        if check(start, start) :
            answer += 1
        elif coin >= 1 and check(start, get) :
            coin -= 1
            answer += 1
        elif coin >= 2 and check(get, get) :
            coin -= 2
            answer += 1
        else :
            break
    return answer