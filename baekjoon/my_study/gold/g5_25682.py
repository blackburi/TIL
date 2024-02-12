import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
lst = [input().rstrip() for _ in range(n)]

# 각각의 matrix는 바꿔야 하는 타일의 수를 나타낸다
# black : white -> black으로 바꿔야 하는 타일의수 (black[0][0]~black[i][j]까지)
# white : black -> white로 바꿔야 하는 타일의수 (black[0][0]~black[i][j]까지)
black = [[0]*(m+1) for _ in range(n+1)]
white = [[0]*(m+1) for _ in range(n+1)]

for i in range(n) :
    for j in range(m) :
        if (i+j) % 2 == 0 :
            if lst[i][j] == 'B' :
                black[i][j] = 1 + black[i-1][j] + black[i][j-1] - black[i-1][j-1]
                white[i][j] = 0 + white[i-1][j] + white[i][j-1] - white[i-1][j-1]
            else : # lst[i][j] == 'W'
                black[i][j] = 0 + black[i-1][j] + black[i][j-1] - black[i-1][j-1]
                white[i][j] = 1 + white[i-1][j] + white[i][j-1] - white[i-1][j-1]
        else : # (i+j) % 2 == 1
            if lst[i][j] == 'W' :
                black[i][j] = 1 + black[i-1][j] + black[i][j-1] - black[i-1][j-1]
                white[i][j] = 0 + white[i-1][j] + white[i][j-1] - white[i-1][j-1]
            else : # lst[i][j] == 'B'
                black[i][j] = 0 + black[i-1][j] + black[i][j-1] - black[i-1][j-1]
                white[i][j] = 1 + white[i-1][j] + white[i][j-1] - white[i-1][j-1]

# 제일 많이 바꿔야 하는 경우
ans = 2000 * 2000 / 2

for i in range(n-k+1) :
    for j in range(m-k+1) :
        black_sum = black[i+k-1][j+k-1] - black[i-1][j+k-1] - black[i+k-1][j-1] + black[i-1][j-1]
        white_sum = white[i+k-1][j+k-1] - white[i-1][j+k-1] - white[i+k-1][j-1] + white[i-1][j-1]
        ans = min(ans, black_sum, white_sum)

print(ans)