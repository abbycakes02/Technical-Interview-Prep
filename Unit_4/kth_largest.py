from ast import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # negate array
        # create heap
        # loop through k times and pop -top elements - 1
        # return heap[0]
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for i in range(0, k - 1):
            heapq.heappop(nums)
        return -nums[0]
    

class Optimized_Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create a new array
        # add element into array
        # if size < k:
            # pop element
        # return top most element
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
    
class Counting_Sort_Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # count occurrences
        # find range (min, max)
        # count = []
        x = max(nums)
        y = min(nums)
        ranges = x - y + 1
        count = [0] * ranges
        for num in nums:
            count[num - y] += 1
        remaining = k
        for i in range(len(count)- 1,-1, -1):
            remaining -= count[i]
            if remaining <= 0:
                return i + y
