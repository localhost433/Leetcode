# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k== 0:
            return head
        count = 1
        ptr = head
        while ptr.next:
            ptr = ptr.next
            count += 1
        k %= count
        if k == 0:
            return head
        ptr.next = head
        last = head
        for _ in range(count-k-1):
            last = last.next
        new = last.next
        last.next = None
        return new