import sys
input = sys.stdin.readline

w, h = map(int, input().split()) # 격자 가로, 세로
p, q = map(int, input().split()) # 출발 가로, 세로
t = int(input()) # 시간

# 가로
a = (p + t) % (w * 2)
if a > w :
    x = 2 * w - a
else : # a < w :
    x = a

# 세로
b = (q + t) % (h * 2)
if b > h :
    y = 2 * h - b
else : # b < h
    y = b


print(x, y)