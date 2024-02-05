T = int(input())

for _ in range(1, T+1) :
    tc, n = list(map(str, input().split()))
    lst = list(map(str, input().split()))
    a0 = a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = 0

    for i in lst :
        if i == "ZRO" :
            a0 += 1
        elif i == "ONE" :
            a1 += 1
        elif i == "TWO" :
            a2 += 1
        elif i == "THR" :
            a3 += 1
        elif i == "FOR" :
            a4 += 1
        elif i == "FIV" :
            a5 += 1
        elif i == "SIX" :
            a6 += 1
        elif i == "SVN" :
            a7 += 1
        elif i == "EGT" :
            a8 += 1
        elif i == "NIN" :
            a9 += 1

    ans = ["ZRO"] * a0 + ["ONE"] * a1 + ["TWO"] * a2 + ["THR"] * a3 + ["FOR"] * a4 + ["FIV"] * a5 + ["SIX"] * a6 + ["SVN"] * a7 + ["EGT"] * a8 + ["NIN"] * a9
    print(f'{tc}')
    print(' '.join(ans))