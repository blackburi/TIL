# 전기 버스

T = int(input())

for tc in range(1, T+1) :
    # k:버스가 한번 가는 정류장수, n : 도착 정류장, m : 충전소가 있는 정류장
    k, n, m = list(map(int, input().split()))
    busstop = list(map(int, input().split()))

    present = 0 # 현재 위치
    cnt = 0

    while present < n :
        present += k

        if present >= n :
            break

        if present not in busstop :
            for i in range(1, k) :
                if (present-i) not in busstop :
                    if i == (k-1) :
                        cnt = 0
                        present = n         
                else :
                    cnt += 1
                    present -= i
                    break

        else :
            cnt += 1

    print(f'#{tc} {cnt}')
