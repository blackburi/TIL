# 숫자 카드

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    num = list(map(int, input()))
    
    dic = {} # {숫자 : 개수}
    for i in range(10) :
        dic[i] = 0
    
    for j in num :
        dic[j] += 1
    
    count_max = 0 # 개수의 최댓값

    for p in range(10) :
        if dic[p] > count_max :
            count_max = dic[p]
    
    # 개수의 최댓값을 갖는 수 list
    num_max = [k for k, v in dic.items() if v == count_max]

    num_max_num = 0 # 개수의 최댓값을 갖는 수 중 최댓값
    for q in num_max :
        if q > num_max_num :
            num_max_num = q

    print(f'#{tc} {num_max_num} {count_max}')