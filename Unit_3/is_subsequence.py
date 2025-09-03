class Solution(object):
    def isSubsequence(self, s, t):

        # create 2 ptrs 
        # create counter
        # while t
        # if equal: update ptr i, update counter
        # update ptr t always
        # if counter < len(s): return False else True

        i, j = 0, 0
        counter = 0
        while j < len(t):
            if i <= len(s) - 1 and s[i] == t[j]:
                i += 1
                counter += 1
            j +=1
        if counter < len(s):
            return False
        return True
    

class Recursive_Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True
        if not t:
            return False
        if s[0] == t[0]:
            return self.isSubsequence(s[1:],t[1:])
        else:
            return self.isSubsequence(s,t[1:])
        

class Solution(object):
    def isSubsequence(self, s, t):
        from collections import defaultdict
        import bisect
        char = defaultdict(list)
        for i,c in enumerate(t):
            char[c].append(i)
        print(char)
        prev = -1
        for c in s:
            if c not in char:
                return False
            i = bisect.bisect_right(char[c], prev)
            if i == len(char[c]):
                return False
            prev = char[c][i]
        return True

        

