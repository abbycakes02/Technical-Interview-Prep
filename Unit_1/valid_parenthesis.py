class Solution:
    def isValid(self, s: str) -> bool:
        # stack 
        # loop thru array
        # append to stack if in dict.keys
        # stack.pop is equal to it's dict map
        # id not return false
        # return true 
        dict = {"(": ")", "[":"]", "{":"}" }
        char_stack = []
        opening = set(dict.keys())
        closing = set(dict.values())
        for element  in s:
            if element in opening:
                char_stack.append(dict[element])
            if element in closing:
                if char_stack:
                    x = char_stack.pop()
                    if element != x:
                        return False
                else:
                    return False
        if len(char_stack) != 0:
            return False
        return True