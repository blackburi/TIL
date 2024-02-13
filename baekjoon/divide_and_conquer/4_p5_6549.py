import sys
input = sys.stdin.readline

while True :
    # 처음 나오는 수는 막대의 개수이므로 n으로 따로 받아준다.
    n, *lst = list(map(int, input().split()))

    if n == 0 :
        break

    stick = [0] + lst + [0]
    # 0을 넣는 이유는 처음 돌릴때 stack에 아무것도 없으면 안돌아가는 것을 방지
    stack = [0]
    area = 0 # 최대 면적

    for i in range(1, n+2) :
        while stack and stick[stack[[-1]]] > stick[-1] :
            