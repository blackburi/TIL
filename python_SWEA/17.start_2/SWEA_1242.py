# 암호의 길이가 늘어나지 않았을때(56자리 일 때)
main_dic = {
    '1011000' : 0,
    '1001100' : 1,
    '1100100' : 2,
    '1011110' : 3,
    '1100010' : 4,
    '1000110' : 5,
    '1111010' : 6,
    '1101110' : 7,
    '1110110' : 8,
    '1101000' : 9
}

# 암호의 길이가 늘어났을 때(56의 배수 일 때)
sub_dic = {}

# 9까지만 하는 이유는 가로 길이의 최대가 500*4이기 때문에
# 암호의 길이는 최대 35배까지 늘어날 수 있기 때문이다.
# 2000/56=35.7... 이기 때문에
for i in range(2, 36) :
    for key in main_dic :
        increase = ''
        for one in key :
            increase += one * i
        sub_dic[increase] = main_dic[key]

T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())

    # 암호가 들어있는 줄만 추출, 겹치는 부분 삭제
    code = []
    for i in range(n) :
        sub = list(map(str, input()))
        if (sub != ['0'] * m) and (sub not in code) :
            code.append(sub)

    # 코드가 들어있는 부분을 2진수로 변환후 그 줄을 하나의 문자열로 생성
    for i in range(len(code)) :
        tmp = ''
        for j in range(len(code[i])) :
            tmp += format(int(code[i][j], 16), 'b').zfill(4)
        code[i] = tmp[::-1]

    # 코드를 확인하기 전 코드 8자리를 먼저 추출(중복되는 숫자를 없애기 위해서)
    # 코드 8개 숫자를 담을 이중 list
    check = []
    
    for i in code :
        # 코드의 시작점 체크
        j = 0
        while j < len(i) :
            if i[j] != '0' :
                # 코드(길이에 맞춰서)를 check에 넣어준다.
                for q in range(1, 36) :
                    if i[j:j+7*q] in main_dic or i[j:j+7*q] in sub_dic :
                        if i[j:j+7*q] not in check :
                            check.append(i[j:j+56*q])
                            break
                # j를 코드 길이만큼 뒤로 넘긴다.
                j += 56*q
            else :
                j += 1

    # check에 있는 암호들을 8자리 숫자들로 바꾸고 올바른 암호라면 합을 ans에 담아준다.
    ans = []
    for i in check :
        k = len(i)//56 # 7자리 암호코드가 늘어난 비율
        if k == 1 :
            lst = []
            for x in range(8) :
                lst.append(main_dic[i[7*x:7*x+7]])
            lst.reverse()
            if lst not in ans :
                ans.append(lst)
        else : # k >= 2
            lst = []
            for x in range(8) :
                lst.append(sub_dic[i[7*x*k:7*x*k+7*k]])
            lst.reverse()
            if lst not in ans :
                ans.append(lst)

    # ans에 있는 8자리 숫자들이 올바른 코드인지 확인한다
    number = []
    for i in ans :
        if ((i[0] + i[2] + i[4] + i[6])*3 + i[1] + i[3] + i[5] + i[7]) % 10 == 0 :
            hap = 0
            for r in range(8) :
                hap += i[r]
            number.append(hap)

    end = 0
    for i in number :
        end += i
    
    print(f'#{tc} {end}')