def f(i, k, t) : # k개의 원소를 가진 배열A, 부분집합 합이 t
    if i == k : # 모든 원소에 대해 결정하면
        ss = 0 # 부분집합 원소의 합
        for j in range(k) :
            if bit[j] : # A[i]가 포함된 경우
                ss += A[j]
        if ss == t :
            for j in range(k) :
                if bit[j] : # A[j]가 포함된 경우
                    print(A[j], end = ' ')
            print()
    else :
        for j in range(1, -1, -1) :
            bit[i] = j
            f(i+1, k, t)
n = 10
t = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * n
f(0, n, t)