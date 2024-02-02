n = int(input())

length = []


for _ in range(6) :
    a, b = map(int, input().split())
    length.append(b)


k = max(length)

p = length.index(k)

if length[(p+1)%6] > length[(p+5)%6] :
    area = length[p] * length[(p+1)%6] - length[(p+3)%6] *length[(p+4)%6]
else : #length[(p+1)%6] < length[(p+5)%6] 같을수는 없음
    area = length[p] * length[(p+5)%6] - length[(p+3)%6] *length[(p+2)%6]

print(area * n)