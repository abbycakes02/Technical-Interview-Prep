from typing import List, Optional
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
        set_num = set(nums)
        memo = {}
        def find_length(num):
            if num not in set_num:
                return 0
            if num in memo:
                return memo[num]
            set_num.remove(num)
            memo[num] = 1 + find_length(num + 1)
            return memo[num]
        max_len = 0
        for num in nums:
            if num - 1 not in set_num:
                max_len = max(max_len, find_length(num))

        return max_len

            
            
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

class BSTSolution:
    def insert(self, root: Optional[TreeNode], val: int) -> TreeNode:
        # create a new TreeNode if root is None
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root 

    def inorder_traversal(self, root: Optional[TreeNode], result: List[int]):
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.val)
            self.inorder_traversal(root.right, result)

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Step 1: Build BST
        root = None
        for num in nums:
            root = self.insert(root, num)
        
        # Step 2: In-order traversal to get sorted unique values
        sorted_nums = []
        self.inorder_traversal(root, sorted_nums)
        
        # Step 3: Find longest consecutive sequence
        longest = 1
        current = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1
        longest = max(longest, current)
        return longest