import sys
input = sys.stdin.readline


for _ in range(4) :
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    if x2 < x3 or x4 < x1 or y1 > y4 or y2 < y3 :
        print('d')
    elif x1 == x4 or x3 == x2 :
        if y2 == y3 or y4 == y1 :
            print('c')
        else :
            print('b')
    elif y2 == y3 or y4 == y1 :
        print('b')
    else :
        print('a')