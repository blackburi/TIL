# 보호 필름

T = int(input())
for tc in range(1, T+1) :
    # 보호 필름 두께, 가로 크기, 합격 기준
    d, w, k = map(int, input().split())

    film = []
    for _ in range(d) :
        film.append(list(map(int, input().split())))