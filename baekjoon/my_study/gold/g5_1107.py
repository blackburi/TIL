import sys
input = sys.stdin.readline

target = int(input())
n = int(input())
broken = list(map(int, input().split()))

# 현재 채널에서 + or -만 이용하여 이동하는 경우
cnt = abs(100-target)

# 채널은 무한대이고 target은 500,000까지이지만
# 그 이상에서 - button을 이용하여 내려오는것도 가능하기 떄문에
# range의 범위를 넓게 잡아준다.
for num in range(1000001) :
    snum = str(num) # 뒤에서 길이를 재기위해 문자열로 변환

    for j in range(len(snum)) :
        if int(snum[j]) in broken :
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 cnt와 비교
        elif j == len(snum) - 1 :
            cnt = min(cnt, abs(num-target)+len(snum))

print(cnt)