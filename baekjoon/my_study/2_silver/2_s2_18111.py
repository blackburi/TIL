import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
data = [0] * 257                            # 0 ~ 256까지 height
for _ in range(n):
    for i in map(int,input().split()):
        data[i]+=1
have = sum(i * data[i] for i in range(257)) # 땅에 있는 전체 블럭의 수
ans = (have*2,0) # (모든 블럭을 제거했을 때의 시간, 높이가 0)
need = 0
t = data[0] # 높이 0부터 현재 높이까지의 블럭 개수의 합
nm = n*m
for i in range(1,257):
    need += t # 필요한 블럭 수
    have -= nm-t # 남은 블럭 수
    t += data[i]
    if have + b - need < 0:
        break
    else:
        ans=min((have * 2 + need, -i),ans) # 왜 여기서 -i ????
print(ans[0],-ans[1])


# 시간초과 - pypy로 돌려야 시간초과 안남
######################################################
######################################################
import sys
input = sys.stdin.readline

n, m, b = list(map(int, input().split()))

ground = []
for _ in range(n) :
    ground.extend(list(map(int, input().split())))
height = 0
time = sys.maxsize


# stand : 최종적으로 만들 땅의 높이
for stand in range(max(ground)+1) :
    plus, minus = 0, 0

    for i in ground :
        if i > stand :
            plus += i - stand
        else : # i <= stand
            minus += stand - i
    if plus + b >= minus :
        if 2 * plus + minus <= time :
            time = 2 * plus + minus
            height = stand

print(time, height)
######################################################
######################################################