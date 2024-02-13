import sys
input = sys.stdin.readline

# 철수의 빙고판
chul = [input().split() for _ in range(5)]

# 사회자가 부르는 번호
call = []
for _ in range(5) :
    call.extend(input().split())

def check_bin(mat) : # mat == chul
    line = 0 # 5개가 전부 지워진 줄의 수

    for i in range(5) : # 가로줄
        if mat[i] == [0, 0, 0, 0, 0] :
            line += 1

    for i in zip(mat[0], mat[1], mat[2], mat[3], mat[4]) : # 세로줄
        if i == (0, 0, 0, 0, 0) :
            line += 1
    
    dia1 = 0 # 대각선1
    dia2 = 0 # 대각선2
    for i in range(5) :
        if mat[i][i] == 0 :
            dia1 += 1
        if mat[i][4-i] == 0 :
            dia2 += 1
    if dia1 == 5 :
        line += 1
    if dia2 == 5 :
        line += 1
    
    return line

def erase(mat, num) : # mat == chul, num == call
    a = num.pop(0)
    for i in range(5) :
        if a in mat[i] :
            b = mat[i].index(a)
            mat[i][b] = 0
            break

for i in range(12) :
    erase(chul, call)

ans = check_bin(chul)

if ans == 3 :
    print(12)
else :
    call_num = 12

    while ans < 3:
        erase(chul, call)
        call_num += 1
        ans = check_bin(chul)

    print(call_num)