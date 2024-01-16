# if 반복문

n = int(input())

for i in range(1, 4*n-2) :
    if i % 2 == 0 :
        if i <= (4*n-2-i) :
            print('* '*(i//2) + ' '*(4*n-3-2*i) + ' *'*(i//2))
        else :
            j = 4*n-2-i
            print('* '*(j//2) + ' '*(4*n-3-2*j) + ' *'*(j//2))
    else : 
        if i < (4*n-2-i) :
            print('* '*((i-1)//2) + '*'*(4*n-2*i-1) + ' *'*((i-1)//2))
        elif i == 2*n-1 :
            print('* '*(2*n-2) + '*')
        else :
            j = 4*n-2-i
            print('* '*((j-1)//2) + '*'*(4*n-2*j-1) + ' *'*((j-1)//2))