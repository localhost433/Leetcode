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
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        l = 0
        r = len(arr) - 1
        arr[r//2].next = None
        while l < r:
            arr[l].next, arr[r].next = arr[r], arr[l].next
            l += 1
            r -= 1