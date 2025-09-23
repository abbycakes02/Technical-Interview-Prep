class Solution(object):
    def reverseWords(self, s):
        # turn string into list
        # reverse list
        # turn back into string
        
        x = s.strip()
        y = x.split()
        y.reverse()
        answer = " ".join(y)
        return answer

class Simple_Solution(object):
    def reverseWords(self, s):
        return " ".join(s.strip().split()[::-1])