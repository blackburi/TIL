import sys
input = sys.stdin.readline

# rule
# a층 b호에 살려면
# (a-1)층 1~b호까지의 사람들의 수의 합만큼 데리고 살아야 한다.


T = int(input()) # test case
for _ in range(T) :
    k = int(input()) # k층
    n = int(input()) # n호

    p = [x for x in range(1, n+1)] # 0층 사람들의 인원
    for i in range(1, k+1) : # 1층부터 n층까지
        for j in range(1, n) : # i층에 있는 인원 list를 만듬
            p[j] += p[j-1]
    
    print(p[-1])