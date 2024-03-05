# K번째 수

# 모든 숫자는 본인의 약수의 개수만큼 나온다

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

for i in range(n) :
    if k == i**2 :
        print(i**2)
        break
    elif k > i**2 :
        continue
    else : # k < i**2
        
















#################################################################
# 메모리 초과 => n <= (10**5) 이기 때문에
#################################################################
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

B = []

for i in range(n) :
    for j in range(n) :
        B.append((i+1)*(j+1))

B.sort()
print(B[k])