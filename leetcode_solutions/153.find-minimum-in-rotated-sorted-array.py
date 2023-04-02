# 230402
def findMin(nums) -> int:

    if len(nums) == 1:
        return nums[0]

    mid = len(nums) // 2
    lmax = nums[mid - 1]
    rmax = nums[len(nums) - 1]

    # even 
    if len(nums) % 2 == 0:
        lead = min(lmax, rmax)
        if mid == 1:
            return lead
        if lead == lmax:
            return findMin(nums[:mid])
        else:
            return findMin(nums[mid:])

    # odd 
    else:
        pivot = nums[mid]
        lead = min(pivot, lmax, rmax)
        if mid == 1:
            return lead
        if lead == pivot:
            return pivot
        elif lead == lmax:
            return findMin(nums[:mid])
        else:
            return findMin(nums[mid + 1:])

nums = [3,4,5,1,2]
print(findMin(nums))

nums = [4,5,6,7,0,1,2]
print(findMin(nums))

nums = [13,15,17,11]
print(findMin(nums))
