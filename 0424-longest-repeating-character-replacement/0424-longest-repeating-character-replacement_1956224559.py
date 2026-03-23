class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_f = 0
        l = 0
        arr = [0] * 26
        for r in range(len(s)):
            arr[ord(s[r])-65] += 1
            max_f = max(max_f, arr[ord(s[r])-65])
            if r - l + 1 - max_f > k:
                arr[ord(s[l])-65] -= 1
                l += 1
        return len(s) - l