# 병합 정렬

def merge_sort(lst) :
    global cnt

    if len(lst) == 1 :
        return lst
    
    l = len(lst)
    left, right = [], []
    middle = l // 2

    for i in range(middle) :
        left.append(lst[i])
    
    for j in range(middle, l) :
        right.append(lst[j])
    
    left, right = merge_sort(left), merge_sort(right)

    if left[-1] > right[-1] :
        cnt += 1

    re = left + right
    re.sort()

    return re


T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    answer = merge_sort(lst)

    print(f'#{tc} {answer[n//2]} {cnt}')