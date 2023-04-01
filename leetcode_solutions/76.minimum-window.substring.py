# 230401
from collections import Counter

def minWindow(s:str, t:str) -> str:
    if t == "":
        return ""

    countT, window = {}, {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:
            # update our result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = r - l + 1
            # pop from the left of our window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l : r + 1] if resLen != float("infinity") else ""

def inc_minWindow(s: str, t:str) -> str:
    start, end = None, None
    target = Counter(t)
    res = ""
    lock = False
    for i, letter in enumerate(s):
        if letter in target:
            if start == None:
                start, end = i, i
            if target[letter] > 0:
                target.subtract(letter)
        if target.total() == 0:
            lock = True
            res = s[start:end+1]
            # minimize
            while s[start] not in target:
                start += 1
                res = s[start:end+1]
        if end != None and end < len(s):
            end += 1
        if lock:
            if s[start] in target:
                target[s[start]] += 1
            start += 1
    return res

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))

s = "a"
t = "a"
print(minWindow(s, t))

s = "a"
t = "aa"
print(minWindow(s, t))

s = "bdab"
t = "ab"
print(minWindow(s, t))
