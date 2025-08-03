class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # initialize dummy node
        dummy = ListNode(0)
        dummy.next = head
        res = dummy 
        for i in range(0, n - 1):
            head = head.next
        while head.next:
            head = head.next
            dummy = dummy.next
        dummy.next = dummy.next.next
        return res.next
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

class Stack_Solution(object):
    def removeNthFromEnd(self, head, n):
        stack = []
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        # 
        while curr:
            stack.append(curr)
            curr = curr.next
        for i in range(n):
            stack.pop()
        prev = stack[-1]
        prev.next = prev.next.next
        
        return dummy.next
    

class Recursive_Solution(object):
    def removeNthFromEnd(self, head, n):
        def dfs(node):
            if not node:
                return 0
            i = dfs(node.next) + 1 # recursively calling 
            if i == n + 1:
                node.next = node.next.next
            return i
        dummy = ListNode(0)
        dummy.next = head
        dfs(dummy)
        return dummy.next


        
        
        