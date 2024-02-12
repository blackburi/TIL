import sys
input = sys.stdin.readline

l, h = map(int, input().split())
n = int(input())

shop = []
for _ in range(n) :
    a, b = map(int, input().split())
    if a == 1 :
        shop.append([b, h])
    elif a == 2 :
        shop.append([b, 0])
    elif a == 3 :
        shop.append([0, h-b])
    elif a == 4 :
        shop.append([l, h-b])

p, q = map(int, input().split())

def dis_close(a, b, c, d) : # dong = [a, b], shop[i] = [c, d]
    return abs(a-c) + abs(b-d)

def dis_far(a, b, c, d) : # dong = [a, b], shop[i] = [c, d]
    global l, h
    if a == 0 or a == l :
        k = min(b, d, h-b, h-d)
        return l + 2*k + abs(b-d)
    elif b == 0 or b == h :
        k = min(a, c, l-a, l-c)
        return h + 2*k + abs(a-c)

dis = 0

if p == 1 :
    dong = [q, h]
    for i in range(n) :
        if shop[i][1] != 0 :
            dis += dis_close(q, h, shop[i][0], shop[i][1])
        else : # shop[i][1] == 0
            dis += dis_far(q, h, shop[i][0], shop[i][1])
elif p == 2 :
    dong = [q, 0]
    for i in range(n) :
        if shop[i][1] != h :
            dis += dis_close(q, 0, shop[i][0], shop[i][1])
        else : # shop[i][1] == h
            dis += dis_far(q, 0, shop[i][0], shop[i][1])
elif p == 3 :
    dong = [0, l-q]
    for i in range(n) :
        if shop[i][0] != l :
            dis += dis_close(0, l-q, shop[i][0], shop[i][1])
        else : # shop[i][0] == l
            dis += dis_far(0, l-q, shop[i][0], shop[i][1])
elif p == 4 :
    dong = [l, h-q]
    for i in range(n) :
        if shop[i][0] != 0 :
            dis += dis_close(l, h-q, shop[i][0], shop[i][1])
        else : # shop[i][0] == 0
            dis += dis_far(l, h-q, shop[i][0], shop[i][1])

print(dis)