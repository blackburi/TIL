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

    # dp[i]가 []이 아니면 염기서열을 1개로 합칠수 있다
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

# 4자리 기준 1111이 된다면 다 셀수 있는것
# dp를 이용한 memoization 재귀
def count_dna(idx) :
    # 초기값을 n+1로 설정 -> n이면 이미 계산된 것
    if numbers[idx] <= n :
        return numbers[idx]

    # a, b를 나누는 이유
    # 만약 dp[a+b]가 하나로 합쳐질수있다면 1
    # dp[a+b] = []가 되어 합칠수 없다면
    # dp[a]와 dp[b]를 통해 최소 개수를 구한다.
    # a+b = idx가 항상 성립해야한다.
    a = 0
    b = 0
    # idx보존을 위해 변수 설정
    tmp_idx = idx
    # 1의 개수를 세는 변수
    tmp = 0
    # 1의 위치에 해당하는 수(10 -> 두번째 1이므로 1이 tmp_lst에 들어간다.)
    # 이때 tmp_lst에 들어가는 것은 python 상에서의 index를 따른다.
    tmp_lst = []
    for i in range(n) :
        if tmp_idx % 2 == 1 :
            a += 2**i
            tmp_lst.append(i)
            tmp += 1
        tmp_idx //= 2

    comparison = [0] * tmp

    # a+b = index가 되는 모든 경우를 탐색후 필요한 염기서열의 갯수 최적화
    # 가능한 이유는 a+= 2**i로 더했기 때문에 2의 거듭제곱으로 더해지는 수는 유일
    # a와 b는 순서가 필요 없고 대칭 가능 -> 지수에 tmp-1을 통해 경우의수를 절반으로 줄여준다.
    for i in range(1, 2**(tmp-1)) :
        for j in range(tmp) :
            # comparison에 1이 없다면 아직 옮긴 수가 없음
            # 또는 더이상 옮길수가 없는 경우
            if comparison[j] == 0 :
                comparison[j] = 1
                a -= 2**tmp_lst[j]
                b += 2**tmp_lst[j]
                break
            # comparison에 1이 있으면 해당하는 수를 a->b로 이동
            # 계속 옮길수 있다면 계속 옮긴다
            else : # comparison[j] == 1
                comparison[j] = 0
                a += 2**tmp_lst[j]
                b -= 2**tmp_lst[j]
        # numbers에서 겹칠수 있는 염기서열을 최대로 만들어
        # 좋은 염기서열의 수를 최소화 한다.
        numbers[idx] = min(numbers[idx], count_dna(a)+count_dna(b))
    return numbers[idx]

for i in range(1, 2**n) :
    memoi(i)

print(numbers[-1])