T = int(input())

for tc in range(1, T+1) :
    lst = list(input())

    # 2진수 숫자를 담을 list
    binary = []
    # 16진수 -> 2진수
    for i in lst :
        binary.extend(list(format(int(f'0x{i}', 16), 'b').zfill(4)))

    ans = []
    # 2진수 -> 10진수
    for i in range(len(binary)//7) :
        ans.append(str(int(''.join(binary[7*i:7*i+7]), 2)))
    # 7씩 자르고 남은 숫자들
    ans.append(str(int(''.join(binary[7*(len(binary)//7):]), 2)))
    
    print(f'#{tc} {" ".join(ans)}')