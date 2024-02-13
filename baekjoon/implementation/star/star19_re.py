## 재귀함수

a = int(input())
rule = 4*a-3
arr = [[' ']*rule for i in range(rule)]

def star(n, x, y) :
  rule = 4*n-3
  if n==1 :
    arr[x][y]='*'
    return
  for j in range(rule) :
    arr[x][y+j]='*'               # 윗변
    arr[x+j][y]='*'               # 좌변
    arr[x+rule-1][y+j]='*'        # 우변
    arr[x+j][y+rule-1]='*'        # 밑변
  star(n-1,x+2,y+2)
  return

star(a,0,0)

for k in arr :
    print(''.join(k))