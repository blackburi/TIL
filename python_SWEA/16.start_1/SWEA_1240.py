dic = {1011000:0,
       1001100:1,
       1100100:2,
       1011110:3,
       1100010:4,
       1000110:5,
       1111010:6,
       1101110:7,
       1110110:8,
       1101000:9
       }

T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())
    mat = [list(map(str, input())) for _ in range(n)]

    # 암호코드가 있는 첫줄을 만나면 break
    for i in range(n) :
        if mat[i] != ['0'] * m :
            lst = mat[i]
            break
    
    # 암호 숫자들의 코드를 뒤집으면 항상 1로 시작 -> 뒤집어서 생각
    lst.reverse()

    # 1을 만나면 break
    for j in range(m) :
        if lst[j] == '1' :
            b = j
            break
    
    # 1을 만난 시점부터 56개를 따로 자름
    ans = []
    lst = lst[b:b+56]
    # 8개씩 잘라서 dic에서 올바른 숫자로 변환
    for i in range(8) :
        sub = int(''.join(lst[7*i:(7*i+7)]))
        ans.append(dic[sub])

    tmp = 0 # 올바른 암호인지 판단
    hap = 0 # 올바른 암호라면 정답 미리 계산
    for i in range(8) :
        if i % 2 == 0 :
            tmp += ans[i] * 3
        else :
            tmp -= ans[i]
        hap += ans[i]
    
    if tmp % 10 == 0 :
        print(f'#{tc} {hap}')
    else : # tmp % 10 != 0
        print(f'#{tc} 0')