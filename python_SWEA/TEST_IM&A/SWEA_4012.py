# 요리사

def yummy(cnt, k) :
    global chai
    if cnt == n//2 :
        A = []
        B = []
        for i in range(n) :
            if visited[i] is True :
                A.append(i)
            else :
                B.append(i)
        hap_A = 0
        hap_B = 0

        # chai와 비교시 //2를 하는 이유
        # i와 j가 뒤바뀌어서도 또 더해지기 때문이다.
        for i in A :
            for j in A :
                hap_A += synergy[i][j] + synergy[j][i]
        for i in B :
            for j in B :
                hap_B += synergy[i][j] + synergy[j][i]
        if chai > abs(hap_A - hap_B)//2 :
            chai = abs(hap_A - hap_B)//2
        return

    for i in range(k, n) :
        if visited[i] is False :
            visited[i] = True
            yummy(cnt+1, i+1)
            visited[i] = False


T = int(input())

for tc in range(1, T+1) :
    n = int(input())

    # A와 B로 나눌 기준
    visited = [False] * n

    synergy = [list(map(int, input().split())) for _ in range(n)]

    # 두 음식의 차이
    chai = 20000 * n**2

    yummy(0, 0)
    print(f'#{tc} {chai}')