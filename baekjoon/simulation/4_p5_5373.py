# 큐빙

import sys
input = sys.stdin.readline

"""
    www
    www
    www
ggg rrr bbb ooo
ggg rrr bbb ooo
ggg rrr bbb ooo
    yyy
    yyy
    yyy

  0
4 2 5 3
  1
"""


# 면과 방향이 주어지면 cube를 돌리는 함수
def turn(side, direction):
    if direction == '+':
        # 윗면
        if side == 'U': 
            change(0)
            temp = cube[2][0]
            cube[2][0] = cube[5][0]
            cube[5][0] = cube[3][0]
            cube[3][0] = cube[4][0]
            cube[4][0] = temp
        # 앞면
        elif side == 'F':
            change(2)
            temp = cube[0][2]
            cube[0][2] = [cube[4][2][2],cube[4][1][2],cube[4][0][2]]
            cube[4][0][2],cube[4][1][2],cube[4][2][2] = [cube[1][0][0],cube[1][0][1],cube[1][0][2]]
            cube[1][0][0],cube[1][0][1],cube[1][0][2] = [cube[5][2][0],cube[5][1][0],cube[5][0][0]]
            cube[5][0][0],cube[5][1][0],cube[5][2][0] = [temp[0], temp[1], temp[2]]
        # 오른쪽면
        elif side == 'R':
            change(5)
            temp = [cube[0][0][2],cube[0][1][2],cube[0][2][2]]
            cube[0][0][2],cube[0][1][2],cube[0][2][2] = [cube[2][0][2],cube[2][1][2],cube[2][2][2]]
            cube[2][0][2],cube[2][1][2],cube[2][2][2] = [cube[1][0][2],cube[1][1][2],cube[1][2][2]]
            cube[1][0][2],cube[1][1][2],cube[1][2][2] = [cube[3][2][0],cube[3][1][0],cube[3][0][0]]
            cube[3][2][0],cube[3][1][0],cube[3][0][0] = [temp[0], temp[1], temp[2]]
        # 뒷면
        elif side == 'B':
            change(3)
            temp = cube[0][0]
            cube[0][0] = [cube[5][0][2],cube[5][1][2],cube[5][2][2]]
            cube[5][0][2],cube[5][1][2],cube[5][2][2] = [cube[1][2][2],cube[1][2][1],cube[1][2][0]]
            cube[1][2][2],cube[1][2][1],cube[1][2][0] = [cube[4][2][0],cube[4][1][0],cube[4][0][0]]
            cube[4][2][0],cube[4][1][0],cube[4][0][0] = [temp[0], temp[1], temp[2]]
        # 왼쪽면
        elif side == 'L':
            change(4)
            temp = [cube[0][0][0],cube[0][1][0],cube[0][2][0]]
            cube[0][2][0],cube[0][1][0],cube[0][0][0] = [cube[3][0][2],cube[3][1][2],cube[3][2][2]] # 반전
            cube[3][0][2],cube[3][1][2],cube[3][2][2] = [cube[1][2][0],cube[1][1][0],cube[1][0][0]] # 반전
            cube[1][0][0],cube[1][1][0],cube[1][2][0] = [cube[2][0][0],cube[2][1][0],cube[2][2][0]]
            cube[2][0][0],cube[2][1][0],cube[2][2][0] = [temp[0], temp[1], temp[2]] #반전
        # 아랫면
        elif side == 'D':
            change(1)
            temp = cube[2][2]
            cube[2][2] = cube[4][2]
            cube[4][2] = cube[3][2]
            cube[3][2] = cube[5][2]
            cube[5][2] = temp
    # - 방향으로 1번 돌리는 것은 +방향으로 3번 돌리는 것과 동일하다.
    elif direction == '-':
        for _ in range(3) :
            turn(side,'+')


# 큐브를 돌리면 돌아가는 면도 돌아간다
"""
123    741
456 -> 852
789    963
"""
def change(i):
    global cube

    tmp = cube[i][0][0]
    cube[i][0][0] = cube[i][2][0]
    cube[i][2][0] = cube[i][2][2]
    cube[i][2][2] = cube[i][0][2]
    cube[i][0][2] = tmp

    tmp = cube[i][0][1]
    cube[i][0][1] = cube[i][1][0]
    cube[i][1][0] = cube[i][2][1]
    cube[i][2][1] = cube[i][1][2]
    cube[i][1][2] = tmp


n = int(input())
for _ in range(n) :
    tc = int(input())
    # 다 맞춰진 큐브 3차원 배열 생성
    cube = [[] for _ in range(6)]
    for _ in range(3) :
        # 윗면
        cube[0].append(['w','w','w'])
        # 아랫면
        cube[1].append(['y','y','y'])
        # 앞면
        cube[2].append(['r','r','r'])
        # 뒷면
        cube[3].append(['o','o','o'])
        # 왼쪽면
        cube[4].append(['g','g','g'])
        # 오른쪽 면
        cube[5].append(['b','b','b'])

    tests = list(map(str, input().rstrip().split()))
    # 입력 받은 값을 돌린다.
    for test in tests :
        # 돌리는 면, 돌리는 방향
        turn(test[0], test[1])

    for i in range(3) :
        print("".join(cube[0][i]))