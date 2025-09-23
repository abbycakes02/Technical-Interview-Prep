from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        count = Counter(arr)
        values = [value for value in count.values()]
        return len(values) == len(set(values))