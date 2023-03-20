# 230320

# Description
# Design an algorithm to encode a list of strings to a string. The encoded
# string is then sent over the network and is decoded back to the original
# list of strings.

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"

# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"

# Please implement encode and decode


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        """
        look thru each chararcter in each string, if we see a ":", then we
        prepend it with another ":". then push the token into out. so long as
        we are within the list of strings, we will append ":;" to mark the end
        of the string.
        """
        out = ""
        for i, string in enumerate(strs):
            token = ""
            for character in list(string):
                if character != ":":
                    token += character
                else:
                    token += ":" + character
            out += token
            if i < len(strs) - 1:
                out += ":;"
        return out

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        """
        split the string, look through each character, if the character is not
        a ":", add it to the token. if the character IS a ":", and we can look
        at the next character, we will consider the token complete and push it
        to out and set the ignore flag to skip the next character which is ";".
        if it is NOT ";", then current character must be the prepended ":" that
        we inserted. we will push to the token a single ":" instead, set the
        ignore flag, then continue parsing the token. at the beginning of each
        step, we check if the ignore flag is set and unset it and effectively
        skip the current character.
        """
        out = []
        split_string = list(str)
        ignore = False
        token = ""
        for i, character in enumerate(split_string):
            if ignore:
                ignore = False
            else:
                if character != ":":
                    token += character
                else:
                    if i < len(split_string) - 1:
                        if split_string[i + 1] == ";":
                            out.append(token)
                            token = ""
                        else:
                            token += ":"
                    ignore = True
                if i == len(split_string) - 1:
                    out.append(token)
        return out
