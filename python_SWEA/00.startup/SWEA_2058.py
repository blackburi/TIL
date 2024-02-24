# SWEA 2058
# 자릿수 더하기

# [제약 사항]
# 자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)
# [입력]
# 입력으로 자연수 N이 주어진다.
# [출력]
# 각 자릿수의 합을 출력한다.

# 입력값
# 6789

# 출력값
# 30

N = int(input())
number = list(map(int,str(N))) 
sum = 0
for i in number:
    sum += i
print(sum)