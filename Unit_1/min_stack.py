from collections import deque
import heapq
class MinStack:

    def __init__(self):
        # queue has slightly more overhead as we need to store 2 pointers
        # append and pop are o(1) for lists
        self.stack = []
        self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            if self.min_stack[-1] >= val:
                self.min_stack.append(val)
        else:
            self.min_stack.append(val)


    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if self.min_stack and self.min_stack[-1] == val:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        
