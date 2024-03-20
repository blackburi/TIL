# 부분집합 합 문제 구현하기

T = int(input())

for tc in range(1, T+1) :
    lst = list(map(int, input().split()))

    # 부분집합의 합이 0이 되는 경우 판별 변수
    tmp = 0

    for i in range(1<<len(lst)) :
        hap = 0
        for j in range(len(lst)) :
            if i & (1<<j) :
                hap += lst[j]
        if hap == 0 :
            tmp += 1
        
        # 2에서 멈추는 이유는 처음에 공집합을 count하기 때문
        if tmp == 2 :
            break
    
    print(f'#{tc} {tmp-1}')