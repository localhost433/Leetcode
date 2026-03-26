# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head) -> None:
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        mid = reverse(mid)
        slow.next = None
        while mid and head:
            h1 = head.next
            head.next = mid
            h2 = mid.next
            mid.next = h1
            mid = h2
            head = h1