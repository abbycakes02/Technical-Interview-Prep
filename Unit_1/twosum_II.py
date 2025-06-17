from typing import List
class TwoPointerSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1 = 0
        ptr2 = len(numbers) - 1
        for i, num in enumerate(numbers):
            if numbers[ptr1] + numbers[ptr2] == target:
                return ptr1 + 1, ptr2 + 1
            if numbers[ptr1] + numbers[ptr2] > target:
                ptr2-=1
            else:
                ptr1+=1

class BinarySearchSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # iterate thru the array and compute the compliment
        # perform a binary search to see if the compliment exists
        # return the indices + 1 if not continue with the next element

        def binary_search(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == target:
                    return mid
                if numbers[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
            
        for i, num in enumerate(numbers):
            answer = target - num
            x = binary_search(i + 1, len(numbers)-1, answer)
            if x != -1:
                return i + 1 , x + 1
class DictionarySolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         