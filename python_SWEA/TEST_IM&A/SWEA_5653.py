# 세포배양

import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1) :
    n, m, k = map(int, input().split())

    # 공간이 정해져 있지 않기 때문에 크게 설정
    # k만 더해도 될줄 알았는데 그러면 공간이 부족함 -> error : out of range
    place = [[0]*(m+k*2) for _ in range(n+k*2)]

    # 세포들의 위치
    cells = [list(map(int, input().rstrip().split())) for _ in range(n)]

    # 번식하는 세포를 담을 list
    cell = []
    for i in range(n) :
        for j in range(m) :
            # 세포의 주기
            x = cells[i][j]
            if x > 0 :
                # [x, x]로 두는 이유
                # 앞의 x는 생존 시간, 뒤의 x는 활성 시간
                place[k+i][k+j] = [x, x]
                cell.append([k+i, k+j])
    
    for p in range(k) :
        # 새로 생기는 세포
        born = []
        for cel in cell :
            a, b = cel[0], cel[1]

            # 분열 전 : 시간이 지나면 -1
            if place[a][b][1] > 0 :
                place[a][b][1] -= 1
            # 세포 분열 후
            elif place[a][b][1] == 0 :
                x = place[a][b][0]
                for mx, my in [[0, 1], [0, -1], [1, 0], [-1, 0]] :
                    if place[a+mx][b+my] == 0 :
                        born.append([a+mx, b+my, x])
                # 생명력 감소
                place[a][b][1] -= 1
                place[a][b][0] -= 1
            # 시간만 경과(분열x, 생명력 감소)
            else :
                if place[a][b][0] > 0 :
                    place[a][b][0] -= 1
        
        # 새로 생긴 세포를 place에 넣어준다
        for born_cell in born :
            a, b, c = born_cell
            if place[a][b] == 0 :
                place[a][b] = [c, c]
                cell.append([a, b])
            else :
                # 세포가 겹치는 경우 생명력 비교
                if place[a][b][0] < c :
                    place[a][b] = [c, c]

    # 살아있는 세포 개수
    cnt = 0
    for i in range(n+k*2) :
        for j in range(m+k*2) :
            if place[i][j] and place[i][j][0] > 0 :
                cnt += 1
    
    print(f'#{tc} {cnt}')