n = int(input())

if n % 2 == 0 :
    for i in range(1, n+1) :
        if i % 2 == 0 :
            print(' *'*n)
        else :
            print('*' + ' *'*(n-1))
else :
    for i in range(1, n+1) :
        if i % 2 == 0 :
            print(' *'*n)
        else :
            print('*' + ' *'*(n-1))