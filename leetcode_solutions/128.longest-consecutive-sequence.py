#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        largest = 0
        for num in nums:
            prior, count, later = num - 1, 1, num + 1
            if later not in nums_set:
                while prior in nums_set:
                    count += 1
                    prior -= 1
                if count > largest:
                    largest = count
        return largest


# @lc code=end
