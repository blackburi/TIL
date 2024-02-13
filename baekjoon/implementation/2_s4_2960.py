# 에라토스테네스의 체

N, K = list(map(int, input().split()))

# 2부터 N까지 list 생성
del_lst = [i for i in range(2, N+1)]

# cut func 정의 (list, K를 인자로 받음)
def cut(lst, num) : 
    p = lst[0] # lst의 0번을 소수로 지정
    for q in lst:
        # 소수 p의 배수를 지우기
        if q % p == 0 :
            # pop으로 q를 지우고 ans로 q를 받음
            ans = lst.pop(lst.index(q))
            num -= 1
            if num == 0 :
                return  lst, ans, num
    return lst, ans, num
    
# K=0 이 될때까지 돌림
while K > 0 :
    del_lst, answer, K = cut(del_lst, K)

print(answer)