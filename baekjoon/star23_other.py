import sys

input = sys.stdin.readline

n = int(input())
enter = (n-2)*2 + 1 # 중간 스페이스
#n-2 center n-2
print('*'*n + ' '*enter + '*'*n)
side = 1 #양옆 스페이스
enter-=2
for i in range(n-2):
    print(' '*side + '*' + ' '*(n-2) + '*' + ' '*enter + '*' + ' '*(n-2) + '*')
    side +=1
    enter-=2
print(' '*side + '*' + ' '*(n-2) +  '*' + ' '*(n-2) + '*' )
#print(side,enter)
for i in range(n-2):
    side -= 1
    enter += 2
    print(' '*side + '*' + ' '*(n-2) + '*' + ' '*enter + '*' + ' '*(n-2) + '*')
enter+=2
print('*'*n + ' '*enter + '*'*n)
