dum = input()
ans = []
stack = []

for i in dum :
    if i.isalpha() :
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