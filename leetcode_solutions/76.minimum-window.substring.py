# 230401
from collections import Counter

def minWindow(s: str, t:str) -> str:
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
