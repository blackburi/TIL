# 이진탐색

T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst1.sort()
    lst2 = list(map(int, input().split()))

    # 정답 개수
    cnt = 0

    for i in lst2 :
        start = 0
        end = n-1

        # 왼 = 1, 우 = 2 / 이전 탐색을 어느 방향으로 했는지 저장
        go = 0

        while start <= end :
            middle = (start + end) // 2

            if i == lst1[middle] :
                cnt += 1
                break
            # 오른쪽으로 탐색 해야함
            elif i > lst1[middle] :
                if go == 2 :
                    break
                else : # go == 0 or go == 1 (처음 시행이거나 이전 시행이 좌측 탐색)
                    start = middle + 1
                    go = 2
            # 왼쪽으로 탐색 해야함
            else : # i < lst1[middle]
                if go == 1 :
                    break
                else :
                    end = middle - 1
                    go = 1
    
    print(f'#{tc} {cnt}')