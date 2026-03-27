class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m: return ""
        target, window = Counter(t), Counter()
        have, need = 0, len(target)
        ret, resLen = [-1, -1], float("infinity")
        j = 0
        for i in range(m):
            char = s[i]
            window[char] += 1
            if char in target and window[char] == target[char]:
                have += 1
            while have == need:
                if i - j + 1 < resLen:
                    ret = [j, i]
                    resLen = i - j + 1
                left = s[j]
                window[left] -= 1
                if left in target and window[left] < target[left]:
                    have -= 1
                j += 1
        return s[ret[0]:ret[1]+1] if resLen != float("infinity") else ""