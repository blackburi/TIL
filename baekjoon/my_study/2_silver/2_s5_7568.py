import sys
input = sys.stdin.readline

person = int(input())

# [무게, 키] 정렬
body = []
for _ in range(person) :
    a, b = map(int, input().split())
    body.append([a, b])

rate = [1] * person
for i in range(person) :
    for j in range(person) :
        if body[i][0] < body[j][0] and body[i][1] < body[j][1] :
            rate[i] += 1

print(*rate)