class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        prev = ListNode(0)
        prev.next = head
        curr = head
        dummy = prev
        deleted = 0
        while curr and curr.next:
            if curr.val == curr.next.val:
                deleted = curr.val
                while curr and curr.val == deleted:
                    curr = curr.next
                    prev.next = curr
                    
            else:
                curr = curr.next
                prev = prev.next
        return dummy.next