class Normal_Solution:
    def romanToInt(self, s: str) -> int:


        # create a dict to store mapping btw numerals and ints
        dict = {"I": 1, "V": 5, "X":10,"L":50, "C": 100 , "D": 500, "M": 1000}
        roman_val = 0
        for num in range(0, len(s) - 1):
            curr = s[num]
            if dict[curr] >= dict[s[num + 1]]:
                roman_val += dict[curr]
            else:
                roman_val -= dict[curr]
        return roman_val + dict[s[-1]]
        # loop thru the array
        # initialive an roman value
        # loop thru array from start to n - 1
        # if curr is larger than or equal to the next:
            # add it
        # else:
            # subtract it
    

class Stack_Solution:
    def romanToInt(self, s: str) -> int:
        # create a dict to store mapping btw numerals and ints
        # using a stack
        # push to stack
        # if curr is smaller than pop the stack and subtract it
        # sum of values in stack
        # good for tracking order
        # more intuitive
        dict = {"I": 1, "V": 5, "X":10,"L":50, "C": 100 , "D": 500, "M": 1000}
        stack = []
        for idx, roman_num in enumerate(s):
            curr = dict[roman_num]
            if stack and stack[-1] < curr:
                stack.append(curr - stack.pop())
            else:
                stack.append(curr)
        return sum(stack)

class Recursive_Solution:
    def romanToInt(self, s: str) -> int:

        roman_dict = {"I": 1, "V": 5, "X":10,"L":50, "C": 100 , "D": 500, "M": 1000}
        if not s:
            return 0
        if len(s) == 1:
            return roman_dict[s[0]]
        # recursive solution
        # dict
        # BASE CASE: if s is empty, return 0
        if roman_dict[s[0]]   >= roman_dict[s[1]]:
            return  roman_dict[s[0]] + self.romanToInt(s[1:])
        else:
            return - roman_dict[s[0]] + self.romanToInt(s[1:])

