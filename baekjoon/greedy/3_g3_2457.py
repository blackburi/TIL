# 공주님의 정원

import sys
input = sys.stdin.readline

n = int(input())

# 꽃이 피고 지는 날짜
flowers = []
for _ in range(n) :
    # 피는 달, 피는 날, 지는 달, 지는 날
    sm, sd, em, ed = map(int, input().split())
    flowers.append((sm * 100 + sd, em * 100 + ed))

# 꽃들을 피는 날짜, 지는 날짜 순서로 오름차순 정렬
flowers.sort()

# 정원의 마지막 꽃이 지는 날짜 -> 꽃이 피는 날짜 < 지는 날짜
# 이후 다음 꽃이 지는 날짜로 계속 갱신 / 12월 1일 이상이 되면 stop
end = 301 # 3월 1일

# 심은 꽃의 갯수
answer = 0

while flowers :
    # 12월 1일 이상 채워졌거나 // 채워지지 않는 경우
    if end >= 1201 or flowers[0][0] > end :
        break

    # 꽃이 피는 날짜가 end 이전일 경우 -> 가장 느리게 지는 날짜로 갱신
    tmp_end = 0

    for _ in range(len(flowers)) :
        # 꽃이 피는 날짜 < end :
        if flowers[0][0] <= end :
            # 가장 느리게 지는 꽃의 날짜를 확인
            if tmp_end <= flowers[0][1] :
                tmp_end = flowers[0][1]
            # 확인후 제거
            flowers.remove(flowers[0])
        else :
            break

    # 제일 마지막 꽃이 지는 날짜 갱신
    end = tmp_end
    answer += 1

if end < 1201 :
    print(0)
else :
    print(answer)