height = [int(input()) for _ in range(9)]

k = sum(height) - 100

for i in range(len(height)-1) :
    for j in range(i+1, len(height)) :
        if height[i] + height[j] == k :
            except1 = height[i]
            except2 = height[j]
            break

height.sort()

for r in range(9) :
    if height[r] == except1 or height[r] == except2 :
        continue
    else :
        print(height[r])