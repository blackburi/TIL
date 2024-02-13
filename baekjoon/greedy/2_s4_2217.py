# 로프

N = int(input())

rope = []

for _ in range(N) :
    rope.append(int(input()))

rope.sort()
rope.reverse()

weight = 0

for i in range(N) :
    if rope[i] * (i+1) >= weight :
        weight = rope[i] * (i+1)
    else :
        continue

print(weight)