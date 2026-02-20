class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 5 == 0 or k % 2 == 0:
            return -1
        n = 1
        rem = 1 % k
        while (rem != 0):
            rem = (rem * 10 + 1) % k
            n += 1
        return n
        