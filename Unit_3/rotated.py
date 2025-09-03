class Solution(object):
    def find_min(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return right
    def binary_search(self, nums, target, l, r):
        left, right = l, r
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid]< target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search(self, nums, target):
        minIndex = self.find_min(nums)
        right = self.binary_search(nums, target, 0, minIndex- 1)
        left = self.binary_search(nums, target, minIndex, len(nums)- 1)
        return max(right, left)

        # binary search 
        # find pivot point 
        # binary search on segment based on target value

        
        