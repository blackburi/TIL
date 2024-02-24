T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())

    # 암호가 들어있는 줄만 추출, 겹치는 부분 삭제
    code = []
    for i in range(n) :
        sub = list(map(str, input()))
        if (sub != ['0'] * m) and (sub not in code) :
            code.append(sub)
    
    for i in code :
        i.reverse()

    