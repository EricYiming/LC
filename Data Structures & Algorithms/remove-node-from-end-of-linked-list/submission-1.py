# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head
        cur = sentinel
        total = 0
        while cur: 
            cur = cur.next
            total += 1
        
        
        cur = sentinel
        count = 0
        while cur and count < total - n - 1: 
            cur = cur.next
            count += 1
        cur.next = cur.next.next

        return sentinel.next