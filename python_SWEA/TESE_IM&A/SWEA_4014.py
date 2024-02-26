# 활주로 건설

# x는 가로줄 또는 세로줄
def slope(lst) :
    global x
    # 높이가 동일한 영역의 길이
    tmp = 1
    for i in range(1, n) :
        # 같은 높이
        if lst[i] == lst[i-1] :
            tmp += 1
        # 높이가 1증가, 높이가 같은 영역의 길이 >= x
        elif lst[i] == lst[i-1] + 1 and tmp >= x :
            tmp = 1
        # 높이가 1감소, 높이가 낮아진 후 -x+1개만큼 더 와야한다.
        elif lst[i] == lst[i-1] - 1 and tmp >= 0 :
            tmp = -x+1
        # 높이가 2씩 차이나는 경우
        else :
            return 0
    if tmp >= 0 :
        return 1
    return 0


T = int(input())

for tc in range(1,T+1) :
    n, x = map(int, input().split())
    mat = []

    # 경우의 수를 셀 변수
    ans = 0

    # 가로줄
    for i in range(n) :
        mat.append(list(map(int, input().split())))
        ans += slope(mat[i])
    
    # 세로줄
    for i in range(n) :
        col = []
        for j in range(n) :
            col.append(mat[j][i])
        ans += slope(col)
    
    print(f'#{tc} {ans}')