# NBA농구

N = int(input())

score1 = 0 # 1team get score
score2 = 0 # 2team get score
time1 = 0 # 1team whole winnig time
time2 = 0 # 2team whole winning time
goal = []

for _ in range(N) :
    a, b = list(map(str, input().split()))
    b, c = b.split(':')
    time = int(b) * 60 + int(c) # time unit : sec
    goal.append([int(a), time])

# 시간 순서로 정렬
goal.sort(key = lambda x : x[1])

now = 0

for N in goal :
    # 1team이 득점한 경우
    if N[0] == 1 :
        if score1 > score2 :
            time1 += N[1] - now
        elif score1 < score2 :
            time2 += N[1] - now
        else : # score1 == score2
            pass
        score1 += 1
    # 2team이 득점한 경우
    else : # N[0] == 2
        if score2 > score1 :
            time2 += N[1] - now
        elif score2 < score1 :
            time1 += N[1] - now
        else : # score2 == score1
            pass
        score2 += 1
    
    now = N[1]

# 48min (endint time)이 된경우
if score1 > score2 :
    time1 += 2880 - now
elif score1 < score2 :
    time2 += 2880 - now

m1 = time1 // 60
s1 = time1 % 60
m2 = time2 // 60
s2 = time2 % 60

ans = [m1, s1, m2, s2]
for _ in range(4) :
    k = ans.pop(0)
    if k < 10 :
        k = '0' + str(k)
        ans.append(k)
    else :
        ans.append(k)

print(f'{ans[0]}:{ans[1]}')
print(f'{ans[2]}:{ans[3]}')