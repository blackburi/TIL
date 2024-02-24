# 보물상자 비밀번호
dic = {'0' : 0,
       '1' : 1,
       '2' : 2,
       '3' : 3,
       '4' : 4,
       '5' : 5,
       '6' : 6,
       '7' : 7,
       '8' : 8,
       '9' : 9,
       'A' : 10,
       'B' : 11,
       'C' : 12,
       'D' : 13,
       'E' : 14,
       'F' : 15
       }

T = int(input())

for tc in range(1, T+1) :
    n, k = map(int, input().split())
    lst = list(input())

    num = []
    for i in range(n) :
        hap = 0
        for j in range(n//4) :
            hap += dic[lst[(i+j)%n]]*(16**(n//4-j-1))
        num.append(hap)
    num = list(set(num))
    num.sort()
    num.reverse()
    print(f'#{tc} {num[k-1]}')