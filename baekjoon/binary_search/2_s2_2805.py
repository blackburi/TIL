import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = max(lst)
k = (start+end)//2

while end - start >= 2 :
    hap = 0
    for i in lst :
        if i >= k :
            hap += i-k
    
    if hap > m :
        start = k
    elif hap < m :
        end = k
    else : # hap = m
        break

    k = (start+end)//2

print(k)