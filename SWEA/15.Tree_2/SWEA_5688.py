T = int(input())

for tc in range(1, T+1) :
    target = int(input())
    
    p = int(target**(1/3))

    if p**3 == target :
        print(f'#{tc} {p}')
    elif (p+1)**3 == target :
        print(f'#{tc} {p+1}')
    else :
        print(f'#{tc} -1')