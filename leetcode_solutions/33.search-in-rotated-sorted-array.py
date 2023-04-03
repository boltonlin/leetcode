# 230403

def search(nums, target) -> int:
    res = -1
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    min_index = l

    l, r = 0, len(nums) - 1
    if target < nums[r]:
        l = min_index
    elif target > nums[r]:
        r = min_index - 1
        if r < 0:
            r += len(nums)
    else:
        return r

    while l < r:
        mid = (l + r) //2
        if target > nums[mid]:
            l = mid + 1
        else:
            r = mid
    if nums[l] == target:
        return l

    return res

nums = [4,5,6,7,0,1,2]
print(search(nums, 4))

nums = [0,1,2,4,5,6,7]
print(search(nums, 8))

nums = [3,1]
print(search(nums,1))
