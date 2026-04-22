class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        d = 0
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                d = max(d, j-i)
                j += 1
            else:
                i += 1
        return d