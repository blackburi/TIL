# 표 병합

mat = [["EMPTY"] * 51 for _ in range(51)]
union_find_mat = [[(r, c) for c in range(51)] for r in range(51)]


# union-find
def find(r, c) :
    if (r, c) == union_find_mat[r][c] :
        return union_find_mat[r][c]
    
    mr, mc = union_find_mat[r][c]
    union_find_mat[r][c] = find(mr, mc)
    return union_find_mat[r][c]

# 제일 상위 셀에 value 삽입
def update(r, c, value) :
    mr, mc = find(r, c)
    mat[mr][mc] = value

# 해당되는 모든 셀을 찾아 value 변경
def updatevalue(v1, v2) :
    for i in range(51) :
        for j in range(51) :
            if mat[i][j] == v1 :
                mat[i][j] = v2


# 셀 병합
def merge(r1, c1, r2, c2) :
    mr1, mc1 = find(r1, c1)
    mr2, mc2 = find(r2, c2)

    if mat[mr1][mc1] == "EMPTY" and mat[mr2][mc2] != "EMPTY" :
        mat[mr1][mc1] = mat[mr2][mc2]
    union_find_mat[mr2][mc2] = union_find_mat[mr1][mc1]


# 셀 분할
def unmerge(r, c) :
    mr, mc = find(r, c)
    tmp = mat[mr][mc]

    lst = []
    for i in range(51) :
        for j in range(51) :
            if find(i, j) == (mr, mc) :
                lst.append((i, j))
    # 해당하는 칸 제외하고 전부 EMPTY로 바꿔줘야 함
    for (i, j) in lst :
        mat[i][j] = "EMPTY"
        union_find_mat[i][j] = (i, j)
    # 해당칸은 기존값을 넣어준다.
    mat[r][c] = tmp


def solution(commands):
    answer = []

    for command in commands :
        command = list(command.split())
        if command[0] == "UPDATE" :
            # update, r, c, value
            if len(command) == 4 :
                update(int(command[1]), int(command[2]), command[3])
            # update value1, value2
            else :
                updatevalue(command[1], command[2])
        elif command[0] == "MERGE" :
            merge(int(command[1]), int(command[2]), int(command[3]), int(command[4]))
        elif command[0] == "UNMERGE" :
            unmerge(int(command[1]), int(command[2]))
        elif command[0] == "PRINT" :
            r, c = find(int(command[1]), int(command[2]))
            answer.append(mat[r][c])
    
    return answer