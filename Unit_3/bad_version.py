class Solution(object):
    def firstBadVersion(self, n):
        # create 2 ptrs
        # while first <= second
        # if equal return idx
        # if <, then mid + 1 and if >, then mid - 1
        first, second = 1, n
        while first < second:
            mid = (first + second) //2
            if isBadVersion(mid) == True:
                second = mid
            if isBadVersion(mid) != True:
                first = mid + 1
        return first