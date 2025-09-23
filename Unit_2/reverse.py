
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Iterative_Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next = head.next
            head.next = prev 
            prev = head # 1 in first node to second node which is start
            head = next # 2 to first node which is end
        return prev
            # store next value
            # reverse ptr to go backwards
            # move prev and head forward
            
        # next node equals current

class Recursive_Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if curr node or next node is none return none
        if not head or not head.next:
            return None
        # this unwinds the recursion
        # recursive reverse the linked list
        reversed = self.reverseList(head.next)
        head.next.next = head # reverse the next pointer to go back to head
        head.next = None # we need to break the link between 1 and 2
        return reversed


        # current node's next to node

