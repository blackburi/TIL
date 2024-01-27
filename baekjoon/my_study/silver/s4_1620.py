import sys
input = sys.stdin.readline

n, m =  map(int, input().split())

monster = {}

for i in range(n) :
    x = input().rstrip()
    monster[x] = i
    monster[i] = x


for j in range(m) :
    k = input().rstrip()
    try :
        l = int(k)
        print(monster[l-1])
    except :
        print(monster[k] + 1)