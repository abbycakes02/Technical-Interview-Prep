class Solution(object):
    def maxSubsequence(self, nums, k):
        # array nums int k
        # dict of index values
        # select the largest k pairs
        # answer = sort by index
        # return answer
        from collections import defaultdict
        import heappush, heappop, heapq
        heap = []
        for i in range(len(nums)):
            heappush(heap, (nums[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        result = [val for val,idx in sorted(heap, key = lambda x: x[1])]
        return result
        

class Greedy_Solution(object):
    def maxSubsequence(self, nums, k):
        for i in range(len(nums)- k):
            min_num = min(nums)
            nums.remove(min_num)
        return nums


        