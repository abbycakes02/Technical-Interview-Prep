class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #base case
        # power of 2 if it is even while dividing until we reach 1
        if n == 1:
            return True
        if n <= 0 or n % 2 != 0:
            return False
        
        return self.isPowerOfTwo(n/2)


class BitWise_Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n - 1))