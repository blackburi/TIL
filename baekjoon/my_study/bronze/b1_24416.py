n = int(input())

mat = [0] * (n+1)
mat[0] = 0
mat[1] = 1
for i in range(2, n+1) :
    mat[i] = mat[i-1] + mat[i-2]

print(mat[n], n-2)