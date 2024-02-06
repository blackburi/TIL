# Flatten

for tc in range(1, 11) :
    dump = int(input())
    height = list(map(int, input().split()))

    height_max = height[0]
    height_min = height[0]

    for i in height :
        if height_max < i :
            height_max = i

        if height_min > i :
            height_min = i

    while dump > 0 :        
        if height_max == height_min or height_max - height_min == 1 :
            break
        
        a = height.index(height_max)
        b = height.index(height_min)
        height[a] -= 1
        height[b] += 1

        height_max = height[0]
        height_min = height[0]

        for i in height :
            if height_max < i :
                height_max = i

            if height_min > i :
                height_min = i

        dump -= 1

    print(f'#{tc} {height_max - height_min}')