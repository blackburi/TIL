# solution 1 - 점화식으로 풀기
T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    n //= 10

    def fibo(k) :
        if k == 1 :
            return 1
        elif k == 2 :
            return 3
        else : # k >= 3
            return fibo(k-1) + 2 * fibo(k-2)
    
    print(f'#{tc} {fibo(n)}')

# solution 2 - 점화식을 방정식으로 바꿔 풀기
T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    print(f'#{tc} {(2**(n//10+1) + (-1)**(n//10))//3}')