class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0
        seen = {}

        for r in range(len(s)):
            ch = s[r]
            while ch in seen:
                del seen[s[l]]
                l += 1
            seen[ch] = seen.get(ch, 0) + 1
            best = max(best, r - l + 1)
        return best