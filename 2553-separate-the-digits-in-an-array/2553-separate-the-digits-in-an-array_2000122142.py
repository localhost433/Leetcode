class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return list([int(x) for x in list("".join([str(x) for x in nums])) ])