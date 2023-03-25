# 230322
import re, math
from collections import defaultdict


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[\W_]+", "", s)
        s = s.lower()
        first_half = s[: math.floor(len(s) / 2)]
        second_half = s[math.ceil(len(s) / 2) : len(s)]
        return all(
            first_half[i] == second_half[len(first_half) - i - 1]
            for i in range(len(first_half))
        
        
