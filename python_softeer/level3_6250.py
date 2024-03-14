#  성적 평가

import sys
input = sys.stdin.readline

# 참가자수
n = int(input())

# 전체 점수를 등록해둘 list
all = [0] * n

# 어차피 대회3개에 대한 결과값은 하나의 함수로 표현 가능
# -> 함수를 만들수 있다면 함수로 한번에 3개의 대회에 대한 출력값을 뽑을 수 있다.
def result(lst) :
    # 등수를 담을 list
    ans = [0] * n

    for i in range(n) :
        lst[i] = (i, lst[i])
    
    # 점수가 높은 순서대로, 사람 번호가 낮은 순서대로
    lst.sort(key = lambda x : (-x[1], x[0]))

    for i in range(n) :
        idx, score = lst[i]

        if idx == 0 or i == 0 :
            ans[idx] = i+1
        else :
            if score == last_score :
                ans[idx] = ans[last_idx]
            else :
                ans[idx] = i+1
        
        last_score = score
        last_idx = idx

    print(*ans)


for _ in range(3) :
    score_list = list(map(int, input().rstrip().split()))

    for i in range(n) :
        all[i] += score_list[i]

    result(score_list)

result(all)