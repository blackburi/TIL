A = [_ for _ in range(1,13)] # 1부터 12까지 숫자의 리스트를 만들어준다.

lst = [] # 빈 리스트 생성

for i in range(1 << len(A)): # 비트연산자로 1*2^len(numbers)
    sub_lst = [] # 빈 부분집합 리스트
    for j in range(len(A)):
        if i & (1 << j):
            sub_lst.append(A[j])
    lst.append(sub_lst) # 부분집합을 만들어 빈 리스트에 부분집합을 넣어준다.

T = int(input())
for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    cnt = 0

    for s in lst:
        hap = 0
        for i in s :
            hap += i

        if len(s) == N and hap == K: # 리스트의 길이는 N, 리스트의 합은 K
            cnt += 1

    print(f'#{tc} {cnt}')
