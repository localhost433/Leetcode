# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur and cur.next:
            n1 = cur.next
            n2 = cur.next.next
            
            n1.next = cur
            cur.next = n2
            prev.next = n1
            
            prev = cur
            cur = n2
            
        return dummy.next