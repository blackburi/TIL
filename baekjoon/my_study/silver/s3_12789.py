# 사람수
N = int(input())

# 번호표 순서
person = list(map(int, input().split()))

# 추가 공간
wait = []

# 현재 지나가는 번호
go = 1

while len(person) > 0 :
    if person[0] == go :
        person.pop(0)
        go += 1
    elif person[0] != go and len(wait) == 0 :
        wait.append(person[0])
        person.pop(0)
    elif person[0] != go and len(wait) != 0:
        if wait[-1] == go :
            wait.pop()
            go += 1
        else :
            wait.append(person[0])
            person.pop(0)


for _ in range(len(wait)-1) :
    if wait[0] > wait[1] :
        wait.pop(0)
    else :
        print('Sad')
        break

if len(wait) == 1 :
    print('Nice')