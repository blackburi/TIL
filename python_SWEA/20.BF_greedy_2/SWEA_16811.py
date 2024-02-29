# 당근 포장하기

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()
    dic = {}
    
    for i in carrot :
        if i not in dic :
            dic[i] = 1
        else : # i in dic
            dic[i] += 1

    # 무게가 같은 것을 묶은 갯수 list
    getsu = list(dic.items())
    getsu.sort(key = lambda x : x[0])
    for i in range(len(getsu)) :
        getsu[i] = getsu[i][1]

    for i in getsu :
        if i > n//2 :
            getsu = []
    
    if getsu == [] :
        print(f'#{tc} -1')
        continue

    # 묶음의 종류(같은 무게는 묶음)
    kind = len(getsu)
    if kind <= 2 :
        print(f'#{tc} -1')
        continue

    # 박스 사이의 갯수 차이의 최솟값
    ans = sum(getsu)

    # i, j는 각각 3개의 박스로 나눌 2개의 포인트
    for i in range(1, kind-1) :
        for j in range(i+1, kind) :
            small = sum(getsu[:i])
            medium = sum(getsu[i:j])
            large = sum(getsu[j:])
            ans = min(ans, max(small, medium, large) - min(small, medium, large))

    print(f'#{tc} {ans}')