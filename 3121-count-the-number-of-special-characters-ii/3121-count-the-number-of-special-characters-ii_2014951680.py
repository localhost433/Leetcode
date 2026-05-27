class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last = [-1] * 26
        first = [-1] * 26
        for i, char in enumerate(word):
            o = ord(char)
            if char.islower():
                last[o-97] = i
            else:
                if first[o-65] == -1:
                    first[o-65] = i
        count = 0
        
        for i in range(26):
            if last[i] != -1 and first[i] != -1:
                if last[i] < first[i]:
                    count += 1
                    
        return count