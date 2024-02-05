import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

cnt = 0

def count(n, r, c) :
    global cnt
    if n == 1 :
        if r == 0 and c == 0 :
            return cnt
        elif r == 0 and c == 1 :
            return cnt + 1
        elif r == 1 and c == 0 :
            return cnt + 2
        elif r == 1 and c == 1 :
            return cnt + 3
    else : # n != 1
        if r >= 2**(n-1) and c >= 2**(n-1) :
            cnt += 3 * (2**(2*n-2))
            r -= 2**(n-1)
            c -= 2**(n-1)
            return count(n-1, r, c)
        elif r >= 2**(n-1) and c < 2**(n-1) :
            cnt += 2 * (2**(2*n-2))
            r -= 2**(n-1)
            return count(n-1, r, c)
        elif r < 2**(n-1) and c >= 2**(n-1) :
            cnt += 2**(2*n-2)
            c -= 2**(n-1)
            return count(n-1, r, c)
        elif r < 2**(n-1) and c < 2**(n-1) :
            return count(n-1, r, c)

print(count(n, r, c))