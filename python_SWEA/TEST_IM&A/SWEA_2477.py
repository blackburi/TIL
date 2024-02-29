# 차량 정비소

from collections import deque

T = int(input())

for tc in range(1, T+1) :
    # 접수 창구, 정비창구, 고객수, 접수창구 번호, 정비창구 번호
    n, m, k, a, b = map(int, input().split())

    # 접수창구 n개
    submit = list(map(int, input().split()))
    for i in range(n) :
        # 손님 번호, 이용시간, 필요시간
        submit[i] = [0, 0, submit[i]]

    # 정비 창구 m개
    fix = list(map(int, input().split()))
    for i in range(m) :
        # 손님 번호, 이용시간, 필요시간
        fix[i] = [0, 0, fix[i]]

    # 고객 방문시간
    time = list(map(int, input().split()))
    time.sort()
    for i in range(k) :
        # 손님 번호, 방문 시간
        time[i] = [i+1, time[i]]
    time = deque(time)

    # a접수창구를 이용한 고객 번호
    ans1 = []
    # b정비창구를 이용한 고객 번호
    ans2 = []
    
    # 정비까지 완료한 손님의 수
    cnt = 0

    # 접수 창구 -> 정비 창구를 가는 손님의 list
    waiting = deque([])

    # 현재 시간
    now = 0
    while cnt < k :
        # 정비가 완료된 손님 out
        for i in range(m) :
            # 사용시간이 필요시간과 동일하다면 제외시켜준다
            if fix[i][1] == fix[i][2] :
                # fix[i] 초기화
                fix[i] = [0, 0, fix[i][2]]
                cnt += 1
        
        # 접수 완료 고객 out
        for i in range(n) :
            # 사용시간과 필요시간이 동일하다면 waiting으로 넘겨준다.
            if submit[i][1] == submit[i][2] :
                waiting.append(submit[i][0])
                submit[i] = [0, 0, submit[i][2]]
        
        # waiting -> fix(정비) 창구로 오는 사람들을 넣어준다.
        if waiting :
            for _ in range(len(waiting)) :
                for i in range(m) :
                    if fix[i][0] == 0 :
                        fix[i] = [waiting[0], 0, fix[i][2]]
                        # 사용한 정비창구가 b와 동일하다면 ans2에 넣어준다.
                        if i+1 == b :
                            ans2.append(fix[i][0])
                        waiting.popleft()
                        break
                else :
                    break

        # 접수 창구로 들어오는 사람 in
        if time :
            while True :
                for _ in range(len(time)) :
                    if time[0][1] <= now :
                        for j in range(n) :
                            if submit[j][0] == 0 :
                                number, _ = time.popleft()
                                submit[j] = [number, 0, submit[j][2]]

                                if j+1 == a :
                                    ans1.append(number)
                                break
                    else :
                        break
                break

        now += 1
        for i in range(n) :
            submit[i][1] += 1
        for i in range(m) :
            fix[i][1] += 1


    # 문제에서 원하는 손님들의 번호를 담는 list
    ans = []

    for p in ans1 :
        if p in ans2 :
            ans.append(p)
    if ans :
        print(f'#{tc} {sum(ans)}')
    else :
        print(f'#{tc} -1')