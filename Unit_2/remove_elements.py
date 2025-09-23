
from typing import Optional
from Unit_2.merge_sorted import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = ListNode(0)
        curr.next = head
        while curr and curr.next:
            if curr.next.val == val:
                if curr.next == head:
                    head = head.next
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

class Recursive_Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        head.next = self.removeElements(head.next, val)
        # ListNode h.next = f(h -> next, val)
        if head.val == val:
            return head.next
        else:
            return head