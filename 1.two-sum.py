#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = dict()
        for i, num in enumerate(nums):
            complement = target - nums[i]
            for key, value in map.items():
                if value == complement:
                    return (key, i)
            map[len(map)] = nums[i]
        return None
# @lc code=end