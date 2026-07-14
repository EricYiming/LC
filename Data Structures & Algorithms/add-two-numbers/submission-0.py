# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        carry = False
        result = ListNode(0)
        cur = result
        while p1 is not None or p2 is not None or carry: 
            res = 0
            if p1: 
                res += p1.val
                p1 = p1.next
            if p2: 
                res += p2.val
                p2 = p2.next
            if carry: 
                res += 1
                carry = False
            if res >= 10: 
                carry = True
            cur.next = ListNode(res % 10)
            cur = cur.next
        
        return result.next
        
            
            

