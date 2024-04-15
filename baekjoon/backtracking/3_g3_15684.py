# 사다리 조작


# i번째가 i번째에 도착하는지 확인하는 함수
def check() :
    for i in range(n) :
        start = i
        for j in range(h) :
            if sadari[j][start] == 'R' :
                start += 1
            elif sadari[j][start] == 'L' :
                start -= 1
        if start != i :
            return False
    return True

"""
x값만 넣고 y값을 넣지 않는 이유
-> 위에서 아래로 내려가면서 탐색
-> 위로 다시 올라가서 탐색할 필요 없음
-> 이전에 탐색완료
y값의 경우에는 정렬이 불가능
"""

def make(cnt, x) :
    global ans

    # 이전 나온 ans보다 크거나 같으면 stop
    if cnt >= ans :
        return

    if check() :
        ans = min(ans, cnt)
        return

    # 사다리 설치는 최대 3개까지 되기 때문에
    if cnt == 4 :
        return

    # 가로줄 선택
    for i in range(x, h) :
        # 설치할 사다리 위치(세로선 1개 -> 자동적으로 2개 선택됨)
        for j in range(n-1) :
            if sadari[i][j] == 'N' and sadari[i][j+1] == 'N' :
                sadari[i][j] = 'R'
                sadari[i][j+1] = 'L'
                make(cnt+1, i)
                sadari[i][j] = 'N'
                sadari[i][j+1] = 'N'


import sys
input = sys.stdin.readline

# 세로선, 가로선, 세로선마다 가로선을 놓을 수 있는 위치의 개수
n, m, h = map(int, input().split())

sadari = [['N']*n for _ in range(h)]
# 사다리의 위치
for _ in range(m) :
    a, b = map(int, input().split())
    sadari[a-1][b-1] = 'R'
    sadari[a-1][b] = 'L'

# 필요한 사다리의 개수
ans = float('inf')
make(0, 0)
if ans > 3 :
    ans = -1
print(ans)