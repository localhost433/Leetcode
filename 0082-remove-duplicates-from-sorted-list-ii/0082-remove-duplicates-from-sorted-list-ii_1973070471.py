class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-float('inf'), head)
        cur = dummy
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                cur.next = head.next
            else:
                cur = cur.next
            head = head.next
        return dummy.next