import sys
input = sys.stdin.readline

while True :
    # 처음 나오는 수는 막대의 개수이므로 n으로 따로 받아준다.
    n, *lst = list(map(int, input().split()))

    if n == 0 :
        break

    stick = [0] + lst + [0]
    # 0을 넣는 이유는 처음 돌릴때 stack에 아무것도 없으면 안돌아가는 것을 방지
    stack = [0] # 항상 오름차순으로 정렬 되도록 
    area = 0 # 최대 면적

    for i in range(1, n+2) :
        # stack에 존재하고
        while stack and stick[stack[-1]] > stick[i] :
            # 현재 높이를 설정할 index
            current = stack.pop()
            area = max(area, (i-1-stack[-1])*stick[current])
        # 모든 높이에 대한 index를 stack에 넣어준다.
        stack.append(i)
    
    print(area)

# while문 설명 (while문 마지막에 i가 항상 stack으로 들어간다.)
# stack이 차 있고 높이가 감소하고 있다면
# stack.pop()
    # 예를 들어 높이가 0 5 4 3 0 이라면
    # 4는 5보다 작기 때문에 5에 대한 index가 stack에서 pop
    # 3은 4보다 작기 때문에 4에 대한 index가 stack에서 pop
    # 그래야 증가했던 구간을 시작으로 감소하는 부분까지
        # (0~5)가 증가하는 부분이므로 stack에는 0(index)만 남아있다
        # 4, 3에 대한 index는 pop이 됨
        # 높이가 낮아지면 현재 높이에 낮아지는 총 구간을 곱하여 사각형을 만들 수 있다.
        # i==4 일때 current는 i=3에 해당되기 때문에 i-stack[-1]에다가 1을 추가로 빼준다.
        # 이것을 stick[current]로 높이 설정을 해준다.
        # 이것을 이전 최대 면적인 area와 비교
# stack이 비어 있거나 높이가 증가하면 (언제 사각형이 만들어질지 모르기 때문에-높이가 고정이 안되서)
# 계속 stack에 append(i)를 한다.