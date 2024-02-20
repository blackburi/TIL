T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    mat = [list(input()) for _ in range(n)]
    
    # x행을 검사
    def row(x) :
        cnt = 0
        for i in range(n) :
            if mat[x][i] == 'o' :
                cnt += 1
                if cnt == 5 :
                    break
            else :
                cnt = 0
        if cnt == 5 :
            return True
        else :
            return False
    
    # y열을 검사
    def col(y) :
        if ['o', 'o', 'o', 'o', 'o'] in zip(mat[i] for i in range(n)) :
            return True
        else :
            return False
    
    # 대각선 검사
    def cross()