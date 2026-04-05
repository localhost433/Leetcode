# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        last = head
        count = 1

        while last.next:
            last = last.next
            count += 1

        k = k % count
        if k == 0:
            return head

        last.next = head
        steps = count - k - 1
        tail = head
        for _ in range(steps):
            tail = tail.next

        new = tail.next
        tail.next = None

        return new