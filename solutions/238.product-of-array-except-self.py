#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        right = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        return [left[i] * right[i] for i in range(len(nums))]


# @lc code=end
