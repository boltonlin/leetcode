# 230327

def lengthOfLongestSubstring(s: str) -> int:
    unique_chars = set()
    longest = 0
    start, end = 0, 0
    while end < len(s):
        old_size = len(unique_chars)
        unique_chars.add(s[end])
        new_size = len(unique_chars)
        longest = max(longest, new_size)
        if new_size == old_size:
            start += 1
            end = start
            unique_chars = set()
            continue
        end += 1
    return longest

input = "pwwkew"
print(lengthOfLongestSubstring(input))

input = "abcabcbb"
print(lengthOfLongestSubstring(input))

input = "dvdf"
print(lengthOfLongestSubstring(input))

def ba_lengthOfLongestSubstring(self, s: str) -> int:
    seen = {}
    l = 0
    output = 0
    for r in range(len(s)):
        """
        If s[r] not in seen, we can keep increasing the window size by moving
        right pointer
        """
        if s[r] not in seen:
            output = max(output,r-l+1)
        """
        There are two cases if s[r] in seen: 

        case1: s[r] is inside the current window, we need to change the window
        by moving left pointer to seen[s[r]] + 1. 

        case2: s[r] is not inside the current window, we can keep increase the
        window
        """
        else:
            if seen[s[r]] < l:
                output = max(output,r-l+1)
            else:
                l = seen[s[r]] + 1
        seen[s[r]] = r
    return output
