# 잃어버린 괄호

equation = input().split('-')

result = 0

for i in range(len(equation)) :
    if i == 0 :
        x = equation[i].split('+')
        for k in x :
            result += int(k)
    else :
        x = equation[i].split('+')
        for j in x :
            result -= int(j)

print(result)