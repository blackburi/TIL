# 특별한 정렬

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    num_list = list(map(int, input().split()))

    ans = []

    num = deque([])

    while len(num_list) > 0 :
        if len(num) == 0 :
            k = num_list.pop()
            num.append(k)
        else : # len(num) != 0
            a = num_list.pop()
            for i in range(len(num)) :
                if a < num[i] :
                    num.insert(i, a)
                    break
                elif a > num[-1] :
                    num.append(a)

    while len(num) > 0 :
        m = num.pop()
        ans.append(m)
        
        if len(num) != 0 :
            l = num.popleft()
            ans.append(l)
    
    if len(ans) > 10 :
        ans = ans[:10]

    print(f'#{tc}', *ans)