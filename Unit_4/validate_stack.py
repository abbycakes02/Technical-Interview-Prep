from ast import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # stacks are good to maintain ordering
        # stack1 = []
        # check if push  equals pop remove popped
        stack = []
        j = 0
        for num in pushed:
            stack.append(num)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return False if stack else True
