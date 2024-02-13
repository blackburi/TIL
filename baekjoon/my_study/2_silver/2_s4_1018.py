N, M = list(map(int, input().split()))

area = [[*input()] for _ in range(N)]
result = []

for i in range(N-7) :
    for j in range(M-7) :
        num1 = 0
        num2 = 0

        for a in range(i, i+8) :
            for b in range(j, j+8) :
                if (a+b) % 2 == 0 :
                    if area[a][b] != 'B' :
                        num1 += 1
                    if area[a][b] != 'W' :
                        num2 += 1
                else :
                    if area[a][b] != 'W' :
                        num1 += 1
                    if area[a][b] != 'B' :
                        num2 += 1
        result.append(num1)
        result.append(num2)

print(min(result))