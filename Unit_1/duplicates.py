from typing import List
from collections import Counter
class HashSetSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use a set to track seen numbers
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False
    # Time: O(n)
    # Space: O(n)

class HashMapSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use a Counter to count occurences of each number
        seen = Counter(nums)
        for count in seen.values():
            if count > 1:
                return True
        return False

class SortedSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Sort the list ad check for adjacent duplicates
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    # Time: O(n log n) due to sorting
    # Space: O(1) if sorting in place, O(n) if using additional space for sorted array

if __name__ == "__main__":
    sol = HashSetSolution()
    sol2 = HashMapSolution()
    sol3 = SortedSolution()
    result = sol.containsDuplicate([1,2,3,1])
    print(result)  # Output: True
    result = sol2.containsDuplicate([1,2,3,4])
    print(result)  # Output: False
    result = sol3.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
    print(result)  # Output: True

