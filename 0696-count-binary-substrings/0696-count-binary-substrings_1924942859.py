class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ret = 0
        cur = 1
        pre = 0
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                cur += 1
            else:
                ret += min(cur, pre)
                pre = cur
                cur = 1
        ret += min(cur, pre)
        return ret
        