class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        arr = [0] * 26
        half = ''
        for char in s[:n//2]:
            arr[ord(char)-97] += 1
        for i, ct in enumerate(arr):
            half += chr(i + 97) * ct
        return half + s[n//2] + half[::-1] if n % 2 else half + half[::-1]