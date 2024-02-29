# 백만장자 프로젝트

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    price = list(map(int, input().split()))

    ans = 0
    stack = []

    stack.append(price.pop())

    while price :
        a = price.pop()
        if a <= stack[-1] :
            ans += stack[-1] - a
        else : # a > stack[-1]
            stack.pop()
            stack.append(a)
    
    print(f'#{tc} {ans}')