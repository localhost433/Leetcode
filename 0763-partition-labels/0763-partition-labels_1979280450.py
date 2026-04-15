class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        arr = [0] * 26
        start = 0
        end = 0
        ret = []
        for i, char in enumerate(s):
            if i > arr[ord(char)-97]:
                arr[ord(char)-97] = i
        for i, char in enumerate(s):
            end = max(end, arr[ord(char)-97])
            if i == end:
                ret.append(i - start + 1)
                start = i + 1
        return ret