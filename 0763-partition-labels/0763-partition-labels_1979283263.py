class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        arr = {c: s.rfind(c) for c in set(s)}
        start = end = 0
        ret = []
        for i, char in enumerate(s):
            end = max(end, arr[char])
            if i == end:
                ret.append(i - start + 1)
                start = i + 1
        return ret