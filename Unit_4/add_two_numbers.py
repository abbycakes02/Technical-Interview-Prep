# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #reverse lists
        r1 = self.reverse(l1)
        r2 = self.reverse(l2)
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        first = r1
        second = r2
        while r1 or r2 or carry:
            num1 = r1.val if r1 else 0
            num2 = r2.val if r2 else 0
            added = num1 + num2 + carry
            carry = added // 10
            curr.next = ListNode(added % 10)
            curr = curr.next
            r1 = r1.next if r1 else 0
            r2 = r2.next if r2 else 0
        return self.reverse(dummy.next)
