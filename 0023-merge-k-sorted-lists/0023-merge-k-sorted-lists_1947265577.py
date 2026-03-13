class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                merged.append(self.merge(l1, l2))
            lists = merged
            
        return lists[0]

    def merge(self, l1, l2):
        dummy = ListNode()
        t = dummy
        while l1 and l2:
            if l1.val < l2.val:
                t.next = l1
                l1 = l1.next
            else:
                t.next = l2
                l2 = l2.next
            t = t.next
        t.next = l1 or l2
        return dummy.next