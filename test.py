# ############################################################

# def f(i, k) :
#     global min_v
#     if i == k :
#         s = 0 # 선택한 원소의 합
#         for j in range(k) :
#             s += arr[j][p[j]] # j행에서 p[j]열을 고른 경우에서의 합
#         if min_v > s :
#             min_v = s
#     else :
#         for j in range(i, k) : 
#             p[i], p[j] = p[j], p[i] # p[i] <-> p[j]
#             f(i+1, k)
#             p[i], p[j] = p[j], p[i] # 교환전으로 복구

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# p = [i for i in range(n)]
# min_v = 100
# f(0, n)
# print(min_v)

a = (1, 2)
print(a[1])