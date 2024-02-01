# 풍선팡
import sys
input = sys.stdin.readline

T = int(input())

def four(x,y,k) :
    sub = 0
    
    if 0 <= x+k <= n-1 and 0 <= y <= m-1 :
        sub += mat[x+k][y]
    
    if 0 <= x-k <= n-1 and 0 <= y <= m-1 :
        sub += mat[x-k][y]
    
    if 0 <= x <= n-1 and 0 <= y+k <= m-1 :
        sub += mat[x][y+k]
    
    if 0 <= x <= n-1 and 0 <= y-k <= m-1 :
        sub += mat[x][y-k]
    
    return sub

for tc in range(1, T+1) :
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    
    hmax = 0
    for i in range(n) :
        for j in range(m) :
            hap = 0
            p = mat[i][j]
            hap += p
            
            for k in range(1, p+1) :
                hap += four(i,j,k)
            
            if hmax < hap :
                hmax = hap
    
    print(f'#{tc} {hmax}')