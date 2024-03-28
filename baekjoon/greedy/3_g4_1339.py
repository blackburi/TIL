# 단어 수학

# 문자에 숫자를 할당하여 더할 필요 없다
# "문자에 숫자 대입 -> 문자의 위치에 그 숫자를 대입 -> 계산" 의 과정이 아닌
# "문자의 위치에 해당하는 자릿수에 숫자 대입 -> 계산"
# 각 문자에 해당하는 숫자를 알고 값만 계산해도 된다.

import sys
input = sys.stdin.readline

n = int(input())
lst = [list(input().rstrip()) for _ in range(n)]

# 알파벳을 자리값을 가져와 더하는 dictionary
# ABC, CAB 두개를 더한다면
# dic = {'A' : 100+10, 'B' : 10+1, 'C' : 100+1}
# 이때 'A'=9를 넣는 것이 아닌
# 9*110('A') + 8*101('C') + 7*11('B')로 계산
dic = {}

for sub in lst :
    tmp = 0
    for _ in range(len(sub)) :
        k = sub.pop()
        if k in dic :
            dic[k] += 10**tmp
        else : # k not in dic
            dic[k] = 10**tmp
        tmp += 1

# 문자에 숫자를
numbers = sorted(dic.values())
numbers.reverse()

# 계산한 결과값
total = 0

num = 9
for i in range(len(numbers)) :
    total += numbers[i]*num
    num -= 1

print(total)