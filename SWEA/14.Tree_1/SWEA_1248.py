T = int(input())

for tc in range(1, T+1) :
    v, e, a, b = map(int, input().split())
    lst = list(map(int, input().split()))

    c1 = [0] * (v+1)
    c2 = [0] * (v+1)

    for i in range(e) :
        