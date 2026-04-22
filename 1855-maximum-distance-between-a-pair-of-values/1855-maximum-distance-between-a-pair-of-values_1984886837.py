class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        for j in range(len(nums2)):
            if nums1[i] > nums2[j]:
                i += 1
                if i == len(nums1):
                    break
        return max(j - i, 0)