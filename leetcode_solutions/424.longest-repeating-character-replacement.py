# 230329
from collections import Counter

def characterReplacement(s: str, k: int) -> int:
    left, right = 0, 0
    counts = Counter()
    longest = 0
    maxf = 0
    while right < len(s):
        counts[s[right]] += 1
        maxf = max(maxf, counts[s[right]])
        windowlen = right - left + 1
        while windowlen - maxf > k:
            counts[s[left]] -= 1
            left += 1
            windowlen = right - left + 1
        longest = max(longest, windowlen)
        right += 1
    return longest

def inc_characterReplacement(s: str, k: int) -> int:
    left, right = 0, 0
    curr_counts = Counter()
    changeables = Counter()
    longest = 0
    most_common = ''
    while right < len(s):
        if changeables.total() + 1 > k and s[right] in changeables:
            changeables = set()
            curr_counts = Counter()
            most_common = ''
            save = s[left]
            while s[left] == save:
                left += 1
            right = left
        curr_counts[s[right]] += 1
        most_common = curr_counts.most_common(1)[0][0]
        changeables[most_common] = 0
        if s[right] != most_common:
            changeables[s[right]] = curr_counts[s[right]] 
        longest = max(longest, right - left + 1)
        right += 1
    pass

s, k = "ABAB", 2
print(characterReplacement(s, k))

s, k = "AABABBA", 1
print(characterReplacement(s, k))

s, k = "ABABBA", 2
print(characterReplacement(s, k))
