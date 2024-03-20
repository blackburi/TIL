# 퀵 정렬

def quick_sort(arr) :
    if len(arr) <= 1 :
        return arr
    
    pivot = arr[len(arr)//2]
    small_arr, equal_arr, big_arr = [], [], []

    for num in arr :
        if num < pivot :
            small_arr.append(num)
        elif num == pivot :
            equal_arr.append(num)
        else : # num > pivot
            big_arr.append(num)
    
    return quick_sort(small_arr) + equal_arr + quick_sort(big_arr)

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    lst = list(map(int, input().split()))
    lst = quick_sort(lst)

    print(f'#{tc} {lst[n//2]}')