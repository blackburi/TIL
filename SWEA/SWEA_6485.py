# 삼성시의 버스 노선

T = int(input())

for tc in range(1, T+1) :
    dic = {} # {정류장 번호 : 지나는 노선의 개수}
    
    for i in range(1, 5001) :
        dic[i] = 0

    N = int(input())
    for _ in range(1, N+1) :
        a, b = list(map(int, input().split()))
        for j in range(a, b+1) :
            dic[j] += 1
    
    P = int(input())
    
    num_list = []
    for _ in range(P) :
        k = int(input())
        num_list.append(str(dic[k]))

    
    print(f'#{tc} {" ".join(num_list)}')