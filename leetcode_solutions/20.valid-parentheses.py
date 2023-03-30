# 230330

def isValid(s: str) -> bool:
    open_brackets = ["(", "{","["]
    close_brackets = [")", "}","]"]
    stack = []
    for char in s:
        if char in open_brackets:
            stack.append(char)
        if char in close_brackets:
            if not len(stack):
                return False
            compare = stack.pop()
            if close_brackets.index(char) != open_brackets.index(compare):
                return False
    return True if not len(stack) else False

s = "()"
print(isValid(s))

s = "()[]{}"
print(isValid(s))

s = "(]"
print(isValid(s))
