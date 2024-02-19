'''
한 점을 고정시키고 구한다음에 *8을 하면 된다.
(8번 회전을 하면 원래 모양으로 돌아오기 때문에)
8번 회전하는 중에 같은 모양이 나와도 제외시키지 않고 count해야한다.
각각의 능력치 이름이 붙어있기 때문에 모양이 동일하더라도
능력치의 위치가 다르면 다르게 count되기 때문이다.

볼록 다각형의 특성을 살펴보면
원점과 연속한 세 점 P, Q, R을 생각해 보자
이 문제의 경우 OP의 길이와 OR의 길이가 동일하고
OQ가 각POR을 이등분 하고 있다.
이때 PR과 OQ(또는 OQ의 연장선)과의 교점을 S라고 할때
OS의 길이가 Q에 해당하는 능력치보다 크면 되고 이 과정을
각 꼭짓점에 대해서 반복하면 된다(8번)

OP = x, OR = y라고 하고 이 문제의 경우 각POR = 90도 이다.
OP : OR = PQ : RQ = x : y
O를 원점, P를 (x, 0), R를 (0, y)라고 두면
점S는 PR을 x:y로 내분하는 점이다.
점S = (xy/(x+y), xy/(x+y)) 가 된다.
이때 OS = sqrt(2)*(xy/(x+y)가 된다.
'''

# 기하+백트래킹 풀이
import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))
sub = [lst[0]]
visited = [False] * 8
cnt = 0

def func() :
    global cnt
    if len(sub) == 8 :
        sub_cnt = 0
        for i in range(8) :
            if 2*(((sub[i%8]*sub[(i+2)%8])/(sub[i%8]+sub[(i+2)%8]))**2) <= (sub[(i+1)%8])**2 :
                sub_cnt += 1
            else :
                break
        if sub_cnt == 8 :
            cnt += 1
    
    for i in range(1, 8) :
        if visited[i] is False :
            visited[i] = True
            sub.append(lst[i])
            func()
            sub.pop()
            visited[i] = False

func()
print(cnt*8)