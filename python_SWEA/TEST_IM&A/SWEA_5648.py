# 원자 소멸 시뮬레이션

T = int(input())

for tc in range(1, T+1) :
    mat = [[0]*2001 for _ in range(2001)]

    # 원자의 개수
    n = int(input())

    # 원자의 위치와 이동방향
    # 상(0), 하(1), 좌(2), 우(3)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    electron = []
    for _ in range(n) :
        # [x, y]:위치, d:direction, e:energy -- [x, y, d, e]
        x, y, d, e = (list(map(int, input().split())))
        mat[x+1000][y+1000] = [x, y, d, e]

    # 에너지의 합
    hap = 0
    t = 2000

    while t and electron :
        for i in electron :
            if 0 <= i[0]+dx[i[2]] <= 2000 and 0 <= i[1]+dy[i[2]] <= 2000 :
                if mat[i[0]+dx[i[2]]][i[1]+dy[i[2]]] != 0 :
                    hap += i[3] + mat[i[0]+dx[i[2]]][i[1]+dy[i[2]]][3]
                    electron.remove(i)
                    mat[i[0]+dx[i[2]]][i[1]+dy[i[2]]][3] = 0
                else :
                    mat[i[0]+dx[i[2]]][i[1]+dy[i[2]]] = i
            else :
                electron.remove(i)
        t -= 1
    
    print(f'#{tc} {hap}')