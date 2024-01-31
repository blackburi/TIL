import sys
input = sys.stdin.readline

n = int(input())
nge= list(map(int, input().split()))

# '-1'로 출력되는 자리를 신경쓰지 않기 위해서
ans = [-1] * n

stack = []
stack_index = []

for i in range(n) :
    while len(stack) > 0 and stack[-1] < nge[i] :
        a = stack.pop()
        b = stack_index.pop()
        ans[b] = nge[i]
    stack.append(nge[i])
    stack_index.append(i)

print(*ans)