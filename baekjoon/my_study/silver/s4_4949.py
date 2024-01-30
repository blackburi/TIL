while True :
    S = list(map(str, input()))

    if S == ['.'] :
        break

    a = 0 # ] 의 개수 - [ 의 개수
    b = 0 # ) 의 개수 - ( 의 개수

    # 오른쪽부터 항상 a >= 0, b >= 0

    for _ in range(len(S)) :
        i = S.pop()

        if i == ']' :
            a += 1
        elif i == '[' :
            a -= 1
        elif i == ')' :
            b += 1
        elif i == '(' :
            b -= 1
        
        if a < 0 and b < 0 :
            print('no')
            break