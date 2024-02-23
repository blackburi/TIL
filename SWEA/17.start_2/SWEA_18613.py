decoding = {'101100' : 0,
            '110010' : 1,
            '110111' : 2,
            '100011' : 3,
            '110001' : 4,
            '111011' : 5,
            '110100' : 6,
            '101111' : 7,
            '100110' : 8,
            '111101' : 9
            }

T = int(input())

for tc in range(1, T+1) :
    s = list(input().strip())
    code = []
    for i in s :
        # 16진수를 10진수로 바꾸고 이것을 2진수로 바꾸면서 4자리를 맞춰준다.
        # 숫자 하나하나를 나누기 위해 list로 변환후 extend
        code.extend(list(format(int(f'0x{i}', 16), 'b').zfill(4)))
    
    # decoding과정에서 마지막 숫자가 1임을 이용하기 위해 뒤집어준다
    code.reverse()

    # 0이 아닌 index를 찾고 그 index를 기준으로 code를 필요한 부분만 잘라준다.
    for i in range(len(code)) :
        if code[i] != '0' :
            code = code[i : len(code)-i]
            break
    
    ans = []
    for i in range(len(code)//6) :
        # decoding하기 위해 필요한 길이만큼 잘라준다.
        ans.append(''.join(code[6*i:6*i+6]))
        # 길이에 해당되는 것을 decoding한다.
        ans[i] = str(decoding[ans[i]])
    
    # 처음에 뒤집어서 시작했기 때문에 다시 뒤집어준다.
    ans.reverse()

    print(f'#{tc} {" ".join(ans)}')