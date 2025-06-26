from typing import List
class HashSetSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max = 0
        hash_set = set(nums)
        for num in hash_set:
            curr = 1
            if (num - 1) not in hash_set:
                while (num + 1) in hash_set:
                    curr+=1
                    num+=1
            if max < curr:
                max = curr
        return max

        # create a hash set with a
        # if start of sequence if num -1 not in hash set
        # check if n-1 exists it not 

class SortedSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_count = 0
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i-1] + 1 == nums[i]:
                curr+=1
            else:
                max_count = max(curr, max_count)
                curr = 1
        return max(curr, max_count)
        # sort the array
        # initialize max and current count
        # iterate through the array



class RecursiveSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # base case: if nums is empty return 0
        # recursively check n - 1 and add 1 to the result
        if not nums:
            return 0
        set = set(nums)
        memo = {}
        def find_length(num):
            if num not in set:
                return 0
            if num - 1 not in set:
                return 1 + find_length(num + 1)
            

class DPSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use dp table
        
        return

class BSTSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use bst
        return