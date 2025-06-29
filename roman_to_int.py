class Solution:
    def romanToInt(self, s: str) -> int:
        # using a stack
        # push to stack
        # if curr is smaller than the next
        # sum of values in stack

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

        # recursive solution
        # dict
        # 