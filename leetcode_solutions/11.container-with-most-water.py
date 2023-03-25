# 230325
import heapq

def prelim_maxArea(height):
    max_areas = list(map(lambda i_x: (-(i_x[1] * (len(height) - i_x[0] - 1)), i_x[0]), enumerate(height)))
    heapq.heapify(max_areas)
    
    result, i = 0, 0
    while i < len(height):
        (max_area, index) = heapq.heappop(max_areas)
        if result > -(max_area): 
            break
        for j in range(len(height) - index - 1):
            rearptr = len(height) - j - 1
            length = min(height[index], height[rearptr])
            width = rearptr - index
            area = length * width
            if area > result: 
                result = area
        i += 1
    
    return result

def better_maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

input = [1,8,6,2,5,4,8,3,7]
print(better_maxArea(input))

input = [1,1]
print(better_maxArea(input))
