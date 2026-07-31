class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        for char in word:
            freq[ord(char)-97] += 1
        freq.sort(reverse=True)
        return sum(freq[:8]) + sum(freq[8:16])*2 + sum(freq[16:24])*3 + sum(freq[24:])*4
