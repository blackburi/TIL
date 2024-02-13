num = []

for _ in range(5) :
    num.append(int(input()))

num.sort()

sum = 0
for i  in num :
    sum += i

print(sum//5)
print(num[2])