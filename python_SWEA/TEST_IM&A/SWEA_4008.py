# 숫자 만들기

def dfs(k, cal) :
    global cal_max, cal_min
    if k == n :
        cal_max = max(cal_max, cal)
        cal_min = min(cal_min, cal)
        return

    for i in range(4) :
        if operator[i] > 0 :
            operator[i] -= 1
            if i == 0 :
                dfs(k+1, cal+numbers[k])
            elif i == 1 :
                dfs(k+1, cal-numbers[k])
            elif i == 2 :
                dfs(k+1, cal*numbers[k])
            else : # i == 3
                dfs(k+1, int(cal/numbers[k]))
            operator[i] += 1


T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    
    # + , -, *, //
    operator = list(map(int, input().split())) 
    numbers = list(map(int, input().split()))

    cal_max = -100000000
    cal_min = 100000000

    dfs(1, numbers[0])
    print(f'#{tc} {cal_max-cal_min}')