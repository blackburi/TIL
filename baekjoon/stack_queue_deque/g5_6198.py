import sys
input = sys.stdin.readline

# 아래 건물을 볼수 있는 윗건물을 세면 된다. (새로운 규칙)
# 5 3 1 4 2 의 경우
# 문제의 규칙 : 4 + 1 + 0 + 1 + 0 = 6
# 새로운 규칙 : 0 + 1 + 2 + 1 + 2 = 6

n = int(input())
ans = 0
stack = []
# stack에 들어가는 원소는 내림차순으로 등록이 되도록 만든다.
# stack에 원소가 들어갈때마다 len(stack)-1을 더해준다
    # 새로운 원소를 볼수 있는 건물의 수만큼 더해주는 것
# 오름차순이 생기면 (n, n+2 순서라면) n은 어차피 n+2 건물을 볼수 없다.
    # pop을 통해 n을 제거 후 n+2을 stack에 새로 넣어준다.
    # stack = [5, 3, 2], height = 4 => stack = [5, 4]

for _ in range(n) :
    height = int(input())
    if len(stack) == 0 : # 첫 건물은 stack에 넣는다.
        stack.append(height)
    else : # len(stack) != 0
        if stack[-1] > height : 
            stack.append(height)
            ans += len(stack) -1 
        else : # stack[-1] <= height
            while len(stack) > 0 and stack[-1] <= height :
                stack.pop()
            stack.append(height)
            ans += len(stack) - 1

print(ans)