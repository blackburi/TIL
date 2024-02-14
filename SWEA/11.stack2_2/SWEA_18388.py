def f(i, hap) :
    global ans
    if i == n :
        if ans > hap :
            ans = hap
    else :
        if hap > ans :
            return
        for j in range(i, n) : 
            idx[i], idx[j] = idx[j], idx[i] # p[i] <-> p[j]
            f(i+1, hap + mat[i][idx[i]])
            idx[i], idx[j] = idx[j], idx[i] # 교환전으로 복구

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    idx = [i for i in range(n)]
    ans = 10 * n
    f(0, 0)
    print(f'#{tc} {ans}')