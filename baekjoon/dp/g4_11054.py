import sys
input = sys.stdin.readline

n = int(input())
# 증가하는 부분을 세는 경우
lst = list(map(int, input().split()))
# 감소하는 부분을 세는 경우
lst_reverse = lst[::-1]

increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]

for i in range(n) :
    for j in range(i) :
        if lst[i] > lst[j] :
            increase[i] = max(increase[i], increase[j]+1)
        if lst_reverse[i] > lst_reverse[j] :
            decrease[i] = max(decrease[i], decrease[j]+1)

ans = [0] * n
for k in range(n) :
    # lst에서 가장 큰 수는 두번 측정이 되기 때문에 한번 빼준다.
    ans[k] = increase[k] + decrease[n-k-1] - 1

print(max(ans))