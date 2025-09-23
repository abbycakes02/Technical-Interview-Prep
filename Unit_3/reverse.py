class Solution(object):
    def reverseString(self, s):
        first = 0
        last = len(s) - 1
        for _ in range(0, last / 2 + 1):
            s[first], s[last] = s[last], s[first]
            first+= 1
            last-=1
        return s
    

