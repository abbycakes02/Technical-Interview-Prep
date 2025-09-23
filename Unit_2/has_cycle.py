
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Floyd_Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr== fast_ptr:
                return True
        return False
    

class Hash_Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head and head.next:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False