# 사람수
N = int(input())

# 번호표 순서
numbers = list(map(int, input().split()))

# 추가 공간
wait = []

# 현재 지나가는 번호
go = 1

while len(numbers) > 0 :
    if numbers[0] == go :
        numbers.pop(0)
        go += 1
    elif numbers[0] != go and len(wait) == 0 :
        wait.append(numbers[0])
        numbers.pop(0)
    elif numbers[0] != go and len(wait) != 0 :
        if wait[-1] == go :
            wait.pop()
            go += 1
        else :
            wait.append(numbers[0])
            numbers.pop(0)

while len(wait) > 0 :
    if wait[-1] == go :
        wait.pop()
        go += 1
    else :
        print('Sad')
        break

if len(wait) == 0 :
    print('Nice')