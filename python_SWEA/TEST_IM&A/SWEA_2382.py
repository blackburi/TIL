# 미생물 격리

import copy

T = int(input())

for tc in range(1, T+1) :
    # n*n matrix, m time, k count
    n, m, k = map(int, input().split())

    # 미생물들의 정보
    miseng = []
    # [x, y], cnt, direction
    # direction (상1, 하2, 좌3, 우4)
    for _ in range(k) :
        x, y, cnt, dir = map(int, input().split())
        miseng.append([x, y, cnt, dir])
    print(miseng)
    # m시간 만큼 이동
    for _ in range(m) :
        # 미생물 한개씩 이동
        # 변경된 이후의 미생물들의 값
        arrive_side = []
        # 약품부분에 도착한 경우 : cnt//2, 방향 반대
        for i in range(len(miseng)) :
            x, y, cnt, dir = miseng[i][0], miseng[i][1], miseng[i][2],miseng[i][3]

            if dir == 1 :
                x -= 1
            elif dir == 2 :
                x += 1
            elif dir == 3 :
                y -= 1
            else : # dir == 4
                y += 1

            # 약품 부분에 도착한 경우
            if x == 0 or y == 0 or x == n-1 or y == n-1 :
                cnt //= 2
                if cnt == 0 :
                    # 삭제
                    continue
                else :
                    if dir == 1 :
                        dir = 2
                    elif dir == 2 :
                        dir = 1
                    elif dir == 3 :
                        dir = 4
                    else : # dir == 4
                        dir = 3
                    arrive_side.append([x, y, cnt, dir])
            else :
                arrive_side.append([x, y, cnt, dir])
        miseng = copy.deepcopy(arrive_side)

        # 미생물들끼리 만난 경우 합쳐야 하기 때문에 정렬
        miseng.sort(key = lambda x :(x[0], x[1]))


        # 미생물들을 규칙에 적용 : 미생물들끼리 만난 경우
        after_meet = []

        # count를 했다면 그만큼 pass
        passing = 0

        for tmp in range(len(miseng)) :
            # 같은 위치에 미생물 군집이 있으면 넣어둘 list
            sub = [miseng[tmp]]

            # 이전에 한번봤다면 continue
            if passing > 0 :
                passing -= 1
                continue

            for i in range(tmp+1, len(miseng)) :
                if miseng[tmp][0] == miseng[i][0] and miseng[tmp][1] == miseng[i][1] :
                    sub.append(miseng[i])
                    passing += 1
                elif (miseng[tmp][0] != miseng[i][0] or miseng[tmp][1] != miseng[i][1]) and len(sub) == 1 :
                    break
                else : # (miseng[tmp][0] != miseng[i][0] or miseng[tmp][1] != miseng[i][1]) and len(sub) != 1
                    # 양 비교를 위한 임시 list
                    compare = []
                    for j in range(len(sub)) :
                        compare.append(sub[j][2])
                    a = compare.index(max(compare))
                    x, y, _, dir = miseng[tmp]
                    after_meet.append([x, y, sum(compare), sub[j][3]])
                    break
        
        miseng = copy.deepcopy(after_meet)
        print(miseng)
    print(f'#{tc} {sum(cnt for x, y, cnt, dir in miseng)}')
