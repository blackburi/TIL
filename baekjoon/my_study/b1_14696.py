# ★ ● ■ ▲ 무승부

n = int(input())

# A : 그림의 총 개수, 그림
# B : 그림의 총 개수, 그림

def AB(A, B, str) :
    if A.count(str) > B.count(str) :
        return 'A'
    elif A.count(str) < B.count(str) :
        return 'B'
    return 'D'

for _ in range(n) :
    A = input().split()
    B = input().split()
    A.pop(0)
    B.pop(0)

    S = AB(A, B, '4')
    if S == 'D' :
        S = AB(A, B, '3')

        if S == 'D' :
            S = AB(A, B, '2')

            if S == 'D' :
                S = AB(A, B, '1')
                print(S)
            else :
                print(S)
        else :
            print(S)
    else :
        print(S)