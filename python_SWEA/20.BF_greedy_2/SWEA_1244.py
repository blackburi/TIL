# 최대 상금

T = int(input())

for tc in range(1, T+1) :
    number, k = map(int, input().split())
    lst = list(str(number))
    for i in range(len(lst)) :
        lst[i] = int(lst[i])

    # 숫자가 모두 다를 경우
    if len(set(lst)) == len(lst) :
        sub = sorted(lst)
        sub.reverse()
        while k :
            for i in range(len(lst)) :
                if lst[i] != sub[i] :
                    a = lst.index(sub[i])
                    lst[i], lst[a] = lst[a], lst[i]
                    k -= 1
                
                if k == 0 :
                    break

                if lst == sub:
                    break
            if lst == sub :
                break
        
        while k :
            lst[-1], lst[-2] = lst[-2], lst[-1]
            k -= 1
        
        print(f'#{tc}', ' ', *lst, sep='')
    
    # 숫자가 같은것이 있는 경우
    else :
        sub = sorted(lst)
        sub.reverse()
        if k >= len(lst) :
            print(f'#{tc}', ' ', *sub, sep='')
        else : # k < len(lst)
            while k :
                # 똑같은 숫자가 몇개 있는지 담는 변수
                tmp = 1
                for i in range(len(lst)) :
                    if lst[i] != sub[i] :
                        a = lst[-1:i:-1].index(sub[i])
                        lst[i], lst[-(a+1)] = lst[-(a+1)], lst[i]
                        k -= 1
                    
                    if i >= 1 and lst[i] == lst[i-1] :
                        tmp += 1
                        if i == 1 :
                            rev = lst[-i-tmp:]
                            rev.sort(reverse = True)
                            lst[-i-tmp:] = rev
                        else :
                            rev = lst[-i-tmp:-i+1]
                            rev.sort(reverse = True)
                            lst[-i-tmp:-i+1] = rev
                    else :
                        tmp = 1

                    # 똑같은 숫자가 있는 경우 k가 남아도 같은 숫자끼리 자리를 바꾸면 된다.
                    if lst == sub :
                        break

                    if k == 0 :
                        break
                
                if lst == sub :
                    break

            print(f'#{tc}', ' ', *lst, sep='')
