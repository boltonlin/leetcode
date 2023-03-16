# 230316

# Approach
# Put s characters in a hash map with their counts, iterate through t and put
# in its own hash map. Deeply compare the two maps.

#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


# @lc code=start
class Solution:
    def makeDict(self, s: str) -> dict:
        d = {}
        for char in list(s):
            if not char in d.keys():
                d[char] = 1
            else:
                d[char] += 1
        return d

    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.makeDict(s)
        t_dict = self.makeDict(t)
        return s_dict == t_dict


# @lc code=end
