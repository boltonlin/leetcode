# 230324

def threeSum(nums):
    checked = set()
    solutions = set()
    
    registry = dict() # key num, value index
    for i, num in enumerate(nums):
        registry[num] = i

    for i, num in enumerate(nums):
        ptr1 = i
        ptr2 = i+1
        if num in checked:
            continue
        while ptr2 < len(nums):
            start_sum = nums[ptr1] + nums[ptr2]
            comp = 0 - start_sum
            if comp in registry and registry[comp] not in [ptr1, ptr2]:
                solution = tuple(sorted([nums[ptr1], nums[ptr2], comp]))
                if solution not in solutions:
                    solutions.add(solution)
            ptr2 += 1
        checked.add(num)

    return [list(solution) for solution in solutions] if len(solutions) > 0 else []

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

nums = [0,1,1]
print(threeSum(nums))

nums = [0,0,0]
print(threeSum(nums))
