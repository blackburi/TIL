# SWEA 2072
# 홀수만 구하기

# [제약 사항]
# 각 수는 0 이상 10000 이하의 정수이다
# [입력]
# 가장 첫 줄에는 test case의 개수 t가 주어지고, 그 아래로 각 test case가 주어진다.
# 각 test case의 첫 번째 줄에는 10개의 수가 주어진다.
# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다. 
# (t는 test case의 번호를 의미하며 1부터 시작한다.)

# 입력값
# 3 
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1

# 출력값
# #1 200
# #2 208
# #3 121

t = int(input())

for i in range(1, t + 1):
    sum = 0
    data = list(input().split())
    for j in range(len(data)):
        if int(data[j]) % 2 == 1:
            sum += int(data[j])
        else:
            pass
    print('#' + str(i), sum)