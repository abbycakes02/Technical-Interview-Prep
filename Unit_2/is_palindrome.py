# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        # find the middle of the linkedlist
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        prev = None
        curr = slow
        while curr:
            next = curr.next 
            curr.next = prev
            prev = curr
            curr = next
        #compare the two halves head and prev
        while head and prev:
            if head.val !=prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

class Solution(object):
    def isPalindrome(self, head):
        
        arr = []
        




        


