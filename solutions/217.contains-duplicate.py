# 230315

#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i, num in enumerate(nums):
            s_len = len(s)
            if num in s:
                return True
            s.add(num)
            if len(s) == s_len:
                return True
        return False


# @lc code=end
