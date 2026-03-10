class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        def findK(a, b, k):
            if not a:
                return b[k-1]
            if not b:
                return a[k-1]
            if k == 1:
                return min(a[0], b[0])

            i = min(len(a), k // 2)
            j = min(len(b), k // 2)

            if a[i-1] < b[j-1]:
                return findK(a[i:], b, k - i)
            else:
                return findK(a, b[j:], k - j)

        if total % 2 == 1:
            return float(findK(A, B, total // 2 + 1))
        return (findK(A, B, total // 2) + findK(A, B, total // 2 + 1)) / 2.0