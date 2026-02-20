class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while (n != 1):
            prev = n & 1
            n = n >> 1
            bit = n & 1
            if bit == prev:
                return False
        return True