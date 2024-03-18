

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
    lst = list(map(int, input().split()))
    print(f'#{tc}', *quick_sort(lst))