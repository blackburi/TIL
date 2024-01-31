import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1) :
    N, K = list(map(int, input().split()))
    cnt = 0
    A = [i for i in range(1, 13)]

    while len(A) > 10 :
        A = [i for i in range(1, 13)]
        d = 0

        a = A.pop(p)
        d += a

        while len(A) > 9
            b = A.pop(q)
            d += b

            for r in range(10) :
                c = A.pop(r)
                d += c

                if d == K :
                    cnt += 1

    print(f'#{tc} {cnt}')