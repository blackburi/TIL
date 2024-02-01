n, k= map(int, input().split()) # 전체 인원수 , 한방에 배정가능한 최대 인원수

# s, y = 성별과 학년 * n

dic = {}
for i in [0, 1] :
    for j in range(1, 7) :
        dic[(i, j)] = 0

for _ in range(n) :
    s, y = list(map(int, input().split()))
    dic[(s, y)] += 1

value = list(dic.values())

room = 0

for i in value :
    if i % k == 0 :
        room += i//k
    else :
        room += i//k + 1

print(room)