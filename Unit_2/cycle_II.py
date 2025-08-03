
from typing import Optional

from Unit_2.has_cycle import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast pointer algortihm to check for cycle
        # restart start pointer
        # update both pointers till they reach the same node
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                break
        else:
            return None
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
