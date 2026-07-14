# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0 
        guard = ListNode(0, head)
        cur = guard
        while cur is not None: 
            cur = cur.next
            len += 1
        cur = guard
        count = 0
        while count < len - n - 1: 
            cur = cur.next
            count += 1
        cur.next = cur.next.next
        return guard.next
        
        