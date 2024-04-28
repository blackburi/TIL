# 책 페이지

import sys
input = sys.stdin.readline

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9의 개수
ans = [0] * 10

number = int(input())

# 자릿수에 따라 갯수는 10의 거듭제곱만큼 많아진다
# 5 : 일의 자리에 5가 1개
# 5_ : 십의 자리에 5가 10개 (50~59)
# 5__ : 백의 자리에 5가 100개 (500~599)
# 자리수를 세는 변수
digit = 1

# 1페이지 부터 세기 시작
page = 1

# 0으로 끝나는 수와 9로 끝나는 수를 짝지어 주면 세기 편하다
# 1157의 경우 1140~1149까지 세고 1150~1157을 따로 센다.
def plus(x, digit) :
    while x > 0 :
        ans[x % 10] += digit
        x //= 10


while page <= number :
    # 마지막 페이지가 9로 끝나지 않는 경우
    while number % 10 != 9 :
        plus(number, digit)
        number -= 1

    # 세야 하는 page가 넘어가면 stop
    if number < page :
        break

    # 세기 시작하는 page가 0으로 시작하지 않는 경우
    while page % 10 != 0 :
        plus(page, digit)
        page += 1

    page //= 10
    number //= 10
    for i in range(10) :
        ans[i] += (number - page + 1) * digit

    digit *= 10

print(*ans)