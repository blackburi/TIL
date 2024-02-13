n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
res = -1

def sort_merge(a, p, r) : # a[p~r]을 오름차순 정렬
    if p < r :
        q = (p+r)//2 # q는 p,r 중간 지점
        sort_merge(a, p, q) # 절반기준 전반부 정렬
        sort_merge(a, q+1, r) # 절반 기준 후반부 정렬
        merge(a, p, q, r) # 병합

# a[p~q]와 a[(q+1)~r]을 병합하여 a[p~r]을 오름차순 정렬된 상태로 만든다.
# a[p~q]와 a[(q+1)~r]은 이미 오름차순으로 정렬되어 있다.
def merge(a, p, q, r) :
    global cnt, res
    i = p
    j = q + 1
    lst = []
  
    while i <= q and j <= r:
        if a[i] <= a[j]:
            lst.append(a[i])
            i += 1
        else:
            lst.append(a[j])
            j += 1
    
    while i <= q : # 왼쪽 배열 부분이 남은 경우
        lst.append(a[i])
        i += 1
  
    while j <= r: # 오른쪽 배열 부분이 남은 경우
        lst.append(a[j])
        j += 1
  
    i = p
    t = 0
  
    while i <= r:  # 결과를 A[p~r]에 저장
        a[i] = lst[t]
        cnt += 1
        if cnt == k:
            res = a[i]
            break
        i += 1
        t += 1

sort_merge(a, 0, n-1)
print(res)