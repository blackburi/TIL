import sys
input = sys.stdin.readline
from collections import deque

while True :
    lst = deque(list(map(int, input().rstrip().split())))

    if lst == deque([0]) :
        break

    n = lst.popleft()
    hmax = 0
    while lst :
        s = lst.popleft()
        hap = s
        for i in range(len(lst)) :
            if lst[i] >= s :
                hap += s
            else :
                break
        
        if hmax < hap :
            hmax = hap
    
    print(hmax)