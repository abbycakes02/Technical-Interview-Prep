class Solution(object):
    def mySqrt(self, x):
        # binary search approach
        first, last = 1, x
        while first <= last:
            mid = (first + last) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                first = mid + 1
            else:
                last = mid - 1
        return last
