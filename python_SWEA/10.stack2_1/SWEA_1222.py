T = 10

for tc in range(1, 11) :
    n = int(input())
    lst = list(input())
    stack = []

    for i in lst :
        if i != '+' :
            stack.append(int(i))
    
    ans = 0
    for j in stack :
        ans += j
    
    print(f'#{tc} {ans}')

# 후위 표기식
dum = input() # 중위 표기식으로 된 입력값
ans = [] # 후위표기식
stack = [] # 연산자를 넣을 stack

for i in dum :
    if i not in ['(', ')', '+', '-', '*', '/'] :
        ans.append(i)
    else :
        if i == '(' :
            stack.append(i)
        elif i == '*' or i == '/' :
            while len(stack) > 0 and (stack[-1] == '*' or stack[-1] == '/') :
                ans.append(stack.pop())
            stack.append(i)
        elif i == '+' or i == '-' :
            while len(stack) > 0 and stack[-1] != '(' :
                ans.append(stack.pop())
            stack.append(i)
        elif i == ')' :
            while len(stack) > 0 and stack[-1] != '(' :
                ans.append(stack.pop())
            stack.pop()

while len(stack) > 0 :
    ans.append(stack.pop())

print(''.join(ans))