# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2: 
            return
        cur1 = l1
        cur2 = l2
        carry = False
        res = ListNode()
        cur3 = res

        while cur1 and cur2: 
            tot = cur1.val + cur2.val
            if carry: 
                tot += 1
                carry = False
            if tot >= 10: 
                tot = tot - 10
                carry = True
            cur1 = cur1.next
            cur2 = cur2.next
            
            cur3.next = ListNode(tot)
            cur3 = cur3.next
        
        while cur1: 
            val = cur1.val
            if carry: 
                val += 1
                carry = False
            if val >= 10: 
                val -= 10
                carry = True
            cur1 = cur1.next
            
            cur3.next = ListNode(val)
            cur3 = cur3.next
        while cur2: 
            val = cur2.val
            if carry: 
                val += 1
                carry = False
            if val >= 10: 
                val -= 10
                carry = True
            cur2 = cur2.next
            
            cur3.next = ListNode(val)
            cur3 = cur3.next
        if carry: 
            cur3.next = ListNode(1)
            
        return res.next



        