# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = ListNode(0, head)
        cur1 = p
        cur2 = p
        for _ in range(n):
            cur1 = cur1.next
        while cur1.next is not None:
            cur1 = cur1.next
            cur2 = cur2.next
        cur2.next = cur2.next.next
        return p.next