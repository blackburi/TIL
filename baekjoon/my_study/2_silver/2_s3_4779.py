import sys
input = sys.stdin.readline

while True :
    try :
        n = int(input())

        def kan(n) :
            if n == 0 :
                return '-'
            else :
                return kan(n-1) + ' '*(3**(n-1)) + kan(n-1)

        print(''.join(kan(n)))
    except :
        break