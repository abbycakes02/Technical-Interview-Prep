import heapq
from typing import List
class Simple_Solution_KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        # create list


    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[- self.k]
        
        # add value to list
        # compute the ordered list
        # return the new val

class Heap_KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # create list
        # create heap
        self.heap = nums[:]
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # make heap only the k largest values




    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
