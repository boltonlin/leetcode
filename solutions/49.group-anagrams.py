#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        result = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if not sorted_word in anagram_dict:
                anagram_dict[sorted_word] = [word]
            else:
                anagram_dict[sorted_word].append(word)
        for key in anagram_dict.keys():
            result.append([*anagram_dict[key]])
        return result


# @lc code=end
