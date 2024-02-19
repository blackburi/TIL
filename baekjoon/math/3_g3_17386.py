# 신발끈 정리의 응용
'''
각각의 선분에 대한 일차방정식을 구하고
일차방정식을 부등식으로 바꿔서
다른 선분의 양 끝점을 대입했을때 양수와 음수가 한번씩 나온다면
(L1에 대해 (x3, y3), (x4, y4)를 계산했을 때 양수한번 음수 한번
L2에 대해 (x1, y1), (x2, y2)를 계산했을 때 양수한번 음수 한번 나오면 된다.)
'''

import sys
input = sys.stdin.readline

x1, y1, x2, y2 = list(map(int, input().rstrip().split()))
x3, y3, x4, y4 = list(map(int, input().rstrip().split()))

def cal(a, b, c, d, e, f) :
    return a*d+c*f+e*b - (b*c+d*e+f*a)

p = cal(x1, y1, x2, y2, x3, y3)
q = cal(x1, y1, x2, y2, x4, y4)
r = cal(x3, y3, x4, y4, x1, y1)
s = cal(x3, y3, x4, y4, x2, y2)

if p*q < 0 and r*s < 0 :
    print(1)
else :
    print(0)