# 산 모양 타일링

# 점화식으로 풀어야 함 -> 점화식, dp
# top이 있는 경우와 없는 경우로 나눈다면 매번 top이 있는 경우와 없는 경우 계산이 바뀜
# 계산이 바뀌지 않고 동일한 점화식을 적용할 방법이 필요
# 역삼각형과 역삼각형의 오른쪽에 삼각형을 붙인 마름모를 사용하는지의 여부로 판단
# 가장 오른쪽 타일을 마름모에 포함하는지 안하는지의 경우와 동일하기 때문
# *****
#  *   *
#   ***** 이 모양의 타일을 기준으로 생각

def solution(n, tops) :
    # 사용하는 경우
    use = [0] * (n+1)
    # 사용하지 않은 경우
    disuse = [0] * (n+1)

    use[0] = 0
    disuse[0] = 1

    for k in range(1, n+1) :
        # k번째 top이 있는 경우(index상으론 k-1)
        if tops[k-1] == 1 :
            use[k] = (use[k-1] + disuse[k-1]) % 10007
            disuse[k] = (2*use[k-1] + 3*disuse[k-1]) % 10007
        # k번째 top이 없는 경우(index상으론 k-1)
        else : # tops[k-1] == 0
            use[k] = (use[k-1] + disuse[k-1]) % 10007
            disuse[k] = (use[k-1] + 2*disuse[k-1]) % 10007

    return (use[n] + disuse[n]) % 10007