# 업무 처리

import sys
input = sys.stdin.readline

# 조직의 높이, 업무의 개수, 진행되는 날짜
h, k, r = map(int, input().split())

# 말단 직원들의 업무 번호
tasks = [list(map(int, input().rstrip().split())) for _ in range(2**h)]

# 말단직원의 number
workers = [i for i in range(2**h)]

# 업무가 완료되는 말단 직원의 number -> 말단직원부터 업무가 완료되는 것을 check하는 3중 list
# "[업무가 완료되는 말단직원] * 말단직원부터 최종완료를 찍어주는 직원까지의 수"를 list로 담음
end = [[[] for _ in range(2**i)] for i in range(h+1)]

end[0][0] = workers

# i : 첫 task가 마무리 되는 시점에서 높이가 짝수면 오른쪽 task를 먼저 마무리 한다.
for i in range(h) :
    for j in range(2**i) :
        tmp = end[i][j]
        # 날짜가 짝수라면 오른쪽 task를 완료
        if i % 2 == 0 :
            # 동시에 두가지 일이 올라왔을때 k가 짝수라면 왼쪽 일을 먼져 가져온다.
            if k % 2 == 0 :
                end[i+1][2*j+1].append(tmp[k])
            else : # k % 2 == 1
                end[i+1][2*j].append(tmp[k])
        # 날짜가 홀수라면 왼쪽 task를완료
        else : # i % 2 == 1
            # 동시에 두가지 일이 올라왔을때 k가 짝수라면 오른쪽 일을 먼져 가져온다.
            if k % 2 == 0 :
                end[i+1][2*j].append(tmp[k])
            else : # k % 2 == 1
                end[i+1][2*j+1].append(tmp[k])