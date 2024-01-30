# 수 이어 쓰기 1

N = int(input())

def digit(M) : # 몇번 돌릴건지
    d = 0
    while M > 0 :
        M //= 10
        d += 1
    return d # N의 자릿수

def sum(M, n) :# 어떻게 돌릴건지
    s = 0 # 원하는 출력 값
    for i in range(n-1) :
         # d자릿수 숫자 제외 전부 합산
        s += 9 * (10**i) * (i+1)
    # d자릿수 숫자 합산
    s += (M - 10**(n-1) + 1) * n 
    print(s)

k = digit(N)
sum(N, k)