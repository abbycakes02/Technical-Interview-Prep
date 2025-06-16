from typing import List
from collections import Counter
# Buyer moor method - leveraging the fact that the majority element appears more than n/2 times
class BoyerMooreSolution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for i in nums:
            if count == 0:
                candidate = i
                count = 1
            elif i == candidate:
                count +=1
            else:
                count -= 1
        return candidate

# Divide and conquer approach 
class DivideAndConquerSolution:
    def majorityElement(self, nums: List[int]) -> int:
        # divide the array into two halves
        # find the majority element in each half
        # if both are ot the same element, count the occurences of each majority element
        # combine the results to find the overall majority element
        def majority(lo, hi):
            if lo == hi:
                return nums[lo]
            mid = (lo + hi) // 2
            left = majority(lo, mid)
            right = majority(mid + 1, hi)
            if left == right:
                return left
            left_count = sum(1 for val in nums[lo:hi+1] if val == left)
            right_count = sum(1 for val in nums[lo:hi+1] if val == right)
            return left if left_count > right_count else right
        return majority(0, len(nums) - 1)

# Hash table approach
class HashMapSolution:
    def majorityElement(self, nums: List[int]) -> int:
        # Create dict to store the count
        # Iterate through the list and update the count
        # Return the element with the highest count
        counter = Counter(nums)
        return max(counter.keys(), key=counter.get)


def run_tests():
    # Test the Boyer-Moore solution
    sol = BoyerMooreSolution()
    result = sol.majorityElement([2,2,1,1,1,2,2])
    assert result == 2

    # Test the Divide and Conquer solution
    sol = DivideAndConquerSolution()
    result = sol.majorityElement([2,2,1,1,1,2,2])
    assert result == 2

    sol = HashMapSolution()

    result = sol.majorityElement([2,2,1,1,1,2,2])
    assert result == 2

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()