from typing import List
class ListSolution:
    def destCity(self, paths: List[List[str]]) -> str:
        # loop thru each tuple
        # check if the second element is in the list of first elements
        # if not we return it
        start_set = set()
        for start, end in paths:
            start_set.append(start)
        for start,end in paths:
            if end not in start_set:
                return end

class SetDifferenceSolution:
    def destCity(self, paths: List[List[str]]) -> str:
        # we can create two sets one for start one for end
        # then we can find the difference
        all_set = set()
        start_set = set()
        for start, end in paths:
            start_set.append(start)
            all_set.append(start,end)
        end_set = all_set - start_set
        return end_set.pop()
    
class RecursiveSolution:
    def destCity(self, paths: List[List[str]]) -> str:
        def helper(current):
            return
        # recursive solution


    
