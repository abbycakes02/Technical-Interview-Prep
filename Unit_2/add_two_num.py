
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        first = l1
        second = l2
        while first or second or carry:
            one_num = first.val if first else 0
            sec_num = second.val if second else 0
            final = one_num + sec_num + carry
            carry = final // 10 
            curr.next = ListNode(final % 10)
            curr = curr.next
            first = first.next if first else 0
            second = second.next if second else 0
        return dummy.next
    

class Recursive_Solution(object):
    def addTwoNumbers(self, l1, l2):
        # create helper function for addition
        def base_function(first, second, carry):
            if not first and not second and not carry:
                return None
            first_num = first.val if first else 0
            second_num = second.val if second else 0
            final = first_num + second_num + carry
            new_node = ListNode(final % 10)
            new_node.next = base_function(first.next if first else None, second.next if second else None, final // 10)
            return new_node
        return base_function(l1 , l2, 0)