# 플레이페어 암호

import sys
input = sys.stdin.readline
from collections import deque

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

mat = []

message = deque(list(input().rstrip()))
password_key = list(input().rstrip())
check = set(password_key)

for i in check :
    if i in alpha :
        alpha.remove(i)

sub = []
for i in password_key :
    if i in check :
        sub.append(i)
        check -= {i}
    else :
        continue

    if len(sub) == 5 :
        mat.append(sub)
        sub = []

for i in alpha :
    if i not in check :
        sub.append(i)
    if len(sub) == 5 :
        mat.append(sub)
        sub = []

# letters는 두글자
def change(letter1, letter2) :
    for i in range(5) :
        for j in range(5) :
            if mat[i][j] == letter1 :
                x1 = i
                y1 = j
            if mat[i][j] == letter2 :
                x2 = i
                y2 = j
    
    # 두 글자가 같은 행에 존재한다면
    if x1 == x2 :
        ans.append(mat[x1][(y1+1)%5])
        ans.append(mat[x2][(y2+1)%5])
    # 두 글자가 같은 열에 존재한다면
    elif y1 == y2 :
        ans.append(mat[(x1+1)%5][y1])
        ans.append(mat[(x2+1)%5][y2])
    else : # if와 elif둘다 만족하지 않는다면
        ans.append(mat[x1][y2])
        ans.append(mat[x2][y1])

    return


ans = []
while message :
    if len(message) >= 2 :
        a = message.popleft()
        b = message.popleft()
    else : # len(message) == 1 :
        a = message.popleft()
        b = 'X'
    if a == b and a != 'X' :
        message.appendleft(b)
        change(a, 'X')
    elif a == b and a == 'X' :
        message.appendleft(b)
        change(a, 'Q')
    else :
        change(a, b)

print(''.join(ans))