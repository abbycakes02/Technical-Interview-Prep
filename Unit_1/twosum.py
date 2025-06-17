from typing import List
class HashSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize a empty hash
        # calculate the compliment 
        # check if compliment exists
        # if not, add current value in hashmap
        dict = {} 
        for i, num in enumerate(nums):
            compliment = target - num 
            if compliment in dict.keys():
                return dict[compliment], i
            else:
                dict[num] = i

class TwoPointerSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_iter = [(nums, i) for i, nums in enumerate(nums)]
        nums_iter.sort()
        print(nums_iter)
        ptr1 = 0
        ptr2 = len(nums) - 1
        while ptr1 < ptr2:
            current_sum = nums_iter[ptr1][0] + nums_iter[ptr2][0]
            if current_sum == target:
                return nums_iter[ptr1][1], nums_iter[ptr2][1]
            elif current_sum < target:
                ptr1 += 1
            else:
                ptr2 -= 1
        

class BinarySearchSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_iter = sorted((num, i) for i, num in enumerate(nums))
        # initialize fixed
        # calcualte the compliment
        # binary search of the sub array 
        # check anf return the indices
        def binary_search(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums_iter[mid][0] == target:
                    return mid
                elif nums[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        for i in range(len(nums_iter)):
            curr_val, curr_idx = nums_iter[i]
            complement = target - curr_val
            j = binary_search(i+1, len(nums_iter) - 1, complement)
            if j!= - 1:
                return sorted([curr_idx, nums_iter[j][1]])



