import sys
input = sys.stdin.readline

while True:
    num = list(map(str, input()))
    num.pop()   # delete '/n'

    if num == ['0']:
        break

    for i in range(len(num)//2):
        if num[0] == num[-1]:
            num.pop(0)
            num.pop(-1)
            if len(num) <= 1:
                break
        else :
            print('no')
            break
    if len(num) <= 1:
        print('yes')