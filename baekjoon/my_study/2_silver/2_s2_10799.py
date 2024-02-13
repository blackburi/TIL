lst = list(input())

a = 0 # 막대의 개수
cnt = 0 # 총 막대의 개수

for i in range(len(lst)) :
    if lst[i] == '(' :
        if lst[i+1] == ')' : # 레이저가 있는경우
            cnt += a
        else : # lst[i+1] == '(' 라면 lst[i] == '(' 는 막대를 나타낸다.
            a += 1
    else : # lst[i] == ')'
        if lst[i-1] == '(' : # 레이저에 해당하는 괄호
            pass
        else : # lst[i-1] == ')' 막대에 해당하는 괄호
            a -= 1
            cnt += 1

print(cnt)