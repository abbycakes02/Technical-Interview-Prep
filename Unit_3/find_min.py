class Solution(object):
    def findMin(self, nums):
        # binary search
        # initialize 2 ptrs 
        first, last = 0, len(nums) - 1
        while first < last:
            mid = (first + last) // 2
            if nums[mid] > nums[last]:
                first = mid + 1
            elif nums[mid] <= nums[last]:
                last = mid 
        return nums[first]
        