# 염기서열 커버

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
dna = []
for _ in range(n) :
    dna.append(list(input().rstrip()))

# dna를 2의 거듭제곱 자리에 배치를 하고
# 모든 정수는 2의 거듭제곱의 합으로 유일하게 표현 가능하다
# 3 = 1 + 2
# 단 dp[0]은 의미가 없는 자리이다.
# 항상 가능하도록 만들어준다.
# dp를 쓰는 이유는 중복된 계산을 피하기 위해서
# 앞에서 1110을 combine function에 넣기 위해서는
# 1000, 0100, 0010 세개의 수를 넣어야 하는데
# dp를 이용하여 이전에 1000, 0100을 계산하였다면 1100과 0010만 계산한다.
dp = [0] * (2**n)
# dp[0]은 실제로 필요없는 값 -> 항등원으로 만들어준다.
dp[0] = ['.'] * m

# 염기서열 개수의 최솟값을 저장하는 list
# 최댓값은 모든 염기를 합칠수 없는 경우 n개일 때 이다 -> 초기값 n+1으로 설정
numbers = [n+1] * (2**n)
# index = 0 인 경우 항등원 0을 설정
numbers[0] = 0

# 기존에 계산이 되어 있는 수를이용하기 위해
# 2진수 기준 제일 오른쪽에 있는 1을 찾는다
# 1110 이라면 오른쪽에서 두번째 1을 찾는 것
def memoi(idx) :
    position = 0
    tmp = idx
    while tmp % 2 == 0 :
        tmp //= 2
        position += 1
    dp[idx] = combine(dna[position], dp[idx - 2**position])

    # dp[i]가 0이 아니면 염기서열을 1개로 합칠수 있다
    if dp[idx] != [] :
        numbers[i] = 1
    else :
        count_dna(i)

# 염기서열 2개를 합칠수 있다면 합친 것을, 아니라면 빈 list를 return
def combine(dna1, dna2) :
    dna = []
    if dna1 == [] or dna2 == [] :
        return dna
    
    for i in range(m) :
        if dna1[i] == '.' :
            dna.append(dna2[i])
        elif dna2[i] == '.' :
            dna.append(dna1[i])
        elif dna1[i] == dna2[i] :
            dna.append(dna1[i])
        else :
            dna = []
            return dna
    return dna

def count_dna(idx) :
    # 초기값을 n+1로 설정 -> n이면 이미 계산된 것
    if numbers[idx] <= n :
        return numbers[idx]
    
    a = 0
    b = 0
    # 1의 위치를 찾아내는 변수
    tmp_idx = idx
    # 1의 개수를 세는 변수
    tmp = 0
    for i in range(n) :
        if tmp_idx % 2 == 1 :
            b += 2**i
            tmp += 10
        tmp_idx //= 2

for i in range(1, 2**n) :
    memoi(i)