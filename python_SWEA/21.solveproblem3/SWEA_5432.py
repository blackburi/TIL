# 쇠막대기 자르기

T = int(input())

for tc in range(1, T+1) :
    lst = list(input())

    # 쇠막대기의 개수
    cnt = 0

    # 총 잘린 쇠막대기의 개수
    total = 0

    for i in range(len(lst)) :
        if lst[i] == '(' :
            # i번쨰가 레이저가 나오는 경우
            if lst[i+1] == ')' :
                total += cnt
            # i번째가 막대기가 추가되는 경우
            else : # lst[i+1] == '('
                cnt += 1
        else : # lst[i] == ')'
            # 레이저였던 경우
            if lst[i-1] == '(' :
                continue
            # 막대가 끝나서 사라지는 경우
            else : # lst[i-1] == ')'
                total += 1
                cnt -= 1
    
    print(f'#{tc} {total}')