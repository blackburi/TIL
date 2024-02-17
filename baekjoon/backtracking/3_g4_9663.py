###################################################################
# python 시간초과, pypy3 맞음 : 내풀이
###################################################################
import sys
input = sys.stdin.readline

n = int(input())
# i 번째 row에 queen이 있는지 확인
# lst[1] = 2 라면 [1][2]에 queen이 있다는 것
lst = [0] * n

# queen을 둘수 있는 방법을 count
cnt = 0

# queen이 존재하는지 확인
def exist(x) :
    for i in range(x) :
        # 같은 행에 있는지 대각선에 있는지 확인, 대각선은 2개 -> abs처리
        if lst[x] == lst[i] or abs(lst[x] - lst[i]) == abs(x-i) :
            return True
    return False

def dfs(x) :
    global cnt

    if x == n :
        cnt += 1
    else :
        for i in range(n) :
            # [x][i]에 queen을 둔다.
            lst[x] = i
            # 같은 행, 대각선에 queen이 없다면
            if not exist(x) :
                dfs(x+1)

dfs(0)
print(cnt)



###################################################################
# python 맞음, pypy3 맞음 : 다른사람 풀이
###################################################################
'''
전체 케이스는 col == n//2 를 중심으로 좌우대칭임

ex)
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0

0 0 1 0
1 0 0 0
0 0 0 1
0 1 0 0

때문에, col(x)가 n//2 까지만 가능한 케이스를 구한후
*2 해주면 전체 케이스에 대한 정답을 알 수 있음
또한 홀수의 경우에는 n//2 + 1 를 따로 구헤줘야함
홀수의 경우에는 상하 좌우대칭이 의미없으므로 *2 해주지 않음
'''
import sys
input = sys.stdin.readline

n = int(input())
check_row = [0 for _ in range(n)]
check_leftcross = [0 for _ in range(n*2)]
check_rightcross = [0 for _ in range(n*2)]
ret = 0

def backtracking(cur):
    if cur==n:
        global ret
        ret += 1
        return 0
    for i in range(n):
        if check_row[i] or check_leftcross[n+cur-i] or check_rightcross[cur+i]:
            continue
        else:
            check_row[i] = 1
            check_leftcross[n+cur-i] = 1
            check_rightcross[cur+i] = 1
            backtracking(cur+1)
            check_row[i] = 0
            check_leftcross[n+cur-i] = 0
            check_rightcross[cur+i] = 0


for i in range(n//2):
    check_row[i] = 1
    check_leftcross[n-i] = 1
    check_rightcross[i] = 1
    backtracking(1)
    check_row[i] = 0
    check_leftcross[n-i] = 0
    check_rightcross[i] = 0
ret = ret*2

if n%2: #홀수일경우
    i=n//2
    check_row[i] = 1
    check_leftcross[n-i] = 1
    check_rightcross[i] = 1
    backtracking(1)
    check_row[i] = 0
    check_leftcross[n-i] = 0
    check_rightcross[i] = 0

print(ret)