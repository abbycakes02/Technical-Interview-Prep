class Solution(object):
    def search(self, nums, target):
        # 2 ptrs 
        # find middle index
        # check if target
        # if less, move left if more move right
        first_ptr = 0
        second_ptr = len(nums) - 1
        while first_ptr <= second_ptr:
            mid = (first_ptr+ second_ptr) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                second_ptr = mid - 1
            else:
                first_ptr = mid + 1
        return -1