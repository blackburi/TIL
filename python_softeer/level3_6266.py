# 회의실 예약

import sys
input = sys.stdin.readline

# n 회의실 개수, m 회의 개수
n, m = map(int, input().split())

# {회의실 이름 : 시간}
room = {}

for i in range(n) :
    name = input().rstrip()
    room[name] = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

# 회의실 이름순으로 정렬
room = dict(sorted(room.items()))

# 회의실 예약시간을 제외하는 함수
def book(name, start, end) :
    for i in range(start, end+1) :
        if i in room[name] :
            room[name].remove(i)

# 예약한 정보와 시간을 받고 처리
for _ in range(m) :
    car, start, end = map(str, input().rstrip().split())
    start = int(start)
    end = int(end)
    book(car, start, end)

